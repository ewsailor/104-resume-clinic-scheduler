"""測試配置檔案。

設定 pytest 的共用配置和全域 fixtures。
負責匯入和管理所有測試相關的 fixtures。
"""

# ===== 第三方套件 =====
import pytest

# 匯入整合測試的 fixtures
from tests.fixtures.integration.database import (  # noqa: F401
    integration_db_override,
    integration_db_session,
    integration_test_client,
)
from tests.fixtures.integration.schedule import (  # noqa: F401
    schedule_create_payload,
    schedule_delete_payload,
    schedule_in_db,
    schedule_update_payload,
)

# ===== 本地模組 =====
# 匯入單元測試的 fixtures
from tests.fixtures.unit.database import (  # noqa: F401
    db_session,
)
from tests.fixtures.unit.schedules import (  # noqa: F401
    test_giver_schedule,
    test_giver_schedule_data,
    test_taker_schedule,
    test_taker_schedule_data,
)
from tests.fixtures.unit.user import (  # noqa: F401
    test_user_data,
)

# 確保 pytest-mock 可用
pytest_plugins = ["pytest_mock"]


# 全域測試配置
def pytest_configure(config):
    """pytest 配置設定。"""
    # 設定測試標記
    config.addinivalue_line("markers", "unit: 標記為單元測試")
    config.addinivalue_line("markers", "integration: 標記為整合測試")
    config.addinivalue_line("markers", "slow: 標記為慢速測試")


def pytest_collection_modifyitems(config, items):
    """修改測試收集行為。"""
    # 為不同類型的測試自動添加標記
    for item in items:
        if "unit" in str(item.fspath):
            item.add_marker(pytest.mark.unit)
        elif "integration" in str(item.fspath):
            item.add_marker(pytest.mark.integration)
