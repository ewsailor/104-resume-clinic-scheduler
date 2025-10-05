"""操作相關的 ENUM 定義模組。

定義各種操作使用的 ENUM 型別，包括操作上下文、刪除還是等。
"""

# ===== 標準函式庫 =====
from enum import Enum


class OperationContext(str, Enum):
    """操作上下文枚舉"""

    CREATE = "建立"
    UPDATE = "更新"
    DELETE = "刪除"
    DUPLICATE = "複製"  # 未來可能的新操作
    ARCHIVE = "封存"  # 未來可能的新操作


class DeletionResult(str, Enum):
    """刪除結果枚舉"""

    SUCCESS = "刪除成功"
    ALREADY_DELETED = "已經刪除"
    NOT_FOUND = "時段不存在"
    CANNOT_DELETE = "無法刪除"
