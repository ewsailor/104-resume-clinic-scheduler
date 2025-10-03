# 速懂新技術與選型理由 AI Prompt 模板

[← 返回根目錄 README.md](../README.md#tech-quickstart-insight)

使用方法說明：
1. 在下方【新名詞】處，填寫想瞭解的【新名詞】
2. 更新【專案情境】
3. 將以下所有 Prompt 內容，複製貼上到 AI 工具的聊天對話框中，即可速懂新技術與選型理由

=====請複製此線以下所有 Prompt 內容=====

# 【新名詞】：

我是一名 Python 工程師，請協助依專案情境，針對「{{新名詞}}」提供一份詳細說明，

以利迅速掌握「{{新名詞}}」概念、專案情境下選擇「{{新名詞}}」的選型理由，且能應用於作品集、面試、完成工作任務。 

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

- **資料庫***：「MySQL/MariaDB、SQLite 測試環境、Alembic」
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

## 【概念與選型理由】

### 核心概念與面試解說
請用白話文簡述「{{新名詞}}」的概念、能解決什麼核心痛點，以利貼到 README.md 上、面試時回答面試官。

### 類似選項
我的專案情境中，「{{新名詞}}」有哪些常見的類似選項，請以表格形式比較類似選項與「{{新名詞}}」在優缺點上的差異（如：適合情境、業界主流程度、安全性、可維護性與可擴充性、可靠性、效能、開發效率）。

### 選型理由
在我的專案情境中，業界 Best Practice 通常採用前述選項中的哪一種方法？說明業界 Best Practice 選擇這種方法的原因，與能帶來哪些具體好處（如：適合情境、安全性、可維護性與可擴充性、可靠性、效能、開發效率）？解決什麼問題？不使用有什麼潛在壞處或風險？

### 限制與解決方案
前述選項中的方法，有什麼缺點，怎麼解決？請以表格形式呈現。

### 職缺要求與面試回覆
- 「{{新名詞}}」常在哪些職缺要求中出現
- 面試官可能詢問哪些問題
- 建議的回答內容

### 驗收標準
在我的專案情境中，實作「{{新名詞}}」需符合哪些驗收標準？回覆範例如下：
- MySQL 資料表與 SQLAlchemy 模型同步
- 根據 SQLAlchemy 模型自動產生 Migration 檔案
- 版本控管每次資料庫的結構變動
- 升級失敗時，能安全回滾到前一版本

### CLI（Command-Line Interface）：
請附上「{{新名詞}}」常用指令、指令功能。回覆範例如下：
- **alembic init alembic**：初始化 Alembic 專案
- **alembic revision -m "..." --autogenerate**：自動根據 model 產生 migration
- **alembic upgrade head**：執行到最新版本
- **alembic downgrade -1**：回到上一版本
- **alembic current**：查看當前 migration 狀態

### GUI（Graphical User Interface）：
若此「{{新名詞}}」有常見搭配的 GUI，例如 MySQL Workbench、Postman 等，請提供：
- 使用說明
- 常用操作或快捷指令
- 下載連結網址

### 學習資源與延伸閱讀
請提供「{{新名詞}}」相關的官方文件、教學文章、Youtube 影片、新手練習資源等，附上網址以利需要深入瞭解時直接查閱。