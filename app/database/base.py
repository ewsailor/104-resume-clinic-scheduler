"""資料庫基礎類別模組。

提供 SQLAlchemy 的 declarative_base 基礎類別。
"""

# ===== 第三方套件 =====
from sqlalchemy.orm import declarative_base

# 建立基礎類別：所有資料表模型，都會繼承這個類別，避免重複的程式碼
Base = declarative_base()

__all__ = [
    "Base",
]
