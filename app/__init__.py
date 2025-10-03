"""104 履歷診療室 - 站內諮詢時間媒合系統。

FastAPI 應用程式主套件，讓 Giver、Taker 在平台內，
方便地設定可面談時間，並完成配對媒合。

主要組件：
- 核心配置（app/core）：應用程式設定、版本管理
- 資料庫操作（app/crud）：資料庫 CRUD 操作
- 資料庫連線（app/database）：資料庫連線管理
- 裝飾器（app/decorators）：錯誤處理、日誌裝飾器
- 枚舉定義（app/enums）：資料庫、操作枚舉類型定義
- 錯誤處理（app/errors）：統一錯誤處理機制
- 中間件（app/middleware）：FastAPI 中間件
- 資料庫模型（app/models）：SQLAlchemy 資料模型定義
- 路由（app/routers）：FastAPI 路由定義
- 資料驗證（app/schemas）：Pydantic 資料模型
- 業務邏輯（app/services）：業務邏輯處理層
- Jinja2 模板引擎（app/templates）：伺服器端渲染模板引擎
- 工具函數（app/utils）：共用工具函數
- 工廠（app/factory）：應用程式工廠
- 主入口點（app/main）：應用程式入口點
"""
