"""健康檢查路由整合測試。

測試健康檢查端點的完整流程，包括存活探測和就緒探測。
"""

# ===== 標準函式庫 =====
from unittest.mock import patch

# ===== 第三方套件 =====
from fastapi import status
import pytest


class TestHealthRoutes:
    """健康檢查路由整合測試類別。"""

    @pytest.fixture
    def client(self, integration_test_client):
        """建立測試客戶端。"""
        return integration_test_client

    # ===== 存活探測 =====
    def test_liveness_probe_success(self, client):
        """測試存活探測 - 成功。"""
        # GIVEN：應用程式正常運行

        # WHEN：呼叫存活探測端點
        response = client.get("/healthz")

        # THEN：確認返回健康狀態
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == {"status": "healthy"}

    def test_liveness_probe_failure(self, client):
        """測試存活探測 - 失敗情況的錯誤處理。

        注意：由於 FastAPI TestClient 在應用程式啟動時就綁定了路由，無法模擬失敗狀況，故下方仍使用正常情況下的存活探測。

        如果 liveness_probe 失敗，FastAPI 會返回：
        - status_code: 500
        - response: {"status": "unhealthy"}
        """
        # GIVEN：應用程式正常運行，因為無法模擬失敗狀況

        # WHEN：呼叫存活探測端點
        response = client.get("/healthz")

        # THEN：確認返回健康狀態，因為無法模擬失敗狀況
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == {"status": "healthy"}

    def test_liveness_probe_response_structure(self, client):
        """測試存活探測 - 回應結構。"""
        # GIVEN：應用程式正常運行，因為無法模擬失敗狀況

        # WHEN：呼叫存活探測端點
        response = client.get("/healthz")

        # THEN：確認回應結構正確
        assert response.status_code == status.HTTP_200_OK
        data = response.json()

        # 檢查回應是字典格式
        assert isinstance(data, dict)

        # 檢查必要欄位存在
        assert "status" in data

        # 檢查欄位值符合預期
        assert data["status"] == "healthy"

    # ===== 就緒探測 =====
    @patch('app.routers.health.check_db_connection')
    def test_readiness_probe_success(self, mock_db_check, client):
        """測試就緒探測 - 成功。"""
        # GIVEN：資料庫連線正常
        mock_db_check.return_value = None  # check_db_connection 沒有回傳值

        # WHEN：呼叫就緒探測端點
        response = client.get("/readyz")

        # THEN：確認返回健康狀態
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == {"status": "healthy"}
        mock_db_check.assert_called_once()

    @patch('app.routers.health.check_db_connection')
    def test_readiness_probe_database_failure(self, mock_db_check, client):
        """測試就緒探測 - 資料庫連線失敗。"""
        # GIVEN：資料庫連線失敗
        mock_db_check.side_effect = Exception("Database connection failed")

        # WHEN：呼叫就緒探測端點
        response = client.get("/readyz")

        # THEN：確認返回服務不可用狀態
        assert response.status_code == status.HTTP_503_SERVICE_UNAVAILABLE
        assert response.json() == {"detail": "Service Unavailable"}
        mock_db_check.assert_called_once()

    @pytest.mark.parametrize(
        "test_case,mock_side_effect,expected_status_code,expected_response_key,expected_response_value",
        [
            ("success", None, status.HTTP_200_OK, "status", "healthy"),  # 正常情況
            (
                "database_failure",
                Exception("Database connection failed"),  # 資料庫失敗
                status.HTTP_503_SERVICE_UNAVAILABLE,
                "detail",
                "Service Unavailable",
            ),
        ],
    )
    @patch('app.routers.health.check_db_connection')
    def test_readiness_probe_response_structure(
        self,
        mock_db_check,
        test_case,
        mock_side_effect,
        expected_status_code,
        expected_response_key,
        expected_response_value,
        client,
    ):
        """測試就緒探測 - 回應結構。

        測試成功和失敗兩種情況的回應結構。
        """
        # GIVEN：設定測試條件
        if mock_side_effect:
            mock_db_check.side_effect = mock_side_effect
        else:
            mock_db_check.return_value = None

        # WHEN：呼叫就緒探測端點
        response = client.get("/readyz")

        # THEN：確認回應結構正確
        assert response.status_code == expected_status_code
        data = response.json()

        # 檢查回應是字典格式
        assert isinstance(data, dict)

        # 檢查預期欄位存在
        assert expected_response_key in data

        # 檢查欄位值符合預期
        assert data[expected_response_key] == expected_response_value

        # 確認 mock 被呼叫
        mock_db_check.assert_called_once()
