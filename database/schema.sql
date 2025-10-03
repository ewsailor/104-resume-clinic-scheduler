-- ===== 104 履歷診療室 - 平台內諮詢時間媒合系統 - 資料庫結構 =====

-- ===== 資料庫 =====
-- 檢查資料庫是否存在：顯示目前 MySQL 伺服器上所有的資料庫名稱
SHOW DATABASES;

-- 刪除並重新創建資料庫，加上字符集和排序規則，然後切換到 scheduler_db 資料庫
DROP DATABASE IF EXISTS `scheduler_db`;
CREATE DATABASE `scheduler_db` 
    DEFAULT CHARACTER SET utf8mb4 
    COLLATE utf8mb4_unicode_ci;
USE `scheduler_db`; 


-- ===== 資料庫使用者 =====
-- 先刪除舊的，確保乾淨狀態（如果使用者已存在）
DROP USER IF EXISTS 'fastapi_user'@'localhost';

-- 重建使用者：新增名為 fastapi_user 的使用者，密碼為 fastapi123
CREATE USER 'fastapi_user'@'localhost' 
    IDENTIFIED BY 'fastapi123';


-- ===== 資料庫權限 =====
-- 撤銷任何意外預設權限（通常 DROP USER 後不需要，但加上更保險）
REVOKE ALL PRIVILEGES ON `scheduler_db`.* 
    FROM 'fastapi_user'@'localhost'; 

-- 授予權限：給予 fastapi_user 在 scheduler_db 這個資料庫上所有資料表，必要的權限
-- （而不是用 GRANT ALL PRIVILEGES，給所有資料表的全部權限）
-- 包含基本的 CRUD 操作和結構管理權限，不包含 DROP、GRANT 等管理權限，確保安全性
GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, INDEX, ALTER 
    ON `scheduler_db`.* 
    TO 'fastapi_user'@'localhost';

-- 重新整理權限表，讓權限即時生效
FLUSH PRIVILEGES;

-- 檢查資料庫使用者權限：顯示 fastapi_user 的所有授權清單，確認是否設置成功
SHOW GRANTS FOR 'fastapi_user'@'localhost';


