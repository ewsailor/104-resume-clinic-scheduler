"""資料庫模型輔助工具模組。

提供共用的模型相關工具函式，避免重複代碼。
"""

# ===== 標準函式庫 =====
from datetime import date, datetime, time
from typing import Any, Union


def format_datetime(
    dt: Union[datetime, date, time, None],
) -> str | None:
    """格式化日期時間為 ISO 字串，如果為 None 則返回 None。

    支援多種日期時間類型：
    - datetime.datetime: 完整日期時間
    - datetime.date: 僅日期
    - datetime.time: 僅時間
    - None: 返回 None
    """
    return dt.isoformat() if dt is not None else None


def safe_getattr(
    obj: Any,
    attr_name: str,
    default: Any = None,
) -> Any:
    """安全地取得物件屬性

    主要用於 ORM 關聯屬性，相比 getattr，能捕獲所有異常並返回預設值，避免沒被捕捉的異常導致 API 失敗。

    Args:
        obj: 目標物件
        attr_name: 屬性名稱
        default: 當發生任何異常時返回的預設值

    Returns:
        屬性值或預設值
    """
    try:
        return getattr(obj, attr_name, default)
    except Exception:
        return default
