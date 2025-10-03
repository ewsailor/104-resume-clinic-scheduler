# 實作功能 AI Prompt 模板

[← 返回根目錄 README.md](../README.md#feature-implementation)

使用方法說明：

1. 在下方【實作功能】處，填寫欲【實作的功能】
2. 更新【專案情境】
3. 將以下所有 Prompt 內容，複製貼上到 AI 工具的聊天對話框中，即可加速實作出功能

=====請複製此線以下所有 Prompt 內容=====

# 【實作功能】：

我是一名 Python 工程師，請協助依專案情境，針對「{{實作功能}}」提供一份詳細說明，

以利迅速完成「Jira」、「Git」、「實作功能」、「測試驗證」。

回覆內容請保留所有細節，像工具使用手冊，篇幅可以長沒關係。

若內容為多欄對照且內容長度較短，請用表格顯示。

## 【專案情境】

回覆我時，請紀錄我的專案情境，以利未來查看時，迅速瞭解製作時設定的情境。

- **回覆使用語言**：「僅繁體中文」

  - 參考選項：[僅繁體中文、僅英文、中英文雙語、其他語言]

- **應用場景**：「迅速掌握「{{新名詞}}」概念、專案情境下選擇「{{新名詞}}」的選型理由、實作於履歷作品集、面試 Demo、工作中解決問題」

  - 參考選項：[迅速掌握「{{新名詞}}」概念、專案情境下選擇「{{新名詞}}」的選型理由、實作於履歷作品集、面試 Demo、工作中解決問題、新人教學]

- **專案規模**：「投履歷用個人作品集（快速產出 MVP）」

  - 參考選項：[投履歷用個人作品集（快速產出 MVP）、小型專案（單人開發）、中大型專案（多人協作）]

- **專案階段**：「本地端開發環境（從零開始建立專案）」

  - 參考選項：[本地端開發環境（從零開始建立專案）、測試環境、預備環境、正式環境（如部署至雲端 AWS RDS、Docker）]

- **後端**：「FastAPI + SQLAlchemy ORM」

  - 參考選項：[FastAPI + SQLAlchemy ORM、Django + Django ORM、Flask + SQLAlchemy ORM]

- **模板引擎**：「Jinja2」

  - 參考選項：[Jinja2、Mako、Django Templates]

- **伺服器**：「Uvicorn」

  - 參考選項：[Uvicorn、Gunicorn]

- **資料庫\***：「MySQL/MariaDB、SQLite 測試環境、Alembic」

  - 參考選項：[MySQL/MariaDB、PostgreSQL、SQLite 測試環境、MongoDB、Redis、Alembic]

- **前端**：「HTML5、CSS3、JavaScript (ES6+)、Bootstrap、Font Awesome」

  - 參考選項：[HTML5、CSS3、JavaScript (ES6+)、TypeScript、React、Vue、Angular、Bootstrap、Font Awesome]

- **專案依賴**：「pyproject.toml（Poetry）」

  - 參考選項：[pyproject.toml（Poetry）、requirements.txt（pip）]

- **讀取環境變數**：「Pydantic BaseSettings」

  - 參考選項：[Pydantic BaseSettings、os.getenv()]

- **測試框架**：「pytest」

  - 參考選項：[pytest、unittest]

- **部署環境**：「Docker」

  - 參考選項：[Docker、虛擬機器 (VM)、Kubernetes]

- **部署**：「AWS」

  - 參考選項：[個人作品（Railway、Render、Vercel）、小型專案（Heroku、DigitalOcean、Fly.io）、大型專案（AWS、GCP、Azure、K8s）]

- **專案結構**：

```
104-resume-clinic-scheduler/
├── .github/workflows/ci.yml       # CI/CD
├── alembic/                       # 資料庫遷移管理配置
├── app/                           # 應用程式主目錄
│   ├── core/                      # 設定管理
│   │   ├── giver_data.py          # 模擬 Giver 資料，用於伺服器端渲染
│   │   └── settings.py            # 應用程式設定
│   ├── crud/                      # CRUD 資料庫操作層
│   │   └── schedule.py            # 時段 CRUD 操作
│   ├── database/                  # 資料庫連線層
│   │   ├── base.py                # 資料庫基礎設定
│   │   └── connection.py          # 資料庫連線管理
│   ├── decorators/                # 裝飾器
│   │   ├── error_handlers.py      # 錯誤處理裝飾器
│   │   └── logging.py             # 日誌裝飾器
│   ├── enums/                     # 枚舉型別定義
│   │   ├── models.py              # 資料庫模型枚舉
│   │   └── operations.py          # 操作枚舉
│   ├── errors/                    # 錯誤處理系統
│   │   ├── error_codes/           # 錯誤代碼
│   │   │   ├── cors.py            # CORS 錯誤代碼
│   │   │   ├── crud.py            # CRUD 錯誤代碼
│   │   │   ├── router.py          # 路由錯誤代碼
│   │   │   ├── service.py         # 服務錯誤代碼
│   │   │   └── system.py          # 系統錯誤代碼
│   │   ├── exceptions.py          # 自定義錯誤例外
│   │   ├── formatters.py          # 錯誤訊息格式化
│   │   └── handlers.py            # 錯誤處理輔助函式
│   ├── middleware/                # 中間件
│   │   ├── cors.py                # CORS 中間件
│   │   └── error_handler.py       # 錯誤處理中間件
│   ├── models/                    # SQLAlchemy 資料模型
│   │   ├── schedule.py            # 時段模型
│   │   └── user.py                # 使用者模型
│   ├── routers/                   # API 路由模組
│   │   ├── api/                   # API 端點
│   │   │   └── schedule.py        # 時段管理 API
│   │   ├── health.py              # 健康檢查 API
│   │   └── main.py                # 主要 API
│   ├── schemas/                   # Pydantic 資料驗證
│   │   └── schedule.py            # 時段資料驗證
│   ├── services/                  # 業務邏輯層
│   │   └── schedule.py            # 時段業務邏輯
│   ├── templates/                 # Jinja2 HTML 模板
│   │   ├── base.html              # 基礎模板
│   │   └── giver_list.html        # Giver 列表模板
│   ├── utils/                     # 工具模組
│   │   ├── model_helpers.py       # 資料庫模型輔助工具
│   │   └── timezone.py            # 時區處理工具
│   ├── factory.py                 # 應用程式工廠
│   └── main.py                    # 應用程式入口點
├── database/                      # 資料庫相關檔案
│   └── schema.sql                 # 資料庫結構
├── docs/                          # 開發文檔
│   ├── postman/                   # Postman 測試集合
│   │   └── 104 Resume Clinic Scheduler.postman_collection.json
│   ├── feature-implementation.md  # 實作功能 AI Prompt 模板
│   ├── tech-quickstart-insight.md # 速懂新技術與選型理由 AI Prompt 模板
│   └── user-stories.md            # 使用者故事
├── htmlcov/                       # 測試覆蓋率報告
│   ├── index.html                 # 覆蓋率報告首頁
│   ├── class_index.html           # 類別覆蓋率
│   ├── function_index.html        # 函式覆蓋率
│   └── ...                        # 其他覆蓋率報告檔案
├── logs/                          # 日誌檔案
├── scripts/                       # 開發工具腳本
│   ├── clear_cache.py             # 清除快取腳本
│   └── fix_imports.py             # 修復匯入腳本
├── static/                        # 靜態檔案
│   ├── css/                       # 樣式檔案
│   ├── images/                    # 圖片資源
│   └── js/                        # JavaScript 檔案
├── tests/                         # 測試檔案
│   ├── fixtures/                  # 測試夾具
│   │   ├── integration/           # 整合測試夾具
│   │   └── unit/                  # 單元測試夾具
│   ├── integration/               # 整合測試
│   │   ├── health.py              # 健康檢查路由整合測試
│   │   ├── main.py                # 主要路由整合測試
│   │   └── schedule.py            # 時段路由整合測試
│   ├── unit/                      # 單元測試
│   │   ├── crud/                  # CRUD 測試
│   │   ├── errors/                # 錯誤處理測試
│   │   ├── models/                # 模型測試
│   │   ├── services/              # 服務測試
│   │   └── utils/                 # 工具測試
│   └── conftest.py                # 測試配置
├── .coveragerc                    # 測試覆蓋率配置
├── .env                           # 環境變數（本地開發）
├── .env.example                   # 環境變數範本
├── .flake8                        # flake8 配置
├── .gitignore                     # Git 忽略檔案
├── .pre-commit-config.yaml        # pre-commit 配置
├── alembic.ini                    # Alembic 配置檔案
├── poetry.lock                    # Poetry 依賴鎖定
├── pyproject.toml                 # Poetry 專案配置
├── pytest-integration.ini         # pytest 整合測試配置
├── pytest.ini                     # pytest 主要配置
└── README.md                      # 專案說明文件
```

## 【Jira】

### 簡介

- **任務標題**：例如，初始導入 Alembic
- **任務類型**：例如，大型工作 Epic、使用者故事 Story、任務 Task、問題 Bug、子任務 Sub-task 等
- **優先順序**：例如，Highest、High、Medium、Low、Lowest
- **故事點**：使用 Fibonacci 數列，例如，1, 2, 3, 5, 8, 13, 21 等

### 目標：解決什麼問題？新增什麼功能？

例如，導入 Alembic，以追蹤與管理 MySQL 資料庫變化

### 驗收標準與做法

請以表現呈現，另為提升開發效率，優先級別較低之任務請標記【後續擴充】。回覆範例如下：

| 驗收標準                                    | 驗收做法                                                                                                                |
| ------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| MySQL 資料表與 SQLAlchemy 模型              | 執行 poetry run alembic upgrade head 後，資料庫會根據最新 Migration 建立或更新對應資料表                                |
| 根據 SQLAlchemy 模型自動產生 Migration 檔案 | 執行 poetry run alembic revision --autogenerate -m "..." 後，自動根據 model 產生會產生包含模型變更內容的 Migration 檔案 |
| 版本控管每次資料庫結構變動                  | 在 MySQL Workbench（或其他資料庫工具）查詢 alembic_version 資料表，能看到目前資料庫的版本號與已執行的 Migration 對應    |
| 資料庫安全回溯                              | 執行 poetry run alembic downgrade -1 後，資料庫結構會成功回退到前一個版本，且資料庫中 alembic_version 的記錄會更新      |
| 查看當前資料庫版本                          | 執行 poetry run alembic current                                                                                         |

### 後續擴充功能

- 支援在 dev、staging、production 等不同環境的資料庫中，自動套用所有變更

## 【Git】

請提供可以一鍵複製的內容，節省我思考分支、commit 怎麼下、複製貼上的時間。

- **提交類型 <type>**：請使用 `feat`、`fix`、`docs`、`style`、`refactor`、`test`、`chore` 其中一個
- **建立本地分支**：
  - 格式：git checkout -b <type>/<描述>
  - 例如：git checkout -b chore/setup-alembic
- **開發後紀錄變更**：
  - 格式：git add . && git commit -m "[Jira issue title] <type>(<scope>): <subject>"
  - 例如：git add . && git commit -m "[CLINIC-1] chore(alembic): initial setup for migration"
- **推送本地分支到遠端分支**：
  - 格式：git push origin <分支名稱>
  - 例如：git push origin chore/setup-alembic
- **代碼審查（Code Review）標題**：
  - 格式：[Jira issue title] <type>(<scope>): <subject>
  - 例如：[CLINIC-1] chore(alembic): initial setup for migration

## 【實作功能】

請提供模組化拆分後，每個檔案的程式碼片段，附上詳細註解，可以直接複製貼上就能運作。

### 前置條件（可填無）

例如：

- [ ] 系統需求：如 Python 3.10 以上，以使用「型別聯集（Type Union）」語法
- [ ] 已完成資料表設計
- [ ] 已設定好資料庫連線

### 專案結構

有更新到的檔案，請加上註解，並簡介此檔案的功能。
沒更新到的檔案，不加上註解，讓我知道此檔案沒被更新，但因為和此次變更相關，所以放入專案結構。

例如：

```
104-resume-clinic-scheduler/
├── .github/workflows/ci.yml       # CI/CD
├── alembic/                       # 資料庫遷移管理配置
├── app/                           # 應用程式主目錄
│   ├── core/                      # 設定管理
│   │   ├── giver_data.py          # 模擬 Giver 資料，用於伺服器端渲染
│   │   └── settings.py            # 應用程式設定
│   ├── crud/                      # CRUD 資料庫操作層
│   │   └── schedule.py            # 時段 CRUD 操作
│   ├── database/                  # 資料庫連線層
│   │   ├── base.py                # 資料庫基礎設定
│   │   └── connection.py          # 資料庫連線管理
│   ├── decorators/                # 裝飾器
│   │   ├── error_handlers.py      # 錯誤處理裝飾器
│   │   └── logging.py             # 日誌裝飾器
│   ├── enums/                     # 枚舉型別定義
│   │   ├── models.py              # 資料庫模型枚舉
│   │   └── operations.py          # 操作枚舉
│   ├── errors/                    # 錯誤處理系統
│   │   ├── error_codes/           # 錯誤代碼
│   │   │   ├── cors.py            # CORS 錯誤代碼
│   │   │   ├── crud.py            # CRUD 錯誤代碼
│   │   │   ├── router.py          # 路由錯誤代碼
│   │   │   ├── service.py         # 服務錯誤代碼
│   │   │   └── system.py          # 系統錯誤代碼
│   │   ├── exceptions.py          # 自定義錯誤例外
│   │   ├── formatters.py          # 錯誤訊息格式化
│   │   └── handlers.py            # 錯誤處理輔助函式
│   ├── middleware/                # 中間件
│   │   ├── cors.py                # CORS 中間件
│   │   └── error_handler.py       # 錯誤處理中間件
│   ├── models/                    # SQLAlchemy 資料模型
│   │   ├── schedule.py            # 時段模型
│   │   └── user.py                # 使用者模型
│   ├── routers/                   # API 路由模組
│   │   ├── api/                   # API 端點
│   │   │   └── schedule.py        # 時段管理 API
│   │   ├── health.py              # 健康檢查 API
│   │   └── main.py                # 主要 API
│   ├── schemas/                   # Pydantic 資料驗證
│   │   └── schedule.py            # 時段資料驗證
│   ├── services/                  # 業務邏輯層
│   │   └── schedule.py            # 時段業務邏輯
│   ├── templates/                 # Jinja2 HTML 模板
│   │   ├── base.html              # 基礎模板
│   │   └── giver_list.html        # Giver 列表模板
│   ├── utils/                     # 工具模組
│   │   ├── model_helpers.py       # 資料庫模型輔助工具
│   │   └── timezone.py            # 時區處理工具
│   ├── factory.py                 # 應用程式工廠
│   └── main.py                    # 應用程式入口點
├── database/                      # 資料庫相關檔案
│   └── schema.sql                 # 資料庫結構
├── docs/                          # 開發文檔
│   ├── postman/                   # Postman 測試集合
│   │   └── 104 Resume Clinic Scheduler.postman_collection.json
│   ├── feature-implementation.md  # 實作功能 AI Prompt 模板
│   ├── tech-quickstart-insight.md # 速懂新技術與選型理由 AI Prompt 模板
│   └── user-stories.md            # 使用者故事
├── htmlcov/                       # 測試覆蓋率報告
│   ├── index.html                 # 覆蓋率報告首頁
│   ├── class_index.html           # 類別覆蓋率
│   ├── function_index.html        # 函式覆蓋率
│   └── ...                        # 其他覆蓋率報告檔案
├── logs/                          # 日誌檔案
├── scripts/                       # 開發工具腳本
│   ├── clear_cache.py             # 清除快取腳本
│   └── fix_imports.py             # 修復匯入腳本
├── static/                        # 靜態檔案
│   ├── css/                       # 樣式檔案
│   ├── images/                    # 圖片資源
│   └── js/                        # JavaScript 檔案
├── tests/                         # 測試檔案
│   ├── fixtures/                  # 測試夾具
│   │   ├── integration/           # 整合測試夾具
│   │   └── unit/                  # 單元測試夾具
│   ├── integration/               # 整合測試
│   │   ├── health.py              # 健康檢查路由整合測試
│   │   ├── main.py                # 主要路由整合測試
│   │   └── schedule.py            # 時段路由整合測試
│   ├── unit/                      # 單元測試
│   │   ├── crud/                  # CRUD 測試
│   │   ├── errors/                # 錯誤處理測試
│   │   ├── models/                # 模型測試
│   │   ├── services/              # 服務測試
│   │   └── utils/                 # 工具測試
│   └── conftest.py                # 測試配置
├── .coveragerc                    # 測試覆蓋率配置
├── .env                           # 環境變數（本地開發）
├── .env.example                   # 環境變數範本
├── .flake8                        # flake8 配置
├── .gitignore                     # Git 忽略檔案
├── .pre-commit-config.yaml        # pre-commit 配置
├── alembic.ini                    # Alembic 配置檔案
├── poetry.lock                    # Poetry 依賴鎖定
├── pyproject.toml                 # Poetry 專案配置
├── pytest-integration.ini         # pytest 整合測試配置
├── pytest.ini                     # pytest 主要配置
└── README.md                      # 專案說明文件
```

### 實作步驟

逐步說明如何從零開始實現這個功能，提供具體指令與操作步驟，讓我瞭解「在哪裡」，輸入「什麼指令」，會看到「什麼輸出結果」。

範例格式如下：

#### Step N：簡介

「在哪裡（Cmder、瀏覽器、Terminal、路徑/檔案名稱等）」
輸入「什麼指令」
看到「什麼輸出結果（程式碼、註解）」。

例如：

#### Step 1：切換到分支

在 Cmder
輸入：git checkout -b chore/MVP-1-setup-alembic
切換到 chore/MVP-1-setup-alembic 分支

### Step 2：更新 database.py

在 app/models/database.py
找到「程式碼、註解段落 A1」，更新成「程式碼、註解段落 B1」
找到「程式碼、註解段落 A2」，更新成「程式碼、註解段落 B2」
最後到 MySQL Workbench
輸入：SHOW TABLES;
應該會看到：

- 內容 C1
- 內容 C2

## 【測試】

- 請至少提供 1 個單元測試檔案，或說明無需提供任何測試檔案的理由
- 如果能使用夾具，務必使用夾具
- 測試程式碼的註解，請使用 GIVEN-WHEN-THEN
- 如果能使用參數化測試，務必使用參數化測試
- 如果可以，請提供整合測試檔案
  - 整合測試的資料庫，使用 MySQL/MariaDB