-- ===== 使用者資料表 `users` ===== 
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (         
    `id` INT UNSIGNED AUTO_INCREMENT PRIMARY KEY 
        COMMENT '使用者 ID',
    `name` VARCHAR(100) NOT NULL 
        COMMENT '使用者姓名', 
    `email` VARCHAR(191) NOT NULL UNIQUE 
        COMMENT '電子信箱（唯一）',    
    `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL 
        COMMENT '建立時間（本地時間）',
    `updated_at` DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP NOT NULL 
        COMMENT '更新時間（本地時間）',
    `deleted_at` DATETIME NULL DEFAULT NULL 
        COMMENT '軟刪除標記（本地時間）'

-- 指定儲存引擎、預設字符集、排序規則
) ENGINE = InnoDB 
    DEFAULT CHARSET = utf8mb4 
    COLLATE = utf8mb4_unicode_ci 
    COMMENT = '使用者資料表 (本地時間戳記)';

-- ===== 加速查詢用的索引 =====
-- 場景：後台查看最新註冊多少位使用者
CREATE INDEX `idx_users_created_at`
    ON `users` (`created_at`);


-- ===== 諮詢時段資料表 `schedules` ===== 
DROP TABLE IF EXISTS `schedules`;
CREATE TABLE `schedules` (
    `id` INT UNSIGNED AUTO_INCREMENT PRIMARY KEY 
        COMMENT '時段 ID',
    `giver_id` INT UNSIGNED NOT NULL 
        COMMENT 'Giver ID',
    `taker_id` INT UNSIGNED NULL 
        COMMENT 'Taker ID，可為 NULL（表示 Giver 提供時段供 Taker 預約）',
    `status` ENUM('DRAFT', 'AVAILABLE', 'PENDING', 'ACCEPTED', 'REJECTED', 'CANCELLED', 'COMPLETED') NOT NULL DEFAULT 'DRAFT'
        COMMENT '時段狀態（後端會根據操作者角色自動決定：GIVER→AVAILABLE，TAKER→PENDING，其他→DRAFT）',
    `date` DATE NOT NULL 
        COMMENT '時段日期',
    `start_time` TIME NOT NULL 
        COMMENT '開始時間',
    `end_time` TIME NOT NULL 
        COMMENT '結束時間',
    `note` VARCHAR(255) NULL 
        COMMENT '備註',
    
    -- ===== 審計欄位 =====
    `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL 
        COMMENT '建立時間（本地時間）',
    `created_by` INT UNSIGNED NULL
        COMMENT '建立者的 ID，可為 NULL（表示系統自動建立）',
    `created_by_role` ENUM('GIVER', 'TAKER', 'SYSTEM') NOT NULL DEFAULT 'SYSTEM'
        COMMENT '建立者角色',
    `updated_at` DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP NOT NULL 
        COMMENT '更新時間（本地時間）',
    `updated_by` INT UNSIGNED NULL 
        COMMENT '最後更新者的 ID，可為 NULL（表示系統自動更新）',
    `updated_by_role` ENUM('GIVER', 'TAKER', 'SYSTEM') NOT NULL DEFAULT 'SYSTEM'
        COMMENT '最後更新者角色',
    `deleted_at` DATETIME NULL 
        COMMENT '軟刪除標記（本地時間）',
    `deleted_by` INT UNSIGNED NULL
        COMMENT '刪除者的 ID，可為 NULL（表示系統自動刪除）',
    `deleted_by_role` ENUM('GIVER', 'TAKER', 'SYSTEM') NULL
        COMMENT '刪除者角色，可為 NULL（未刪除時）',
    
    -- ===== 外鍵約束 =====
    CONSTRAINT `fk_schedules_giver_id` 
        FOREIGN KEY (`giver_id`) 
        REFERENCES `users`(`id`) 
        -- 保護：不能刪除有時段的 Giver，避免資料不一致
        ON DELETE RESTRICT      
        ON UPDATE CASCADE,
    
    CONSTRAINT `fk_schedules_taker_id` 
        FOREIGN KEY (`taker_id`) 
        REFERENCES `users`(`id`) 
        -- 靈活：Taker 刪除時設為 NULL（時段變可預約）
        ON DELETE SET NULL      
        ON UPDATE CASCADE,
    
    CONSTRAINT `fk_schedules_created_by` 
        FOREIGN KEY (`created_by`) 
        REFERENCES `users`(`id`)
        ON DELETE SET NULL 
        ON UPDATE CASCADE,
        
    CONSTRAINT `fk_schedules_updated_by` 
        FOREIGN KEY (`updated_by`) 
        REFERENCES `users`(`id`)
        ON DELETE SET NULL      
        ON UPDATE CASCADE,
    
    CONSTRAINT `fk_schedules_deleted_by` 
        FOREIGN KEY (`deleted_by`) 
        REFERENCES `users`(`id`)
        ON DELETE SET NULL 
        ON UPDATE CASCADE

-- 指定儲存引擎、預設字符集、排序規則
) ENGINE = InnoDB 
    DEFAULT CHARSET = utf8mb4 
    COLLATE = utf8mb4_unicode_ci 
    COMMENT = '諮詢時段資料表 (本地時間戳記)';

-- ===== 加速查詢用的索引 =====
-- 場景：Giver 查詢自己含各種狀態的時段，可以是某個日期範圍內，或依日期、開始時間排序
CREATE INDEX `idx_schedule_giver_date` 
    ON `schedules` (`giver_id`, `date`, `start_time`);

-- 場景：Taker 查詢自己含各種狀態的時段，可以是某個日期範圍內，或依日期、開始時間排序
CREATE INDEX `idx_schedule_taker_date` 
    ON `schedules` (`taker_id`, `date`, `start_time`);

-- 場景：後台查詢各種狀態的時段，如多少時段被預約、多少時段被接受、多少時段被拒絕等
CREATE INDEX `idx_schedule_status`
    ON `schedules` (`status`);

-- 場景：時間衝突檢查
CREATE INDEX `idx_schedule_giver_time` 
    ON `schedules` (`giver_id`, `start_time`, `end_time`);

-- ===== 顯示資料表結構 =====
SHOW TABLES;

DESCRIBE `users`;
DESCRIBE `schedules`;

-- ===== 顯示索引資訊 =====
SHOW INDEX FROM `users`;
SHOW INDEX FROM `schedules`;

-- ===== 快速查詢資料 =====
SELECT * FROM scheduler_db.schedules ORDER BY id DESC;  
SELECT * FROM scheduler_db.users ORDER BY id DESC;  
