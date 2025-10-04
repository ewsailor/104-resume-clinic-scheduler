"""單元測試使用者相關的測試 Fixtures。

提供單元測試用的使用者資料和實例。
"""

# ===== 第三方套件 =====
import pytest


# ===== 資料 (Data)：字典格式 =====
@pytest.fixture
def test_user_data():
    """提供測試用的通用使用者資料。"""
    return {
        "name": "測試使用者",
        "email": "test@example.com",
    }
