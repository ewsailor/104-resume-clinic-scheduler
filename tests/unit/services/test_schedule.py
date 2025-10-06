"""時段服務層測試。"""

# ===== 標準函式庫 =====
from datetime import date, datetime, time
from unittest.mock import Mock, patch

# ===== 第三方套件 =====
import pytest

# ===== 本地模組 =====
from app.enums.models import ScheduleStatusEnum, UserRoleEnum
from app.enums.operations import OperationContext
from app.errors.exceptions import (
    DatabaseError,
    ScheduleNotFoundError,
    ScheduleOverlapError,
)
from app.schemas import ScheduleBase
from app.services.schedule import ScheduleService


class TestScheduleService:
    """時段服務層測試類別。"""

    @pytest.fixture
    def service(self):
        """建立服務實例。"""
        return ScheduleService()

    @pytest.fixture
    def sample_schedule_base(self):
        """建立範例時段資料 - ScheduleBase 格式，專為服務層測試使用。

        因為 ScheduleService 的方法，主要接受 ScheduleBase 作為輸入參數，所以測試時也使用 ScheduleBase 格式
        """
        return ScheduleBase(
            giver_id=1,
            schedule_date=date(2024, 1, 15),
            start_time=time(9, 0),
            end_time=time(10, 0),
        )

    @pytest.fixture
    def mock_db(self):
        """建立 Mock 物件模擬資料庫會話，用於服務層測試。

        適合服務層測試，因為不需要真實資料庫操作的測試。
        """
        return Mock()

    @pytest.fixture
    def mock_query(self):
        """建立 Mock 物件模擬查詢物件。"""
        return Mock()

    def setup_mock_query_chain(
        self, mock_db, mock_query, result=[], has_exclude_filter=False
    ):
        """設定 Mock 查詢鏈的通用方法。

        Args:
            mock_db: Mock 資料庫會話 (模擬 db)
            mock_query: Mock 查詢物件 (模擬 query)
            result: 查詢結果，預設為空列表
            has_exclude_filter: 是否有排除自己的額外 filter
        """
        # 模擬 db.query(Schedule).options(...).filter(...)，返回查詢物件
        if has_exclude_filter:
            # 當有 exclude_schedule_id 時，查詢鏈會多一個 .filter() 呼叫
            mock_db.query.return_value.options.return_value.filter.return_value.filter.return_value = (
                mock_query
            )
        else:
            # 一般情況：db.query(Schedule).options(...).filter(...)
            mock_db.query.return_value.options.return_value.filter.return_value = (
                mock_query
            )

        # 模擬 query.filter(...).all()，重疊檢查和執行查詢
        mock_query.filter.return_value.all.return_value = result

    def create_mock_schedule(self, **kwargs):
        """建立模擬時段物件。"""
        return Mock(**kwargs)

    def create_mock_schedule_base(self, **kwargs):
        """建立模擬時段基礎物件。"""
        return ScheduleBase(**kwargs)

    # ===== 檢查單一時段重疊 =====
    @pytest.mark.parametrize(
        "case,deleted_at",
        [
            ("不同 Giver", None),
            ("不同日期", None),
            ("已軟刪除時段", datetime.now()),
        ],
    )
    def test_check_schedule_overlap_no_overlap(
        self, service, mock_db, mock_query, case, deleted_at
    ):
        """測試檢查單一時段重疊 - 無重疊。"""
        # GIVEN：建立模擬的資料庫中現有時段
        mock_existing_schedule = self.create_mock_schedule(
            id=1,
            giver_id=1,
            date=date(2024, 1, 15),
            start_time=time(9, 0),
            end_time=time(10, 0),
        )

        # WHEN：根據測試案例設定不同的參數和 Mock 結果
        if case == "不同 Giver":
            # 資料庫中有 giver_id=1 的時段，但查詢 giver_id=2 的時段，所以沒有重疊
            self.setup_mock_query_chain(mock_db, mock_query, result=[])
            result = service.check_schedule_overlap(
                db=mock_db,
                giver_id=2,  # 不同的 Giver
                schedule_date=date(2024, 1, 15),
                start_time=time(9, 0),
                end_time=time(10, 0),
            )
        elif case == "不同日期":
            # 資料庫中有 date=2024-01-15 的時段，但查詢 date=2024-01-16 的時段，所以沒有重疊
            self.setup_mock_query_chain(mock_db, mock_query, result=[])
            result = service.check_schedule_overlap(
                db=mock_db,
                giver_id=1,
                schedule_date=date(2024, 1, 16),  # 不同的日期
                start_time=time(9, 0),
                end_time=time(10, 0),
            )
        elif case == "已軟刪除時段":
            # 參數化測試設定傳入的資料 deleted_at 為 datetime.now()，表示資料庫中的時段已軟刪除
            self.setup_mock_query_chain(mock_db, mock_query, result=[])
            result = service.check_schedule_overlap(
                db=mock_db,
                giver_id=1,
                schedule_date=date(2024, 1, 15),
                start_time=time(9, 0),
                end_time=time(10, 0),
            )

        # THEN：確認沒有重疊的時段
        assert result == []

    def test_check_schedule_overlap_with_overlap(self, service, mock_db, mock_query):
        """測試檢查單一時段重疊 - 有重疊。"""
        # GIVEN：建立模擬的重疊時段
        mock_overlapping_schedule = self.create_mock_schedule(
            id=1,
            giver_id=1,
            date=date(2024, 1, 15),
            start_time=time(9, 30),
            end_time=time(10, 30),
        )

        # 設定 Mock 查詢鏈，模擬有重疊情況
        self.setup_mock_query_chain(
            mock_db, mock_query, result=[mock_overlapping_schedule]
        )

        # WHEN：檢查時段重疊
        result = service.check_schedule_overlap(
            db=mock_db,
            giver_id=1,
            schedule_date=date(2024, 1, 15),
            start_time=time(9, 0),
            end_time=time(10, 0),
        )

        # THEN：確認找到重疊的時段
        assert len(result) == 1
        assert result[0].id == 1

    @patch('app.services.schedule.logger')
    def test_check_schedule_overlap_exclude_self(
        self, mock_logger, service, mock_db, mock_query
    ):
        """測試檢查時段重疊 - 排除自己（更新模式）。"""
        # GIVEN：建立模擬的資料庫中現有時段
        mock_existing_schedule = self.create_mock_schedule(
            id=1,
            giver_id=1,
            date=date(2024, 1, 15),
            start_time=time(9, 0),
            end_time=time(10, 0),
        )

        # 模擬查詢結果：排除自己後沒有重疊
        self.setup_mock_query_chain(
            mock_db, mock_query, result=[], has_exclude_filter=True
        )

        # WHEN：檢查時段重疊，排除自己（模擬更新模式）
        result = service.check_schedule_overlap(
            db=mock_db,
            giver_id=1,
            schedule_date=date(2024, 1, 15),
            start_time=time(9, 0),
            end_time=time(10, 0),
            exclude_schedule_id=1,  # 排除自己，避免「和自己重疊」的誤判
        )

        # THEN：確認沒有重疊（因為排除了自己）
        assert result == []

    @patch('app.services.schedule.logger')
    def test_check_schedule_overlap_exclude_self_with_other_overlap(
        self, mock_logger, service, mock_db, mock_query
    ):
        """測試檢查時段重疊 - 排除自己但與其他時段重疊。"""
        # GIVEN：建立模擬的其他重疊時段
        mock_other_overlapping_schedule = self.create_mock_schedule(
            id=2,  # 不同的 ID
            giver_id=1,
            date=date(2024, 1, 15),
            start_time=time(9, 30),
            end_time=time(10, 30),
        )

        # 模擬查詢結果：排除自己後仍有其他重疊時段
        self.setup_mock_query_chain(
            mock_db,
            mock_query,
            result=[mock_other_overlapping_schedule],
            has_exclude_filter=True,
        )

        # WHEN：檢查時段重疊，排除自己但與其他時段重疊
        result = service.check_schedule_overlap(
            db=mock_db,
            giver_id=1,
            schedule_date=date(2024, 1, 15),
            start_time=time(9, 0),
            end_time=time(10, 0),
            exclude_schedule_id=1,  # 排除自己
        )

        # THEN：確認找到其他重疊的時段
        assert len(result) == 1
        assert result[0].id == 2  # 確認是其他時段，不是被排除的自己
        assert result[0].giver_id == 1
        assert result[0].date == date(2024, 1, 15)
        assert result[0].start_time == time(9, 30)
        assert result[0].end_time == time(10, 30)

    # ===== 檢查多個時段重疊 =====
    def test_check_multiple_schedules_overlap_no_overlap(
        self, service, mock_db, mock_query
    ):
        """測試檢查多個時段重疊 - 無重疊。"""
        # GIVEN：建立多個時段資料
        mock_existing_schedules = [
            self.create_mock_schedule_base(
                giver_id=1,
                schedule_date=date(2024, 1, 15),
                start_time=time(9, 0),
                end_time=time(10, 0),
            ),
            self.create_mock_schedule_base(
                giver_id=1,
                schedule_date=date(2024, 1, 15),
                start_time=time(11, 0),
                end_time=time(12, 0),
            ),
        ]

        # 設定 Mock 查詢鏈，模擬無重疊情況
        self.setup_mock_query_chain(mock_db, mock_query, result=[])

        # WHEN：檢查多個時段重疊
        result = service.check_multiple_schedules_overlap(
            db=mock_db,
            schedules=mock_existing_schedules,
        )

        # THEN：確認沒有重疊的時段
        assert result == []

    def test_check_multiple_schedules_overlap_with_overlap(
        self, service, mock_db, mock_query
    ):
        """測試檢查多個時段重疊 - 有重疊。"""
        # GIVEN：建立多個時段資料
        mock_existing_schedules = [
            self.create_mock_schedule_base(
                giver_id=1,
                schedule_date=date(2024, 1, 15),
                start_time=time(9, 0),
                end_time=time(10, 0),
            ),
            self.create_mock_schedule_base(
                giver_id=1,
                schedule_date=date(2024, 1, 15),
                start_time=time(10, 0),
                end_time=time(11, 0),
            ),
        ]

        # 建立模擬的重疊時段
        mock_overlapping_schedule = self.create_mock_schedule(
            id=1,
            giver_id=1,
            date=date(2024, 1, 15),
            start_time=time(8, 0),
            end_time=time(12, 0),
        )

        # 設定 Mock 查詢鏈，模擬有重疊情況
        self.setup_mock_query_chain(
            mock_db, mock_query, result=[mock_overlapping_schedule]
        )

        # WHEN：檢查多個時段重疊
        result = service.check_multiple_schedules_overlap(
            db=mock_db,
            schedules=mock_existing_schedules,
        )

        # THEN：確認找到重疊的時段（每個時段都會檢查，所以會有 2 個重疊）
        assert len(result) == 2
        assert result[0].id == 1
        assert result[1].id == 1

    # ===== 決定時段狀態 =====
    def test_determine_schedule_status_with_specified_status(self, service):
        """測試決定時段狀態 - 指定狀態優先。"""
        # GIVEN：建立有時段狀態的時段資料
        schedule_with_status = self.create_mock_schedule_base(
            giver_id=1,
            schedule_date=date(2024, 1, 15),
            start_time=time(9, 0),
            end_time=time(10, 0),
            status=ScheduleStatusEnum.ACCEPTED,  # 指定狀態
        )
        created_by_role = UserRoleEnum.GIVER  # 指定角色為 GIVER

        # WHEN：決定時段狀態
        status = service.determine_schedule_status(
            created_by_role, schedule_with_status
        )

        # THEN：確認使用指定的狀態，而不是根據角色決定的狀態
        assert status == ScheduleStatusEnum.ACCEPTED  # 應該使用指定的狀態
        assert status != ScheduleStatusEnum.AVAILABLE  # 不應該使用 GIVER 角色的預設狀態

    @pytest.mark.parametrize(
        "role,expected_status",
        [
            (UserRoleEnum.TAKER, ScheduleStatusEnum.PENDING),
            (UserRoleEnum.GIVER, ScheduleStatusEnum.AVAILABLE),
            (None, ScheduleStatusEnum.DRAFT),
        ],
    )
    def test_determine_schedule_status(
        self,
        service,
        sample_schedule_base,
        role,
        expected_status,
    ):
        """測試決定時段狀態。"""
        # GIVEN：角色和範例時段資料，從夾具中取得

        # WHEN：決定時段狀態
        status = service.determine_schedule_status(role, sample_schedule_base)

        # THEN：確認狀態符合預期
        assert status == expected_status

    # ===== 記錄時段詳情 =====
    @patch('app.services.schedule.logger')
    def test_log_schedule_details_with_schedules(self, mock_logger, service):
        """測試記錄時段詳情 - 有時段資料。"""
        # GIVEN：建立時段資料
        schedules = [
            self.create_mock_schedule_base(
                giver_id=1,
                schedule_date=date(2024, 1, 15),
                start_time=time(9, 0),
                end_time=time(10, 0),
            ),
            self.create_mock_schedule_base(
                giver_id=1,
                schedule_date=date(2024, 1, 16),
                start_time=time(11, 0),
                end_time=time(12, 0),
            ),
        ]

        # WHEN：記錄時段詳情
        service.log_schedule_details(schedules)

        # THEN：確認記錄了正確的日誌
        mock_logger.info.assert_called_once_with(
            "建立時段詳情: 時段1: 2024-01-15 09:00:00-10:00:00, 時段2: 2024-01-16 11:00:00-12:00:00"
        )

    @patch('app.services.schedule.logger')
    def test_log_schedule_details_empty_schedules(self, mock_logger, service):
        """測試記錄時段詳情 - 空時段列表。"""
        # GIVEN：空的時段列表
        schedules = []

        # WHEN：記錄時段詳情
        service.log_schedule_details(schedules)

        # THEN：確認記錄了空資料的日誌
        mock_logger.info.assert_called_once_with("建立時段: 無時段資料")

    @patch('app.services.schedule.logger')
    def test_log_schedule_details_default_context(self, mock_logger, service):
        """測試記錄時段詳情 - 預設操作上下文（CREATE）。"""
        # GIVEN：建立時段資料
        schedules = [
            self.create_mock_schedule_base(
                giver_id=1,
                schedule_date=date(2024, 1, 15),
                start_time=time(9, 0),
                end_time=time(10, 0),
            ),
        ]

        # WHEN：記錄時段詳情（不指定操作上下文，使用預設值）
        service.log_schedule_details(schedules)

        # THEN：確認記錄了正確的日誌（預設為建立操作）
        mock_logger.info.assert_called_once_with(
            "建立時段詳情: 時段1: 2024-01-15 09:00:00-10:00:00"
        )

    @pytest.mark.parametrize(
        "context,expected_log",
        [
            (
                OperationContext.CREATE,
                "建立時段詳情: 時段1: 2024-01-15 09:00:00-10:00:00",
            ),
            (
                OperationContext.UPDATE,
                "更新時段詳情: 時段1: 2024-01-15 09:00:00-10:00:00",
            ),
            (
                OperationContext.DELETE,
                "刪除時段詳情: 時段1: 2024-01-15 09:00:00-10:00:00",
            ),
        ],
    )
    @patch('app.services.schedule.logger')
    def test_log_schedule_details_with_context(
        self, mock_logger, service, context, expected_log
    ):
        """測試記錄時段詳情 - 指定操作上下文。"""
        # GIVEN：建立時段資料
        schedules = [
            self.create_mock_schedule_base(
                giver_id=1,
                schedule_date=date(2024, 1, 15),
                start_time=time(9, 0),
                end_time=time(10, 0),
            ),
        ]

        # WHEN：記錄時段詳情（指定操作上下文）
        service.log_schedule_details(schedules, context)

        # THEN：確認記錄了正確的日誌
        mock_logger.info.assert_called_once_with(expected_log)

    # ===== 建立時段 ORM 物件 =====
    def test_create_schedule_orm_objects_success(self, service):
        """測試建立時段 ORM 物件 - 成功。"""
        # GIVEN：建立時段資料和建立者資訊
        schedules = [
            self.create_mock_schedule_base(
                giver_id=1,
                taker_id=2,
                schedule_date=date(2024, 1, 15),
                start_time=time(9, 0),
                end_time=time(10, 0),
                note="第一個測試時段",
            ),
            self.create_mock_schedule_base(
                giver_id=1,
                taker_id=3,
                schedule_date=date(2024, 1, 16),
                start_time=time(14, 0),
                end_time=time(15, 0),
                note="第二個測試時段",
            ),
        ]
        created_by = 1
        created_by_role = UserRoleEnum.GIVER

        # WHEN：建立時段 ORM 物件
        result = service.create_schedule_orm_objects(
            schedules, created_by, created_by_role
        )

        # THEN：確認建立了正確的 ORM 物件
        assert len(result) == 2

        # 檢查第一個時段
        first_schedule = result[0]
        assert first_schedule.giver_id == 1
        assert first_schedule.taker_id == 2
        assert first_schedule.date == date(2024, 1, 15)
        assert first_schedule.start_time == time(9, 0)
        assert first_schedule.end_time == time(10, 0)
        assert first_schedule.note == "第一個測試時段"
        assert (
            first_schedule.status == ScheduleStatusEnum.AVAILABLE
        )  # GIVER 角色預設為 AVAILABLE
        assert first_schedule.created_by == 1
        assert first_schedule.created_by_role == UserRoleEnum.GIVER
        assert first_schedule.updated_by == 1
        assert first_schedule.updated_by_role == UserRoleEnum.GIVER
        assert first_schedule.deleted_by is None
        assert first_schedule.deleted_by_role is None

        # 檢查第二個時段
        second_schedule = result[1]
        assert second_schedule.giver_id == 1
        assert second_schedule.taker_id == 3
        assert second_schedule.date == date(2024, 1, 16)
        assert second_schedule.start_time == time(14, 0)
        assert second_schedule.end_time == time(15, 0)
        assert second_schedule.note == "第二個測試時段"
        assert second_schedule.status == ScheduleStatusEnum.AVAILABLE
        assert second_schedule.created_by == 1
        assert second_schedule.created_by_role == UserRoleEnum.GIVER
        assert second_schedule.updated_by == 1
        assert second_schedule.updated_by_role == UserRoleEnum.GIVER
        assert second_schedule.deleted_by is None
        assert second_schedule.deleted_by_role is None

    def test_create_schedule_orm_objects_empty_list(self, service):
        """測試建立時段 ORM 物件 - 空列表。"""
        # GIVEN：空的時段列表
        schedules = []
        created_by = 1
        created_by_role = UserRoleEnum.GIVER

        # WHEN：建立時段 ORM 物件
        result = service.create_schedule_orm_objects(
            schedules, created_by, created_by_role
        )

        # THEN：確認返回空列表
        assert result == []

    # ===== 建立多個時段 =====
    @patch('app.services.schedule.logger')
    def test_create_schedules_success(
        self,
        mock_logger,
        service,
        mock_db,
        sample_schedule_base,
    ):
        """測試建立多個時段 - 成功。"""
        # GIVEN：使用夾具中的範例時段資料
        schedules = [sample_schedule_base]
        created_by = 1
        created_by_role = UserRoleEnum.GIVER

        # 模擬沒有任何重疊排程
        with patch.object(
            service, 'check_multiple_schedules_overlap', return_value=[]
        ) as mock_check:
            # 模擬將輸入的 Pydantic 資料成功轉換為 ORM 物件
            with patch.object(
                service, 'create_schedule_orm_objects'
            ) as mock_create_orm:
                # 模擬 CRUD 層成功將 ORM 物件儲存到資料庫
                with patch.object(
                    service.schedule_crud, 'create_schedules'
                ) as mock_crud:
                    # 設定模擬返回值
                    mock_schedule_orm = Mock()  # 建立從資料庫回傳的模擬時段 ORM 物件
                    mock_schedule_orm.id = (
                        1  # 設定模擬時段 ID 為 1，代表資料庫自動產生的主鍵
                    )
                    mock_create_orm.return_value = [
                        mock_schedule_orm
                    ]  # 模擬將 Pydantic 模型轉換為 ORM 物件
                    mock_crud.return_value = [
                        mock_schedule_orm
                    ]  # 模擬將 ORM 物件儲存到資料庫

                    # WHEN：建立多個時段
                    result = service.create_schedules(
                        mock_db, schedules, created_by, created_by_role
                    )

                    # THEN：驗證重疊檢查只被呼叫一次，且參數正確
                    mock_check.assert_called_once_with(mock_db, schedules)

                    # 驗證 ORM 物件建立只被呼叫一次，且參數正確
                    mock_create_orm.assert_called_once_with(
                        schedules, created_by, created_by_role
                    )

                    # 驗證 CRUD 建立只被呼叫一次，且參數正確
                    mock_crud.assert_called_once_with(mock_db, [mock_schedule_orm])

                    # 確認成功建立
                    assert result == [mock_schedule_orm]

                    # 確認記錄了成功日誌
                    mock_logger.info.assert_called()

    @patch('app.services.schedule.logger')
    def test_create_schedules_overlap_error(
        self,
        mock_logger,
        service,
        mock_db,
        sample_schedule_base,
    ):
        """測試建立多個時段 - 重疊錯誤。"""
        # GIVEN：使用夾具中的範例時段資料
        schedules = [sample_schedule_base]
        created_by = 1
        created_by_role = UserRoleEnum.GIVER

        with patch.object(service, 'check_multiple_schedules_overlap') as mock_check:
            # 設定模擬返回值
            mock_overlapping_schedule = Mock()  # 建立模擬的重疊時段
            mock_check.return_value = [mock_overlapping_schedule]  # 模擬時段重疊

            # WHEN & THEN：當檢測到重疊時段時，拋出錯誤並阻止建立
            with pytest.raises(ScheduleOverlapError):
                service.create_schedules(
                    mock_db, schedules, created_by, created_by_role
                )

            # 驗證警告日誌內容正確
            mock_logger.warning.assert_called_with(
                f"建立時段時檢測到重疊: "
                f"重疊數量={len([mock_overlapping_schedule])}, "
            )

    @patch('app.services.schedule.logger')
    def test_create_schedules_orm_conversion_error(
        self,
        mock_logger,
        service,
        mock_db,
        sample_schedule_base,
    ):
        """測試建立多個時段 - Pydantic 轉換成 ORM 物件錯誤。"""
        # GIVEN：使用夾具中的範例時段資料
        schedules = [sample_schedule_base]
        created_by = 1
        created_by_role = UserRoleEnum.GIVER

        # 模擬重疊檢查通過
        with patch.object(service, 'check_multiple_schedules_overlap', return_value=[]):
            # 模擬 ORM 轉換時拋出錯誤
            with patch.object(
                service,
                'create_schedule_orm_objects',
                side_effect=ValueError("ORM 轉換失敗"),
            ):
                # WHEN & THEN：確認拋出轉換錯誤（會被裝飾器轉換為 DatabaseError）
                with pytest.raises(DatabaseError):
                    service.create_schedules(
                        mock_db, schedules, created_by, created_by_role
                    )

    @patch('app.services.schedule.logger')
    def test_create_schedules_crud_error(
        self, mock_logger, service, mock_db, sample_schedule_base
    ):
        """測試建立多個時段 - CRUD 層將 ORM 物件儲存到資料庫錯誤。"""
        # GIVEN：使用夾具中的範例時段資料
        schedules = [sample_schedule_base]
        created_by = 1
        created_by_role = UserRoleEnum.GIVER

        # 模擬重疊檢查通過
        with patch.object(service, 'check_multiple_schedules_overlap', return_value=[]):
            # 模擬 ORM 轉換成功
            with patch.object(
                service, 'create_schedule_orm_objects'
            ) as mock_create_orm:
                mock_schedule_orm = Mock()
                mock_create_orm.return_value = [mock_schedule_orm]

                # 模擬 CRUD 操作失敗
                with patch.object(
                    service.schedule_crud,
                    'create_schedules',
                    side_effect=Exception("資料庫操作失敗"),
                ):
                    # WHEN & THEN：確認拋出 CRUD 錯誤（會被裝飾器轉換為 DatabaseError）
                    with pytest.raises(DatabaseError):
                        service.create_schedules(
                            mock_db, schedules, created_by, created_by_role
                        )

    # ===== 查詢時段列表 =====
    @patch('app.services.schedule.logger')
    def test_list_schedules_success(self, mock_logger, service, mock_db):
        """測試查詢時段列表 - 無使用篩選條件 - 成功。"""
        # GIVEN：建立模擬的時段列表（所有篩選條件都為 None）
        giver_id = None
        taker_id = None
        status_filter = None

        mock_schedules = [
            self.create_mock_schedule(
                id=1,
                giver_id=1,
                taker_id=2,
                date=date(2024, 1, 15),
                start_time=time(9, 0),
                end_time=time(10, 0),
                status=ScheduleStatusEnum.AVAILABLE,
            ),
            self.create_mock_schedule(
                id=2,
                giver_id=1,
                taker_id=3,
                date=date(2024, 1, 16),
                start_time=time(14, 0),
                end_time=time(15, 0),
                status=ScheduleStatusEnum.PENDING,
            ),
        ]

        # 模擬 CRUD 層查詢返回時段列表
        with patch.object(service.schedule_crud, 'list_schedules') as mock_list:
            # 設定模擬返回值
            mock_list.return_value = mock_schedules

            # WHEN：查詢時段列表
            result = service.list_schedules(mock_db, giver_id, taker_id, status_filter)

            # THEN：驗證 CRUD 層被正確呼叫
            mock_list.assert_called_once_with(
                mock_db, giver_id, taker_id, status_filter
            )

            # 確認查詢成功
            assert result == mock_schedules
            assert len(result) == 2

            # 確認記錄了查詢日誌
            mock_logger.info.assert_called_once_with(
                f"查詢時段列表完成: giver_id={giver_id}, taker_id={taker_id}, "
                f"status_filter={status_filter}, 找到 {len(mock_schedules)} 個時段"
            )

    @patch('app.services.schedule.logger')
    @pytest.mark.parametrize(
        "giver_id,taker_id,status_filter,expected_count",
        [
            # 單一篩選條件
            (1, None, None, 2),  # 只篩選 giver_id (時段1,2)
            (None, 2, None, 2),  # 只篩選 taker_id (時段1,3)
            (None, None, "AVAILABLE", 1),  # 只篩選 status (時段1)
            (None, None, "PENDING", 2),  # 只篩選 status (時段2,3)
            # 多重篩選條件
            (1, 2, None, 1),  # giver_id + taker_id (時段1)
            (1, None, "AVAILABLE", 1),  # giver_id + status (時段1)
            (None, 2, "PENDING", 1),  # taker_id + status (時段3)
            (1, 2, "AVAILABLE", 1),  # 所有篩選條件 (時段1)
        ],
    )
    def test_list_schedules_with_filters(
        self,
        mock_logger,
        service,
        mock_db,
        giver_id,
        taker_id,
        status_filter,
        expected_count,
    ):
        """測試查詢時段列表 - 使用篩選條件 - 成功。"""
        # GIVEN：建立模擬的時段列表
        mock_schedules = [
            self.create_mock_schedule(
                id=1,
                giver_id=1,
                taker_id=2,
                date=date(2024, 1, 15),
                start_time=time(9, 0),
                end_time=time(10, 0),
                status=ScheduleStatusEnum.AVAILABLE,
            ),
            self.create_mock_schedule(
                id=2,
                giver_id=1,
                taker_id=3,
                date=date(2024, 1, 16),
                start_time=time(14, 0),
                end_time=time(15, 0),
                status=ScheduleStatusEnum.PENDING,
            ),
            self.create_mock_schedule(
                id=3,
                giver_id=2,
                taker_id=2,
                date=date(2024, 1, 17),
                start_time=time(16, 0),
                end_time=time(17, 0),
                status=ScheduleStatusEnum.PENDING,
            ),
        ]

        # 根據篩選條件篩選模擬資料
        filtered_schedules = []
        for schedule in mock_schedules:
            match = True  # 預設匹配，只要有任何條件不符合就設為 False

            # 檢查 giver_id 篩選條件：如果指定了 giver_id 但時段的 giver_id 不匹配，則不符合
            if giver_id is not None and schedule.giver_id != giver_id:
                match = False

            # 檢查 taker_id 篩選條件：如果指定了 taker_id 但時段的 taker_id 不匹配，則不符合
            if taker_id is not None and schedule.taker_id != taker_id:
                match = False

            # 檢查 status 篩選條件：如果指定了 status 但時段的狀態不匹配，則不符合
            if status_filter is not None and schedule.status.value != status_filter:
                match = False

            # 如果所有篩選條件都符合，則將時段加入結果列表
            if match:
                filtered_schedules.append(schedule)

        # 模擬 CRUD 層查詢返回時段列表
        with patch.object(service.schedule_crud, 'list_schedules') as mock_list:
            # 設定模擬返回值
            mock_list.return_value = filtered_schedules

            # WHEN：查詢時段列表（使用篩選條件）
            result = service.list_schedules(mock_db, giver_id, taker_id, status_filter)

            # THEN：確認 CRUD 層被正確呼叫
            mock_list.assert_called_once_with(
                mock_db, giver_id, taker_id, status_filter
            )

            # 確認查詢成功
            assert result == filtered_schedules
            assert len(result) == expected_count

            # 確認記錄了查詢日誌
            mock_logger.info.assert_called_once_with(
                f"查詢時段列表完成: giver_id={giver_id}, taker_id={taker_id}, "
                f"status_filter={status_filter}, 找到 {len(filtered_schedules)} 個時段"
            )

    @patch('app.services.schedule.logger')
    @pytest.mark.parametrize(
        "giver_id,taker_id,status_filter,error_message",
        [
            # 無效的 giver_id
            (-1, None, None, "無效的 giver_id"),
            (0, None, None, "無效的 giver_id"),
            # 無效的 taker_id
            (None, -1, None, "無效的 taker_id"),
            (None, 0, None, "無效的 taker_id"),
            # 無效的 status_filter
            (None, None, "INVALID_STATUS", "無效的狀態篩選條件"),
            (None, None, "", "無效的狀態篩選條件"),
            (None, None, "invalid_status", "無效的狀態篩選條件"),
            # 多重無效參數
            (-1, -1, "INVALID_STATUS", "無效的篩選參數"),
        ],
    )
    def test_list_schedules_invalid_parameters(
        self,
        mock_logger,
        service,
        mock_db,
        giver_id,
        taker_id,
        status_filter,
        error_message,
    ):
        """測試查詢時段列表 - 無效的篩選參數。"""
        # GIVEN：準備測試參數（包含無效的篩選條件）

        # 模擬 CRUD 層拋出驗證錯誤
        with patch.object(service.schedule_crud, 'list_schedules') as mock_list:
            # 設定模擬拋出異常
            mock_list.side_effect = ValueError(error_message)

            # WHEN & THEN：確認拋出資料庫錯誤（會被裝飾器轉換為 DatabaseError）
            with pytest.raises(DatabaseError):
                service.list_schedules(mock_db, giver_id, taker_id, status_filter)

            # 確認 CRUD 層被正確呼叫
            mock_list.assert_called_once_with(
                mock_db, giver_id, taker_id, status_filter
            )

    @patch('app.services.schedule.logger')
    @pytest.mark.parametrize(
        "giver_id,taker_id,status_filter,error_message",
        [
            # 單一參數組合的 CRUD 錯誤
            (1, None, None, "資料庫操作失敗"),
            (None, 2, None, "資料庫操作失敗"),
            (None, None, "AVAILABLE", "資料庫操作失敗"),
            # 多重參數組合的 CRUD 錯誤
            (1, 2, None, "資料庫操作失敗"),
            (1, None, "PENDING", "資料庫操作失敗"),
            (None, 2, "AVAILABLE", "資料庫操作失敗"),
            (1, 2, "AVAILABLE", "資料庫操作失敗"),
            # 無篩選條件的 CRUD 錯誤
            (None, None, None, "資料庫操作失敗"),
        ],
    )
    def test_list_schedules_crud_error(
        self,
        mock_logger,
        service,
        mock_db,
        giver_id,
        taker_id,
        status_filter,
        error_message,
    ):
        """測試查詢時段列表 - CRUD 層錯誤。"""
        # GIVEN：準備測試參數

        # 模擬 CRUD 層拋出資料庫錯誤
        with patch.object(service.schedule_crud, 'list_schedules') as mock_list:
            # 設定模擬拋出異常
            mock_list.side_effect = Exception(error_message)

            # WHEN & THEN：確認拋出資料庫錯誤（會被裝飾器轉換為 DatabaseError）
            with pytest.raises(DatabaseError):
                service.list_schedules(mock_db, giver_id, taker_id, status_filter)

            # 確認 CRUD 層被正確呼叫
            mock_list.assert_called_once_with(
                mock_db, giver_id, taker_id, status_filter
            )

    # ===== 查詢單一時段 =====
    @patch('app.services.schedule.logger')
    def test_get_schedule_success(self, mock_logger, service, mock_db):
        """測試查詢單一時段 - 成功。"""
        # GIVEN：準備測試資料
        schedule_id = 1

        mock_schedule = self.create_mock_schedule(
            id=1,
            giver_id=1,
            taker_id=2,
            date=date(2024, 1, 15),
            start_time=time(9, 0),
            end_time=time(10, 0),
            status=ScheduleStatusEnum.AVAILABLE,
        )

        # 模擬 CRUD 層查詢返回時段
        with patch.object(service.schedule_crud, 'get_schedule') as mock_get:
            # 設定模擬返回值
            mock_get.return_value = mock_schedule

            # WHEN：查詢單一時段
            result = service.get_schedule(mock_db, schedule_id)

            # THEN：驗證 CRUD 層被正確呼叫
            mock_get.assert_called_once_with(mock_db, schedule_id)

            # 驗證查詢成功
            assert result == mock_schedule

            # 驗證返回對象的屬性值
            assert result.id == 1
            assert result.giver_id == 1
            assert result.taker_id == 2
            assert result.date == date(2024, 1, 15)
            assert result.start_time == time(9, 0)
            assert result.end_time == time(10, 0)
            assert result.status == ScheduleStatusEnum.AVAILABLE

            # 確認記錄了查詢日誌
            mock_logger.info.assert_called_once_with(
                f"查詢時段完成: schedule_id={schedule_id}, "
                f"giver_id={mock_schedule.giver_id}, taker_id={mock_schedule.taker_id}, "
                f"status={mock_schedule.status.value}, date={mock_schedule.date}"
            )

    @patch('app.services.schedule.logger')
    def test_get_schedule_not_found(self, mock_logger, service, mock_db):
        """測試查詢單一時段 - 時段不存在。"""
        # GIVEN：準備測試資料
        schedule_id = 999  # 不存在的 ID

        # 模擬 CRUD 層查詢返回 None（時段不存在）
        with patch.object(service.schedule_crud, 'get_schedule') as mock_get:
            # 設定模擬返回值
            mock_get.return_value = None

            # WHEN & THEN：確認拋出時段不存在錯誤
            with pytest.raises(ScheduleNotFoundError):
                service.get_schedule(mock_db, schedule_id)

    # # ===== 更新時段 =====
    # @patch('app.services.schedule.logger')
    # def test_update_schedule_success(self, mock_logger, service, mock_db):
    #     """測試更新時段 - 成功。"""
    #     # GIVEN：準備測試資料
    #     schedule_id = 1
    #     updated_by = 2
    #     updated_by_role = UserRoleEnum.GIVER

    #     # 更新前的時段資料（原始狀態）
    #     original_schedule_data = {
    #         "schedule_date": date(2024, 1, 15),
    #         "start_time": time(9, 0),
    #         "end_time": time(10, 0),
    #         "note": "原始備註",
    #     }

    #     # 更新後的時段資料（要更新的內容）
    #     update_data = {
    #         "schedule_date": date(2024, 1, 16),  # 更新：日期從 15 改為 16
    #         "start_time": time(10, 0),  # 更新：開始時間從 9:00 改為 10:00
    #         "end_time": time(11, 0),  # 更新：結束時間從 10:00 改為 11:00
    #         "note": "更新後的備註",  # 更新：備註內容改變
    #     }

    #     # 建立模擬的更新後時段
    #     mock_updated_schedule = self.create_mock_schedule(
    #         id=schedule_id,
    #         giver_id=1,
    #         taker_id=2,
    #         date=update_data["schedule_date"],  # 使用更新後的日期
    #         start_time=update_data["start_time"],  # 使用更新後的開始時間
    #         end_time=update_data["end_time"],  # 使用更新後的結束時間
    #         note=update_data["note"],  # 使用更新後的備註
    #         status=ScheduleStatusEnum.AVAILABLE,
    #     )

    #     # 模擬重疊檢查：返回空列表表示沒有重疊
    #     with patch.object(service, 'check_update_overlap', return_value=[]):
    #         # 模擬 CRUD 層更新：返回更新後的時段
    #         with patch.object(service.schedule_crud, 'update_schedule') as mock_update:
    #             # 設定模擬返回值
    #             mock_update.return_value = mock_updated_schedule

    #             # WHEN：更新時段
    #             result = service.update_schedule(
    #                 mock_db, schedule_id, updated_by, updated_by_role, **update_data
    #             )

    #             # THEN：驗證重疊檢查被正確呼叫
    #             service.check_update_overlap.assert_called_once_with(
    #                 mock_db, schedule_id, **update_data
    #             )

    #             # 驗證 CRUD 層被正確呼叫
    #             mock_update.assert_called_once_with(
    #                 db=mock_db,
    #                 schedule_id=schedule_id,
    #                 updated_by=updated_by,
    #                 updated_by_role=updated_by_role,
    #                 **update_data,
    #             )

    #             # 確認更新成功
    #             assert result == mock_updated_schedule

    #             # 確認記錄了更新成功日誌
    #             mock_logger.info.assert_any_call(
    #                 f"時段 {schedule_id} 更新成功，更新者: {updated_by} (角色: {updated_by_role.value})"
    #             )

    # @patch('app.services.schedule.logger')
    # def test_update_schedule_overlap_error(self, mock_logger, service, mock_db):
    #     """測試更新時段 - 重疊錯誤。"""
    #     # GIVEN：準備測試資料
    #     schedule_id = 1
    #     updated_by = 2
    #     updated_by_role = UserRoleEnum.GIVER

    #     # 要更新的時段資料（會與現有時段重疊）
    #     update_data = {
    #         "schedule_date": date(2024, 1, 16),  # 更新到新日期
    #         "start_time": time(10, 0),  # 更新開始時間
    #         "end_time": time(11, 0),  # 更新結束時間
    #     }

    #     # 建立模擬的現有重疊時段（資料庫中已存在的時段）
    #     mock_overlapping_schedule = self.create_mock_schedule(
    #         id=2,  # 不同的時段 ID
    #         giver_id=1,  # 同一個 Giver
    #         date=date(2024, 1, 16),  # 同一個日期
    #         start_time=time(9, 30),  # 重疊：9:30-10:30 與 10:00-11:00 重疊
    #         end_time=time(10, 30),
    #     )

    #     # 模擬重疊檢查：返回重疊時段
    #     with patch.object(
    #         service, 'check_update_overlap', return_value=[mock_overlapping_schedule]
    #     ):
    #         # WHEN & THEN：當檢測到重疊時段時，拋出錯誤並阻止建立
    #         with pytest.raises(ScheduleOverlapError):
    #             service.update_schedule(
    #                 mock_db, schedule_id, updated_by, updated_by_role, **update_data
    #             )

    #         # 確認記錄了警告日誌
    #         mock_logger.warning.assert_called_with(
    #             f"更新時段 {schedule_id} 時檢測到重疊: "
    #             f"重疊數量={len([mock_overlapping_schedule])}, "
    #             f"更新者={updated_by}, 角色={updated_by_role.value}"
    #         )

    # # ===== 刪除時段 =====
    # @patch('app.services.schedule.logger')
    # def test_delete_schedule_success(self, mock_logger, service, mock_db):
    #     """測試刪除時段 - 成功。"""
    #     # GIVEN：準備測試資料
    #     schedule_id = 1
    #     deleted_by = 2
    #     deleted_by_role = UserRoleEnum.GIVER

    #     # 模擬 CRUD 層刪除返回成功結果
    #     with patch.object(service.schedule_crud, 'delete_schedule') as mock_delete:
    #         # 設定模擬返回值
    #         mock_delete.return_value = DeletionResult.SUCCESS

    #         # WHEN：刪除時段
    #         result = service.delete_schedule(
    #             mock_db, schedule_id, deleted_by, deleted_by_role
    #         )

    #         # THEN：驗證 CRUD 層被正確呼叫
    #         mock_delete.assert_called_once_with(
    #             mock_db, schedule_id, deleted_by, deleted_by_role
    #         )

    #         # 確認刪除成功
    #         assert result is True

    #         # 確認記錄了成功日誌
    #         mock_logger.info.assert_called_once_with(
    #             f"時段 {schedule_id} 軟刪除成功, "
    #             f"deleted_by={deleted_by}, role={deleted_by_role}"
    #         )

    # @patch('app.services.schedule.logger')
    # def test_delete_schedule_not_found(self, mock_logger, service, mock_db):
    #     """測試刪除時段 - 時段不存在。"""
    #     # GIVEN：準備測試資料
    #     schedule_id = 999  # 不存在的 ID
    #     deleted_by = 2
    #     deleted_by_role = UserRoleEnum.GIVER

    #     # 模擬 CRUD 層刪除返回不存在結果
    #     with patch.object(service.schedule_crud, 'delete_schedule') as mock_delete:
    #         # 設定模擬返回值
    #         mock_delete.return_value = DeletionResult.NOT_FOUND

    #         # WHEN & THEN：確認拋出時段不存在錯誤
    #         with pytest.raises(ScheduleNotFoundError):
    #             service.delete_schedule(
    #                 mock_db, schedule_id, deleted_by, deleted_by_role
    #             )

    #         # 驗證 CRUD 層被正確呼叫
    #         mock_delete.assert_called_once_with(
    #             mock_db, schedule_id, deleted_by, deleted_by_role
    #         )

    #         # 確認記錄了警告日誌
    #         mock_logger.warning.assert_called_once_with(f"時段 {schedule_id} 不存在")

    # @pytest.mark.parametrize(
    #     "schedule_status,expected_status_value",
    #     [
    #         (ScheduleStatusEnum.ACCEPTED, "ACCEPTED"),
    #         (ScheduleStatusEnum.COMPLETED, "COMPLETED"),
    #     ],
    # )
    # @patch('app.services.schedule.logger')
    # def test_delete_schedule_cannot_delete(
    #     self, mock_logger, service, mock_db, schedule_status, expected_status_value
    # ):
    #     """測試刪除時段 - 無法刪除（狀態不允許）。"""
    #     # GIVEN：準備測試資料
    #     schedule_id = 1
    #     deleted_by = 2
    #     deleted_by_role = UserRoleEnum.GIVER

    #     # 建立模擬的時段（狀態不允許刪除）
    #     mock_schedule = self.create_mock_schedule(
    #         id=schedule_id,
    #         status=schedule_status,
    #     )

    #     # 模擬 CRUD 層刪除返回無法刪除結果
    #     with patch.object(service.schedule_crud, 'delete_schedule') as mock_delete:
    #         mock_delete.return_value = DeletionResult.CANNOT_DELETE

    #         # 模擬查詢時段（包含已刪除的）
    #         with patch.object(
    #             service.schedule_crud, 'get_schedule_including_deleted'
    #         ) as mock_get:
    #             mock_get.return_value = mock_schedule

    #             # WHEN & THEN：確認拋出無法刪除錯誤
    #             with pytest.raises(ScheduleCannotBeDeletedError):
    #                 service.delete_schedule(
    #                     mock_db, schedule_id, deleted_by, deleted_by_role
    #                 )

    #             # 驗證 CRUD 層被正確呼叫
    #             mock_delete.assert_called_once_with(
    #                 mock_db, schedule_id, deleted_by, deleted_by_role
    #             )
    #             mock_get.assert_called_once_with(mock_db, schedule_id)

    #             # 確認記錄了警告日誌
    #             mock_logger.warning.assert_called_once_with(
    #                 f"時段 {schedule_id} 無法刪除，狀態不允許，當前狀態: {expected_status_value}"
    #             )

    # @patch('app.services.schedule.logger')
    # def test_delete_schedule_already_deleted(self, mock_logger, service, mock_db):
    #     """測試刪除時段 - 已經刪除。"""
    #     # GIVEN：準備測試資料
    #     schedule_id = 1
    #     deleted_by = 2
    #     deleted_by_role = UserRoleEnum.GIVER

    #     # 模擬 CRUD 層刪除返回已經刪除結果
    #     with patch.object(service.schedule_crud, 'delete_schedule') as mock_delete:
    #         # 設定模擬返回值
    #         mock_delete.return_value = DeletionResult.ALREADY_DELETED

    #         # WHEN & THEN：確認拋出時段不存在錯誤
    #         with pytest.raises(ScheduleNotFoundError):
    #             service.delete_schedule(
    #                 mock_db, schedule_id, deleted_by, deleted_by_role
    #             )

    #         # 驗證 CRUD 層被正確呼叫
    #         mock_delete.assert_called_once_with(
    #             mock_db, schedule_id, deleted_by, deleted_by_role
    #         )

    #         # 確認記錄了警告日誌
    #         mock_logger.warning.assert_called_once_with(f"時段 {schedule_id} 已經刪除")

    # @patch('app.services.schedule.logger')
    # def test_delete_schedule_unknown_result(self, mock_logger, service, mock_db):
    #     """測試刪除時段 - 防禦性程式設計：處理未預期的刪除結果。"""
    #     # GIVEN：準備測試資料
    #     schedule_id = 1
    #     deleted_by = 2
    #     deleted_by_role = UserRoleEnum.GIVER

    #     # 使用不存在的枚舉值，模擬未知結果以觸發 case _: 分支
    #     unknown_result = "UNKNOWN_RESULT"

    #     # 模擬 CRUD 層刪除返回未知結果
    #     with patch.object(service.schedule_crud, 'delete_schedule') as mock_delete:
    #         # 設定模擬返回值為未知結果
    #         mock_delete.return_value = unknown_result

    #         # WHEN & THEN：確認拋出業務邏輯錯誤
    #         with pytest.raises(BusinessLogicError) as exc_info:
    #             service.delete_schedule(
    #                 mock_db, schedule_id, deleted_by, deleted_by_role
    #             )

    #         # 驗證錯誤訊息包含未知結果
    #         assert "未知的刪除結果" in str(exc_info.value)
    #         assert str(unknown_result) in str(exc_info.value)

    #         # 驗證 CRUD 層被正確呼叫
    #         mock_delete.assert_called_once_with(
    #             mock_db, schedule_id, deleted_by, deleted_by_role
    #         )

    #         # 確認記錄了錯誤日誌
    #         mock_logger.error.assert_called_once_with(
    #             f"時段 {schedule_id} 刪除時發生未知錯誤: {unknown_result}"
    #         )
