"""時段 CRUD 操作測試模組。

測試時段相關的資料庫操作，包括建立、查詢、更新和刪除時段。
"""

# ===== 標準函式庫 =====
from datetime import date, time
from unittest.mock import patch

# ===== 第三方套件 =====
import pytest
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import joinedload, Session

# ===== 本地模組 =====
from app.crud.schedule import ScheduleCRUD
from app.enums.models import ScheduleStatusEnum, UserRoleEnum
from app.errors.exceptions import BadRequestError, ScheduleNotFoundError
from app.models.schedule import Schedule
from app.utils.timezone import get_local_now_naive


class TestScheduleCRUD:
    """時段 CRUD 操作測試類別。"""

    @pytest.fixture(autouse=True)
    def setup_crud(self):
        """設定 CRUD 實例，每個測試自動使用。"""
        self.crud = ScheduleCRUD()

    # ===== 建立多個時段 =====
    def test_create_single_giver_schedule_success(
        self, db_session: Session, test_giver_schedule: Schedule
    ):
        """測試 Giver 成功建立單一時段。"""
        # Given: 使用夾具的時段資料

        # When: 建立時段
        schedules = self.crud.create_schedules(db_session, [test_giver_schedule])

        # Then: 驗證建立結果
        assert len(schedules) == 1

        # Then: 驗證資料完整性
        assert schedules[0].giver_id == test_giver_schedule.giver_id
        assert schedules[0].date == test_giver_schedule.date
        assert schedules[0].start_time == test_giver_schedule.start_time
        assert schedules[0].end_time == test_giver_schedule.end_time
        assert schedules[0].note == test_giver_schedule.note

        # Then: 驗證業務邏輯
        assert schedules[0].taker_id is None
        assert schedules[0].status == test_giver_schedule.status
        assert schedules[0].is_available is True

    @pytest.mark.parametrize(
        "field_name,invalid_value",
        [
            ("giver_id", None),
            ("date", None),
            ("start_time", None),
            ("end_time", None),
        ],
    )
    def test_create_single_giver_schedule_null_constraint_errors(
        self,
        db_session: Session,
        test_giver_schedule_data: dict,
        field_name: str,
        invalid_value: None,
    ) -> None:
        """測試 Giver 建立單一時段：非空約束錯誤。

        使用參數化測試來測試所有 nullable=False 的欄位。
        """
        # Given: 使用夾具的時段資料
        schedule_data = test_giver_schedule_data.copy()

        # When: 嘗試建立無效時段，將指定欄位設為無效值
        schedule_data[field_name] = invalid_value

        # Then: 應該拋出 IntegrityError
        with pytest.raises(IntegrityError):
            invalid_schedule = Schedule(**schedule_data)
            self.crud.create_schedules(db_session, [invalid_schedule])

    def test_create_multiple_giver_schedules_success(
        self,
        db_session: Session,
    ):
        """測試 Giver 成功建立多個時段。"""
        # Given: 準備多個時段資料
        schedules_data = [
            Schedule(
                giver_id=1,
                taker_id=None,
                status=ScheduleStatusEnum.AVAILABLE,
                date=date(2024, 1, 1),
                start_time=time(9, 0),
                end_time=time(10, 0),
                note="Giver 時段 1",
            ),
            Schedule(
                giver_id=1,
                taker_id=None,
                status=ScheduleStatusEnum.AVAILABLE,
                date=date(2024, 1, 2),
                start_time=time(14, 0),
                end_time=time(15, 0),
                note="Giver 時段 2",
            ),
        ]

        # When: 建立多個時段
        schedules = self.crud.create_schedules(db_session, schedules_data)

        # Then: 驗證建立結果
        assert len(schedules) == 2

        # Then: 驗證資料完整性
        assert schedules[0].giver_id == 1
        assert schedules[0].date == date(2024, 1, 1)
        assert schedules[0].start_time == time(9, 0)
        assert schedules[0].end_time == time(10, 0)
        assert schedules[0].note == "Giver 時段 1"

        assert schedules[1].giver_id == 1
        assert schedules[1].date == date(2024, 1, 2)
        assert schedules[1].start_time == time(14, 0)
        assert schedules[1].end_time == time(15, 0)
        assert schedules[1].note == "Giver 時段 2"

        # Then: 驗證業務邏輯
        assert all(s.taker_id is None for s in schedules)
        assert all(s.status == ScheduleStatusEnum.AVAILABLE for s in schedules)
        assert all(s.is_available is True for s in schedules)

    def test_create_single_taker_schedule_success(
        self, db_session: Session, test_taker_schedule: Schedule
    ):
        """測試 Taker 成功建立單一時段。"""
        # Given: 使用夾具的時段資料

        # When: 建立時段
        schedules = self.crud.create_schedules(db_session, [test_taker_schedule])

        # Then: 驗證建立結果
        assert len(schedules) == 1

        # Then: 驗證資料完整性
        assert schedules[0].giver_id == test_taker_schedule.giver_id
        assert schedules[0].taker_id == test_taker_schedule.taker_id
        assert schedules[0].date == test_taker_schedule.date
        assert schedules[0].start_time == test_taker_schedule.start_time
        assert schedules[0].end_time == test_taker_schedule.end_time
        assert schedules[0].note == test_taker_schedule.note

        # Then: 驗證業務邏輯
        assert schedules[0].status == test_taker_schedule.status

    @pytest.mark.parametrize(
        "field_name,invalid_value",
        [
            ("giver_id", None),
            ("date", None),
            ("start_time", None),
            ("end_time", None),
        ],
    )
    def test_create_single_taker_schedule_null_constraint_errors(
        self,
        db_session: Session,
        test_taker_schedule_data: dict,
        field_name: str,
        invalid_value: None,
    ) -> None:
        """測試 Taker 建立單一時段：非空約束錯誤。

        使用參數化測試來測試所有 nullable=False 的欄位。
        """
        # Given: 使用夾具的時段資料
        schedule_data = test_taker_schedule_data.copy()
        # 將指定欄位設為無效值
        schedule_data[field_name] = invalid_value

        # When: 嘗試建立無效時段

        # Then: 應該拋出 IntegrityError
        with pytest.raises(IntegrityError):
            invalid_schedule = Schedule(**schedule_data)
            self.crud.create_schedules(db_session, [invalid_schedule])

    def test_create_multiple_taker_schedules_success(self, db_session: Session):
        """測試 Taker 成功建立多個時段。"""
        # Given: 準備多個時段資料
        schedules_data = [
            Schedule(
                giver_id=1,
                taker_id=1,
                status=ScheduleStatusEnum.PENDING,
                date=date(2024, 1, 1),
                start_time=time(9, 0),
                end_time=time(10, 0),
                note="Taker 時段 1",
            ),
            Schedule(
                giver_id=1,
                taker_id=1,
                status=ScheduleStatusEnum.PENDING,
                date=date(2024, 1, 2),
                start_time=time(14, 0),
                end_time=time(15, 0),
                note="Taker 時段 2",
            ),
        ]

        # When: 建立多個時段
        schedules = self.crud.create_schedules(db_session, schedules_data)

        # Then: 驗證建立結果
        assert len(schedules) == 2

        # Then: 驗證資料完整性
        assert schedules[0].giver_id == 1
        assert schedules[0].taker_id == 1
        assert schedules[0].date == date(2024, 1, 1)
        assert schedules[0].start_time == time(9, 0)
        assert schedules[0].end_time == time(10, 0)
        assert schedules[0].note == "Taker 時段 1"

        assert schedules[1].giver_id == 1
        assert schedules[1].taker_id == 1
        assert schedules[1].date == date(2024, 1, 2)
        assert schedules[1].start_time == time(14, 0)
        assert schedules[1].end_time == time(15, 0)
        assert schedules[1].note == "Taker 時段 2"

        # Then: 驗證業務邏輯
        assert all(s.status == ScheduleStatusEnum.PENDING for s in schedules)

    # ===== 查詢選項 =====
    def test_get_schedule_query_options_default(self):
        """測試取得時段查詢選項：預設行為。"""
        # Given: 測試預設行為（include_relations=None）

        # When: 取得時段查詢選項
        options = self.crud.get_schedule_query_options()

        # Then: 驗證返回所有關聯載入選項
        assert len(options) == 3
        # 驗證所有選項都是 SQLAlchemy 的關聯載入選項（具有 path 屬性）
        assert all(hasattr(opt, 'path') for opt in options)

    def test_get_schedule_query_options_with_relations(self):
        """測試取得時段查詢選項：指定有效關聯。"""
        # Given: 測試指定有效關聯
        include_relations = ['created_by_user', 'updated_by_user']

        # When: 取得時段查詢選項
        options = self.crud.get_schedule_query_options(include_relations)

        # Then: 驗證返回所有關聯載入選項
        assert len(include_relations) == 2
        assert len(options) == 2
        assert all(hasattr(opt, 'path') for opt in options)

    def test_get_schedule_query_options_with_invalid_relations(self):
        """測試取得時段查詢選項：包含無效關聯。"""
        # Given: 測試包含無效關聱名稱
        include_relations = ['created_by_user', 'invalid_relation', 'updated_by_user']

        # When: 取得時段查詢選項
        options = self.crud.get_schedule_query_options(include_relations)

        # Then: 驗證只返回有效的關聯選項（2個有效關聯）
        assert len(include_relations) == 3
        assert len(options) == 2
        assert all(hasattr(opt, 'path') for opt in options)

    # ===== 篩選功能測試 =====
    @pytest.mark.parametrize(
        "include_deleted,expected_count,description",
        [
            (False, 0, "排除已刪除記錄（預設行為）"),
            (True, 1, "包含已刪除記錄"),
        ],
    )
    def test_apply_filters_deleted_records(
        self,
        db_session: Session,
        test_giver_schedule: Schedule,
        include_deleted: bool,
        expected_count: int,
        description: str,
    ):
        """測試套用篩選條件：包含/排除已刪除記錄。"""
        # Given: 軟刪除時段
        test_giver_schedule.deleted_at = get_local_now_naive()
        test_giver_schedule.deleted_by = test_giver_schedule.giver_id
        test_giver_schedule.deleted_by_role = UserRoleEnum.GIVER
        db_session.commit()

        # Given: 建立查詢
        query = db_session.query(Schedule)

        # When: 套用篩選條件
        filtered_query = self.crud._apply_filters(
            query,
            include_deleted=include_deleted,
        )
        results = filtered_query.all()

        # Then: 驗證結果數量
        assert len(results) == expected_count

        # Then: 驗證結果內容（如果包含已刪除記錄）
        if include_deleted and expected_count > 0:
            assert results[0].deleted_at is not None

    @pytest.mark.parametrize(
        "giver_id,taker_id,status_filter,expected_count,description",
        [
            # 單一條件篩選
            (
                1,
                None,
                None,
                2,
                "單一條件：giver_id 篩選",
            ),  # 兩個夾具都有相同的 giver_id
            (
                None,
                1,
                None,
                1,
                "單一條件：taker_id 篩選",
            ),  # 只有 test_taker_schedule 有 taker_id
            (
                None,
                None,
                ScheduleStatusEnum.AVAILABLE,
                1,
                "單一條件：status 篩選",
            ),  # 只有 test_giver_schedule 是 AVAILABLE 狀態
            # 多重條件篩選
            (
                1,
                None,
                ScheduleStatusEnum.AVAILABLE,
                1,
                "多重條件：giver_id + status 篩選",
            ),
            (1, 1, None, 1, "多重條件：giver_id + taker_id 篩選"),
            (
                None,
                1,
                ScheduleStatusEnum.PENDING,
                1,
                "多重條件：taker_id + status 篩選",
            ),
            (1, 1, ScheduleStatusEnum.PENDING, 1, "多重條件：所有條件篩選"),
            # 無篩選條件
            (None, None, None, 2, "無篩選條件：查詢所有時段"),
        ],
    )
    def test_apply_filters_conditions(
        self,
        db_session: Session,
        test_giver_schedule: Schedule,
        test_taker_schedule: Schedule,
        giver_id: int | None,
        taker_id: int | None,
        status_filter: ScheduleStatusEnum | None,
        expected_count: int,
        description: str,
    ):
        """測試套用篩選條件：各種篩選參數組合。"""
        # Given: 使用夾具的時段資料，建立查詢
        query = db_session.query(Schedule)

        # When: 套用篩選條件
        filtered_query = self.crud._apply_filters(
            query,
            giver_id=giver_id,
            taker_id=taker_id,
            status_filter=status_filter.value if status_filter else None,
            include_deleted=False,
        )
        results = filtered_query.all()

        # Then: 驗證結果數量
        assert len(results) == expected_count

        # Then: 驗證結果內容，確保每個返回的時段都符合篩選條件
        for schedule in results:
            # 驗證 giver_id 篩選條件
            if giver_id is not None:
                assert schedule.giver_id == giver_id

            # 驗證 taker_id 篩選條件
            if taker_id is not None:
                assert schedule.taker_id == taker_id

            # 驗證 status 篩選條件
            if status_filter is not None:
                assert schedule.status == status_filter

    @pytest.mark.parametrize(
        "giver_id,taker_id",
        [
            # 無效的 giver_id 值
            (-1, None),  # 負數 ID
            (0, None),  # 零 ID
            # 無效的 taker_id 值
            (None, -1),  # 負數 ID
            (None, 0),  # 零 ID
            # 組合無效值
            (-1, -1),  # 負數 ID 組合
            (0, 0),  # 零 ID 組合
        ],
    )
    def test_apply_filters_invalid_id_values(
        self, db_session: Session, giver_id: int | None, taker_id: int | None
    ):
        """測試套用篩選條件：無效的 ID 值。

        unsigned 約束：只在插入數據時生效，不在查詢時生效。
        故不會拋出異常，但業務邏輯無效。"""
        # Given: 準備查詢對象
        query = db_session.query(Schedule)

        # When: 套用無效的 ID 篩選條件
        result = self.crud._apply_filters(
            query,
            giver_id=giver_id,
            taker_id=taker_id,
            status_filter=None,
            include_deleted=False,
        )

        # Then: 驗證方法返回了查詢對象（SQLAlchemy 不會拋出異常）
        assert result is not None

    @pytest.mark.parametrize(
        "status_filter,expected_error",
        [
            ("INVALID_STATUS", "'INVALID_STATUS' is not a valid ScheduleStatusEnum"),
            ("", "'' is not a valid ScheduleStatusEnum"),
            ("draft", "'draft' is not a valid ScheduleStatusEnum"),  # 小寫
            ("AVAILABLE ", "'AVAILABLE ' is not a valid ScheduleStatusEnum"),  # 有空格
            ("NONE", "'NONE' is not a valid ScheduleStatusEnum"),
        ],
    )
    def test_apply_filters_invalid_status_filter(
        self, db_session: Session, status_filter: str, expected_error: str
    ):
        """測試套用篩選條件：無效的狀態篩選值（會拋出異常）。"""
        # Given: 準備查詢對象
        query = db_session.query(Schedule)

        # When & Then: 確認拋出 ValueError
        with pytest.raises(ValueError, match=expected_error):
            self.crud._apply_filters(
                query,
                giver_id=None,
                taker_id=None,
                status_filter=status_filter,
                include_deleted=False,
            )

    # ===== 查詢時段列表測試 =====
    def test_list_schedules(
        self,
        db_session: Session,
        test_giver_schedule: Schedule,
        test_taker_schedule: Schedule,
    ):
        """測試查詢所有時段 - 成功。"""
        # Given: 使用夾具的時段資料

        # When: 查詢所有時段
        schedules = self.crud.list_schedules(db_session)

        # Then: 驗證返回的時段數量
        assert len(schedules) == 2

    @pytest.mark.parametrize(
        "mock_options_count,description",
        [
            (0, "不載入任何關聯"),
            (1, "只載入 created_by_user"),
            (2, "載入兩個關聯"),
            (3, "載入所有關聯：created_by_user, updated_by_user, deleted_by_user"),
        ],
    )
    def test_list_schedules_query_options_success(
        self,
        db_session: Session,
        test_giver_schedule: Schedule,
        mock_options_count: int,
        description: str,
    ):
        """測試 list_schedules 方法的查詢選項功能：成功載入關聯資料。"""
        # Given: 使用夾具的時段資料，並 mock get_schedule_query_options 方法
        with patch.object(self.crud, 'get_schedule_query_options') as mock_options:
            # 設定 mock 返回值：返回指定數量的查詢選項
            mock_options.return_value = [
                joinedload(Schedule.created_by_user) for _ in range(mock_options_count)
            ]

            # When: 查詢時段（會應用 get_schedule_query_options）
            schedules = self.crud.list_schedules(
                db_session, giver_id=test_giver_schedule.giver_id
            )

            # Then: 驗證 get_schedule_query_options 被正確呼叫
            mock_options.assert_called_once_with()

            # 驗證返回了時段列表
            assert len(schedules) > 0
            assert isinstance(schedules, list)

    @pytest.mark.parametrize(
        "invalid_relations,expected_warning",
        [
            (['invalid_relation'], "忽略無效的關聯名稱: ['invalid_relation']"),
            (
                ['created_by_user', 'invalid_relation'],
                "忽略無效的關聯名稱: ['invalid_relation']",
            ),
            (['invalid1', 'invalid2'], "忽略無效的關聯名稱: ['invalid1', 'invalid2']"),
        ],
    )
    def test_list_schedules_query_options_failure(
        self,
        db_session: Session,
        test_giver_schedule: Schedule,
        invalid_relations: list[str],
        expected_warning: str,
    ):
        """測試 list_schedules 方法的查詢選項功能：無效關聯名稱處理。"""
        # Given: 使用夾具的時段資料
        with patch.object(self.crud, 'get_schedule_query_options') as mock_options:
            # 設定 mock 返回空列表（模擬無效關聯的情況）
            mock_options.return_value = []

            # When: 查詢時段
            schedules = self.crud.list_schedules(
                db_session, giver_id=test_giver_schedule.giver_id
            )

            # Then: 驗證 get_schedule_query_options 被正確呼叫
            mock_options.assert_called_once_with()

            # 驗證仍然返回了時段列表（不會因為無效關聯而失敗）
            assert len(schedules) > 0

    @pytest.mark.parametrize(
        "giver_id,taker_id,status_filter,expected_count,description",
        [
            (1, None, None, 2, "giver_id 篩選成功"),
            (None, 1, None, 1, "taker_id 篩選成功"),
            (None, None, "AVAILABLE", 1, "status_filter 篩選成功"),
            (1, 1, "PENDING", 1, "多重篩選條件成功"),
        ],
    )
    def test_list_schedules_apply_filters_success(
        self,
        db_session: Session,
        test_giver_schedule: Schedule,
        test_taker_schedule: Schedule,
        giver_id: int | None,
        taker_id: int | None,
        status_filter: str | None,
        expected_count: int,
        description: str,
    ):
        """測試 list_schedules 方法的篩選功能：成功套用篩選條件。"""
        # Given: 使用夾具的時段資料，並 mock _apply_filters 方法
        with patch.object(self.crud, '_apply_filters') as mock_apply_filters:
            # 設定 mock 返回查詢對象
            mock_query = db_session.query(Schedule)
            mock_apply_filters.return_value = mock_query

            # When: 查詢時段
            schedules = self.crud.list_schedules(
                db_session,
                giver_id=giver_id,
                taker_id=taker_id,
                status_filter=status_filter,
            )

            # Then: 驗證 _apply_filters 被正確呼叫
            mock_apply_filters.assert_called_once()
            call_args = mock_apply_filters.call_args
            assert call_args[1]['giver_id'] == giver_id
            assert call_args[1]['taker_id'] == taker_id
            assert call_args[1]['status_filter'] == status_filter

            # 驗證返回了時段列表
            assert isinstance(schedules, list)

    @pytest.mark.parametrize(
        "giver_id,taker_id,status_filter,expected_error_type",
        [
            (None, None, "INVALID_STATUS", ValueError),  # 無效狀態篩選
            (None, None, "", ValueError),  # 空狀態篩選
            (None, None, "draft", ValueError),  # 小寫狀態篩選
        ],
    )
    def test_list_schedules_apply_filters_failure(
        self,
        db_session: Session,
        giver_id: int | None,
        taker_id: int | None,
        status_filter: str | None,
        expected_error_type: type,
    ):
        """測試 list_schedules 方法的篩選功能：篩選條件錯誤處理。"""
        # Given: 使用夾具的時段資料，並 mock _apply_filters 方法拋出異常
        with patch.object(self.crud, '_apply_filters') as mock_apply_filters:
            # 設定 mock 拋出異常
            mock_apply_filters.side_effect = expected_error_type(
                f"無效的篩選條件: {status_filter}"
            )

            # When & Then: 確認拋出預期的異常
            with pytest.raises(expected_error_type):
                self.crud.list_schedules(
                    db_session,
                    giver_id=giver_id,
                    taker_id=taker_id,
                    status_filter=status_filter,
                )

    # ===== 查詢單一時段（排除軟刪除） =====
    def test_get_schedule_success(
        self,
        db_session: Session,
        test_giver_schedule: Schedule,
    ):
        """測試查詢單一時段（排除軟刪除）成功。"""
        # Given: 使用夾具的時段資料

        # When: 查詢單一時段
        found_schedule = self.crud.get_schedule(
            db_session,
            test_giver_schedule.id,
        )

        # Then: 驗證資料完整性
        assert found_schedule.giver_id == test_giver_schedule.giver_id
        assert found_schedule.taker_id == test_giver_schedule.taker_id
        assert found_schedule.status == test_giver_schedule.status
        assert found_schedule.date == test_giver_schedule.date
        assert found_schedule.start_time == test_giver_schedule.start_time
        assert found_schedule.end_time == test_giver_schedule.end_time
        assert found_schedule.note == test_giver_schedule.note

        # Then: 驗證業務邏輯
        assert found_schedule is not None
        assert found_schedule.id == test_giver_schedule.id
        assert found_schedule.deleted_at is None
        assert found_schedule.is_active is True
        assert found_schedule.is_deleted is False

    def test_get_schedule_not_found_truly_missing(self, db_session: Session):
        """測試查詢單一時段（排除軟刪除）：404 資源不存在錯誤。"""
        # Given: 測試查詢不存在的時段

        # When: 查詢單一時段

        # Then: 應該拋出 ScheduleNotFoundError
        with pytest.raises(ScheduleNotFoundError, match="時段不存在: ID=999"):
            self.crud.get_schedule(db_session, 999)

    def test_get_schedule_not_found_soft_deleted(
        self,
        db_session: Session,
        test_giver_schedule: Schedule,
    ):
        """測試查詢單一時段（排除軟刪除）：404 資源已軟刪除錯誤。"""
        # Given: 軟刪除時段

        # When: 查詢單一時段

        # Then: 應該拋出 ScheduleNotFoundError
        self.crud.delete_schedule(
            db_session,
            test_giver_schedule.id,
            deleted_by=test_giver_schedule.giver_id,
            deleted_by_role=UserRoleEnum.GIVER,
        )

        # Then: 使用 get_schedule 查詢已軟刪除的時段，應該拋出錯誤
        with pytest.raises(
            ScheduleNotFoundError, match=f"時段不存在: ID={test_giver_schedule.id}"
        ):
            self.crud.get_schedule(db_session, test_giver_schedule.id)

    # ===== 查詢單一時段（包含軟刪除） =====
    def test_get_schedule_including_deleted_success(
        self,
        db_session: Session,
        test_giver_schedule: Schedule,
    ):
        """測試查詢單一時段（包含軟刪除）成功。"""
        # Given: 軟刪除時段

        # When: 查詢單一時段
        self.crud.delete_schedule(
            db_session,
            test_giver_schedule.id,
            deleted_by=test_giver_schedule.giver_id,
            deleted_by_role=UserRoleEnum.GIVER,
        )

        # When: 使用 get_schedule_including_deleted 查詢，應該能找到
        found_schedule = self.crud.get_schedule_including_deleted(
            db_session, test_giver_schedule.id
        )

        # Then: 驗證資料完整性
        assert found_schedule.giver_id == test_giver_schedule.giver_id
        assert found_schedule.taker_id == test_giver_schedule.taker_id
        assert found_schedule.date == test_giver_schedule.date
        assert found_schedule.start_time == test_giver_schedule.start_time
        assert found_schedule.end_time == test_giver_schedule.end_time
        assert found_schedule.note == test_giver_schedule.note

        # Then: 驗證業務邏輯
        assert found_schedule is not None
        assert found_schedule.id == test_giver_schedule.id
        assert (
            found_schedule.status == ScheduleStatusEnum.CANCELLED
        )  # 軟刪除後狀態變為 CANCELLED
        assert found_schedule.deleted_at is not None
        assert found_schedule.deleted_by == test_giver_schedule.giver_id
        assert found_schedule.deleted_by_role == UserRoleEnum.GIVER
        assert found_schedule.is_active is False
        assert found_schedule.is_deleted is True

    def test_get_schedule_including_deleted_not_found(self, db_session: Session):
        """測試查詢單一時段（包含軟刪除）：404 資源不存在錯誤。"""
        # Given: 測試查詢不存在的時段

        # When: 查詢單一時段

        # Then: 應該返回 None
        result = self.crud.get_schedule_including_deleted(db_session, 999)
        assert result is None

    # ===== 更新時段欄位 =====
    def test_update_schedule_fields_alias_schedule_date(
        self,
        db_session: Session,
        test_giver_schedule: Schedule,
    ):
        """測試更新時段欄位：別名 schedule_date 處理。"""
        # Given: 測試 schedule_date 別名（對應到模型的 date 欄位）
        new_date = date(2024, 12, 31)
        old_date = test_giver_schedule.date

        # When: 更新時段欄位
        updated_fields = self.crud._update_schedule_fields(
            test_giver_schedule,
            schedule_date=new_date,
        )

        # Then: 驗證更新結果
        assert len(updated_fields) == 1
        assert f"date: {old_date} -> {new_date}" in updated_fields
        assert test_giver_schedule.date == new_date

    @pytest.mark.parametrize(
        "field,new_value",
        [
            ("status", ScheduleStatusEnum.PENDING),
            ("start_time", time(11, 0)),
            ("end_time", time(12, 0)),
            ("note", "新的備註"),
        ],
    )
    def test_update_schedule_fields_non_schedule_date_fields(
        self,
        db_session: Session,
        test_giver_schedule: Schedule,
        field,
        new_value,
    ):
        """參數化測試：更新非 schedule_date 相關欄位（status、start_time、end_time、note）。"""
        # Given: 取得舊值
        old_value = getattr(test_giver_schedule, field)

        # When: 單一欄位更新
        updated_fields = self.crud._update_schedule_fields(
            test_giver_schedule,
            **{field: new_value},
        )

        # Then: 僅有一個欄位被更新，內容與模型同步
        assert len(updated_fields) == 1
        assert f"{field}: {old_value} -> {new_value}" in updated_fields
        assert getattr(test_giver_schedule, field) == new_value

    def test_update_schedule_fields_non_existing_field(
        self,
        db_session: Session,
        test_giver_schedule: Schedule,
        caplog,
    ):
        """測試更新時段欄位：不存在的 Schedule 模型欄位。"""
        # Given: 測試更新不存在的欄位

        # When: 更新時段欄位
        updated_fields = self.crud._update_schedule_fields(
            test_giver_schedule,
            non_existing_field="無效值",
        )

        # Then: 所有欄位都不存在，應該返回空列表
        assert len(updated_fields) == 0

        # Then: 驗證原始欄位值沒有改變，表示不存在的欄位被忽略
        assert test_giver_schedule.giver_id == 1
        assert test_giver_schedule.taker_id is None
        assert test_giver_schedule.status == ScheduleStatusEnum.AVAILABLE
        assert test_giver_schedule.date == date(2024, 1, 1)
        assert test_giver_schedule.start_time == time(9, 0)
        assert test_giver_schedule.end_time == time(10, 0)
        assert test_giver_schedule.note == "Giver 提供的可預約時段"

        # Then: 驗證警告日誌被正確記錄
        assert len(caplog.records) == 1
        assert caplog.records[0].levelname == "WARNING"
        assert "忽略無效的欄位: non_existing_field" in caplog.records[0].message

    # ===== 更新時段 =====
    def test_update_schedule_success(
        self,
        db_session: Session,
        test_giver_schedule: Schedule,
        caplog,
    ):
        """測試成功更新時段。"""
        # Given: 使用夾具的時段資料

        # When: 更新時段
        updated_schedule = self.crud.update_schedule(
            db_session,
            test_giver_schedule.id,
            updated_by=test_giver_schedule.giver_id,
            updated_by_role=UserRoleEnum.GIVER,
            schedule_date=date(2025, 9, 16),
            start_time=time(14, 0),
            end_time=time(15, 0),
            note="更新後的備註",
        )

        # Then: 驗證資料完整性：未更新的欄位保持不變
        assert updated_schedule.id == test_giver_schedule.id
        assert updated_schedule.giver_id == test_giver_schedule.giver_id
        assert updated_schedule.taker_id == test_giver_schedule.taker_id
        assert updated_schedule.status == test_giver_schedule.status

        # Then: 驗證更新欄位
        assert updated_schedule.date == date(2025, 9, 16)
        assert updated_schedule.start_time == time(14, 0)
        assert updated_schedule.end_time == time(15, 0)
        assert updated_schedule.note == "更新後的備註"

        # Then: 驗證業務邏輯
        assert updated_schedule is not None
        assert updated_schedule.updated_at is not None
        assert updated_schedule.updated_by == test_giver_schedule.giver_id
        assert updated_schedule.updated_by_role == UserRoleEnum.GIVER

    @pytest.mark.parametrize(
        "start_time,end_time,description",
        [
            # 測試開始時間等於結束時間的情況
            (time(9, 0), time(9, 0), "開始時間等於結束時間"),
            # 測試開始時間晚於結束時間的情況
            (time(10, 0), time(9, 0), "開始時間晚於結束時間"),
            (time(11, 30), time(10, 0), "開始時間晚於結束時間（不同分鐘）"),
            (time(12, 0), time(11, 30), "開始時間晚於結束時間（跨小時）"),
        ],
    )
    def test_update_schedule_time_validation_error(
        self,
        db_session: Session,
        test_giver_schedule: Schedule,
        start_time,
        end_time,
        description,
    ):
        """時間邏輯驗證錯誤（開始時間必須早於結束時間）。"""
        # Given: 準備測試資料
        schedule_id = test_giver_schedule.id
        updated_by = 1
        updated_by_role = UserRoleEnum.GIVER

        # When & Then: 驗證會拋出 BadRequestError
        with pytest.raises(BadRequestError) as exc_info:
            self.crud.update_schedule(
                db_session,
                schedule_id,
                updated_by=updated_by,
                updated_by_role=updated_by_role,
                start_time=start_time,
                end_time=end_time,
            )

        # 驗證錯誤訊息
        assert "開始時間必須早於結束時間" in str(exc_info.value)

    def test_update_schedule_not_found(
        self,
        db_session: Session,
        test_giver_schedule: Schedule,
    ):
        """測試更新時段：404 資源不存在錯誤。"""
        # Given: 測試更新不存在的時段

        # When: 更新時段

        # Then: 應該拋出 ScheduleNotFoundError
        with pytest.raises(ScheduleNotFoundError, match="時段不存在: ID=999"):
            self.crud.update_schedule(
                db_session,
                999,
                updated_by=test_giver_schedule.giver_id,
                updated_by_role=UserRoleEnum.SYSTEM,
                note="測試時段不存在",
            )

    # # ===== 軟刪除時段 =====
    # def test_delete_schedule_success(
    #     self,
    #     db_session: Session,
    #     test_giver_schedule: Schedule,
    # ):
    #     """測試成功軟刪除時段。"""
    #     # Given: 軟刪除時段

    #     # When: 軟刪除時段
    #     result = self.crud.delete_schedule(
    #         db_session,
    #         test_giver_schedule.id,
    #         deleted_by=test_giver_schedule.giver_id,
    #         deleted_by_role=UserRoleEnum.GIVER,
    #     )

    #     # Then: 驗證軟刪除結果
    #     assert result == DeletionResult.SUCCESS

    #     # Then: 確認時段仍然存在但已被軟刪除
    #     found_schedule_with_deleted = self.crud.get_schedule_including_deleted(
    #         db_session,
    #         test_giver_schedule.id,
    #     )

    #     # Then: 驗證資料完整性
    #     assert found_schedule_with_deleted.giver_id == test_giver_schedule.giver_id
    #     assert found_schedule_with_deleted.taker_id == test_giver_schedule.taker_id
    #     assert found_schedule_with_deleted.date == test_giver_schedule.date
    #     assert found_schedule_with_deleted.start_time == test_giver_schedule.start_time
    #     assert found_schedule_with_deleted.end_time == test_giver_schedule.end_time
    #     assert found_schedule_with_deleted.note == test_giver_schedule.note

    #     # Then: 驗證業務邏輯
    #     assert found_schedule_with_deleted.deleted_at is not None
    #     assert found_schedule_with_deleted.id == test_giver_schedule.id
    #     assert found_schedule_with_deleted.status == ScheduleStatusEnum.CANCELLED
    #     assert found_schedule_with_deleted.deleted_by == test_giver_schedule.giver_id
    #     assert found_schedule_with_deleted.deleted_by_role == UserRoleEnum.GIVER
    #     assert found_schedule_with_deleted.is_active is False
    #     assert found_schedule_with_deleted.is_deleted is True

    # def test_delete_schedule_already_deleted(
    #     self,
    #     db_session: Session,
    #     test_giver_schedule: Schedule,
    # ):
    #     """測試重複軟刪除時段。"""
    #     # Given: 第一次軟刪除

    #     # When: 第一次軟刪除
    #     result1 = self.crud.delete_schedule(
    #         db_session,
    #         test_giver_schedule.id,
    #         deleted_by=test_giver_schedule.giver_id,
    #         deleted_by_role=UserRoleEnum.GIVER,
    #     )

    #     # Then: 驗證軟刪除結果
    #     assert result1 == DeletionResult.SUCCESS

    #     # Given: 第二次軟刪除（應該返回已經刪除）

    #     # When: 第二次軟刪除
    #     result2 = self.crud.delete_schedule(
    #         db_session,
    #         test_giver_schedule.id,
    #         deleted_by=test_giver_schedule.giver_id,
    #         deleted_by_role=UserRoleEnum.GIVER,
    #     )

    #     # Then: 驗證軟刪除結果
    #     assert result2 == DeletionResult.ALREADY_DELETED

    #     # Then: 確認時段仍然存在但已被軟刪除
    #     found_schedule = self.crud.get_schedule_including_deleted(
    #         db_session,
    #         test_giver_schedule.id,
    #     )

    #     # Then: 驗證資料完整性
    #     assert found_schedule.giver_id == test_giver_schedule.giver_id
    #     assert found_schedule.taker_id == test_giver_schedule.taker_id
    #     assert found_schedule.date == test_giver_schedule.date
    #     assert found_schedule.start_time == test_giver_schedule.start_time
    #     assert found_schedule.end_time == test_giver_schedule.end_time
    #     assert found_schedule.note == test_giver_schedule.note

    #     # Then: 驗證業務邏輯
    #     assert found_schedule is not None
    #     assert found_schedule.id == test_giver_schedule.id
    #     assert (
    #         found_schedule.status == ScheduleStatusEnum.CANCELLED
    #     )  # 軟刪除後狀態變為 CANCELLED
    #     assert found_schedule.deleted_at is not None
    #     assert found_schedule.deleted_by == test_giver_schedule.giver_id
    #     assert found_schedule.deleted_by_role == UserRoleEnum.GIVER
    #     assert found_schedule.is_active is False
    #     assert found_schedule.is_deleted is True

    # def test_delete_schedule_not_found(self, db_session: Session):
    #     """測試刪除時段：404 資源不存在錯誤。"""
    #     # Given: 測試刪除不存在的時段

    #     # When: 刪除時段

    #     # Then: 應該返回 NOT_FOUND
    #     result = self.crud.delete_schedule(
    #         db_session,
    #         999,
    #     )

    #     assert result == DeletionResult.NOT_FOUND

    # @pytest.mark.parametrize(
    #     "status,note",
    #     [
    #         (ScheduleStatusEnum.ACCEPTED, "測試已接受的時段"),
    #         (ScheduleStatusEnum.COMPLETED, "測試已完成的時段"),
    #     ],
    # )
    # def test_delete_schedule_cannot_delete_final_states(
    #     self,
    #     db_session: Session,
    #     status: ScheduleStatusEnum,
    #     note: str,
    # ):
    #     """測試刪除最終狀態的時段（已接受、已完成）。

    #     這些狀態的時段不應該被刪除，因為它們代表已確定的業務狀態。

    #     Args:
    #         status: 時段狀態（ACCEPTED 或 COMPLETED）
    #         note: 時段備註
    #     """
    #     # Given: 建立指定狀態的時段

    #     # When: 建立指定狀態的時段
    #     schedule = Schedule(
    #         giver_id=1,
    #         taker_id=1,
    #         status=status,
    #         date=date(2025, 9, 15),
    #         start_time=time(9, 0),
    #         end_time=time(10, 0),
    #         note=note,
    #     )
    #     db_session.add(schedule)
    #     db_session.commit()

    #     # When: 嘗試刪除最終狀態的時段
    #     result = self.crud.delete_schedule(
    #         db_session,
    #         schedule.id,
    #         deleted_by=1,
    #         deleted_by_role=UserRoleEnum.GIVER,
    #     )

    #     # Then: 應該返回無法刪除的結果
    #     assert result == DeletionResult.CANNOT_DELETE

    #     # Then: 驗證時段狀態沒有改變
    #     db_session.refresh(schedule)
    #     assert schedule.status == status
    #     assert schedule.deleted_at is None
