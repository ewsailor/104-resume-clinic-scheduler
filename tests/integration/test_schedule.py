"""時段路由整合測試。

測試時段管理 API 的完整流程，包括建立、查詢、更新和刪除時段。
"""

# ===== 標準函式庫 =====
from datetime import date, time

# ===== 第三方套件 =====
from fastapi import status
import pytest

# ===== 本地模組 =====
from app.enums.models import ScheduleStatusEnum
from app.models.schedule import Schedule as ScheduleModel


class TestScheduleRoutes:
    """時段路由整合測試類別。"""

    @pytest.fixture
    def client(self, integration_test_client):
        """建立測試客戶端。"""
        return integration_test_client

    # ===== 建立時段 =====
    def test_create_schedules_success(
        self, client, integration_db_session, schedule_create_payload
    ):
        """測試建立時段 - 成功（201）。"""
        # GIVEN：使用 fixture 提供的資料

        # WHEN：呼叫建立時段 API
        response = client.post("/api/v1/schedules", json=schedule_create_payload)

        # THEN：確認建立成功
        assert response.status_code == status.HTTP_201_CREATED
        data = response.json()  # 轉成 Python 物件
        assert isinstance(data, list)  # 回傳格式是 list
        assert len(data) == 1

        # ===== 驗證回應資料結構 =====
        schedule_json = data[0]

        # 基本欄位驗證
        assert "id" in schedule_json
        assert schedule_json["giver_id"] == 1
        assert schedule_json["taker_id"] is None
        assert schedule_json["note"] == "測試時段"
        assert schedule_json["created_by"] == 1
        assert schedule_json["created_by_role"] == "GIVER"
        assert schedule_json["updated_by"] == 1
        assert schedule_json["updated_by_role"] == "GIVER"

        # JSON Response 只能存字串或數字，不能存 Python Enum 物件
        # 用 .value 取出 Python Enum 物件的值
        assert (
            schedule_json["status"] == ScheduleStatusEnum.AVAILABLE.value
        )  # GIVER 建立時段時狀態應為 AVAILABLE

        # JSON Response 中，date、time 是字串格式
        assert schedule_json["date"] == "2024-12-25"
        assert schedule_json["start_time"] == "09:00:00"
        assert schedule_json["end_time"] == "10:00:00"

        # 時間戳記驗證
        assert "created_at" in schedule_json
        assert "updated_at" in schedule_json
        assert schedule_json["created_at"] is not None
        assert schedule_json["updated_at"] is not None

        # 建立時，create 和 update 以下 2 個欄位應該相同
        assert schedule_json["created_by"] == schedule_json["updated_by"]
        assert schedule_json["created_by_role"] == schedule_json["updated_by_role"]

        # 軟刪除相關（建立時應為 null）
        assert schedule_json["deleted_at"] is None
        assert schedule_json["deleted_by"] is None
        assert schedule_json["deleted_by_role"] is None

        # ===== 查詢資料庫，驗證寫入的內容是否正確 =====
        # 從 API 回傳取得 id
        schedule_id = schedule_json["id"]

        # 查主鍵，故使用 get() 而不是 .query().filter(...).first()
        db_schedule = integration_db_session.get(ScheduleModel, schedule_id)

        # 驗證記錄存在
        assert db_schedule is not None

        # 驗證欄位值寫入正確
        assert db_schedule.id == schedule_json["id"]
        assert db_schedule.giver_id == 1
        assert db_schedule.taker_id is None
        assert db_schedule.note == "測試時段"
        assert db_schedule.created_by == 1
        assert db_schedule.created_by_role == "GIVER"
        assert db_schedule.updated_by == 1
        assert db_schedule.updated_by_role == "GIVER"

        # ORM 將資料庫中 Enum 物件，轉回 Python 的 Enum 物件，故可以直接用 Enum 比對
        assert db_schedule.status == ScheduleStatusEnum.AVAILABLE

        # 驗證 ORM 資料型別轉換
        # 1. 請求階段，API 傳入的 date、time 是 JSON 字串格式
        # 2. Pydantic schema 將 JSON 字串，轉成 Python 的 date、time 物件
        # 3. ORM 將 Python 的 date、time 物件，寫入 MySQL/MariaDB 資料庫成 DATE、TIME 物件
        # 4. 查詢資料庫時，ORM 將資料庫中 DATE、TIME 物件，轉回 Python 的 date、time 物件
        assert db_schedule.date == date(2024, 12, 25)
        assert db_schedule.start_time == time(9, 0, 0)
        assert db_schedule.end_time == time(10, 0, 0)
        # 驗證 ORM 物件轉為字串後，與原始請求一致 (JSON 格式)
        assert str(db_schedule.date) == "2024-12-25"
        assert str(db_schedule.start_time) == "09:00:00"
        assert str(db_schedule.end_time) == "10:00:00"

        # 時間戳記驗證
        assert db_schedule.created_at is not None
        assert db_schedule.updated_at is not None

        # 建立時，create 和 update 以下 2 個欄位應該相同
        assert db_schedule.created_by == db_schedule.updated_by
        assert db_schedule.created_by_role == db_schedule.updated_by_role

        # 軟刪除相關（建立時應為 null）
        assert db_schedule.deleted_at is None
        assert db_schedule.deleted_by is None
        assert db_schedule.deleted_by_role is None

    def test_create_schedules_end_before_start(self, client, schedule_create_payload):
        """測試建立時段 - 結束時間早於開始時間（400）。"""
        # GIVEN：使用夾具資料並修改為無效的時間邏輯
        invalid_payload = schedule_create_payload.copy()
        invalid_payload["schedules"][0]["start_time"] = "10:00:00"
        invalid_payload["schedules"][0]["end_time"] = "09:00:00"

        # WHEN：呼叫建立時段 API
        response = client.post("/api/v1/schedules", json=invalid_payload)

        # THEN：確認返回時間邏輯錯誤
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        data = response.json()
        assert "error" in data

        # 驗證錯誤回應的完整格式
        error = data["error"]
        assert error["message"] == "開始時間必須早於結束時間"
        assert error["status_code"] == 400
        assert error["code"] == "ROUTER_BAD_REQUEST"
        assert "timestamp" in error
        assert "details" in error

    def test_create_schedules_time_conflict(self, client, schedule_create_payload):
        """測試建立時段 - 時段衝突錯誤（409）。"""
        # GIVEN：先建立一個時段，然後嘗試建立重疊的時段
        # 1. 先建立第一個時段
        first_payload = schedule_create_payload.copy()
        first_payload["schedules"][0]["date"] = "2024-01-15"
        first_payload["schedules"][0]["start_time"] = "09:00:00"
        first_payload["schedules"][0]["end_time"] = "10:00:00"

        # 建立第一個時段
        first_response = client.post("/api/v1/schedules", json=first_payload)
        assert first_response.status_code == status.HTTP_201_CREATED

        # 2. 建立重疊的時段
        conflict_payload = schedule_create_payload.copy()
        conflict_payload["schedules"][0]["date"] = "2024-01-15"
        conflict_payload["schedules"][0]["start_time"] = "09:30:00"  # 與第一個時段重疊
        conflict_payload["schedules"][0]["end_time"] = "10:30:00"

        # WHEN：呼叫建立時段 API
        response = client.post("/api/v1/schedules", json=conflict_payload)

        # THEN：確認返回時段衝突錯誤
        assert response.status_code == status.HTTP_409_CONFLICT
        data = response.json()
        assert "error" in data

        # 驗證錯誤回應的完整格式
        error = data["error"]
        assert "檢測到" in error["message"]
        assert "重疊時段" in error["message"]
        assert error["status_code"] == 409
        assert error["code"] == "SERVICE_SCHEDULE_OVERLAP"
        assert "timestamp" in error
        assert "details" in error
        assert "overlapping_schedules" in error["details"]

    def test_create_schedules_validation_error(self, client, schedule_create_payload):
        """測試建立時段 - 參數驗證錯誤（422）。"""
        # GIVEN：使用夾具資料並移除必填欄位
        invalid_payload = schedule_create_payload.copy()
        invalid_payload["schedules"][0].pop("date")  # 移除必填欄位創造 422 錯誤

        # WHEN：呼叫建立時段 API
        response = client.post("/api/v1/schedules", json=invalid_payload)

        # THEN：確認返回驗證錯誤
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        data = response.json()
        assert "detail" in data

        # 驗證 422 錯誤的完整格式
        detail = data["detail"]
        assert isinstance(detail, list)
        assert len(detail) > 0

        # 驗證錯誤詳情的結構
        error_detail = detail[0]
        assert "type" in error_detail
        assert "loc" in error_detail
        assert "msg" in error_detail
        assert "input" in error_detail

    # ===== 查詢時段列表 =====
    def test_list_schedules_success(self, client, schedule_in_db):
        """測試查詢時段列表 - 成功（200）。"""
        # GIVEN：資料已經在資料庫中（通過夾具）

        # WHEN：呼叫查詢時段列表 API
        response = client.get("/api/v1/schedules")

        # THEN：確認查詢成功
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert isinstance(data, list)
        assert len(data) == 1

        # 驗證回傳資料的格式和內容
        schedule_data = data[0]

        # 基本欄位
        assert "id" in schedule_data
        assert schedule_data["giver_id"] == 1
        assert schedule_data["taker_id"] is None  # 夾具沒有設定 taker_id
        assert schedule_data["status"] == "DRAFT"  # 預設狀態
        assert schedule_data["date"] == "2024-12-25"
        assert schedule_data["start_time"] == "09:00:00"
        assert schedule_data["end_time"] == "10:00:00"
        assert schedule_data["note"] == "資料庫中的時段資料"

        # 審計欄位
        assert "created_at" in schedule_data
        assert "created_by" in schedule_data
        assert "created_by_role" in schedule_data
        assert "updated_at" in schedule_data
        assert "updated_by" in schedule_data
        assert "updated_by_role" in schedule_data

        # 系統欄位（軟刪除）
        assert "deleted_at" in schedule_data
        assert "deleted_by" in schedule_data
        assert "deleted_by_role" in schedule_data

    @pytest.mark.parametrize(
        "query_params,expected_count",
        [
            # 測試 giver_id 篩選
            ("giver_id=1", 1),  # 找到 1 筆資料
            ("giver_id=2", 0),  # 找不到資料
            # 測試 taker_id 篩選
            ("taker_id=1", 0),  # 找不到資料（夾具沒有設定 taker_id）
            ("taker_id=2", 0),  # 找不到資料
            # 測試 status 篩選
            ("status_filter=DRAFT", 1),  # 找到 1 筆資料（預設狀態）
            ("status_filter=AVAILABLE", 0),  # 找不到資料
            ("status_filter=PENDING", 0),  # 找不到資料
            # 測試組合篩選
            ("giver_id=1&status_filter=DRAFT", 1),  # 找到 1 筆資料
            ("giver_id=1&status_filter=AVAILABLE", 0),  # 找不到資料
            ("giver_id=2&status_filter=DRAFT", 0),  # 找不到資料
        ],
    )
    def test_list_schedules_with_filters(
        self, client, schedule_in_db, query_params, expected_count
    ):
        """測試查詢時段列表 - 使用篩選條件（200）。"""
        # GIVEN：資料已經在資料庫中（通過夾具）

        # WHEN：使用篩選條件查詢時段列表
        response = client.get(f"/api/v1/schedules?{query_params}")

        # THEN：確認查詢成功
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert isinstance(data, list)
        assert len(data) == expected_count

    @pytest.mark.parametrize(
        "invalid_query_params",
        [
            # 測試無效的 giver_id
            "giver_id=0",  # giver_id 必須大於 0
            "giver_id=-1",  # giver_id 不能為負數
            # 測試無效的 taker_id
            "taker_id=0.5",  # taker_id 不能為小數
            "taker_id=0",  # taker_id 必須大於 0
            # 測試無效的 status
            "status_filter=NONE_EXIST",  # 不存在的狀態
            "status_filter=INVALID",  # 無效的狀態值
            "status_filter=123",  # 非字串狀態值
            # 測試無效的組合
            "giver_id=0&status_filter=DRAFT",  # 無效 giver_id + 有效 status
            "giver_id=1&status_filter=INVALID",  # 有效 giver_id + 無效 status
        ],
    )
    def test_list_schedules_invalid_filters(self, client, invalid_query_params):
        """測試查詢時段列表 - 無效篩選條件（422）。"""
        # GIVEN：無效的查詢參數

        # WHEN：使用無效的篩選條件查詢
        response = client.get(f"/api/v1/schedules?{invalid_query_params}")

        # THEN：確認返回驗證錯誤
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        data = response.json()
        assert "detail" in data

        # 驗證 422 錯誤的完整格式
        detail = data["detail"]
        assert isinstance(detail, list)
        assert len(detail) > 0

        # 驗證錯誤詳情的結構
        error_detail = detail[0]
        assert "type" in error_detail
        assert "loc" in error_detail
        assert "msg" in error_detail
        assert "input" in error_detail

    # ===== 取得單一時段 =====
    def test_get_schedule_success(self, client, schedule_in_db):
        """測試取得單一時段 - 成功（200）。"""
        # GIVEN：資料已經在資料庫中（通過夾具）
        schedule_id = schedule_in_db.id

        # WHEN：呼叫取得單一時段 API
        response = client.get(f"/api/v1/schedules/{schedule_id}")

        # THEN：確認取得成功
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert isinstance(data, dict)  # 單一時段返回字典，不是列表

        # 驗證回傳資料的格式和內容
        # 基本欄位
        assert data["id"] == schedule_id
        assert data["giver_id"] == 1
        assert data["taker_id"] is None  # 夾具沒有設定 taker_id
        assert data["status"] == "DRAFT"  # 預設狀態
        assert data["date"] == "2024-12-25"
        assert data["start_time"] == "09:00:00"
        assert data["end_time"] == "10:00:00"
        assert data["note"] == "資料庫中的時段資料"

        # 審計欄位
        assert "created_at" in data
        assert "created_by" in data
        assert "created_by_role" in data
        assert "updated_at" in data
        assert "updated_by" in data
        assert "updated_by_role" in data

        # 系統欄位（軟刪除）
        assert "deleted_at" in data
        assert "deleted_by" in data
        assert "deleted_by_role" in data

    def test_get_schedule_not_found(self, client):
        """測試取得單一時段 - 時段不存在（404）。"""
        # GIVEN：不存在的時段 ID

        # WHEN：呼叫取得單一時段 API
        response = client.get("/api/v1/schedules/99999")

        # THEN：確認返回找不到錯誤
        assert response.status_code == status.HTTP_404_NOT_FOUND
        data = response.json()
        assert "error" in data

        # 驗證錯誤回應的完整格式
        error = data["error"]
        assert "時段不存在" in data["error"]["message"]
        assert error["message"] == "時段不存在: ID=99999"
        assert error["status_code"] == 404
        assert error["code"] == "SERVICE_SCHEDULE_NOT_FOUND"
        assert "timestamp" in error
        assert "details" in error

    def test_get_schedule_validation_error(self, client):
        """測試取得單一時段 - 參數驗證錯誤（422）。"""
        # GIVEN：無效的時段 ID（必須大於 0）

        # WHEN：使用無效的時段 ID 呼叫 API
        response = client.get("/api/v1/schedules/0")

        # THEN：確認返回驗證錯誤
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        data = response.json()
        assert "detail" in data

        # 驗證 422 錯誤的完整格式
        detail = data["detail"]
        assert isinstance(detail, list)
        assert len(detail) > 0

        # 驗證錯誤詳情的結構
        error_detail = detail[0]
        assert "type" in error_detail
        assert "loc" in error_detail
        assert "msg" in error_detail
        assert "input" in error_detail

    # ===== 更新時段 =====
    def test_update_schedule_success(
        self,
        client,
        schedule_in_db,
        schedule_update_payload,
        integration_db_session,
    ):
        """測試更新時段 - 成功（200）。"""
        # GIVEN：資料已經在資料庫中（通過夾具）
        schedule_id = schedule_in_db.id

        # WHEN：呼叫更新時段 API
        response = client.patch(
            f"/api/v1/schedules/{schedule_id}", json=schedule_update_payload
        )

        # THEN：確認更新成功
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert isinstance(data, dict)  # 回傳格式是 dict

        # ===== 驗證回應資料結構 =====
        # 驗證更新後的資料
        assert data["note"] == "更新後的時段"
        assert data["updated_by"] == 1
        assert data["updated_by_role"] == "GIVER"

        # 驗證其他欄位保持不變
        assert data["id"] == schedule_id
        assert data["giver_id"] == 1
        assert data["taker_id"] is None
        assert data["status"] == "DRAFT"  # 夾具中的預設狀態
        assert data["date"] == "2024-12-25"
        assert data["start_time"] == "09:00:00"
        assert data["end_time"] == "10:00:00"
        assert data["created_by"] is None  # 夾具中沒有設定 created_by
        assert data["created_by_role"] == "SYSTEM"  # 預設角色

        # 時間戳記驗證
        assert "created_at" in data
        assert "updated_at" in data
        assert data["created_at"] is not None
        assert data["updated_at"] is not None

        # 更新後，updated_at 應該不同於 created_at
        assert data["created_at"] != data["updated_at"]

        # 軟刪除相關（更新時應仍為 null）
        assert data["deleted_at"] is None
        assert data["deleted_by"] is None
        assert data["deleted_by_role"] is None

        # ===== 查詢資料庫，驗證更新後的內容是否正確 =====
        # 查主鍵，故使用 get() 而不是 .query().filter(...).first()
        db_schedule = integration_db_session.get(ScheduleModel, schedule_id)

        # 驗證記錄存在
        assert db_schedule is not None

        # 驗證更新後的資料
        assert db_schedule.note == "更新後的時段"
        assert db_schedule.updated_by == 1
        assert db_schedule.updated_by_role == "GIVER"

        # 驗證其他欄位保持不變
        assert db_schedule.id == schedule_id
        assert db_schedule.giver_id == 1
        assert db_schedule.taker_id is None
        assert db_schedule.created_by is None  # 夾具中沒有設定 created_by
        assert db_schedule.created_by_role == "SYSTEM"  # 預設角色

        # ORM 將資料庫中 Enum 物件，轉回 Python 的 Enum 物件，故可以直接用 Enum 比對
        assert db_schedule.status == ScheduleStatusEnum.DRAFT  # 夾具中的預設狀態

        # 驗證 ORM 資料型別轉換
        # 1. 請求階段，API 傳入的 date、time 是 JSON 字串格式
        # 2. Pydantic schema 將 JSON 字串，轉成 Python 的 date、time 物件
        # 3. ORM 將 Python 的 date、time 物件，寫入 MySQL/MariaDB 資料庫成 DATE、TIME 物件
        # 4. 查詢資料庫時，ORM 將資料庫中 DATE、TIME 物件，轉回 Python 的 date、time 物件
        assert db_schedule.date == date(2024, 12, 25)
        assert db_schedule.start_time == time(9, 0, 0)
        assert db_schedule.end_time == time(10, 0, 0)
        # 驗證 ORM 物件轉為字串後，與原始請求一致 (JSON 格式)
        assert str(db_schedule.date) == "2024-12-25"
        assert str(db_schedule.start_time) == "09:00:00"
        assert str(db_schedule.end_time) == "10:00:00"

        # 時間戳記驗證
        assert db_schedule.created_at is not None
        assert db_schedule.updated_at is not None

        # 更新後，updated_at 應該不同於 created_at
        assert db_schedule.created_at != db_schedule.updated_at

        # 軟刪除相關（更新時應仍為 null）
        assert db_schedule.deleted_at is None
        assert db_schedule.deleted_by is None
        assert db_schedule.deleted_by_role is None

    def test_update_schedule_end_before_start(
        self, client, schedule_in_db, schedule_update_payload
    ):
        """測試更新時段 - 參數驗證錯誤（400）。"""
        # GIVEN：資料已經在資料庫中（通過夾具）
        schedule_id = schedule_in_db.id

        # 修改為無效的時間邏輯：結束時間早於開始時間
        invalid_data = schedule_update_payload.copy()
        invalid_data["schedule"]["start_time"] = "10:00:00"
        invalid_data["schedule"]["end_time"] = "09:00:00"

        # WHEN：呼叫更新時段 API
        response = client.patch(f"/api/v1/schedules/{schedule_id}", json=invalid_data)

        # THEN：確認返回驗證錯誤
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        data = response.json()
        assert "error" in data

        # 驗證錯誤回應的完整格式
        error = data["error"]
        assert error["message"] == "開始時間必須早於結束時間"
        assert error["status_code"] == 400
        assert error["code"] == "ROUTER_BAD_REQUEST"
        assert "timestamp" in error
        assert "details" in error

    def test_update_schedule_not_found(self, client, schedule_update_payload):
        """測試更新時段 - 時段不存在（404）。"""
        # GIVEN：不存在的時段 ID 和有效的更新資料

        # WHEN：呼叫更新時段 API
        response = client.patch("/api/v1/schedules/99999", json=schedule_update_payload)

        # THEN：確認返回找不到錯誤
        assert response.status_code == status.HTTP_404_NOT_FOUND
        data = response.json()
        assert "error" in data

        # 驗證錯誤回應的完整格式
        error = data["error"]
        assert error["message"] == "時段不存在: ID=99999"
        assert error["status_code"] == 404
        assert error["code"] == "SERVICE_SCHEDULE_NOT_FOUND"
        assert "timestamp" in error
        assert "details" in error

    def test_update_schedule_time_conflict(
        self, client, schedule_in_db, schedule_update_payload, schedule_create_payload
    ):
        """測試更新時段 - 時段衝突錯誤（409）。"""
        # GIVEN：先建立一個時段，然後嘗試更新為重疊的時段
        # 1. 先建立第一個時段
        first_payload = schedule_create_payload.copy()
        first_payload["schedules"][0]["date"] = "2024-01-15"
        first_payload["schedules"][0]["start_time"] = "09:00:00"
        first_payload["schedules"][0]["end_time"] = "10:00:00"

        # 建立第一個時段
        first_response = client.post("/api/v1/schedules", json=first_payload)
        assert first_response.status_code == status.HTTP_201_CREATED

        # 2. 更新現有時段為重疊的時間
        schedule_id = schedule_in_db.id
        conflict_update_data = schedule_update_payload.copy()
        conflict_update_data["schedule"]["date"] = "2024-01-15"
        conflict_update_data["schedule"]["start_time"] = "09:30:00"  # 與第一個時段重疊
        conflict_update_data["schedule"]["end_time"] = "10:30:00"

        # WHEN：呼叫更新時段 API
        response = client.patch(
            f"/api/v1/schedules/{schedule_id}", json=conflict_update_data
        )

        # THEN：確認返回時段衝突錯誤
        assert response.status_code == status.HTTP_409_CONFLICT
        data = response.json()
        assert "error" in data

        # 驗證錯誤回應的完整格式
        error = data["error"]
        assert "更新時段" in error["message"]
        assert "檢測到" in error["message"]
        assert "重疊時段" in error["message"]
        assert error["status_code"] == 409
        assert error["code"] == "SERVICE_SCHEDULE_OVERLAP"
        assert "timestamp" in error
        assert "details" in error
        assert "overlapping_schedules" in error["details"]

    def test_update_schedule_validation_error(
        self, client, schedule_in_db, schedule_update_payload
    ):
        """測試更新時段 - 參數驗證錯誤（422）。"""
        # GIVEN：資料已經在資料庫中（通過夾具）
        schedule_id = schedule_in_db.id

        # 使用夾具資料並添加無效的欄位值創造 422 錯誤
        invalid_data = schedule_update_payload.copy()
        invalid_data["schedule"]["giver_id"] = -1  # 無效的 giver_id（必須大於 0）

        # WHEN：呼叫更新時段 API
        response = client.patch(f"/api/v1/schedules/{schedule_id}", json=invalid_data)

        # THEN：確認返回驗證錯誤
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        data = response.json()
        assert "detail" in data

        # 驗證 422 錯誤的完整格式
        detail = data["detail"]
        assert isinstance(detail, list)
        assert len(detail) > 0

        # 驗證錯誤詳情的結構
        error_detail = detail[0]
        assert "type" in error_detail
        assert "loc" in error_detail
        assert "msg" in error_detail
        assert "input" in error_detail

    # ===== 刪除時段 =====
    def test_delete_schedule_success(
        self,
        client,
        schedule_in_db,
        schedule_delete_payload,
        integration_db_session,
    ):
        """測試刪除時段 - 成功（204）。"""
        # GIVEN：資料已經在資料庫中（通過夾具）
        schedule_id = schedule_in_db.id

        # WHEN：呼叫刪除時段 API
        # client.delete() 不支援 json、data 參數，故使用 client.request() 方法
        response = client.request(
            "DELETE",
            f"/api/v1/schedules/{schedule_id}",
            json=schedule_delete_payload,
        )

        # THEN：確認刪除成功
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert response.content == b""  # 204 回應應該為空

        # ===== 查詢資料庫，驗證軟刪除的內容是否正確 =====
        # 查主鍵，故使用 get() 而不是 .query().filter(...).first()
        db_schedule = integration_db_session.get(ScheduleModel, schedule_id)

        # 驗證記錄存在（軟刪除不會真正刪除記錄）
        assert db_schedule is not None

        # 驗證基本欄位保持不變
        assert db_schedule.id == schedule_id
        assert db_schedule.giver_id == 1
        assert db_schedule.taker_id is None
        assert db_schedule.note == "資料庫中的時段資料"  # 夾具中的資料
        assert db_schedule.created_by is None  # 夾具中沒有設定 created_by
        assert db_schedule.created_by_role == "SYSTEM"  # 預設角色
        assert db_schedule.updated_by == 1
        assert db_schedule.updated_by_role == "GIVER"

        # ORM 將資料庫中 Enum 物件，轉回 Python 的 Enum 物件，故可以直接用 Enum 比對
        # 刪除時段時，狀態會自動改為 CANCELLED
        assert db_schedule.status == ScheduleStatusEnum.CANCELLED

        # 驗證 ORM 資料型別轉換
        # 1. 請求階段，API 傳入的 date、time 是 JSON 字串格式
        # 2. Pydantic schema 將 JSON 字串，轉成 Python 的 date、time 物件
        # 3. ORM 將 Python 的 date、time 物件，寫入 MySQL/MariaDB 資料庫成 DATE、TIME 物件
        # 4. 查詢資料庫時，ORM 將資料庫中 DATE、TIME 物件，轉回 Python 的 date、time 物件
        assert db_schedule.date == date(2024, 12, 25)
        assert db_schedule.start_time == time(9, 0, 0)
        assert db_schedule.end_time == time(10, 0, 0)
        # 驗證 ORM 物件轉為字串後，與原始請求一致 (JSON 格式)
        assert str(db_schedule.date) == "2024-12-25"
        assert str(db_schedule.start_time) == "09:00:00"
        assert str(db_schedule.end_time) == "10:00:00"

        # 時間戳記驗證
        assert db_schedule.created_at is not None
        assert db_schedule.updated_at is not None

        # 軟刪除相關（刪除後應設定）
        assert db_schedule.deleted_at is not None  # 刪除時間應該被設定
        assert db_schedule.deleted_by == 1  # 刪除者應為 1
        assert db_schedule.deleted_by_role == "GIVER"  # 刪除者角色應為 GIVER

        # 驗證 is_deleted 屬性
        assert db_schedule.is_deleted is True
        assert db_schedule.is_active is False

    def test_delete_schedule_not_found(self, client, schedule_delete_payload):
        """測試刪除時段 - 時段不存在（404）。"""
        # GIVEN：不存在的時段 ID 和有效的刪除資料

        # WHEN：呼叫刪除時段 API
        response = client.request(
            "DELETE",
            "/api/v1/schedules/99999",
            json=schedule_delete_payload,
        )

        # THEN：確認返回找不到錯誤
        assert response.status_code == status.HTTP_404_NOT_FOUND
        data = response.json()
        assert "error" in data

        # 驗證錯誤回應的完整格式
        error = data["error"]
        assert error["message"] == "時段不存在: ID=99999"
        assert error["status_code"] == 404
        assert error["code"] == "SERVICE_SCHEDULE_NOT_FOUND"
        assert "timestamp" in error
        assert "details" in error

    @pytest.mark.parametrize(
        "status_enum,expected_status_name",
        [
            (ScheduleStatusEnum.ACCEPTED, "ACCEPTED"),
            (ScheduleStatusEnum.COMPLETED, "COMPLETED"),
        ],
    )
    def test_delete_schedule_cannot_be_deleted(
        self,
        client,
        schedule_in_db,
        schedule_delete_payload,
        status_enum,
        expected_status_name,
    ):
        """測試刪除時段 - 時段無法刪除錯誤（409）。"""
        # GIVEN：資料已經在資料庫中（通過夾具），但狀態不允許刪除
        schedule_id = schedule_in_db.id

        # 將時段狀態設為不允許刪除的狀態
        schedule_in_db.status = status_enum

        # WHEN：呼叫刪除時段 API
        response = client.request(
            "DELETE",
            f"/api/v1/schedules/{schedule_id}",
            json=schedule_delete_payload,
        )

        # THEN：確認返回時段無法刪除錯誤
        assert response.status_code == status.HTTP_409_CONFLICT
        data = response.json()
        assert "error" in data

        # 驗證錯誤回應的完整格式
        error = data["error"]
        assert "時段無法刪除" in error["message"]
        assert "ID=" in error["message"]
        assert error["status_code"] == 409
        assert error["code"] == "SERVICE_SCHEDULE_CANNOT_BE_DELETED"
        assert "timestamp" in error
        assert "details" in error
        assert "reason" in error["details"]
        assert "current_status" in error["details"]
        assert "explanation" in error["details"]

        # 驗證當前狀態
        assert error["details"]["current_status"] == expected_status_name

    def test_delete_schedule_validation_error(
        self, client, schedule_in_db, schedule_delete_payload
    ):
        """測試刪除時段 - 參數驗證錯誤（422）。"""
        # GIVEN：資料已經在資料庫中（通過夾具）
        schedule_id = schedule_in_db.id

        # 修改為無效的刪除資料，創造 422 錯誤
        invalid_data = schedule_delete_payload.copy()
        invalid_data["deleted_by"] = -1  # 無效的 deleted_by（必須大於 0）

        # WHEN：呼叫刪除時段 API
        response = client.request(
            "DELETE",
            f"/api/v1/schedules/{schedule_id}",
            json=invalid_data,
        )

        # THEN：確認返回驗證錯誤
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        data = response.json()
        assert "detail" in data

        # 驗證 422 錯誤的完整格式
        detail = data["detail"]
        assert isinstance(detail, list)
        assert len(detail) > 0

        # 驗證錯誤詳情的結構
        error_detail = detail[0]
        assert "type" in error_detail
        assert "loc" in error_detail
        assert "msg" in error_detail
        assert "input" in error_detail
