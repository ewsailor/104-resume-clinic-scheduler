"""時段服務層模組。

提供時段相關的業務邏輯處理，包括時段重疊檢查、時段管理等。
"""

# ===== 標準函式庫 =====
import logging

# ===== 第三方套件 =====
# from sqlalchemy import and_
from sqlalchemy.orm import Session

# ===== 本地模組 =====
from app.crud.schedule import ScheduleCRUD

# from app.decorators import (
#     handle_service_errors_sync,
#     log_operation,
# )
from app.enums.models import UserRoleEnum
from app.enums.operations import OperationContext  # , DeletionResult

# from app.errors import (
#     create_business_logic_error,
#     # create_schedule_cannot_be_deleted_error,
#     # create_schedule_not_found_error,
#     create_schedule_overlap_error,
# )
# from app.errors.exceptions import ScheduleNotFoundError
from app.models.schedule import Schedule
from app.schemas import ScheduleBase

# from typing import Any


# 建立日誌記錄器：可在日誌中看到訊息從哪個模組來，利於除錯與維運
logger = logging.getLogger(__name__)


class ScheduleService:
    """時段服務類別。"""

    def __init__(self) -> None:
        """初始化服務實例。"""
        self.schedule_crud = ScheduleCRUD()

    # def check_schedule_overlap(
    #     self,
    #     db: Session,
    #     giver_id: int,
    #     schedule_date: date,
    #     start_time: time,
    #     end_time: time,
    #     exclude_schedule_id: int | None = None,
    # ) -> list[Schedule]:
    #     """檢查單一時段重疊。"""
    #     query = (
    #         db.query(Schedule)  # 查詢 Schedule 資料表
    #         .options(*self.schedule_crud.get_schedule_query_options())  # 載入所有關聯
    #         .filter(
    #             Schedule.giver_id == giver_id,  # 限定同一個 Giver 的時段
    #             Schedule.date == schedule_date,  # 限定同一個日期的時段
    #             Schedule.deleted_at.is_(None),  # 排除已軟刪除的時段
    #         )
    #     )

    #     # 更新時段時排除自己，避免查詢結果「和自己重疊」造成誤判
    #     if exclude_schedule_id is not None:  # 判斷是否處於「修改」模式
    #         query = query.filter(Schedule.id != exclude_schedule_id)

    #     # 檢查時間重疊：確保新時段與現有時段不重疊
    #     overlapping_schedules = query.filter(
    #         and_(
    #             start_time
    #             < Schedule.end_time,  # 新時段開始時間必須小於現有時段結束時間
    #             end_time
    #             > Schedule.start_time,  # 新時段結束時間必須大於現有時段開始時間
    #         )
    #     ).all()  # 取出符合條件的所有紀錄，非空代表有重疊

    #     logger.info(
    #         f"時段重疊檢查完成: giver_id={giver_id}, date={schedule_date}, "
    #         f"time={start_time}-{end_time}, 重疊數量={len(overlapping_schedules)}"
    #     )

    #     return overlapping_schedules

    # def check_multiple_schedules_overlap(
    #     self,
    #     db: Session,
    #     schedules: list[ScheduleBase],
    # ) -> list[Schedule]:
    #     """檢查多個時段重疊。"""
    #     # 初始化重疊時段列表，用於收集所有重疊的時段
    #     all_overlapping_schedules = []

    #     # 逐一檢查每個時段是否與現有資料庫中的時段重疊
    #     for schedule_data in schedules:
    #         overlapping_schedules = self.check_schedule_overlap(
    #             db=db,
    #             giver_id=schedule_data.giver_id,
    #             schedule_date=schedule_data.schedule_date,
    #             start_time=schedule_data.start_time,
    #             end_time=schedule_data.end_time,
    #         )

    #         # 如果發現重疊時段，將其加入到總重疊列表中
    #         if overlapping_schedules:
    #             all_overlapping_schedules.extend(overlapping_schedules)

    #     # 不做錯誤處理，因為 check_schedule_overlap 已經處理錯誤日誌

    #     return all_overlapping_schedules

    # def determine_schedule_status(
    #     self,
    #     created_by_role: UserRoleEnum,
    #     schedule_data: ScheduleBase,
    # ) -> ScheduleStatusEnum:
    #     """根據建立者角色決定時段狀態。"""
    #     # 如果 schedule_data 有明確指定狀態（不是預設的 DRAFT），優先使用，例如系統匯入舊資料庫中的時段
    #     if (
    #         schedule_data.status is not None
    #         and schedule_data.status != ScheduleStatusEnum.DRAFT
    #     ):
    #         return schedule_data.status

    #     # 如果狀態是 DRAFT（預設值），則根據建立者角色決定預設狀態
    #     match created_by_role:
    #         case UserRoleEnum.TAKER:
    #             return ScheduleStatusEnum.PENDING
    #         case UserRoleEnum.GIVER:
    #             return ScheduleStatusEnum.AVAILABLE
    #         case _:
    #             # 預設為 DRAFT
    #             return ScheduleStatusEnum.DRAFT

    # def log_schedule_details(
    #     self,
    #     schedules: list[ScheduleBase],
    #     context: OperationContext = OperationContext.CREATE,  # 預設為建立操作
    # ) -> None:
    #     """記錄時段詳情。"""
    #     # 檢查時段列表是否為空，避免處理空資料
    #     if not schedules:
    #         logger.info(f"{context.value}時段: 無時段資料")
    #         return

    #     # 初始化時段詳情列表，用於收集格式化的時段資訊
    #     schedule_details = []

    #     # 逐一處理每個時段，生成可讀的詳情描述
    #     for i, schedule_data in enumerate(schedules):
    #         # 格式化單一時段資訊：序號 + 日期 + 時間範圍
    #         detail = (
    #             f"時段{i+1}: {schedule_data.schedule_date} "  # 時段序號和日期
    #             f"{schedule_data.start_time}-{schedule_data.end_time}"  # 時間範圍
    #         )
    #         schedule_details.append(detail)

    #     logger.info(f"{context.value}時段詳情: {', '.join(schedule_details)}")

    def create_schedule_orm_objects(
        self,
        schedules: list[ScheduleBase],
        created_by: int,
        created_by_role: UserRoleEnum,
    ) -> list[Schedule]:
        """建立時段 ORM 物件列表。"""
        # 初始化 ORM 物件列表，用於收集所有建立的時段實體
        schedule_orm_objects = []

        # 逐一處理每個時段資料，轉換為 ORM 物件
        for schedule_data in schedules:
            # 根據建立者角色決定時段狀態
            # status = self.determine_schedule_status(created_by_role, schedule_data)

            # 建立時段 ORM 實體，將 Pydantic 模型轉換為 SQLAlchemy 模型
            schedule_orm = Schedule(
                giver_id=schedule_data.giver_id,
                taker_id=schedule_data.taker_id,
                date=schedule_data.schedule_date,
                start_time=schedule_data.start_time,
                end_time=schedule_data.end_time,
                note=schedule_data.note,
                status=schedule_data.status,
                created_by=created_by,
                created_by_role=created_by_role,
                updated_by=created_by,
                updated_by_role=created_by_role,
                deleted_by=None,
                deleted_by_role=None,
            )

            # 將建立的 ORM 物件加入到列表中
            schedule_orm_objects.append(schedule_orm)

        return schedule_orm_objects

    # @handle_service_errors_sync("建立時段")
    # @log_operation("建立時段")
    def create_schedules(
        self,
        db: Session,
        schedules: list[ScheduleBase],
        created_by: int,
        created_by_role: UserRoleEnum,
    ) -> list[Schedule]:
        """建立多個時段。"""
        # 記錄時段詳情，便於追蹤和除錯
        # self.log_schedule_details(schedules, OperationContext.CREATE)

        # 檢查時段重疊：確保新時段與現有時段不重疊
        # overlapping_schedules = self.check_multiple_schedules_overlap(db, schedules)

        # # 如果發現重疊，記錄警告並拋出錯誤，阻止建立時段
        # if overlapping_schedules:
        #     logger.warning(
        #         f"建立時段時檢測到重疊: " f"重疊數量={len(overlapping_schedules)}, "
        #     )
        #     error_msg = (
        #         f"檢測到 {len(overlapping_schedules)} 個重疊時段，請調整時段之時間"
        #     )
        #     raise create_schedule_overlap_error(error_msg, overlapping_schedules)

        # 將 Pydantic 模型轉換為 ORM 物件
        created_schedules = self.create_schedule_orm_objects(
            schedules, created_by, created_by_role
        )

        # 呼叫 CRUD 層，將 ORM 物件儲存到資料庫
        created_schedules = self.schedule_crud.create_schedules(db, created_schedules)

        logger.info(
            f"成功建立 {len(created_schedules)} 個時段，"
            f"ID 範圍: {[s.id for s in created_schedules]}"
        )

        return created_schedules

    # @handle_service_errors_sync("查詢時段列表")
    # @log_operation("查詢時段列表")
    # def list_schedules(
    #     self,
    #     db: Session,
    #     giver_id: int | None = None,
    #     taker_id: int | None = None,
    #     status_filter: str | None = None,
    # ) -> list[Schedule]:
    #     """查詢時段列表。"""
    #     # 呼叫 CRUD 層進行資料庫查詢，支援多種篩選條件
    #     schedules = self.schedule_crud.list_schedules(
    #         db, giver_id, taker_id, status_filter
    #     )

    #     logger.info(
    #         f"查詢時段列表完成: giver_id={giver_id}, taker_id={taker_id}, "
    #         f"status_filter={status_filter}, 找到 {len(schedules)} 個時段"
    #     )

    #     return schedules

    # @handle_service_errors_sync("查詢單一時段")
    # @log_operation("查詢單一時段")
    # def get_schedule(
    #     self,
    #     db: Session,
    #     schedule_id: int,
    # ) -> Schedule:
    #     """根據 ID 查詢單一時段。"""
    #     # 呼叫 CRUD 層查詢指定 ID 的時段
    #     schedule = self.schedule_crud.get_schedule(db, schedule_id)

    #     # 檢查時段是否存在
    #     if schedule is None:
    #         raise ScheduleNotFoundError(schedule_id)

    #     logger.info(
    #         f"查詢時段完成: schedule_id={schedule_id}, "
    #         f"giver_id={schedule.giver_id}, taker_id={schedule.taker_id}, "
    #         f"status={schedule.status.value}, date={schedule.date}"
    #     )

    #     return schedule

    # def new_updated_time_values(
    #     self,
    #     db: Session,
    #     schedule_id: int,
    #     **kwargs: Any,
    # ) -> tuple[date, time, time]:
    #     """更新後的時間值。"""
    #     # 取得現有時段的資訊，用於比較和預設值
    #     schedule = self.schedule_crud.get_schedule(db, schedule_id)

    #     # 取得更新後的時間值：如果沒有提供新值，則使用現有值
    #     new_date = kwargs.get("schedule_date", schedule.date)
    #     new_start_time = kwargs.get("start_time", schedule.start_time)
    #     new_end_time = kwargs.get("end_time", schedule.end_time)

    #     return new_date, new_start_time, new_end_time

    # def _needs_overlap_check(self, **kwargs: Any) -> bool:
    #     """檢查是否需要進行重疊檢查。

    #     只有更新時間相關欄位（日期、開始時間或結束時間）才需要檢查重疊。
    #     """
    #     time_related_fields = ["schedule_date", "start_time", "end_time"]
    #     return any(field in kwargs for field in time_related_fields)

    # def check_update_overlap(
    #     self,
    #     db: Session,
    #     schedule_id: int,
    #     **kwargs: Any,
    # ) -> list[Schedule]:
    #     """檢查更新時段時的重疊情況。"""
    #     # 如果沒有更新時間相關欄位，則不需要檢查重疊
    #     if not self._needs_overlap_check(**kwargs):
    #         return []

    #     # 取得現有時段資訊和更新後的時間值
    #     schedule = self.schedule_crud.get_schedule(db, schedule_id)
    #     new_date, new_start_time, new_end_time = self.new_updated_time_values(
    #         db, schedule_id, **kwargs
    #     )

    #     # 更新時段時排除自己，避免查詢結果「和自己重疊」造成誤判
    #     overlapping_schedules = self.check_schedule_overlap(
    #         db=db,
    #         giver_id=int(schedule.giver_id),
    #         schedule_date=new_date,
    #         start_time=new_start_time,
    #         end_time=new_end_time,
    #         exclude_schedule_id=schedule_id,
    #     )

    #     return overlapping_schedules

    # @handle_service_errors_sync("更新時段")
    # @log_operation("更新時段")
    # def update_schedule(
    #     self,
    #     db: Session,
    #     schedule_id: int,
    #     updated_by: int,
    #     updated_by_role: UserRoleEnum,
    #     **kwargs: Any,
    # ) -> Schedule:
    #     """更新時段。"""
    #     # 檢查更新時是否會造成時段重疊
    #     overlapping_schedules = self.check_update_overlap(db, schedule_id, **kwargs)

    #     # 如果發現重疊，記錄警告並拋出錯誤阻止更新
    #     if overlapping_schedules:
    #         logger.warning(
    #             f"更新時段 {schedule_id} 時檢測到重疊: "
    #             f"重疊數量={len(overlapping_schedules)}, "
    #             f"更新者={updated_by}, 角色={updated_by_role.value}"
    #         )
    #         error_msg = f"更新時段 {schedule_id} 時，檢測到 {len(overlapping_schedules)} 個重疊時段，請調整時段之時間"
    #         raise create_schedule_overlap_error(error_msg, overlapping_schedules)

    #     # 呼叫 CRUD 層進行實際的資料庫更新操作
    #     updated_schedule = self.schedule_crud.update_schedule(
    #         db=db,
    #         schedule_id=schedule_id,
    #         updated_by=updated_by,
    #         updated_by_role=updated_by_role,
    #         **kwargs,
    #     )

    #     logger.info(
    #         f"時段 {schedule_id} 更新成功，更新者: {updated_by} (角色: {updated_by_role.value})"
    #     )

    #     return updated_schedule

    # @handle_service_errors_sync("軟刪除時段")
    # @log_operation("軟刪除時段")
    # def delete_schedule(
    #     self,
    #     db: Session,
    #     schedule_id: int,
    #     deleted_by: int | None = None,
    #     deleted_by_role: UserRoleEnum | None = None,
    # ) -> bool:
    #     """軟刪除時段。"""
    #     # 呼叫 CRUD 層進行軟刪除操作，取得刪除結果
    #     deletion_result = self.schedule_crud.delete_schedule(
    #         db, schedule_id, deleted_by, deleted_by_role
    #     )

    #     # 使用 match-case 語法處理不同的刪除結果
    #     match deletion_result:
    #         case DeletionResult.SUCCESS:
    #             # 刪除成功：記錄成功日誌並返回 True
    #             logger.info(
    #                 f"時段 {schedule_id} 軟刪除成功, "
    #                 f"deleted_by={deleted_by}, role={deleted_by_role}"
    #             )
    #             return True
    #         case DeletionResult.NOT_FOUND:
    #             # 時段不存在：記錄警告並拋出錯誤
    #             logger.warning(f"時段 {schedule_id} 不存在")
    #             raise create_schedule_not_found_error(schedule_id)
    #         case DeletionResult.CANNOT_DELETE:
    #             # 無法刪除：時段狀態為 ACCEPTED 或 COMPLETED 不允許刪除
    #             schedule = self.schedule_crud.get_schedule_including_deleted(
    #                 db, schedule_id
    #             )

    #             # 如果時段不存在或狀態為 None，則標記為 UNKNOWN，避免 None 值造成的錯誤
    #             schedule_status = (
    #                 schedule.status.value if schedule and schedule.status else "UNKNOWN"
    #             )

    #             # 記錄無法刪除的警告，包含時段 ID 和當前狀態
    #             logger.warning(
    #                 f"時段 {schedule_id} 無法刪除，狀態不允許，當前狀態: {schedule_status}"
    #             )

    #             # 拋出業務邏輯錯誤，包含時段 ID、刪除原因和當前狀態，幫助使用者理解為什麼無法刪除
    #             raise create_schedule_cannot_be_deleted_error(
    #                 schedule_id,
    #                 reason="狀態不允許刪除",
    #                 schedule_status=schedule_status,
    #             )
    #         case DeletionResult.ALREADY_DELETED:
    #             # 已經刪除：記錄警告
    #             logger.warning(f"時段 {schedule_id} 已經刪除")
    #             raise create_schedule_not_found_error(schedule_id)
    #         case _:  # 防禦性程式設計：處理未預期的刪除結果
    #             # 未知錯誤：記錄錯誤並拋出業務邏輯錯誤
    #             logger.error(
    #                 f"時段 {schedule_id} 刪除時發生未知錯誤: {deletion_result}"
    #             )
    #             raise create_business_logic_error(f"未知的刪除結果: {deletion_result}")


# 建立服務實例，供其他模組使用
schedule_service = ScheduleService()
