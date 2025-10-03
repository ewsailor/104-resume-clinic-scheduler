// ======================================================================
//   1. 基礎常數和配置 (Base Constants and Configurations)
// ======================================================================

// 全域常數設定
const CONFIG = {
  // 全域實例
  INSTANCES: {
    GIVER_MODAL: null
  },
  
  // API 配置
  API: {
    BASE_URL: '/api/v1/givers',
    POSTER_URL: 'https://randomuser.me/api/portraits/',
    TIMEOUT: 10000,
    RETRY_DELAY: 1000,
    MAX_RETRIES: 3
  },
  
  // 分頁配置：每頁顯示 12 筆資料
  PAGINATION: {
    GIVERS_PER_PAGE: 12,
    MAX_PAGES_DISPLAY: 10
  },
  
  // UI 配置
  UI: {
    ANIMATION_DURATION: 300,
    DEBOUNCE_DELAY: 250,
    THROTTLE_LIMIT: 100,
    LOADING_TIMEOUT: 5000,
    ERROR_DISPLAY_TIME: 5000
  },
  
  // 顏色配置
  COLORS: {
    DISABLED_TEXT: '#6c757d',  // 禁用狀態的文字顏色（灰色）
    SUCCESS: '#28a745',        // 成功狀態顏色（綠色）
    WARNING: '#ffc107',        // 警告狀態顏色（黃色）
    DANGER: '#dc3545',         // 危險狀態顏色（紅色）
    PRIMARY: '#007bff',        // 主要顏色（藍色）
    SECONDARY: '#6c757d'       // 次要顏色（灰色）
  },
  
  // 聊天配置
  CHAT: {
    MAX_MESSAGE_LENGTH: 2000,
    TYPING_INDICATOR_DELAY: 1000,
    MESSAGE_DISPLAY_TIME: 3000,
    AUTO_SCROLL_DELAY: 100
  },
  
  // 日期選擇器配置
  DATE_PICKER: {
    DEFAULT_OFFSET_DAYS: 7,  // 預設日期偏移天數（一週後）
    MAX_MONTHS_AHEAD: 3,  // 最多可選擇幾個月後的日期
    BUSINESS_HOURS: {
      START: '08:00', // 多數人休息時間開始時間
      END: '24:00' // 多數人休息時間結束時間
    },
    CALENDAR: {
      WEEKS_TO_DISPLAY: 6,     // 顯示的週數
      DAYS_PER_WEEK: 7,        // 每週天數
      TOTAL_CELLS: 42,         // 總格子數 (6週 × 7天)
      MONTHS_IN_YEAR: 12,      // 一年中的月份數
      FIRST_MONTH_INDEX: 0,    // 第一個月份的索引
      LAST_MONTH_INDEX: 11     // 最後一個月份的索引
    },
    TIME: {
      MIN_HOURS: 0,            // 最小小時數
      MAX_HOURS: 23,           // 最大小時數
      MIN_MINUTES: 0,          // 最小分鐘數
      MAX_MINUTES: 59,         // 最大分鐘數
      TIME_INPUT_LENGTH: 4,    // 時間輸入長度
      HOURS_START: 0,          // 小時開始位置
      HOURS_END: 2,            // 小時結束位置
      MINUTES_START: 2,        // 分鐘開始位置
      MINUTES_END: 4,          // 分鐘結束位置
      REGEX: {
        HOURS_PATTERN: '([01]?[0-9]|2[0-3])',  // 小時正則表達式
        MINUTES_PATTERN: '[0-5][0-9]'           // 分鐘正則表達式
      }
    },
    FORMAT: {
      PADDING_LENGTH: 2,       // 補零長度
      PADDING_CHAR: '0'        // 補零字符
    },
    REGEX: {
      DATE_PATTERN: '\\d{4}\\/\\d{2}\\/\\d{2}',  // 日期正則表達式
      SCHEDULE_PATTERN: '(\\d{4}\\/\\d{2}\\/\\d{2})\\s+(\\d{2}:\\d{2})-(\\d{2}:\\d{2})'  // 時段正則表達式
    },
    LOCALE_OPTIONS: {
      HOUR: '2-digit',
      MINUTE: '2-digit',
      HOUR12: false
    },
    SEPARATORS: {
      TIME: ':',                // 時間分隔符
      DATE: '/',                // 日期分隔符
      SCHEDULE: '-',            // 時段分隔符
      PERIOD: '~'               // 時段範圍分隔符
    },
    CALCULATION: {
      MINUTES_PER_HOUR: 60,    // 每小時分鐘數
      MONTH_OFFSET: 1          // 月份偏移量（JavaScript 月份從 0 開始）
    },
    MONTH_NAMES: [
      '一月', '二月', '三月', '四月', '五月', '六月',
      '七月', '八月', '九月', '十月', '十一月', '十二月'
    ],
    WEEKDAYS: ['日', '一', '二', '三', '四', '五', '六']
  },
  
  // 快取配置
  CACHE: {
    EXPIRY_TIME: 5 * 60 * 1000, // 5分鐘
    MAX_SIZE: 100,
    CLEANUP_INTERVAL: 10 * 60 * 1000 // 10分鐘
  },
  
  // DOM 選擇器配置
  SELECTORS: {
    GIVER_PANEL: '#giver-panel',
    PAGINATOR: '#paginator',
    CHAT_INPUT: '#chat-input-message',
    CHAT_SEND_BTN: '#chat-send-btn',
    CHAT_MESSAGES: '#chat-messages',
    GIVER_MODAL: '#giver-modal',
    CONFIRM_MODAL: '#confirm-modal',
    CHAT_MODAL_LABEL: '#chatModalLabel'
  },
  
  // CSS 類別配置
  CLASSES: {
    GIVER_CARD: 'giverCard',
    GIVER_CARD_WRAPPER: 'mb-4',
    GIVER_CARD_POINTER: 'giverCard__pointer',
    GIVER_CARD_AVATAR: 'giverCard__avatar',
    GIVER_CARD_AVATAR_CONTAINER: 'giverCard__avatar-container',
    GIVER_CARD_AVATAR_IMG: 'giverCard__avatar-img',
    GIVER_CARD_USER_INFO: 'giverCard__user-info',
    GIVER_CARD_NAME: 'giverCard__name',
    GIVER_CARD_ICON_GRAY: 'giverCard__icon-gray',
    GIVER_CARD_TITLE: 'giverCard__title',
    GIVER_CARD_COMPANY: 'giverCard__company',
    GIVER_CARD_COUNT: 'giverCard__count',
    GIVER_CARD_COUNT_ITEM: 'giverCard__count-item',
    GIVER_CARD_COUNT_VALUE: 'giverCard__count-value',
    GIVER_CARD_COUNT_LABEL: 'giverCard__count-label',
    GIVER_CARD_DIVIDER: 'giverCard__divider',
    GIVER_CARD_TOPIC: 'giverCard__topic',
    GIVER_CARD_TOPIC_BUTTON: 'btn-topic-sm',
    GIVER_CARD_ACTION: 'giverCard__action',
    GIVER_CARD_ACTION_BUTTON: 'giverCard__action-button',
    PAGINATOR_ITEM: 'pagination__item',
    PAGINATOR_ITEM_ACTIVE: 'pagination__item--active',
    PAGINATOR_ITEM_DISABLED: 'pagination__item--disabled',
    PAGINATOR_LINK: 'pagination__link',
    PAGINATOR_LINK_PREV: 'pagination__link--prev',
    PAGINATOR_LINK_NEXT: 'pagination__link--next',
    PAGINATOR_LINK_PAGE: 'pagination__link--page'
  },
  
  // 預設值配置
  DEFAULTS: {
    GIVER: {
      NAME: '未知用戶',
      TITLE: '職位未填寫',
      COMPANY: '公司未填寫',
      CONSULTED: '0',
      RESPONDING_TIME: '未知',
      EXPERIENCE: '未知',
      IMAGE: 'men/1.jpg'
    }
  },
  
  // 錯誤訊息配置
  MESSAGES: {
    ERROR: {
      NETWORK: '網路連線異常，請檢查網路設定',
      LOADING: '資料載入失敗，請稍後再試',
      VALIDATION: '資料驗證失敗',
      UNKNOWN: '發生未知錯誤'
    },
    SUCCESS: {
      LOADING: '資料載入成功',
      SAVE: '資料儲存成功',
      UPDATE: '資料更新成功'
    },
    INFO: {
      LOADING: '載入中...',
      NO_DATA: '暫無資料'
    }
  },
  
  // Demo 預約時間配置
  DEMO_TIME_SLOTS: {
    "demo-time-1": {
      label: "2025/11/01（週六）20:00~22:00",
      date: "2025/11/01",
      weekday: "週六",
      time: "20:00~22:00"
    },
    "demo-time-2": {
      label: "2025/11/02（週日）20:00~22:00",
      date: "2025/11/02",
      weekday: "週日",
      time: "20:00~22:00"
    }
  },
  
  // UI 文字配置
  UI_TEXT: {
    // 按鈕文字配置
    BUTTONS: {
      SCHEDULE: '我想預約 Giver 時間',
      SKIP: '暫不預約 Giver 時間', 
      CANCEL_RESERVATION: '取消預約',
      CANCEL_OPTION: '取消此選項',
      CANCEL_SCHEDULE: '取消本次預約 Giver 時間',
      VIEW_GIVER_TIME: '查看 Giver 方便的時間',
      VIEW_MY_SCHEDULES_RESERVATION: '查看我已預約 Giver 的時間',
      VIEW_MY_SCHEDULES_PROVIDE: '查看我已提供時段的狀態',
      PROVIDE_SINGLE_TIME: '提供單筆方便時段',
      PROVIDE_MULTIPLE_TIMES: '提供多筆方便時段',
      PROVIDE_MY_TIME: '提供我方便的時間給 Giver',
      PROVIDE_MY_TIME_NOT_AVAILABLE: '可惜 Giver 提供的時間目前我都不方便，讓我提供我方便的時間給 Giver',
      CONTINUE_PROVIDE_SINGLE_TIME: '繼續提供單筆方便時段',
      CONTINUE_PROVIDE_MULTIPLE_TIMES: '繼續提供多筆方便時段',
      SUBMIT_SCHEDULES: '已新增完成所有時段，請協助送出給 Giver',
    },
    // 按鈕組合配置
    BUTTON_GROUPS: {
      'schedule': { text: '我想預約 Giver 時間', class: 'btn-outline btn-option' }, 
      'skip': { text: '暫不預約 Giver 時間', class: 'btn-outline btn-option' },
      'cancel': { text: '取消本次預約 Giver 時間', class: 'btn-outline' },
      'view-times': { text: '查看 Giver 方便的時間', class: 'btn-outline' },
      'view-my-schedules-reservation': { text: '查看我已預約 Giver 的時間', class: 'btn-outline' },
      'view-all': { text: '查看我已提供時段的狀態', class: 'btn-outline' },
      'single-time': { text: '提供單筆方便時段', class: 'btn-outline' },
      'multiple-times': { text: '提供多筆方便時段', class: 'btn-outline' },
      'continue-single-time': { text: '繼續提供單筆方便時段', class: 'btn-outline' },
      'continue-multiple-times': { text: '繼續提供多筆方便時段', class: 'btn-outline' },
      'submit-schedules': { text: '已新增完成所有時段，請協助送出給 Giver', class: 'btn-orange' }
    },
    // 狀態文字配置
    STATUS: {
      GIVER: { // Giver 提供時段，供 Taker 預約
        DRAFT: '草稿：尚未公開預約',
        AVAILABLE: '已公開，尚無人預約',
        PENDING: '有人預約您的時間，待您回覆中',
        ACCEPTED: '您已接受預約',
        REJECTED: '您已婉拒預約',
        CANCELLED: '您已取消提供此時段',
        COMPLETED: '諮詢已完成，感謝您的參與'
      },
      TAKER_VIEW: { // Giver 提供時段後，如果 Taker 時間可以則預約 Giver 的時段，如果 Taker 時間不行則選擇提供時間給 Giver（即下方的 TAKER_OFFER）
        PENDING: '預約 Giver 時間成功，待 Giver 回覆',
        ACCEPTED: 'Giver 已接受預約',
        REJECTED: 'Giver 已婉拒預約', // 如果 Giver 原本可以的時間，在 Taker 預約後，Giver 因為某種原因不行，則顯示此狀態
        CANCELLED: '您已取消預約 Giver 的時間',
        COMPLETED: '諮詢已完成，感謝您的參與'
      },
      TAKER_OFFER: { // Taker 提供時段，供 Giver 回覆是否可以預約，如果 Giver 接受則預約成功，如果 Giver 婉拒則預約失敗
        DRAFT: '草稿：尚未送出給 Giver',
        PENDING: '提供時間成功，待 Giver 回覆',
        ACCEPTED: 'Giver 已接受預約',
        REJECTED: 'Giver 已婉拒預約',
        CANCELLED: '您已取消提供此時段給 Giver',
        COMPLETED: '諮詢已完成，感謝您的參與'
      }
    },
    // 表格標題配置
    TABLE_HEADERS: {
      FIVE_COLUMNS: {
        ORDER: '序',
        STATUS: '狀態',
        TIME_SLOT: '時段',
        NOTES: '備註',
        ACTIONS: '調整'
      }
    },
    
    // 提示文字配置
    PROMPTS: {
      SELECT_NEXT_ACTION: '請選擇接下來的動作：',
    },
    // 預約成功提示文字配置
    RESERVATION_SUCCESS: {
      TEXT: '✅ 預約已送出！<br><br>Giver 已收到您對上述時段的預約通知，請耐心等待對方確認回覆。<br><br>⚠️ 貼心提醒：<br><br>Giver 可能因臨時狀況無法如期面談，請以對方回覆確認為準，謝謝您的體諒！<br><br>以下是您的預約時段：'
    }
  }
};

// 全域常數：為了向後相容，保留舊的常數引用
const BASE_URL = CONFIG.API.BASE_URL;
const POSTER_URL = CONFIG.API.POSTER_URL;
const GIVERS_PER_PAGE = CONFIG.PAGINATION.GIVERS_PER_PAGE;

//  DOM 快取物件：用於快取 DOM 元素，避免重複查詢
const DOM_CACHE = {
  // 私有快取屬性
  _chatMessages: null,
  _scheduleForm: null,
  _dateInput: null,
  _startTimeInput: null,
  _endTimeInput: null,
  _notesInput: null,
  _timeScheduleForm: null,
  _datePickerModal: null,
  _currentMonthYear: null,
  _datePickerCalendar: null,
  _prevMonthBtn: null,
  _nextMonthBtn: null,
  _confirmDateBtn: null,
  _confirmSelectionBtn: null,
  _chatInputMessage: null,
  _chatSendBtn: null,
  _giverModal: null,
  _confirmModal: null,
  _chatModalLabel: null,
  _continueBtn: null,
  _leaveBtn: null,
  
  // Getter 方法 - 懶載入
  get chatMessages() {
    return this._chatMessages || (this._chatMessages = document.getElementById('chat-messages'));
  },
  get scheduleForm() {
    return this._scheduleForm || (this._scheduleForm = document.getElementById('schedule-form'));
  },
  get dateInput() {
    return this._dateInput || (this._dateInput = document.getElementById('schedule-date'));
  },
  get startTimeInput() {
    return this._startTimeInput || (this._startTimeInput = document.getElementById('schedule-start-time'));
  },
  get endTimeInput() {
    return this._endTimeInput || (this._endTimeInput = document.getElementById('schedule-end-time'));
  },
  get notesInput() {
    return this._notesInput || (this._notesInput = document.getElementById('schedule-notes'));
  },
  get timeScheduleForm() {
    return this._timeScheduleForm || (this._timeScheduleForm = document.getElementById('time-schedule-form'));
  },
  get datePickerModal() {
    // 每次都重新抓 DOM，避免快取導致狀態異常
    return document.getElementById('date-picker-modal');
  },
  get currentMonthYear() {
    return this._currentMonthYear || (this._currentMonthYear = document.getElementById('current-month-year'));
  },
  get datePickerCalendar() {
    return this._datePickerCalendar || (this._datePickerCalendar = document.getElementById('date-picker-calendar'));
  },
  get prevMonthBtn() {
    return this._prevMonthBtn || (this._prevMonthBtn = document.getElementById('prev-month'));
  },
  get nextMonthBtn() {
    return this._nextMonthBtn || (this._nextMonthBtn = document.getElementById('next-month'));
  },
  get confirmDateBtn() {
    return this._confirmDateBtn || (this._confirmDateBtn = document.getElementById('confirm-date'));
  },
  get confirmSelectionBtn() {
    return this._confirmSelectionBtn || (this._confirmSelectionBtn = document.getElementById('confirm-selection-btn'));
  },
  get chatInputMessage() {
    return this._chatInputMessage || (this._chatInputMessage = document.getElementById('chat-input-message'));
  },
  get chatSendBtn() {
    return this._chatSendBtn || (this._chatSendBtn = document.getElementById('chat-send-btn'));
  },
  get giverModal() {
    return this._giverModal || (this._giverModal = document.getElementById('giver-modal'));
  },
  get confirmModal() {
    return this._confirmModal || (this._confirmModal = document.getElementById('confirm-modal'));
  },
  get chatModalLabel() {
    return this._chatModalLabel || (this._chatModalLabel = document.getElementById('chatModalLabel'));
  },
  get continueBtn() {
    return this._continueBtn || (this._continueBtn = document.getElementById('continue-btn'));
  },
  get leaveBtn() {
    return this._leaveBtn || (this._leaveBtn = document.getElementById('leave-btn'));
  },
  
  // 重設快取方法
  resetChatMessages() {
    this._chatMessages = null;
  },
  resetScheduleForm() {
    this._scheduleForm = null;
  },
  resetFormInputs() {
    this._dateInput = null;
    this._startTimeInput = null;
    this._endTimeInput = null;
    this._notesInput = null;
    this._timeScheduleForm = null;
  },

  // 清空表單輸入欄位值
  clearFormInputs() {
    const inputs = this.getFormInputs();
    
    // 使用通用設定器清空所有輸入欄位
    const clearConfig = {
      defaultValue: ''
    };
    
    if (inputs.dateInput) setupInputField(inputs.dateInput, clearConfig);
    if (inputs.startTimeInput) setupInputField(inputs.startTimeInput, clearConfig);
    if (inputs.endTimeInput) setupInputField(inputs.endTimeInput, clearConfig);
    if (inputs.notesInput) setupInputField(inputs.notesInput, clearConfig);
  },
  
  // 一次性取得所有表單輸入欄位
  getFormInputs() {
    return {
      dateInput: this.dateInput,
      startTimeInput: this.startTimeInput,
      endTimeInput: this.endTimeInput,
      notesInput: this.notesInput,
      timeScheduleForm: this.timeScheduleForm
    };
  },
  
  // 取得表單資料
  getFormData() {
    const inputs = this.getFormInputs();
    return {
      date: inputs.dateInput?.value || '',
      startTime: inputs.startTimeInput?.value || '',
      endTime: inputs.endTimeInput?.value || '',
      notes: inputs.notesInput?.value || ''
    };
  },
  
  // 重置日期選擇器快取
  resetDatePicker() {
    this._datePickerModal = null;
    this._currentMonthYear = null;
    this._datePickerCalendar = null;
    this._prevMonthBtn = null;
    this._nextMonthBtn = null;
    this._confirmDateBtn = null;
  },

  // 重置所有快取
  resetAll() {
    this._chatMessages = null;
    this._scheduleForm = null;
    this._dateInput = null;
    this._startTimeInput = null;
    this._endTimeInput = null;
    this._notesInput = null;
    this._timeScheduleForm = null;
    this._datePickerModal = null;
    this._currentMonthYear = null;
    this._datePickerCalendar = null;
    this._prevMonthBtn = null;
    this._nextMonthBtn = null;
    this._confirmDateBtn = null;
    this._confirmSelectionBtn = null;
    this._chatInputMessage = null;
    this._chatSendBtn = null;
    this._giverModal = null;
    this._confirmModal = null;
    this._chatModalLabel = null;
    this._continueBtn = null;
    this._leaveBtn = null;
  }
};

// ======================================================================
//   2. 基礎工具：工具函數和通用模組 (Base Tools: Utility Functions and Common Modules)
// ======================================================================

// ======================================================
//   2-1. 延遲函數 (Delay Functions)
// ======================================================

// 延遲時間常數
const DELAY_TIMES = {
  // 聊天相關延遲
  CHAT: {
    RESPONSE: 1000,         // Giver 回覆延遲
    FORM_SUBMIT: 1000,      // 表單提交後延遲
    OPTION_SELECT: 1000,    // 選項選擇後延遲
    SUCCESS_MESSAGE: 1000,  // 成功訊息延遲
    CANCEL_MESSAGE: 1000,   // 取消訊息延遲
    VIEW_TIMES: 1000,       // 查看時間延遲
    SINGLE_TIME: 100,       // 單筆時段處理延遲
    MULTIPLE_TIMES: 1000,   // 多筆時段處理延遲
    SUBMISSION_RESULT: 1000 // 提交結果延遲
  },
  
  // UI 相關延遲
  UI: {
    MODAL_CLEANUP: 150,    // Modal 清理延遲
    FOCUS_TRANSFER: 0,     // 焦點轉移延遲
    FOCUS_RETRY: 50,       // 焦點重試延遲
    BACKDROP_CLEANUP: 0,   // Backdrop 清理延遲
    CLOSE_CONFIRMATION: 150 // 關閉確認延遲
  },
  
  // 錯誤處理延遲
  ERROR: {
    AUTO_REMOVE: 5000,     // 錯誤訊息自動移除
    TOAST_DURATION: 3000,  // Toast 顯示時間
    SUCCESS_DURATION: 3000, // 成功訊息顯示時間
    INFO_DURATION: 3000,    // 資訊訊息顯示時間
    VALIDATION_ERROR: 1000  // 驗證錯誤延遲
  },
  
  // 動畫和過渡延遲
  ANIMATION: {
    TOPIC_OVERFLOW: 1000,  // 主題溢出檢查延遲
    DOM_UPDATE: 0,         // DOM 更新延遲
    RESIZE_DEBOUNCE: 300   // 視窗大小調整防抖延遲
  },
  
  // 資料載入延遲
  DATA: {
    RETRY_DELAY: 1000,     // 重試延遲
    LOADING_TIMEOUT: 30000 // 載入超時
  }
};

// Promise 版本的延遲函數，替代 setTimeout
const delay = (ms) => {
  return new Promise(resolve => setTimeout(resolve, ms));
};

// 非阻塞延遲函數，用於不需要等待的延遲操作
const nonBlockingDelay = async (ms, callback) => {
  await delay(ms);
  callback();
};

// ======================================================
//   2-2. 工具函數 (Utility Functions)
// ======================================================

// Modal 清理工具
const ModalCleanupUtils = {
  // 清理 Modal 相關的 DOM 元素和樣式
  cleanupModal: (options = {}) => {
    console.log('ModalCleanupUtils.cleanupModal called：清理 Modal 相關元素和樣式', options);
    
    const {
      removeBackdrop = true,
      removeModalOpen = true,
      clearOverflow = true,
      clearPaddingRight = true,
      delay = 0
    } = options;
    
    const cleanup = () => {
      // 移除所有 modal backdrop 元素
      if (removeBackdrop) {
        document.querySelectorAll('.modal-backdrop').forEach(bd => {
          console.log('ModalCleanupUtils.cleanupModal: 移除 backdrop 元素', bd);
          bd.remove();
        });
      }
      
      // 移除 body 的 modal-open 類別
      if (removeModalOpen) {
        console.log('ModalCleanupUtils.cleanupModal: 移除 body modal-open 類別');
        document.body.classList.remove('modal-open');
      }
      
      // 清除 body 的 overflow 樣式
      if (clearOverflow) {
        console.log('ModalCleanupUtils.cleanupModal: 清除 body overflow 樣式');
        document.body.style.overflow = '';
      }
      
      // 清除 body 的 paddingRight 樣式
      if (clearPaddingRight) {
        console.log('ModalCleanupUtils.cleanupModal: 清除 body paddingRight 樣式');
        document.body.style.paddingRight = '';
      }
      
      console.log('ModalCleanupUtils.cleanupModal: Modal 清理完成');
    };
    
    // 如果有延遲，使用 setTimeout，否則立即執行
    if (delay > 0) {
      console.log(`ModalCleanupUtils.cleanupModal: 延遲 ${delay}ms 後執行清理`);
      setTimeout(cleanup, delay);
    } else {
      cleanup();
    }
  },
  
  // 快速清理（使用預設選項）
  quickCleanup: () => {
    console.log('ModalCleanupUtils.quickCleanup called：快速清理 Modal');
    ModalCleanupUtils.cleanupModal();
  },
  
  // 延遲清理（使用預設選項但帶延遲）
  delayedCleanup: (delay = 200) => {
    console.log(`ModalCleanupUtils.delayedCleanup called：延遲 ${delay}ms 清理 Modal`);
    ModalCleanupUtils.cleanupModal({ delay });
  }
};

// 生成按鈕 HTML 的通用函數
const generateActionButtons = (schedule, index, buttonType = 'schedule') => {
  console.log('generateActionButtons called: 生成按鈕 HTML', { schedule, index, buttonType });
  
  const isDraft = schedule.isDraft || false;
  
  if (isDraft) {
    // 草稿狀態：顯示修改和刪除按鈕
    if (buttonType === 'provide') {
      return `
        <div class="d-flex gap-1 justify-content-center">
          <button class="btn btn-link btn-sm p-0 edit-provide-btn" data-option="edit-provide-${index}">修改</button>
          <button class="btn btn-link btn-sm text-danger p-0 delete-provide-btn" data-option="delete-provide-${index}">刪除</button>
        </div>
      `;
    } else {
      return `
        <div class="d-flex gap-1 justify-content-center">
          <button class="btn btn-link btn-sm p-0 schedule-edit-btn">修改</button>
          <button class="btn btn-link btn-sm text-danger p-0 schedule-delete-btn">刪除</button>
        </div>
      `;
    }
  } else {
    // 已提交狀態：只顯示刪除按鈕
    if (buttonType === 'provide') {
      return `
        <div class="d-flex gap-1 justify-content-center">
          <button class="btn btn-link btn-sm text-danger p-0 delete-provide-btn" data-option="delete-provide-${index}">刪除</button>
        </div>
      `;
    } else {
      return `
        <div class="d-flex gap-1 justify-content-center">
          <button class="btn btn-link btn-sm text-danger p-0 schedule-delete-btn">刪除</button>
        </div>
      `;
    }
  }
};

// 通用時段表格行生成函數
const generateScheduleTableRow = (schedule, index, options = {}) => {
  console.log('generateScheduleTableRow called: 生成時段表格行', { schedule, index, options });
  
  // 解構選項參數，提供預設值
  const {
    showNumber = true,
    showStatus = true,
    showNotes = true,
    showButtons = true,
    buttonType = 'schedule',
    useGlobalIndex = false,
    startIndex = 0
  } = options;
  
  // 計算實際索引
  const actualIndex = useGlobalIndex ? startIndex + index : index;
  const scheduleNumber = index + 1;
  
  // 處理日期和時間格式
  const dateObj = new Date(schedule.date);
  const weekdays = ['日', '一', '二', '三', '四', '五', '六'];
  const weekday = weekdays[dateObj.getDay()];
  const formattedDate = schedule.date;
  
  const startTime = DateUtils.formatTimeWithoutSeconds(schedule.startTime || '');
  const endTime = DateUtils.formatTimeWithoutSeconds(schedule.endTime || '');
  const notes = schedule.notes || '';
  const period = `${formattedDate}（週${weekday}）${startTime}~${endTime}`;
  
  // 處理狀態
  const isDraft = schedule.isDraft || false;
  const statusClass = isDraft ? 'text-warning' : 'text-success';
  const statusText = isDraft ? CONFIG.UI_TEXT.STATUS.TAKER_OFFER.DRAFT : CONFIG.UI_TEXT.STATUS.TAKER_OFFER.PENDING;
  
  // 生成按鈕 HTML
  const buttonsHTML = showButtons ? generateActionButtons(schedule, actualIndex, buttonType) : '';
  
  // 生成表格行 HTML
  const rowHTML = `
    <tr data-index="${actualIndex}">
      ${showNumber ? `<td class="text-center">${scheduleNumber}</td>` : ''}
      ${showStatus ? `<td class="text-center ${statusClass}">${statusText}</td>` : ''}
      <td class="text-center">${period}</td>
      ${showNotes ? `<td class="text-center">${notes}</td>` : ''}
      ${showButtons ? `<td class="text-center">${buttonsHTML}</td>` : ''}
    </tr>
  `;
  
  console.log('generateScheduleTableRow completed: 表格行已生成', { actualIndex, scheduleNumber, period });
  return rowHTML;
};

// 通用時段資料合併函數
const getAllSchedulesWithDraftStatus = () => {
  console.log('getAllSchedulesWithDraftStatus called: 合併正式提供和草稿時段');
  
  // 獲取所有時段（正式提供 + 草稿）
  const providedSchedules = ChatStateManager.getProvidedSchedules();
  const draftSchedules = ChatStateManager.get(ChatStateManager.CONFIG.STATE_KEYS.DRAFT_SCHEDULES) || [];
  
  // 合併並標記狀態
  const allSchedules = [
    ...providedSchedules.map(schedule => ({ ...schedule, isDraft: false })),
    ...draftSchedules.map(schedule => ({ ...schedule, isDraft: true }))
  ];
  
  const scheduleCount = allSchedules.length;
  
  console.log('getAllSchedulesWithDraftStatus completed: 時段資料已合併', { 
    providedCount: providedSchedules.length, 
    draftCount: draftSchedules.length, 
    totalCount: scheduleCount 
  });
  
  return {
    allSchedules,
    scheduleCount,
    providedSchedules,
    draftSchedules
  };
};

// 通用表格內容生成函數
const generateTableContent = (tableRows) => {
  console.log('generateTableContent called: 生成表格內容', { tableRowsLength: tableRows.length });
  
  const tableContent = `
    ${TEMPLATES.chat.tableHeaders.fiveColumns()}
    <tbody>
      ${tableRows}
    </tbody>
  `;
  
  console.log('generateTableContent completed: 表格內容已生成');
  return tableContent;
};

// 通用預約表格行生成函數
const generateReservationTableRows = (items, options = {}) => {
  console.log('generateReservationTableRows called: 生成預約表格行', { items, options });
  
  // 解構選項參數，提供預設值
  const {
    startIndex = 1,
    statusClass = 'text-success',
    statusText = CONFIG.UI_TEXT.STATUS.TAKER_VIEW.PENDING,
    buttonText = CONFIG.UI_TEXT.BUTTONS.CANCEL_RESERVATION,
    buttonClass = 'btn btn-sm btn-outline-danger cancel-reservation-btn',
    notesColumn = '-'
  } = options;
  
  let tableRows = '';
  let rowIndex = startIndex;
  
  items.forEach(item => {
    // 處理不同的資料結構
    const timeSlot = item.timeSlot || getDemoTimeLabel(item.option) || item.label || item.text || '';
    const status = item.status || statusText;
    const option = item.option || item.dataOption || '';
    const buttonDataOption = item.buttonDataOption || option;
    const customButtonText = item.buttonText || buttonText;
    
    tableRows += `
      <tr>
        <td class="text-center">${rowIndex}</td>
        <td class="text-center ${statusClass}">${status}</td>
        <td class="text-center">${timeSlot}</td>
        <td class="text-center">${notesColumn}</td>
        <td class="text-center">
          <button class="${buttonClass}" data-option="${buttonDataOption}">
            ${customButtonText}
          </button>
        </td>
      </tr>
    `;
    rowIndex++;
  });
  
  console.log('generateReservationTableRows completed: 預約表格行已生成', { rowCount: items.length });
  return tableRows;
};

// 通用時段重疊檢查函數：支援排除特定索引
  const checkScheduleOverlap = (schedule, existingSchedules, excludeIndex = null) => {
    console.log('checkScheduleOverlap called: 檢查時段重疊', {
      schedule,
      existingSchedulesCount: existingSchedules.length,
      excludeIndex
    });

    const isDuplicate = existingSchedules.some((existingSchedule, index) => {
      // 排除指定索引的時段（用於編輯時排除自己）
      if (excludeIndex !== null && index === parseInt(excludeIndex)) {
        return false;
      }

      // 檢查是否為完全相同的時段
      const isExactDuplicate = existingSchedule.date === schedule.date &&
        existingSchedule.startTime === schedule.startTime &&
        existingSchedule.endTime === schedule.endTime;

      if (isExactDuplicate) {
        console.log('checkScheduleOverlap: 檢測到完全相同時段', { schedule, existingSchedule });
        return true;
      }

      // 檢查是否為重疊時段（相同日期且時間有重疊）
      if (existingSchedule.date === schedule.date) {
        const existingStart = existingSchedule.startTime;
        const existingEnd = existingSchedule.endTime;
        const newStart = schedule.startTime;
        const newEnd = schedule.endTime;

        // 檢查時間重疊：新時段的開始時間 < 現有時段的結束時間 且 新時段的結束時間 > 現有時段的開始時間
        const isOverlapping = newStart < existingEnd && newEnd > existingStart;

        if (isOverlapping) {
          console.log('checkScheduleOverlap: 檢測到時間重疊', {
            schedule,
            existingSchedule,
            newStart,
            newEnd,
            existingStart,
            existingEnd
          });
        }

        return isOverlapping;
      }

      return false;
    });

    console.log('checkScheduleOverlap completed: 重疊檢查完成', { isDuplicate });
    return isDuplicate;
  };


// 生成時段表格的共用函數
const generateScheduleTable = (allSchedules, includeButtons = false) => {
  console.log('generateScheduleTable called: 生成時段表格', { 
    scheduleCount: allSchedules.length, 
    includeButtons 
  });
  
  let tableRows = '';
  allSchedules.forEach((schedule, index) => {
    // 使用通用函數生成表格行
    tableRows += generateScheduleTableRow(schedule, index, {
      buttonType: 'schedule',
      showNotes: true
    });
  });
  
  const scheduleCount = allSchedules.length;
  const tableContent = `
    <div class="table-responsive mt-2">
      <table class="table table-sm table-bordered table-hover schedule-table">
        ${generateTableContent(tableRows)}
      </table>
    </div>
  `;
  
  let buttonsHTML = '';
  if (includeButtons) {
    buttonsHTML = `
      ${getPromptText('SELECT_NEXT_ACTION')}
      <div class="chat-options-buttons mt-2" id="after-view-all-options">
        ${TEMPLATES.chat.buttonGroup(['continue-single-time', 'continue-multiple-times', 'submit-schedules'])}
      </div>
    `;
  }
  
  const result = `
    <div class="message giver-message">
      <div class="d-flex align-items-center">
        <img id="chat-giver-avatar-small" src="/static/images/icons/chat-avatar.svg" alt="Giver" class="chat-avatar-modal">
      </div>
      <div class="message-content">
        <p class="message-title">您目前已提供 ${scheduleCount} 個時段，進度如下：</p>
        ${tableContent}
        ${buttonsHTML}
      </div>
    </div>
  `;
  
  console.log('generateScheduleTable completed: 表格模板已生成');
  return result;
};

// Demo 預約時間函數：根據 option 取得對應的 demo 時間標籤
function getDemoTimeLabel(option) {
  const result = CONFIG.DEMO_TIME_SLOTS[option]?.label || "";
  return result;
}

// 取得統一的提示文字：用於在聊天訊息中顯示提示文字
function getPromptText(key, className = 'mt-2') {
  const text = CONFIG.UI_TEXT.PROMPTS[key] || '';
  const result = `<p class="${className}">${text}</p>`;
  return result;
}

// ======================================================
//   2-3. 通用按鈕處理器 (Universal Button Handler)
// ======================================================

// 從按鈕元素提取資料的通用函數
const extractButtonData = (btn, dataAttributes = []) => {
  const data = {};
  
  // 提取基本資料
  data.element = btn;
  data.text = btn.textContent.trim();
  data.className = btn.className;
  
  // 提取指定的資料屬性
  dataAttributes.forEach(attr => {
    const value = btn.getAttribute(attr);
    if (value !== null) {
      data[attr.replace('data-', '')] = value;
    }
  });
  
  // 提取表格相關資料
  const tr = btn.closest('tr');
  if (tr) {
    const index = tr.getAttribute('data-index');
    if (index !== null) {
      data.index = parseInt(index);
    }
  }
  
  // 提取表格類型
  data.isScheduleTable = !!btn.closest('.schedule-table');
  data.isSuccessProvideTable = !!btn.closest('.success-provide-table');
  data.isProvideTable = !!btn.closest('.success-provide-table');
  
  return data;
};

// 通用按鈕處理器工廠函數
const createButtonHandler = (handlerType, config) => {
  return async (btn, e) => {
    const data = extractButtonData(btn, config.dataAttributes);
    
    try {
      // // 執行預處理（如果有的話）
      // if (config.preprocess && !config.preprocess(data, btn, e)) {
      //   return;
      // }
      
      // 執行主要處理邏輯
      await config.handler(data, btn, e);
      
      // 執行成功回調
      if (config.onSuccess) {
        config.onSuccess(data, btn, e);
      }
      
    } catch (error) {
      
      // 執行錯誤回調
      if (config.onError) {
        config.onError(error, data, btn, e);
      }
    }
  };
};

// ======================================================================
//   3. 核心業務模組：依賴基礎工具 (Core Business Modules: Dependencies on Base Tools)
// ======================================================================

// ======================================================
//   3-1. 應用程式狀態管理 (Application State Management)
// ======================================================

const appState = {
  // Giver 資料
  givers: [],
  
  // 當前頁面
  currentPage: 1,
  
  // 載入狀態
  isLoading: false,
  
  // 錯誤狀態
  error: null,
  
  // 聊天對話框實例
  giverModalInstance: null
};

// ======================================================
//   3-2. 聊天狀態管理模組 (Chat State Management Module)
// ======================================================

const ChatStateManager = {
  // 狀態配置
  CONFIG: {
    // 狀態鍵值
    STATE_KEYS: {
      CURRENT_GIVER: 'currentGiver',
      CURRENT_USER_ID: 'currentUserId',
      IS_ACTIVE: 'isActive',
      MESSAGE_HISTORY: 'messageHistory',
      LAST_MESSAGE_TIME: 'lastMessageTime',
      PROVIDED_SCHEDULES: 'providedSchedules',
      BOOKED_SCHEDULES: 'bookedSchedules',
      IS_MULTIPLE_TIMES_MODE: 'isMultipleTimesMode',
      SELECTED_DATE: 'selectedDate',
      DRAFT_SCHEDULES: 'draftSchedules' 
    },
    
    // 預設狀態
    DEFAULT_STATE: {
      currentGiver: null,
      currentUserId: null,
      isActive: false,
      messageHistory: [],
      lastMessageTime: null,
      providedSchedules: [],
      bookedSchedules: [],
      isMultipleTimesMode: false,
      selectedDate: null,
      draftSchedules: [] 
    },
    
    // 狀態驗證規則
    VALIDATION_RULES: {
      MESSAGE_HISTORY_MAX_LENGTH: 1000,
      PROVIDED_SCHEDULES_MAX_LENGTH: 50,
      LAST_MESSAGE_TIME_MAX_AGE: 24 * 60 * 60 * 1000 // 24小時
    }
  },
  
  // 內部狀態存儲
  _state: {
    currentGiver: null,
    currentUserId: null,
    isActive: false,
    messageHistory: [],
    lastMessageTime: null,
    providedSchedules: [],
    bookedSchedules: [],
    isMultipleTimesMode: false,
    selectedDate: null,
    draftSchedules: [] 
  },
  
  // 狀態變更監聽器
  _listeners: new Map(),
  
  // 初始化狀態管理器
  init: () => {
    console.log('ChatStateManager.init called：初始化聊天狀態管理器');
    ChatStateManager.reset();
    console.log('ChatStateManager.init: 狀態管理器初始化完成');
  },
  
  // 重置狀態到預設值
  reset: () => {
    console.log('ChatStateManager.reset called：重置聊天狀態');
    ChatStateManager._state = { ...ChatStateManager.CONFIG.DEFAULT_STATE };
    ChatStateManager._notifyListeners('reset', ChatStateManager._state);
    console.log('ChatStateManager.reset: 狀態已重置', ChatStateManager._state);
  },
  
  // 獲取完整狀態
  getState: () => {
    return { ...ChatStateManager._state };
  },
  
  // 獲取特定狀態值
  get: (key) => {
    console.log('ChatStateManager.get called', { key });
    const value = ChatStateManager._state[key];
    console.log('ChatStateManager.get: 獲取狀態值', { key, value });
    return value;
  },
  
  // 設定特定狀態值
  set: (key, value) => {
    console.log('ChatStateManager.set called', { key, value });
    
    // 驗證狀態鍵值
    if (!Object.values(ChatStateManager.CONFIG.STATE_KEYS).includes(key)) {
      console.warn('ChatStateManager.set: 無效的狀態鍵值', { key });
      return false;
    }
    
    // 驗證狀態值
    if (!ChatStateManager._validateStateValue(key, value)) {
      console.warn('ChatStateManager.set: 狀態值驗證失敗', { key, value });
      return false;
    }
    
    const oldValue = ChatStateManager._state[key];
    ChatStateManager._state[key] = value;
    
    // 通知監聽器
    ChatStateManager._notifyListeners(key, value, oldValue);
    
    console.log('ChatStateManager.set: 狀態值已更新', { key, oldValue, newValue: value });
    return true;
  },
  
  // 批量更新狀態
  setMultiple: (updates) => {
    console.log('ChatStateManager.setMultiple called', { updates });
    
    const results = {};
    let hasChanges = false;
    
    for (const [key, value] of Object.entries(updates)) {
      const success = ChatStateManager.set(key, value);
      results[key] = success;
      if (success) hasChanges = true;
    }
    
    if (hasChanges) {
      ChatStateManager._notifyListeners('multiple', updates);
    }
    
    console.log('ChatStateManager.setMultiple: 批量更新完成', { results });
    return results;
  },
  
  // 初始化聊天會話
  initChatSession: (giver, userId = 1) => {
    console.log('ChatStateManager.initChatSession called', { giver, userId });
    
    const updates = {
      [ChatStateManager.CONFIG.STATE_KEYS.CURRENT_GIVER]: giver,
      [ChatStateManager.CONFIG.STATE_KEYS.CURRENT_USER_ID]: userId,
      [ChatStateManager.CONFIG.STATE_KEYS.IS_ACTIVE]: true,
      [ChatStateManager.CONFIG.STATE_KEYS.MESSAGE_HISTORY]: [],
      [ChatStateManager.CONFIG.STATE_KEYS.LAST_MESSAGE_TIME]: new Date(),
      [ChatStateManager.CONFIG.STATE_KEYS.PROVIDED_SCHEDULES]: [],
      [ChatStateManager.CONFIG.STATE_KEYS.BOOKED_SCHEDULES]: [],
      [ChatStateManager.CONFIG.STATE_KEYS.IS_MULTIPLE_TIMES_MODE]: false,
      [ChatStateManager.CONFIG.STATE_KEYS.SELECTED_DATE]: null,
      [ChatStateManager.CONFIG.STATE_KEYS.DRAFT_SCHEDULES]: [] 
    };
    
    ChatStateManager.setMultiple(updates);
    console.log('ChatStateManager.initChatSession: 聊天會話已初始化');
  },
  
  // 結束聊天會話
  endChatSession: () => {
    console.log('ChatStateManager.endChatSession called');
    
    const updates = {
      [ChatStateManager.CONFIG.STATE_KEYS.CURRENT_GIVER]: null,
      [ChatStateManager.CONFIG.STATE_KEYS.IS_ACTIVE]: false,
      [ChatStateManager.CONFIG.STATE_KEYS.IS_MULTIPLE_TIMES_MODE]: false,
      [ChatStateManager.CONFIG.STATE_KEYS.SELECTED_DATE]: null
    };
    
    ChatStateManager.setMultiple(updates);
    console.log('ChatStateManager.endChatSession: 聊天會話已結束');
  },
  
  // 添加訊息到歷史記錄
  addMessage: (message) => {
    console.log('ChatStateManager.addMessage called', { message });
    
    const messageHistory = ChatStateManager.get(ChatStateManager.CONFIG.STATE_KEYS.MESSAGE_HISTORY);
    
    // 檢查訊息歷史長度限制
    if (messageHistory.length >= ChatStateManager.CONFIG.VALIDATION_RULES.MESSAGE_HISTORY_MAX_LENGTH) {
      // 移除最舊的訊息
      messageHistory.shift();
    }
    
    // 添加新訊息
    messageHistory.push({
      ...message,
      timestamp: new Date()
    });
    
    // 更新狀態
    ChatStateManager.setMultiple({
      [ChatStateManager.CONFIG.STATE_KEYS.MESSAGE_HISTORY]: messageHistory,
      [ChatStateManager.CONFIG.STATE_KEYS.LAST_MESSAGE_TIME]: new Date()
    });
    
    console.log('ChatStateManager.addMessage: 訊息已添加到歷史記錄');
  },
  
  // 添加使用者訊息
  addUserMessage: (content) => {
    console.log('ChatStateManager.addUserMessage called', { content });
    
    const message = {
      type: 'user',
      content: content,
      timestamp: new Date()
    };
    
    ChatStateManager.addMessage(message);
  },
  
  // 添加 Giver 訊息
  addGiverMessage: (content) => {
    console.log('ChatStateManager.addGiverMessage called', { content });
    
    const message = {
      type: 'giver',
      content: content,
      timestamp: new Date()
    };
    
    ChatStateManager.addMessage(message);
  },
  
  // 添加時段到已提供時段列表
  addSchedule: (schedule) => {
    console.log('ChatStateManager.addSchedule called', { schedule });
    
    const providedSchedules = ChatStateManager.get(ChatStateManager.CONFIG.STATE_KEYS.PROVIDED_SCHEDULES);
    
    // 檢查時段列表長度限制
    if (providedSchedules.length >= ChatStateManager.CONFIG.VALIDATION_RULES.PROVIDED_SCHEDULES_MAX_LENGTH) {
      console.warn('ChatStateManager.addSchedule: 時段列表已達最大長度限制');
      return false;
    }
    
    // 檢查重複時段（與已提供時段和草稿時段的重複）
    const draftSchedules = ChatStateManager.get(ChatStateManager.CONFIG.STATE_KEYS.DRAFT_SCHEDULES) || [];
    const allExistingSchedules = [...providedSchedules, ...draftSchedules];    
    const isDuplicate = checkScheduleOverlap(schedule, allExistingSchedules);
    
    if (isDuplicate) {
      console.warn('ChatStateManager.addSchedule: 檢測到重複或重疊時段', schedule);
      return false;
    }
    
    // 添加新時段
    providedSchedules.push({
      ...schedule,
      timestamp: new Date()
    });
    
    ChatStateManager.set(ChatStateManager.CONFIG.STATE_KEYS.PROVIDED_SCHEDULES, providedSchedules);
    console.log('ChatStateManager.addSchedule: 時段已添加到列表');
    return true;
  },
  
  // 添加草稿時段到草稿時段列表
  addDraftSchedule: (schedule) => {
    console.log('ChatStateManager.addDraftSchedule called', { schedule });
    
    const draftSchedules = ChatStateManager.get(ChatStateManager.CONFIG.STATE_KEYS.DRAFT_SCHEDULES);
    
    // 檢查時段列表長度限制
    if (draftSchedules.length >= ChatStateManager.CONFIG.VALIDATION_RULES.PROVIDED_SCHEDULES_MAX_LENGTH) {
      console.warn('ChatStateManager.addDraftSchedule: 草稿時段列表已達最大長度限制');
      return false;
    }
    
    // 檢查重複時段（與已提供時段和草稿時段的重複）
    const providedSchedules = ChatStateManager.get(ChatStateManager.CONFIG.STATE_KEYS.PROVIDED_SCHEDULES);
    const allExistingSchedules = [...providedSchedules, ...draftSchedules];
    const isDuplicate = checkScheduleOverlap(schedule, allExistingSchedules);
    
    if (isDuplicate) {
      console.warn('ChatStateManager.addDraftSchedule: 檢測到重複或重疊時段', schedule);
      return false;
    }
    
    // 添加新草稿時段
    draftSchedules.push({
      ...schedule,
      timestamp: new Date(),
      isDraft: true
    });
    
    ChatStateManager.set(ChatStateManager.CONFIG.STATE_KEYS.DRAFT_SCHEDULES, draftSchedules);
    console.log('ChatStateManager.addDraftSchedule: 草稿時段已添加到列表');
    return true;
  },
  
  // 批量添加時段
  addSchedules: (schedules) => {
    console.log('ChatStateManager.addSchedules called', { schedules });
    
    const providedSchedules = ChatStateManager.get(ChatStateManager.CONFIG.STATE_KEYS.PROVIDED_SCHEDULES);
    
    // 檢查是否會超過長度限制
    if (providedSchedules.length + schedules.length > ChatStateManager.CONFIG.VALIDATION_RULES.PROVIDED_SCHEDULES_MAX_LENGTH) {
      console.warn('ChatStateManager.addSchedules: 批量添加會超過長度限制');
      return false;
    }
    
    // 檢查重複時段（與已提供時段和草稿時段的重複）
    const draftSchedules = ChatStateManager.get(ChatStateManager.CONFIG.STATE_KEYS.DRAFT_SCHEDULES) || [];
    const allExistingSchedules = [...providedSchedules, ...draftSchedules];
    const duplicateSchedules = [];
    
    schedules.forEach(schedule => {
      const isDuplicate = checkScheduleOverlap(schedule, allExistingSchedules);
      
      if (isDuplicate) {
        duplicateSchedules.push(schedule);
      }
    });
    
    // 檢查批次內的重複時段
    const batchDuplicateSchedules = [];
    
    for (let i = 0; i < schedules.length; i++) {
      for (let j = i + 1; j < schedules.length; j++) {
        const schedule1 = schedules[i];
        const schedule2 = schedules[j];
        
        // 檢查是否為完全相同的時段
        const isDuplicate = checkScheduleOverlap(schedule1, [schedule2]);

        if (isDuplicate) {
          if (!batchDuplicateSchedules.includes(schedule1)) {
            batchDuplicateSchedules.push(schedule1);
          }
          if (!batchDuplicateSchedules.includes(schedule2)) {
            batchDuplicateSchedules.push(schedule2);
          }
        }
      }
    }
    
    // 合併所有重複時段
    const allDuplicateSchedules = [...duplicateSchedules, ...batchDuplicateSchedules];
    
    if (allDuplicateSchedules.length > 0) {
      console.warn('ChatStateManager.addSchedules: 檢測到重複或重疊時段', allDuplicateSchedules);
      return false;
    }
    
    // 批量添加時段
    const newSchedules = schedules.map(schedule => ({
      ...schedule,
      timestamp: new Date()
    }));
    
    providedSchedules.push(...newSchedules);
    ChatStateManager.set(ChatStateManager.CONFIG.STATE_KEYS.PROVIDED_SCHEDULES, providedSchedules);
    console.log('ChatStateManager.addSchedules: 批量時段已添加到列表');
    return true;
  },
  
  // 批量添加草稿時段
  addDraftSchedules: (schedules) => {
    console.log('ChatStateManager.addDraftSchedules called', { schedules });
    
    const draftSchedules = ChatStateManager.get(ChatStateManager.CONFIG.STATE_KEYS.DRAFT_SCHEDULES);
    
    // 檢查是否會超過長度限制
    if (draftSchedules.length + schedules.length > ChatStateManager.CONFIG.VALIDATION_RULES.PROVIDED_SCHEDULES_MAX_LENGTH) {
      console.warn('ChatStateManager.addDraftSchedules: 批量添加會超過長度限制');
      return false;
    }
    
    // 檢查重複時段（與已提供時段和草稿時段的重複）
    const providedSchedules = ChatStateManager.get(ChatStateManager.CONFIG.STATE_KEYS.PROVIDED_SCHEDULES);
    const allExistingSchedules = [...providedSchedules, ...draftSchedules];
    const duplicateSchedules = [];
    
    // 使用通用函數檢查重複時段
    schedules.forEach(schedule => {
      const isDuplicate = checkScheduleOverlap(schedule, allExistingSchedules);

      if (isDuplicate) {
        duplicateSchedules.push(schedule);
      }
    });
    
    // 檢查批次內的重複時段 - 使用通用 checkScheduleOverlap 函數
    const batchDuplicateSchedules = [];
    
    for (let i = 0; i < schedules.length; i++) {
      for (let j = i + 1; j < schedules.length; j++) {
        const schedule1 = schedules[i];
        const schedule2 = schedules[j];
        
        // 使用通用函數檢查重疊
        const isDuplicate = checkScheduleOverlap(schedule1, [schedule2]);
        
        if (isDuplicate) {
          if (!batchDuplicateSchedules.includes(schedule1)) {
            batchDuplicateSchedules.push(schedule1);
          }
          if (!batchDuplicateSchedules.includes(schedule2)) {
            batchDuplicateSchedules.push(schedule2);
          }
        }
      }
    }
    
    // 合併所有重複時段
    const allDuplicateSchedules = [...duplicateSchedules, ...batchDuplicateSchedules];
    
    if (allDuplicateSchedules.length > 0) {
      console.warn('ChatStateManager.addDraftSchedules: 檢測到重複或重疊時段', allDuplicateSchedules);
      return false;
    }
    
    // 批量添加草稿時段
    const newDraftSchedules = schedules.map(schedule => ({
      ...schedule,
      timestamp: new Date(),
      isDraft: true
    }));
    
    draftSchedules.push(...newDraftSchedules);
    ChatStateManager.set(ChatStateManager.CONFIG.STATE_KEYS.DRAFT_SCHEDULES, draftSchedules);
    console.log('ChatStateManager.addDraftSchedules: 批量草稿時段已添加到列表');
    return true;
  },
  
  // 設定多筆時段模式
  setMultipleTimesMode: (isEnabled) => {
    console.log('ChatStateManager.setMultipleTimesMode called', { isEnabled });
    ChatStateManager.set(ChatStateManager.CONFIG.STATE_KEYS.IS_MULTIPLE_TIMES_MODE, isEnabled);
  },
  
  // 設定選中的日期
  setSelectedDate: (date) => {
    console.log('ChatStateManager.setSelectedDate called', { date });
    ChatStateManager.set(ChatStateManager.CONFIG.STATE_KEYS.SELECTED_DATE, date);
  },
  
  
  // 獲取訊息歷史
  getMessageHistory: () => {
    console.log('ChatStateManager.getMessageHistory called');
    const messageHistory = ChatStateManager.get(ChatStateManager.CONFIG.STATE_KEYS.MESSAGE_HISTORY);
    return [...messageHistory];
  },
  
  // 清空訊息歷史
  clearMessageHistory: () => {
    console.log('ChatStateManager.clearMessageHistory called');
    ChatStateManager.set(ChatStateManager.CONFIG.STATE_KEYS.MESSAGE_HISTORY, []);
  },
  
  // 獲取已提供時段列表
  getProvidedSchedules: () => {
    console.log('ChatStateManager.getProvidedSchedules called');
    const providedSchedules = ChatStateManager.get(ChatStateManager.CONFIG.STATE_KEYS.PROVIDED_SCHEDULES);
    return [...providedSchedules];
  },
  
  // 清空已提供時段列表
  clearProvidedSchedules: () => {
    console.log('ChatStateManager.clearProvidedSchedules called');
    ChatStateManager.set(ChatStateManager.CONFIG.STATE_KEYS.PROVIDED_SCHEDULES, []);
  },
  
  // 獲取已預約時段列表
  getBookedSchedules: () => {
    console.log('ChatStateManager.getBookedSchedules called');
    const bookedSchedules = ChatStateManager.get(ChatStateManager.CONFIG.STATE_KEYS.BOOKED_SCHEDULES);
    return [...bookedSchedules];
  },
  
  // 添加預約時段
  addBookedSchedule: (schedule) => {
    console.log('ChatStateManager.addBookedSchedule called', { schedule });
    
    const bookedSchedules = ChatStateManager.get(ChatStateManager.CONFIG.STATE_KEYS.BOOKED_SCHEDULES);
    
    // 檢查是否會超過長度限制
    if (bookedSchedules.length >= ChatStateManager.CONFIG.VALIDATION_RULES.PROVIDED_SCHEDULES_MAX_LENGTH) {
      console.warn('ChatStateManager.addBookedSchedule: 已達到預約時段數量限制');
      return false;
    }
    
    // 添加新預約時段
    bookedSchedules.push({
      ...schedule,
      timestamp: new Date()
    });
    
    ChatStateManager.set(ChatStateManager.CONFIG.STATE_KEYS.BOOKED_SCHEDULES, bookedSchedules);
    console.log('ChatStateManager.addBookedSchedule: 預約時段已添加到列表');
    return true;
  },
  
  // 批量添加預約時段
  addBookedSchedules: (schedules) => {
    console.log('ChatStateManager.addBookedSchedules called', { schedules });
    
    const bookedSchedules = ChatStateManager.get(ChatStateManager.CONFIG.STATE_KEYS.BOOKED_SCHEDULES);
    
    // 檢查是否會超過長度限制
    if (bookedSchedules.length + schedules.length > ChatStateManager.CONFIG.VALIDATION_RULES.PROVIDED_SCHEDULES_MAX_LENGTH) {
      console.warn('ChatStateManager.addBookedSchedules: 批量添加會超過長度限制');
      return false;
    }
    
    // 批量添加預約時段
    const newSchedules = schedules.map(schedule => ({
      ...schedule,
      timestamp: new Date()
    }));
    
    bookedSchedules.push(...newSchedules);
    ChatStateManager.set(ChatStateManager.CONFIG.STATE_KEYS.BOOKED_SCHEDULES, bookedSchedules);
    console.log('ChatStateManager.addBookedSchedules: 批量預約時段已添加到列表');
    return true;
  },
  
  // 清空已預約時段列表
  clearBookedSchedules: () => {
    console.log('ChatStateManager.clearBookedSchedules called');
    ChatStateManager.set(ChatStateManager.CONFIG.STATE_KEYS.BOOKED_SCHEDULES, []);
  },
  
  // 檢查聊天是否活躍
  isActive: () => {
    console.log('ChatStateManager.isActive called');
    return ChatStateManager.get(ChatStateManager.CONFIG.STATE_KEYS.IS_ACTIVE);
  },
  
  // 獲取當前 Giver
  getCurrentGiver: () => {
    console.log('ChatStateManager.getCurrentGiver called');
    return ChatStateManager.get(ChatStateManager.CONFIG.STATE_KEYS.CURRENT_GIVER);
  },
  
  // 獲取當前使用者 ID
  getCurrentUserId: () => {
    console.log('ChatStateManager.getCurrentUserId called');
    return ChatStateManager.get(ChatStateManager.CONFIG.STATE_KEYS.CURRENT_USER_ID);
  },
  
  // 設定當前使用者 ID
  setCurrentUserId: (userId) => {
    console.log('ChatStateManager.setCurrentUserId called', { userId });
    ChatStateManager.set(ChatStateManager.CONFIG.STATE_KEYS.CURRENT_USER_ID, userId);
  },
  
  // 檢查是否為多筆時段模式
  isMultipleTimesMode: () => {
    console.log('ChatStateManager.isMultipleTimesMode called');
    return ChatStateManager.get(ChatStateManager.CONFIG.STATE_KEYS.IS_MULTIPLE_TIMES_MODE);
  },
  
  // 獲取選中的日期
  getSelectedDate: () => {
    console.log('ChatStateManager.getSelectedDate called');
    return ChatStateManager.get(ChatStateManager.CONFIG.STATE_KEYS.SELECTED_DATE);
  },
  
  // 添加狀態變更監聽器
  addListener: (key, callback) => {
    console.log('ChatStateManager.addListener called', { key, callback });
    
    if (!ChatStateManager._listeners.has(key)) {
      ChatStateManager._listeners.set(key, new Set());
    }
    
    ChatStateManager._listeners.get(key).add(callback);
    console.log('ChatStateManager.addListener: 監聽器已添加');
  },
  
  // 移除狀態變更監聽器
  removeListener: (key, callback) => {
    console.log('ChatStateManager.removeListener called', { key, callback });
    
    if (ChatStateManager._listeners.has(key)) {
      ChatStateManager._listeners.get(key).delete(callback);
      console.log('ChatStateManager.removeListener: 監聽器已移除');
    }
  },
  
  // 通知監聽器
  _notifyListeners: (key, newValue, oldValue) => {
    console.log('ChatStateManager._notifyListeners called', { key, newValue, oldValue });
    
    if (ChatStateManager._listeners.has(key)) {
      const callbacks = ChatStateManager._listeners.get(key);
      callbacks.forEach(callback => {
        try {
          callback(newValue, oldValue);
        } catch (error) {
          console.error('ChatStateManager._notifyListeners: 監聽器執行錯誤', error);
        }
      });
    }
  },
  
  // 驗證狀態值
  _validateStateValue: (key, value) => {
    console.log('ChatStateManager._validateStateValue called', { key, value });
    
    switch (key) {
      case ChatStateManager.CONFIG.STATE_KEYS.CURRENT_GIVER:
        return value === null || typeof value === 'object';
        
      case ChatStateManager.CONFIG.STATE_KEYS.CURRENT_USER_ID:
        return value === null || typeof value === 'number';
        
      case ChatStateManager.CONFIG.STATE_KEYS.IS_ACTIVE:
      case ChatStateManager.CONFIG.STATE_KEYS.IS_MULTIPLE_TIMES_MODE:
        return typeof value === 'boolean';
        
      case ChatStateManager.CONFIG.STATE_KEYS.MESSAGE_HISTORY:
        return Array.isArray(value);
        
      case ChatStateManager.CONFIG.STATE_KEYS.LAST_MESSAGE_TIME:
        return value === null || value instanceof Date;
        
      case ChatStateManager.CONFIG.STATE_KEYS.PROVIDED_SCHEDULES:
      case ChatStateManager.CONFIG.STATE_KEYS.BOOKED_SCHEDULES:
        return Array.isArray(value);
        
      case ChatStateManager.CONFIG.STATE_KEYS.SELECTED_DATE:
        return value === null || value instanceof Date;
        
      case ChatStateManager.CONFIG.STATE_KEYS.DRAFT_SCHEDULES:
        return Array.isArray(value);
        
      default:
        return true;
    }
  },
  
  // 調試功能
  debug: () => {
  },
  
  // 匯出狀態（用於持久化）
  export: () => {
    console.log('ChatStateManager.export called');
    const state = ChatStateManager.getState();
    const exportData = {
      ...state,
      lastMessageTime: state.lastMessageTime ? state.lastMessageTime.toISOString() : null,
      selectedDate: state.selectedDate ? state.selectedDate.toISOString() : null
    };
    console.log('ChatStateManager.export: 狀態匯出完成', exportData);
    return exportData;
  },
  
  // 匯入狀態（用於恢復）
  import: (data) => {
    console.log('ChatStateManager.import called', { data });
    
    if (!data || typeof data !== 'object') {
      console.warn('ChatStateManager.import: 無效的匯入資料');
      return false;
    }
    
    try {
      const importedState = {
        ...data,
        lastMessageTime: data.lastMessageTime ? new Date(data.lastMessageTime) : null,
        selectedDate: data.selectedDate ? new Date(data.selectedDate) : null
      };
      
      // 驗證匯入的資料
      for (const [key, value] of Object.entries(importedState)) {
        if (!ChatStateManager._validateStateValue(key, value)) {
          console.warn('ChatStateManager.import: 匯入資料驗證失敗', { key, value });
          return false;
        }
      }
      
      // 更新狀態
      ChatStateManager._state = { ...ChatStateManager.CONFIG.DEFAULT_STATE, ...importedState };
      ChatStateManager._notifyListeners('import', ChatStateManager._state);
      
      console.log('ChatStateManager.import: 狀態匯入完成');
      return true;
    } catch (error) {
      console.error('ChatStateManager.import: 狀態匯入失敗', error);
      return false;
    }
  },
  
  // 從資料庫載入使用者提供給特定 Giver 的時段
  loadUserSchedulesFromDatabase: async (giverId, userId) => {
    console.log('ChatStateManager.loadUserSchedulesFromDatabase called', { giverId, userId });
    
    try {
      // 呼叫 API 獲取使用者提供給該 Giver 的時段
      const response = await fetch(`/api/v1/schedules?giver_id=${giverId}&taker_id=${userId}`);
      
      if (!response.ok) {
        console.error('ChatStateManager.loadUserSchedulesFromDatabase: API 請求失敗', response.status);
        return [];
      }
      
      const schedules = await response.json();
      console.log('ChatStateManager.loadUserSchedulesFromDatabase: 從資料庫載入的時段', schedules);
      
      // 將資料庫中的時段轉換為前端格式
      const convertedSchedules = schedules.map(schedule => ({
        id: schedule.id,
        date: schedule.date.replace(/-/g, '/'), // 轉換日期格式：yyyy-mm-dd -> yyyy/mm/dd
        startTime: schedule.start_time,
        endTime: schedule.end_time,
        note: schedule.note,
        status: schedule.status,
        role: schedule.created_by_role,
        giverId: schedule.giver_id,
        takerId: schedule.taker_id,
        createdAt: schedule.created_at,
        createdBy: schedule.created_by,
        createdByRole: schedule.created_by_role,
        updatedAt: schedule.updated_at,
        updatedBy: schedule.updated_by,
        updatedByRole: schedule.updated_by_role,
        deletedAt: schedule.deleted_at,
        deletedBy: schedule.deleted_by,
        deletedByRole: schedule.deleted_by_role
      }));
      
      console.log('ChatStateManager.loadUserSchedulesFromDatabase: 轉換後的時段', convertedSchedules);
      return convertedSchedules;
      
    } catch (error) {
      console.error('ChatStateManager.loadUserSchedulesFromDatabase: 載入時段失敗', error);
      return [];
    }
  }
};

// ======================================================
//   3-3. 日期時間處理模組 (Date Time Utilities Module)
// ======================================================

const DateUtils = {
  // 格式化選項
  FORMATS: {
    DATE: 'YYYY/MM/DD',
    TIME: 'HH:MM',
    DATETIME: 'YYYY/MM/DD HH:MM',
    TIMESTAMP: 'HH:MM:SS'
  },
  
  // 格式化日期為 YYYY/MM/DD
  formatDate: (date) => {
    console.log('DateUtils.formatDate called', { date });
    if (!date) return '';
    
    const d = new Date(date);
    if (isNaN(d.getTime())) return '';
    
    const year = d.getFullYear();
    const month = String(d.getMonth() + CONFIG.DATE_PICKER.CALCULATION.MONTH_OFFSET).padStart(CONFIG.DATE_PICKER.FORMAT.PADDING_LENGTH, CONFIG.DATE_PICKER.FORMAT.PADDING_CHAR);
    const day = String(d.getDate()).padStart(CONFIG.DATE_PICKER.FORMAT.PADDING_LENGTH, CONFIG.DATE_PICKER.FORMAT.PADDING_CHAR);
    
    const formatted = `${year}${CONFIG.DATE_PICKER.SEPARATORS.DATE}${month}${CONFIG.DATE_PICKER.SEPARATORS.DATE}${day}`;
    return formatted;
  },
  
  // 格式化時間為 HH:MM:SS
  formatTime: (date) => {
    if (!date) return '';
    
    const d = new Date(date);
    if (isNaN(d.getTime())) return '';
    
    const hours = String(d.getHours()).padStart(CONFIG.DATE_PICKER.FORMAT.PADDING_LENGTH, CONFIG.DATE_PICKER.FORMAT.PADDING_CHAR);
    const minutes = String(d.getMinutes()).padStart(CONFIG.DATE_PICKER.FORMAT.PADDING_LENGTH, CONFIG.DATE_PICKER.FORMAT.PADDING_CHAR);
    const seconds = String(d.getSeconds()).padStart(CONFIG.DATE_PICKER.FORMAT.PADDING_LENGTH, CONFIG.DATE_PICKER.FORMAT.PADDING_CHAR);
    
    const formatted = `${hours}${CONFIG.DATE_PICKER.SEPARATORS.TIME}${minutes}${CONFIG.DATE_PICKER.SEPARATORS.TIME}${seconds}`;
    return formatted;
  },
  
  // 將時間格式化為 HH:MM 格式（移除秒數）
  formatTimeWithoutSeconds: (timeStr) => {
    
    // 如果是 HH:MM:SS 格式，移除秒數
    if (timeStr.includes(':') && timeStr.split(':').length === 3) {
      const [hours, minutes] = timeStr.split(':');
      const formatted = `${hours}:${minutes}`;
      return formatted;
    }
    // 如果已經是 HH:MM 格式，直接返回
    if (timeStr.includes(':') && timeStr.split(':').length === 2) {
      return timeStr;
    }
    // 如果是其他格式，嘗試解析並格式化
    return timeStr;
  },
  
  // 格式化為本地時間字串
  formatToLocalTime: (date) => {
    if (!date) return '';
    
    const d = new Date(date);
    if (isNaN(d.getTime())) return '';
    
    const formatted = d.toLocaleTimeString('zh-TW', {
      hour: CONFIG.DATE_PICKER.LOCALE_OPTIONS.HOUR,
      minute: CONFIG.DATE_PICKER.LOCALE_OPTIONS.MINUTE,
      hour12: CONFIG.DATE_PICKER.LOCALE_OPTIONS.HOUR12
    });
    
    return formatted;
  },
  
  // 獲取今天的日期
  getToday: () => {
    const today = new Date();
    return today;
  },
  
  // 比較兩個時間字串 (HH:MM 格式)
  compareTimes: (time1, time2) => {
    
    if (!time1 || !time2) {
      return 0;
    }
    
    // 將時間字串轉換為分鐘數（內部工具函式）
    const parseTime = (timeStr) => {
      const [hours, minutes] = timeStr.split(CONFIG.DATE_PICKER.SEPARATORS.TIME).map(Number);
      return hours * CONFIG.DATE_PICKER.CALCULATION.MINUTES_PER_HOUR + minutes;
    };
    
    const minutes1 = parseTime(time1);
    const minutes2 = parseTime(time2);
    
    const result = minutes1 - minutes2;
    return result;
  },
  
  // 驗證時間格式 (HH:MM)
  isValidTimeFormat: (timeStr) => {
    console.log('DateUtils.isValidTimeFormat called', { timeStr });
    
    if (!timeStr || typeof timeStr !== 'string') {
      console.log('DateUtils.isValidTimeFormat: 驗證結果', { isValid: false, reason: '空值或非字串' });
      return false;
    }
    
    const timeRegex = new RegExp(`^(${CONFIG.DATE_PICKER.TIME.REGEX.HOURS_PATTERN}):${CONFIG.DATE_PICKER.TIME.REGEX.MINUTES_PATTERN}$`);
    const isValid = timeRegex.test(timeStr);
    
    console.log('DateUtils.isValidTimeFormat: 驗證結果', { isValid });
    return isValid;
  },
  
  // 驗證日期格式 (YYYY/MM/DD)
  isValidDateFormat: (dateStr) => {
    console.log('DateUtils.isValidDateFormat called', { dateStr });
    
    if (!dateStr || typeof dateStr !== 'string') {
      console.log('DateUtils.isValidDateFormat: 驗證結果', { isValid: false, reason: '空值或非字串' });
      return false;
    }
    
    const dateRegex = new RegExp(`^${CONFIG.DATE_PICKER.REGEX.DATE_PATTERN}$`);
    if (!dateRegex.test(dateStr)) {
      console.log('DateUtils.isValidDateFormat: 驗證結果', { isValid: false, reason: '格式不符' });
      return false;
    }
    
    const [year, month, day] = dateStr.split(CONFIG.DATE_PICKER.SEPARATORS.DATE).map(Number);
    const date = new Date(year, month - CONFIG.DATE_PICKER.CALCULATION.MONTH_OFFSET, day);
    
    const isValid = date.getFullYear() === year &&
                   date.getMonth() === month - CONFIG.DATE_PICKER.CALCULATION.MONTH_OFFSET &&
                   date.getDate() === day;
    
    console.log('DateUtils.isValidDateFormat: 驗證結果', { isValid });
    return isValid;
  },
  
  // 解析多筆時段字串
  parseMultipleSchedules: (message) => {
    console.log('DateUtils.parseMultipleSchedules called', { message });
    
    if (!message || typeof message !== 'string') {
      console.log('DateUtils.parseMultipleSchedules: 無效訊息', { message });
      return { isValid: false, schedules: [] };
    }
    
    const lines = message.split('\n').filter(line => line.trim());
    const schedules = [];
    
    for (const line of lines) {
      const trimmedLine = line.trim();
      if (!trimmedLine) continue;
      
      // 匹配格式：日期 時間範圍
      // 例如：2024/01/15 14:00-16:00
      const scheduleRegex = new RegExp(CONFIG.DATE_PICKER.REGEX.SCHEDULE_PATTERN);
      const match = trimmedLine.match(scheduleRegex);
      
      if (match) {
        const [, date, startTime, endTime] = match;
        
        // 驗證日期和時間格式
        if (DateUtils.isValidDateFormat(date) && 
            DateUtils.isValidTimeFormat(startTime) && 
            DateUtils.isValidTimeFormat(endTime)) {
          
          // 驗證時間邏輯
          if (DateUtils.compareTimes(startTime, endTime) < 0) {
            const formattedSchedule = DOM.chat.formatScheduleWithWeekday(date, startTime, endTime);
            schedules.push({
              date,
              startTime,
              endTime,
              formattedSchedule,
              timestamp: new Date()
            });
          }
        }
      }
    }
    
    const isValid = schedules.length > 0;
    console.log('DateUtils.parseMultipleSchedules: 解析結果', { isValid, schedules });
    return { isValid, schedules };
  },
  
  // 新增：取得一週後日期的格式化字串
  getTodayFormatted: () => {
    return DateUtils.formatDate(DateUtils.getToday());
  },
  
  // 新增：取得一週後日期的格式化字串
  getNextWeekFormatted: () => {
    const today = DateUtils.getToday();
    const nextWeek = new Date(today.getTime() + CONFIG.DATE_PICKER.DEFAULT_OFFSET_DAYS * 24 * 60 * 60 * 1000);
    const result = DateUtils.formatDate(nextWeek);
    return result;
  },
  
  // 驗證日期是否在允許的月份範圍內
  validateDateWithinAllowedMonths: (date, showError = false) => {
    console.log('DateUtils.validateDateWithinAllowedMonths called', { date, showError });
    
    if (!date) {
      console.log('DateUtils.validateDateWithinAllowedMonths: 驗證結果', { isValid: false, reason: '日期為空' });
      if (showError) {
        FormValidator.showValidationError(FormValidator.ERROR_MESSAGES.SCHEDULE_FORM.DATE_REQUIRED);
      }
      return false;
    }
    
    const today = DateUtils.getToday();
    const selectedDateObj = new Date(date);
    const maxMonthsAhead = CONFIG.DATE_PICKER.MAX_MONTHS_AHEAD;
    
    // 修正：使用相同的時區進行比較，避免時區轉換問題
    // 將日期轉換為 YYYY/MM/DD 格式進行比較，避免時區影響
    const todayStr = DateUtils.formatDate(today);
    const selectedDateStr = DateUtils.formatDate(selectedDateObj);
    const maxAllowedDate = new Date(today.getFullYear(), today.getMonth() + maxMonthsAhead, today.getDate());
    const maxAllowedDateStr = DateUtils.formatDate(maxAllowedDate);
    
    // 使用字串比較，避免時區問題
    const isValid = selectedDateStr <= maxAllowedDateStr;
    
    console.log('DateUtils.validateDateWithinAllowedMonths: 驗證結果', { 
      date, 
      today: todayStr, 
      selectedDate: selectedDateStr,
      maxMonthsAhead,
      maxAllowedDate: maxAllowedDateStr, 
      isValid 
    });
    
    // 如果需要顯示錯誤訊息且驗證失敗
    if (!isValid && showError) {
      console.log(`DateUtils.validateDateWithinAllowedMonths: 日期超過${maxMonthsAhead}個月，顯示錯誤訊息`);
      // 檢查是否在日期選擇器中，如果是則不顯示 alert
      const datePickerModal = document.getElementById('date-picker-modal');
      const isInDatePicker = datePickerModal && datePickerModal.classList.contains('show');
      
      if (!isInDatePicker) {
        FormValidator.showValidationError(FormValidator.ERROR_MESSAGES.SCHEDULE_FORM.DATE_TOO_FAR);
      }
    }
    
    return isValid;
  },  
};

// ======================================================
//   3-4. 表單驗證模組 (Form Validation Module)
// ======================================================

// 錯誤元素處理工具
const ErrorElementUtils = {
  // 清除指定輸入欄位的錯誤訊息
  clearInputError: (input) => {
    console.log('ErrorElementUtils.clearInputError called：清除輸入欄位錯誤', { input });
    
    if (!input) {
      console.warn('ErrorElementUtils.clearInputError: 輸入元素不存在');
      return;
    }
    
    const errorElement = input.parentNode.querySelector('.validation-error');
    if (errorElement) {
      errorElement.classList.remove('error-visible');
      errorElement.classList.add('error-hidden');
      errorElement.textContent = '';
      console.log('ErrorElementUtils.clearInputError: 錯誤元素已清除');
    } else {
      console.log('ErrorElementUtils.clearInputError: 未找到錯誤元素');
    }
  },
  
  // 清除多個輸入欄位的錯誤訊息
  clearMultipleInputErrors: (inputs) => {
    console.log('ErrorElementUtils.clearMultipleInputErrors called：清除多個輸入欄位錯誤', { inputCount: inputs.length });
    
    if (!Array.isArray(inputs)) {
      console.warn('ErrorElementUtils.clearMultipleInputErrors: 輸入參數不是陣列');
      return;
    }
    
    inputs.forEach(input => {
      if (input) {
        ErrorElementUtils.clearInputError(input);
      }
    });
    
    console.log('ErrorElementUtils.clearMultipleInputErrors: 所有錯誤元素已清除');
  },
  
  // 檢查輸入欄位是否有錯誤訊息
  hasInputError: (input, errorText = '') => {
    console.log('ErrorElementUtils.hasInputError called：檢查輸入欄位是否有錯誤', { input, errorText });
    
    if (!input) {
      console.warn('ErrorElementUtils.hasInputError: 輸入元素不存在');
      return false;
    }
    
    const errorElement = input.parentNode.querySelector('.validation-error.error-visible');
    if (!errorElement) {
      console.log('ErrorElementUtils.hasInputError: 未找到可見的錯誤元素');
      return false;
    }
    
    if (errorText && !errorElement.textContent.includes(errorText)) {
      console.log('ErrorElementUtils.hasInputError: 錯誤文字不匹配');
      return false;
    }
    
    console.log('ErrorElementUtils.hasInputError: 找到匹配的錯誤元素');
    return true;
  },
  
  // 獲取輸入欄位的錯誤元素
  getInputErrorElement: (input) => {
    console.log('ErrorElementUtils.getInputErrorElement called：獲取輸入欄位錯誤元素', { input });
    
    if (!input) {
      console.warn('ErrorElementUtils.getInputErrorElement: 輸入元素不存在');
      return null;
    }
    
    const errorElement = input.parentNode.querySelector('.validation-error');
    console.log('ErrorElementUtils.getInputErrorElement: 錯誤元素', { errorElement });
    return errorElement;
  }
};

const FormValidator = {
  // 驗證規則配置
  RULES: {
    // 聊天訊息驗證規則
    CHAT_MESSAGE: {
      MAX_LENGTH: CONFIG.CHAT.MAX_MESSAGE_LENGTH,
      MIN_LENGTH: 1,
      ALLOWED_CHARS: /^[\s\S]*$/, // 允許所有字符
      FORBIDDEN_PATTERNS: [
        /<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>/gi, // 防止 XSS
        /javascript:/gi,
        /on\w+\s*=/gi
      ]
    },
    
    // 時段表單驗證規則
    SCHEDULE_FORM: {
      DATE: {
        REQUIRED: true,
        FORMAT: 'YYYY/MM/DD',
        MIN_DATE: 'today', // 不能選擇過去的日期
        MAX_DATE: '+1year' // 最多預約一年後
      },
      TIME: {
        REQUIRED: true,
        FORMAT: 'HH:MM',
        MIN_TIME: '00:00',
        MAX_TIME: '23:59',
        BUSINESS_HOURS: {
          START: CONFIG.DATE_PICKER.BUSINESS_HOURS.START,
          END: CONFIG.DATE_PICKER.BUSINESS_HOURS.END
        }
      },
      NOTES: {
        MAX_LENGTH: 255,
        ALLOWED_CHARS: /^[\s\S]*$/ // 允許所有字符
      }
    },
    
    // 多筆時段驗證規則
    MULTIPLE_SCHEDULES: {
      MAX_SCHEDULES: 10, // 最多一次提交 10 個時段
      MIN_SCHEDULES: 1,
      FORMAT_PATTERN: /^\d{4}\/\d{2}\/\d{2}\s+\d{2}:\d{2}-\d{2}:\d{2}$/,
      TIME_SEPARATOR: '-',
      LINE_SEPARATOR: '\n'
    }
  },
  
  // 錯誤訊息配置
  ERROR_MESSAGES: {
    // 聊天訊息錯誤
    CHAT_MESSAGE: {
      EMPTY: '訊息不能為空',
      TOO_LONG: `訊息長度不能超過 ${CONFIG.CHAT.MAX_MESSAGE_LENGTH} 個字符`,
      INVALID_CHARS: '訊息包含無效字符',
      FORBIDDEN_PATTERN: '訊息包含禁止的內容'
    },
    
    // 時段表單錯誤
    SCHEDULE_FORM: {
      DATE_REQUIRED: '請選擇日期',
      DATE_INVALID: '日期格式不正確，請使用 YYYY/MM/DD 格式',
      DATE_PAST: '不能選擇過去的日期',
      DATE_TOO_FAR: `不能預約 ${CONFIG.DATE_PICKER.MAX_MONTHS_AHEAD} 個月後的日期`,
      START_TIME_REQUIRED: '請輸入開始時間',
      END_TIME_REQUIRED: '請輸入結束時間',
      TIME_INVALID: '目前輸入內容非 4 位數字，請輸入 4 位數字，無需輸入":"',
      TIME_LOGIC: '結束時間必須晚於開始時間',
      TIME_BUSINESS_HOURS: `您輸入的時間是多數人的休息時間（${CONFIG.DATE_PICKER.BUSINESS_HOURS.END}-${CONFIG.DATE_PICKER.BUSINESS_HOURS.START}），請重新輸入`,
      NOTES_TOO_LONG: '備註不能超過 255 個字符',
      NOTES_INVALID: '備註包含無效字符',
      DUPLICATE_SCHEDULE: '您正輸入的時段，和您之前曾輸入的「{{EXISTING_SCHEDULE}}」時段重複或重疊，請重新輸入'
    },
    
    // 多筆時段錯誤
    MULTIPLE_SCHEDULES: {
      EMPTY: '請輸入時段資料',
      INVALID_FORMAT: '如未來有需要預約 Giver 時間，請使用聊天輸入區域下方的功能按鈕。',
      TOO_MANY: '一次最多只能提交 10 個時段',
      NO_VALID_SCHEDULES: '沒有有效的時段資料'
    }
  },

  // 生成重複時段詳細錯誤訊息
  generateDuplicateScheduleMessage: (newSchedule, existingSchedules) => {
    console.log('FormValidator.generateDuplicateScheduleMessage called', { newSchedule, existingSchedules });
    const conflictingSchedules = [];
    
    existingSchedules.forEach((schedule, index) => {
      // 使用通用函數檢查重疊或完全相同
      const isDuplicate = checkScheduleOverlap(newSchedule, [schedule]);
      
      if (isDuplicate) {
        // 檢查是否為完全相同的時段
        const isExactDuplicate = schedule.date === newSchedule.date && 
          schedule.startTime === newSchedule.startTime && 
          schedule.endTime === newSchedule.endTime;
        
        conflictingSchedules.push({
          type: isExactDuplicate ? 'exact' : 'overlapping',
          schedule: schedule,
          index: index
        });
      }
    });
    
    if (conflictingSchedules.length === 0) {
      return null;
    }
    
    // 生成詳細錯誤訊息
    const conflictingList = conflictingSchedules.map(conflict => {
      const schedule = conflict.schedule;
      const formattedSchedule = DOM.chat.formatScheduleWithWeekday(schedule.date, schedule.startTime, schedule.endTime);
      return formattedSchedule;
    });
    
    if (conflictingList.length === 1) {
      return FormValidator.ERROR_MESSAGES.SCHEDULE_FORM.DUPLICATE_SCHEDULE.replace('{{EXISTING_SCHEDULE}}', conflictingList[0]);
    } else {
      const scheduleList = conflictingList.join('、');
      return `您正輸入的時段，和您之前曾輸入的「${scheduleList}」時段重複或重疊，請重新輸入`;
    }
  },

  // 驗證聊天訊息
  validateChatMessage: (message) => {
    console.log('FormValidator.validateChatMessage called', { message });
    
    const rules = FormValidator.RULES.CHAT_MESSAGE;
    const errors = [];
    
    // 檢查是否為空
    if (!message || typeof message !== 'string') {
      errors.push(FormValidator.ERROR_MESSAGES.CHAT_MESSAGE.EMPTY);
    } else {
      const trimmedMessage = message.trim();
      
      // 檢查長度
      if (trimmedMessage.length === 0) {
        errors.push(FormValidator.ERROR_MESSAGES.CHAT_MESSAGE.EMPTY);
      } else if (trimmedMessage.length > rules.MAX_LENGTH) {
        errors.push(FormValidator.ERROR_MESSAGES.CHAT_MESSAGE.TOO_LONG);
      }
      
      // 檢查禁止的模式
      for (const pattern of rules.FORBIDDEN_PATTERNS) {
        if (pattern.test(trimmedMessage)) {
          errors.push(FormValidator.ERROR_MESSAGES.CHAT_MESSAGE.FORBIDDEN_PATTERN);
          break;
        }
      }
    }
    
    const isValid = errors.length === 0;
    console.log('FormValidator.validateChatMessage: 驗證結果', { isValid, errors });
    
    return {
      isValid,
      errors,
      message: errors.length > 0 ? errors[0] : null
    };
  },
  
  // 驗證時段表單
  validateScheduleForm: (formData) => {
    console.log('FormValidator.validateScheduleForm called', { formData });
    
    const rules = FormValidator.RULES.SCHEDULE_FORM;
    const errors = [];
    
    // 驗證日期
    if (rules.DATE.REQUIRED && (!formData.date || !formData.date.trim())) {
      errors.push(FormValidator.ERROR_MESSAGES.SCHEDULE_FORM.DATE_REQUIRED);
    } else if (formData.date) {
      if (!DateUtils.isValidDateFormat(formData.date)) {
        // 檢查是否已經有日期格式錯誤訊息
        const dateInput = document.getElementById('schedule-date');
        const hasExistingDateFormatError = ErrorElementUtils.hasInputError(dateInput, '日期格式不正確');
        
        if (!hasExistingDateFormatError) {
          errors.push(FormValidator.ERROR_MESSAGES.SCHEDULE_FORM.DATE_INVALID);
        } else {
          errors.push('__HIDDEN_ERROR__');
        }
      } else {
        // 檢查是否為過去日期
        const today = DateUtils.getToday();
        const selectedDate = new Date(formData.date.replace(/\//g, '-'));
        if (selectedDate < new Date(today.getFullYear(), today.getMonth(), today.getDate())) {
          // 檢查是否已經有過去日期錯誤訊息
          const dateInput = document.getElementById('schedule-date');
          const hasExistingPastDateError = ErrorElementUtils.hasInputError(dateInput, '不能選擇過去的日期');
          
          if (!hasExistingPastDateError) {
            errors.push(FormValidator.ERROR_MESSAGES.SCHEDULE_FORM.DATE_PAST);
          } else {
            errors.push('__HIDDEN_ERROR__');
          }
        }
        
        // 檢查是否超過 3 個月
        if (!DateUtils.validateDateWithinAllowedMonths(selectedDate)) {
          // 檢查是否已經有超過3個月錯誤訊息
          const dateInput = document.getElementById('schedule-date');
          const hasExistingTooFarError = ErrorElementUtils.hasInputError(dateInput, '不能預約 3 個月後的日期');
          
          if (!hasExistingTooFarError) {
            errors.push(FormValidator.ERROR_MESSAGES.SCHEDULE_FORM.DATE_TOO_FAR);
          } else {
            errors.push('__HIDDEN_ERROR__');
          }
        }
      }
    }
    
    // 驗證開始時間
    if (rules.TIME.REQUIRED && (!formData.startTime || !formData.startTime.trim())) {
      errors.push(FormValidator.ERROR_MESSAGES.SCHEDULE_FORM.START_TIME_REQUIRED);
    } else if (formData.startTime && !DateUtils.isValidTimeFormat(formData.startTime)) {
      // 檢查是否已經有錯誤訊息
      const startTimeInput = document.getElementById('schedule-start-time');
      const hasExistingError = ErrorElementUtils.hasInputError(startTimeInput);
      if (!hasExistingError) {
        // 如果沒有現有錯誤訊息，添加預設錯誤訊息
        errors.push(FormValidator.ERROR_MESSAGES.SCHEDULE_FORM.TIME_INVALID);
      } else {
        // 如果有現有錯誤訊息，添加一個隱藏的錯誤來阻止表單提交，但不顯示新訊息
        errors.push('__HIDDEN_ERROR__');
      }
    }
    
    // 驗證結束時間
    if (rules.TIME.REQUIRED && (!formData.endTime || !formData.endTime.trim())) {
      errors.push(FormValidator.ERROR_MESSAGES.SCHEDULE_FORM.END_TIME_REQUIRED);
    } else if (formData.endTime && !DateUtils.isValidTimeFormat(formData.endTime)) {
      // 檢查是否已經有錯誤訊息
      const endTimeInput = document.getElementById('schedule-end-time');
      const hasExistingError = ErrorElementUtils.hasInputError(endTimeInput);
      if (!hasExistingError) {
        // 如果沒有現有錯誤訊息，添加預設錯誤訊息
        errors.push(FormValidator.ERROR_MESSAGES.SCHEDULE_FORM.TIME_INVALID);
      } else {
        // 如果有現有錯誤訊息，添加一個隱藏的錯誤來阻止表單提交，但不顯示新訊息
        errors.push('__HIDDEN_ERROR__');
      }
    }
    
    // 驗證時間邏輯
    if (formData.startTime && formData.endTime && 
        DateUtils.isValidTimeFormat(formData.startTime) && 
        DateUtils.isValidTimeFormat(formData.endTime)) {
      
      if (DateUtils.compareTimes(formData.startTime, formData.endTime) >= 0) {
        // 生成包含具體時間值的錯誤訊息
        const timeLogicError = `結束時間「${formData.endTime}」，必須晚於開始時間「${formData.startTime}」`;
        errors.push(timeLogicError);
      }
      
      // 檢查多數人休息時間
      const businessStart = rules.TIME.BUSINESS_HOURS.START;
      const businessEnd = rules.TIME.BUSINESS_HOURS.END;
      
      if (DateUtils.compareTimes(formData.startTime, businessStart) < 0 ||
          DateUtils.compareTimes(formData.endTime, businessEnd) > 0) {
        // 檢查是否已經有多數人休息時間相關的錯誤訊息
        const startTimeInput = document.getElementById('schedule-start-time');
        const endTimeInput = document.getElementById('schedule-end-time');
        const hasExistingBusinessHoursError = (
          ErrorElementUtils.hasInputError(startTimeInput, '多數人休息時間') ||
          ErrorElementUtils.hasInputError(endTimeInput, '多數人休息時間')
        );
        
        if (!hasExistingBusinessHoursError) {
          errors.push(FormValidator.ERROR_MESSAGES.SCHEDULE_FORM.TIME_BUSINESS_HOURS);
        } else {
          // 如果有現有錯誤訊息，添加一個隱藏的錯誤來阻止表單提交，但不顯示新訊息
          errors.push('__HIDDEN_ERROR__');
        }
      }
    }
    
    // 驗證備註
    if (formData.notes && formData.notes.trim()) {
      const notes = formData.notes.trim();
      
      if (notes.length > rules.NOTES.MAX_LENGTH) {
        // 檢查是否已經有備註相關的錯誤訊息
        const notesInput = document.getElementById('schedule-notes');
        const hasExistingNotesError = ErrorElementUtils.hasInputError(notesInput, '備註不能超過');
        
        if (!hasExistingNotesError) {
          errors.push(FormValidator.ERROR_MESSAGES.SCHEDULE_FORM.NOTES_TOO_LONG);
        } else {
          // 如果有現有錯誤訊息，添加一個隱藏的錯誤來阻止表單提交，但不顯示新訊息
          errors.push('__HIDDEN_ERROR__');
        }
      }
      
      if (!rules.NOTES.ALLOWED_CHARS.test(notes)) {
        errors.push(FormValidator.ERROR_MESSAGES.SCHEDULE_FORM.NOTES_INVALID);
      }
    }
    
    const isValid = errors.length === 0;
    console.log('FormValidator.validateScheduleForm: 驗證結果', { isValid, errors });
    
    return {
      isValid,
      errors,
      message: errors.length > 0 ? errors[0] : null
    };
  },
  
  // 驗證多筆時段
  validateMultipleSchedules: (message) => {
    console.log('FormValidator.validateMultipleSchedules called', { message });
    
    const rules = FormValidator.RULES.MULTIPLE_SCHEDULES;
    const errors = [];
    
    // 檢查是否為空
    if (!message || typeof message !== 'string' || !message.trim()) {
      errors.push(FormValidator.ERROR_MESSAGES.MULTIPLE_SCHEDULES.EMPTY);
    } else {
      // 使用 DateUtils 解析多筆時段
      const { isValid, schedules } = DateUtils.parseMultipleSchedules(message);
      
      if (!isValid) {
        errors.push(FormValidator.ERROR_MESSAGES.MULTIPLE_SCHEDULES.INVALID_FORMAT);
      } else if (schedules.length > rules.MAX_SCHEDULES) {
        errors.push(FormValidator.ERROR_MESSAGES.MULTIPLE_SCHEDULES.TOO_MANY);
      } else if (schedules.length < rules.MIN_SCHEDULES) {
        errors.push(FormValidator.ERROR_MESSAGES.MULTIPLE_SCHEDULES.NO_VALID_SCHEDULES);
      }
    }
    
    const isValid = errors.length === 0;
    console.log('FormValidator.validateMultipleSchedules: 驗證結果', { isValid, errors });
    
    return {
      isValid,
      errors,
      message: errors.length > 0 ? errors[0] : null
    };
  },
  
  // 驗證表單欄位（即時驗證）
  validateField: (fieldName, value, formType = 'schedule') => {
    console.log('FormValidator.validateField called', { fieldName, value, formType });
    
    let isValid = true;
    let errorMessage = null;
    
    switch (formType) {
      case 'schedule':
        switch (fieldName) {
          case 'date':
            if (!value || !value.trim()) {
              isValid = false;
              errorMessage = FormValidator.ERROR_MESSAGES.SCHEDULE_FORM.DATE_REQUIRED;
            } else if (!DateUtils.isValidDateFormat(value)) {
              isValid = false;
              errorMessage = FormValidator.ERROR_MESSAGES.SCHEDULE_FORM.DATE_INVALID;
            }
            break;
            
          case 'startTime':
          case 'endTime':
            if (!value || !value.trim()) {
              isValid = false;
              errorMessage = fieldName === 'startTime' 
                ? FormValidator.ERROR_MESSAGES.SCHEDULE_FORM.START_TIME_REQUIRED
                : FormValidator.ERROR_MESSAGES.SCHEDULE_FORM.END_TIME_REQUIRED;
            } else if (!DateUtils.isValidTimeFormat(value)) {
              isValid = false;
              errorMessage = FormValidator.ERROR_MESSAGES.SCHEDULE_FORM.TIME_INVALID;
            }
            break;
            
          case 'notes':
            if (value && value.trim().length > FormValidator.RULES.SCHEDULE_FORM.NOTES.MAX_LENGTH) {
              isValid = false;
              errorMessage = FormValidator.ERROR_MESSAGES.SCHEDULE_FORM.NOTES_TOO_LONG;
            }
            break;
        }
        break;
        
      case 'chat':
        if (fieldName === 'message') {
          const result = FormValidator.validateChatMessage(value);
          isValid = result.isValid;
          errorMessage = result.message;
        }
        break;
    }
    
    console.log('FormValidator.validateField: 驗證結果', { isValid, errorMessage });
    
    return {
      isValid,
      errorMessage
    };
  },
  
  // 顯示驗證錯誤
  showValidationError: (message, element = null) => {
    console.log('FormValidator.showValidationError called', { message, element });
    
    if (element) {
      // 檢查是否為時間邏輯錯誤，如果是則顯示在表單下方
      if (message && message.includes('結束時間') && message.includes('必須晚於開始時間')) {
        FormValidator.showDuplicateScheduleError(message);
        return;
      }
      
      // 先清除該元素的所有現有錯誤訊息
      FormValidator.clearValidationError(element);
      
      // 在特定元素上顯示錯誤
      let errorElement = ErrorElementUtils.getInputErrorElement(element);
      
      if (errorElement) {
        // 使用現有的錯誤元素
        errorElement.textContent = message;
        if (message) {
          errorElement.classList.remove('error-hidden');
          errorElement.classList.add('error-visible');
        } else {
          errorElement.classList.remove('error-visible');
          errorElement.classList.add('error-hidden');
        }
      } else {
        // 創建新的錯誤元素
        const errorDiv = document.createElement('div');
        errorDiv.className = 'validation-error text-danger small mt-1';
        errorDiv.textContent = message;
        if (message) {
          errorDiv.classList.add('error-visible');
        } else {
          errorDiv.classList.add('error-hidden');
        }
        element.parentNode.appendChild(errorDiv);
      }
    } else {
      // 檢查是否為重複時段錯誤或時間邏輯錯誤，如果是則顯示在表單下方
      if (message && (
        message.includes('重複或重疊') || 
        message.includes('DUPLICATE_SCHEDULE') ||
        (message.includes('結束時間') && message.includes('必須晚於開始時間'))
      )) {
        FormValidator.showDuplicateScheduleError(message);
      } else {
        // 使用 alert 顯示其他錯誤
        if (message) {
          alert(message);
        }
      }
    }
  },
  
  // 清除驗證錯誤
  clearValidationError: (element) => {
    console.log('FormValidator.clearValidationError called', { element });
    
    if (element) {
      // 只清除該元素及其直接父元素的錯誤訊息，不清除表單下方的錯誤訊息
      const errorElement = ErrorElementUtils.getInputErrorElement(element);
      
      if (errorElement) {
        // 檢查是否為表單下方的錯誤訊息（duplicate-schedule-error），如果是則不清除
        if (!errorElement.classList.contains('duplicate-schedule-error')) {
          ErrorElementUtils.clearInputError(element);
        }
      }
    }
  },
  
  // 顯示重複時段錯誤在表單下方
  showDuplicateScheduleError: (message) => {
    console.log('FormValidator.showDuplicateScheduleError called', { message });
    
    // 找到表單元素
    const formElement = document.getElementById('time-schedule-form');
    if (!formElement) {
      console.warn('FormValidator.showDuplicateScheduleError: 找不到表單元素');
      return;
    }
    
    // 先清除現有的重複時段錯誤
    FormValidator.clearDuplicateScheduleError();
    
    // 創建錯誤訊息元素
    const errorDiv = document.createElement('div');
    errorDiv.className = 'validation-error text-danger small mt-2 duplicate-schedule-error';
    errorDiv.textContent = message;
    errorDiv.style.display = 'block';
    
    // 將錯誤訊息插入到表單的確認按鈕下方
    const confirmButton = formElement.querySelector('button[type="submit"]');
    if (confirmButton) {
      // 找到確認按鈕的父容器（通常是 d-flex justify-content-end gap-2）
      const buttonContainer = confirmButton.parentNode;
      // 直接在按鈕容器後面插入錯誤訊息
      buttonContainer.parentNode.insertBefore(errorDiv, buttonContainer.nextSibling);
    } else {
      // 如果找不到確認按鈕，則插入到表單的最後
      formElement.appendChild(errorDiv);
    }
    
    console.log('FormValidator.showDuplicateScheduleError: 重複時段錯誤已顯示');
  },
  
  // 清除重複時段錯誤
  clearDuplicateScheduleError: () => {
    console.log('FormValidator.clearDuplicateScheduleError called');
    
    const formElement = document.getElementById('time-schedule-form');
    if (formElement) {
      const existingError = formElement.querySelector('.duplicate-schedule-error');
      if (existingError) {
        existingError.remove();
      }
    }
  },
  
  // 清空表單所有錯誤訊息
  clearAllValidationErrors: (formElement) => {
    console.log('FormValidator.clearAllValidationErrors called', { formElement });
    
    if (formElement) {
      // 清空表單內所有錯誤訊息
      const errorElements = formElement.querySelectorAll('.validation-error');
      errorElements.forEach(errorElement => {
        errorElement.classList.remove('error-visible');
        errorElement.classList.add('error-hidden');
        errorElement.textContent = '';
      });
      
      // 也清空表單外但相關的錯誤訊息（如時間輸入欄位的錯誤）
      const startTimeInput = document.getElementById('schedule-start-time');
      const endTimeInput = document.getElementById('schedule-end-time');
      const dateInput = document.getElementById('schedule-date');
      const notesInput = document.getElementById('schedule-notes');
      
      // 使用 ErrorElementUtils 清除多個輸入欄位的錯誤
      ErrorElementUtils.clearMultipleInputErrors([startTimeInput, endTimeInput, dateInput, notesInput]);
      
      // 清除重複時段錯誤
      FormValidator.clearDuplicateScheduleError();
    }
  },
  
  // 驗證整個表單並返回結果
  validateForm: (formElement, formType = 'schedule') => {
    console.log('FormValidator.validateForm called', { formElement, formType });
    
    const formData = {};
    const errors = [];
    
    // 收集表單資料
    const inputs = formElement.querySelectorAll('input, textarea, select');
    inputs.forEach(input => {
      if (input.name || input.id) {
        const fieldName = input.name || input.id.replace(/^schedule-/, '');
        formData[fieldName] = input.value;
      }
    });
    
    console.log('FormValidator.validateForm: 收集的表單資料', formData);
    
    // 根據表單類型進行驗證
    let validationResult;
    switch (formType) {
      case 'schedule':
        validationResult = FormValidator.validateScheduleForm(formData);
        break;
      case 'chat':
        validationResult = FormValidator.validateChatMessage(formData.message || '');
        break;
      case 'multiple-schedules':
        validationResult = FormValidator.validateMultipleSchedules(formData.message || '');
        break;
      default:
        validationResult = { isValid: false, errors: ['未知的表單類型'] };
    }
    
    // 清除所有錯誤顯示
    inputs.forEach(input => {
      FormValidator.clearValidationError(input);
    });
    
    // 顯示錯誤
    if (!validationResult.isValid) {
      validationResult.errors.forEach(error => {
        // 時間邏輯錯誤顯示在表單下方，多數人休息時間錯誤使用彈出顯示
        if (error && error.includes('多數人休息時間')) {
          FormValidator.showValidationError(error);
        } else {
          FormValidator.showValidationError(error, formElement);
        }
      });
    }
    
    console.log('FormValidator.validateForm: 驗證結果', validationResult);
    
    return validationResult;
  }
};

// ======================================================
//   3-5. 業務邏輯模組 (Business Logic Module)
// ======================================================

const BusinessLogic = {
  chat: {
    // 驗證訊息
    validateMessage: (message) => {
      if (!message || typeof message !== 'string') return false;
      if (message.trim().length === 0) return false;
      if (message.length > CONFIG.CHAT.MAX_MESSAGE_LENGTH) return false;
      return true;
    },
    // 生成回應
    generateResponse: (userMessage) => {
      const responses = [
        '如未來有需要預約 Giver 時間，請使用聊天輸入區域下方的功能按鈕。',
      ];
      const randomIndex = Math.floor(Math.random() * responses.length);
      return responses[randomIndex];
    }
  }
};

// ======================================================================
//   4. UI 和互動模組：依賴核心模組 (UI and Interaction Modules: Dependencies on Core Modules)
// ======================================================================

// ======================================================
//   4-1. 模板管理 (Template Management)
// ======================================================

const TEMPLATES = {

  // 分頁導覽模板
  paginator: {
    // 頁碼按鈕模板
    item: (pageNumber) => `
      <li class="${CONFIG.CLASSES.PAGINATOR_ITEM} ${pageNumber === appState.currentPage ? CONFIG.CLASSES.PAGINATOR_ITEM_ACTIVE : CONFIG.CLASSES.PAGINATOR_ITEM_DISABLED}">
        <a class="${CONFIG.CLASSES.PAGINATOR_LINK} ${CONFIG.CLASSES.PAGINATOR_LINK_PAGE}" href="#" data-page="${pageNumber}" aria-label="第 ${pageNumber} 頁">${pageNumber}</a>
      </li>
    `,

    // 分頁導覽容器模板
    container: () => '<ul class="pagination paginator-container" role="navigation" aria-label="分頁導覽">',

    // 上一頁按鈕模板
    prevButton: () => `
      <li class="${CONFIG.CLASSES.PAGINATOR_ITEM} ${CONFIG.CLASSES.PAGINATOR_ITEM_DISABLED}">
        <a class="${CONFIG.CLASSES.PAGINATOR_LINK} ${CONFIG.CLASSES.PAGINATOR_LINK_PREV}" href="#" data-page="prev" aria-label="前往上一頁" aria-disabled="true">
          <i class="fas fa-chevron-left"></i>
        </a>
      </li>
    `,

    // 下一頁按鈕模板
    nextButton: () => `
      <li class="${CONFIG.CLASSES.PAGINATOR_ITEM}">
        <a class="${CONFIG.CLASSES.PAGINATOR_LINK} ${CONFIG.CLASSES.PAGINATOR_LINK_NEXT}" href="#" data-page="next" aria-label="前往下一頁">
          <i class="fas fa-chevron-right"></i>
        </a>
      </li>
    `,

    // 省略號模板
    ellipsis: () => `
      <li class="${CONFIG.CLASSES.PAGINATOR_ITEM} ${CONFIG.CLASSES.PAGINATOR_ITEM_ACTIVE}">
        <span class="${CONFIG.CLASSES.PAGINATOR_LINK} ${CONFIG.CLASSES.PAGINATOR_LINK_PAGE}" aria-hidden="true">...</span>
      </li>
    `,

    // 頁碼按鈕模板
    pageNumber: (pageNumber, isActive) => `
      <li class="${CONFIG.CLASSES.PAGINATOR_ITEM} ${isActive ? CONFIG.CLASSES.PAGINATOR_ITEM_ACTIVE : CONFIG.CLASSES.PAGINATOR_ITEM_DISABLED}">
        <a class="${CONFIG.CLASSES.PAGINATOR_LINK} ${CONFIG.CLASSES.PAGINATOR_LINK_PAGE}" href="#" data-page="${pageNumber}" aria-label="第 ${pageNumber} 頁" ${isActive ? 'aria-current="page"' : ''}>${pageNumber}</a>
      </li>
    `,
  },

  // 無資料提示模板
  noDataMessage: () => `
    <div class="text-center py-5">
      <i class="fas fa-inbox fa-3x text-muted mb-3"></i>
      <p class="text-muted">${CONFIG.MESSAGES.INFO.NO_DATA}</p>
    </div>
  `,

  // 聊天相關模板
  chat: {
    button: (key) => {
      const config = CONFIG.UI_TEXT.BUTTON_GROUPS[key];
      if (!config) return '';
      return `<button class="btn ${config.class} btn-option chat-option-btn" data-option="${key}">${config.text}</button>`;
    },

    buttonGroup: (keys) => keys.map(TEMPLATES.chat.button).join('\n'),
    
    // 表格標題模板
    tableHeaders: {
      // 5 欄位表格標題（序、狀態、時段、備註、調整）
      fiveColumns: () => `
        <thead class="table-light">
          <tr>
            <th class="text-center">${CONFIG.UI_TEXT.TABLE_HEADERS.FIVE_COLUMNS.ORDER}</th>
            <th class="text-center">${CONFIG.UI_TEXT.TABLE_HEADERS.FIVE_COLUMNS.STATUS}</th>
            <th class="text-center">${CONFIG.UI_TEXT.TABLE_HEADERS.FIVE_COLUMNS.TIME_SLOT}</th>
            <th class="text-center">${CONFIG.UI_TEXT.TABLE_HEADERS.FIVE_COLUMNS.NOTES}</th>
            <th class="text-center">${CONFIG.UI_TEXT.TABLE_HEADERS.FIVE_COLUMNS.ACTIONS}</th>
          </tr>
        </thead>
      `,
    },

    // 訊息容器模板
    messageContainer: {
      // 帶頭像的完整訊息容器
      withAvatar: (title, buttonGroup) => `
        <div class="message giver-message">
          <div class="d-flex align-items-center">
            <img id="chat-giver-avatar-small" src="/static/images/icons/chat-avatar.svg" alt="Giver" class="chat-avatar-modal">
          </div>
          <div class="message-content">
            <p class="message-title">${title}</p>
            <div class="chat-options-buttons mt-2">
              ${buttonGroup}
            </div>
          </div>
        </div>
      `,

      // 只有按鈕的容器
      buttonsOnly: (buttonGroup) => `
        <div class="chat-options-buttons mt-2">
          ${buttonGroup}
        </div>
      `,

      // 帶表格的訊息容器
      withTable: (title, tableContent, tableClass = 'table-hover') => `
        <div class="message giver-message">
          <div class="d-flex align-items-center">
            <img id="chat-giver-avatar-small" src="/static/images/icons/chat-avatar.svg" alt="Giver" class="chat-avatar-modal">
          </div>
          <div class="message-content">
            <p class="message-title">${title}</p>
            <div class="table-responsive mt-2">
              <table class="table table-sm table-bordered ${tableClass}">
                ${tableContent}
              </table>
            </div>
          </div>
        </div>
      `,

      // 帶內容的訊息容器（可包含任意內容）
      withContent: (title, content) => `
        <div class="message giver-message">
          <div class="d-flex align-items-center">
            <img id="chat-giver-avatar-small" src="/static/images/icons/chat-avatar.svg" alt="Giver" class="chat-avatar-modal">
          </div>
          <div class="message-content">
            <p class="message-title">${title}</p>
            ${content}
          </div>
        </div>
      `,

      // 帶表格和按鈕的訊息容器
      withTableAndButtons: (title, tableContent, buttonGroup, tableClass = 'table-hover') => `
        <div class="message giver-message">
          <div class="d-flex align-items-center">
            <img id="chat-giver-avatar-small" src="/static/images/icons/chat-avatar.svg" alt="Giver" class="chat-avatar-modal">
          </div>
          <div class="message-content">
            <p class="message-title">${title}</p>
            <div class="table-responsive mt-2">
              <table class="table table-sm table-bordered ${tableClass}">
                ${tableContent}
              </table>
            </div>
            ${getPromptText('SELECT_NEXT_ACTION')}
            <div class="chat-options-buttons mt-2">
              ${buttonGroup}
            </div>
          </div>
        </div>
      `
    },

    // 初始聊天訊息模板
    initialMessage: () =>`
      <div class="message giver-message">
        <div class="d-flex align-items-center mb-2">
            <img id="chat-giver-avatar-small" src="/static/images/icons/chat-avatar.svg" alt="Giver 頭像"
                class="chat-avatar-modal">
        </div>
        <div class="message-content">
            <p class="message-title">如想與 Giver 進行諮詢，例如線上模擬面試、即時文字訊息往返，請點此預約 Giver 時間。</p>
            <!-- 直接顯示的選項按鈕 -->
            <div class="chat-options-buttons" role="group" aria-label="諮詢選項">
                <button class="btn btn-outline btn-option" data-option="schedule"
                    aria-label="預約 Giver 時間">
                    ${CONFIG.UI_TEXT.BUTTONS.SCHEDULE}
                </button>
                <button class="btn btn-outline btn-option" data-option="skip" aria-label="暫不預約">
                    ${CONFIG.UI_TEXT.BUTTONS.SKIP}
                </button>
            </div>
        </div>
    </div>
    `,

    // 預約選項按鈕模板
    scheduleOptions: () => `
      <div class="message giver-message">
        <div class="d-flex align-items-center">
            <img id="chat-giver-avatar-small" src="/static/images/icons/chat-avatar.svg" alt="Giver" class="chat-avatar-modal">
        </div>
        
        <div class="message-content">
          <p class="message-title">好的！我來幫您安排預約時間。請選擇以下選項：</p>
          <div class="chat-options-buttons mt-2">
            ${TEMPLATES.chat.buttonGroup(['view-times', 'single-time', 'multiple-times', 'cancel'])}
          </div>
        </div>
      </div>
    `,

    // 預約表單模板
    scheduleForm: () => `
      <div id="schedule-form" class="message user-message schedule-form-visible">
        <div class="message-content-giver">
          <p class="message-title">請提供您方便的時段：</p>
          <form id="time-schedule-form" class="schedule-form">
            <div class="form-group mb-3">
              <label for="schedule-date" class="form-label">日期 <span class="text-danger">*</span></label>
              <input type="text" id="schedule-date" class="form-control" placeholder="請選擇日期" required>
            </div>
            <div class="row">
              <div class="col-md-6">
                <div class="form-group mb-3">
                  <label for="schedule-start-time" class="form-label">開始時間<span class="text-danger">*</span></label>
                  <input type="text" id="schedule-start-time" class="form-control" placeholder="請輸入 4 位數字如「2000」，無需輸入「:」" required>
                </div>
              </div>
              <div class="col-md-6">
                <div class="form-group mb-3">
                  <label for="schedule-end-time" class="form-label">結束時間<span class="text-danger">*</span></label>
                  <input type="text" id="schedule-end-time" class="form-control" placeholder="請輸入 4 位數字如「2200」，無需輸入「:」" required>
                </div>
              </div>
            </div>
            <div class="form-group mb-3">
              <label for="schedule-notes" class="form-label">備註（非必填）</label>
              <input type="text" id="schedule-notes" class="form-control" placeholder="請輸入備註（非必填）">
            </div>
            <div class="d-flex justify-content-end gap-2">
              <button type="button" class="btn btn-outline-secondary" id="cancel-schedule-form">取消</button>
              <button type="submit" class="btn btn-orange">確認</button>
            </div>
          </form>
        </div>
      </div>
    `,

    // 表單提交後選項按鈕模板
    afterScheduleOptions: (formattedSchedule, notes) => {
      // 獲取所有時段（正式提供 + 草稿）
      const { allSchedules, scheduleCount } = getAllSchedulesWithDraftStatus();
      
      // 生成表格內容
      let tableRows = '';
      allSchedules.forEach((schedule, index) => {
        // 使用通用函數生成表格行
        tableRows += generateScheduleTableRow(schedule, index, {
          buttonType: 'schedule'
        });
      });
      
      const tableContent = generateTableContent(tableRows);
      
      const buttonGroup = TEMPLATES.chat.buttonGroup(['continue-single-time', 'continue-multiple-times', 'submit-schedules']);
      return TEMPLATES.chat.messageContainer.withTableAndButtons(
        `您目前已提供 ${scheduleCount} 個時段，進度如下：`,
        tableContent,
        buttonGroup,
        'schedule-table table-hover'
      );
    },

    // 多筆時段提交後選項按鈕模板
    afterMultipleScheduleOptions: () => {
      // 獲取所有時段（正式提供 + 草稿）
      const { allSchedules, scheduleCount } = getAllSchedulesWithDraftStatus();
      
      // 生成表格內容
      let tableRows = '';
      allSchedules.forEach((schedule, index) => {
        // 使用通用函數生成表格行
        tableRows += generateScheduleTableRow(schedule, index, {
          buttonType: 'schedule'
        });
      });
      
      const tableContent = generateTableContent(tableRows);
      
      const buttonGroup = TEMPLATES.chat.buttonGroup(['continue-single-time', 'continue-multiple-times', 'submit-schedules']);
      return TEMPLATES.chat.messageContainer.withTableAndButtons(
        `您目前已提供 ${scheduleCount} 個時段，進度如下：`,
        tableContent,
        buttonGroup,
        'schedule-table table-hover'
      );
    },

    // 查看所有時段選項按鈕模板
    viewAllSchedulesOptions: (scheduleList, scheduleCount) =>
      TEMPLATES.chat.messageContainer.withAvatar(
        `您目前已提供 ${scheduleCount} 個時段，進度如下：<br>${scheduleList}<br>${CONFIG.UI_TEXT.PROMPTS.SELECT_NEXT_ACTION}`,
        TEMPLATES.chat.buttonGroup(['single-time', 'multiple-times', 'submit-schedules', 'cancel'])
      ),

    // 時段表格模板
    scheduleTable: (schedules) => {
      let tableRows = '';
      schedules.forEach((schedule, index) => {
        // 使用通用函數生成表格行
        tableRows += generateScheduleTableRow(schedule, index, {
          buttonType: 'schedule',
          showNotes: true
        });
      });
      const scheduleCount = schedules.length;
      const tableContent = generateTableContent(tableRows);
      const buttonGroup = TEMPLATES.chat.buttonGroup(['single-time', 'multiple-times', 'submit-schedules', 'cancel']);
      return TEMPLATES.chat.messageContainer.withTableAndButtons(
        `您目前已提供 ${scheduleCount} 個時段，進度如下：`,
        tableContent,
        buttonGroup,
        'schedule-table table-hover'
      );
    },

    // 5 按鈕版本模板
    scheduleOptionsWithViewAll: () => 
      TEMPLATES.chat.messageContainer.withAvatar(
        '好的！我來幫您安排預約時間。請選擇以下選項：', 
        TEMPLATES.chat.buttonGroup(['view-times', 'single-time', 'multiple-times', 'view-all', 'cancel'])
      ),

    // 只有提供時段按鈕的模板
    onlyScheduleButtons: () => 
      TEMPLATES.chat.messageContainer.buttonsOnly( 
        TEMPLATES.chat.buttonGroup(['view-times', 'single-time', 'multiple-times', 'view-all', 'cancel'])
      ),

    // 您目前還沒有提供任何時段的模板
    noSchedulesWithButtons: () => 
      TEMPLATES.chat.messageContainer.withAvatar(
        '您目前還沒有提供任何時段，請先提供方便時段，然後再查看。', 
        TEMPLATES.chat.buttonGroup(['view-times', 'single-time', 'multiple-times', 'cancel'])
      ),

    // Giver 尚末提供方便時間的模板
    noGiverTimesWithButtons: () =>
      TEMPLATES.chat.messageContainer.withAvatar(
        `Giver 尚末提供方便的時間。請選擇以下選項：`,
        TEMPLATES.chat.buttonGroup(['single-time', 'multiple-times', 'cancel'])
      ),

    // 您目前還沒有預約任何 Giver 時間的模板
    noBookedTimesWithButtons: () =>
      TEMPLATES.chat.messageContainer.withAvatar(
        `您目前還沒有預約任何 Giver 時間。請選擇以下選項：`,
        TEMPLATES.chat.buttonGroup(['view-times', 'single-time', 'multiple-times', 'cancel'])
      ), 

    // 多筆時段功能的模板：預計於未來開放
    multipleTimesUnderConstruction: () => 
      TEMPLATES.chat.messageContainer.withAvatar(
        `此功能預計於未來開放，請先使用「提供單筆方便時段」方式新增時間，謝謝。`,
        TEMPLATES.chat.buttonGroup(['single-time', 'cancel'])
      ), 

    // 成功提供時間的模板
    successProvideTime: (schedules, startIndex = 0) => {
      console.log('TEMPLATES.chat.successProvideTime called', { schedules, startIndex });
      let tableRows = '';
      schedules.forEach((schedule, localIndex) => {
        // 使用通用函數生成表格行，使用全域索引
        tableRows += generateScheduleTableRow(schedule, localIndex, {
          buttonType: 'provide',
          useGlobalIndex: true,
          startIndex: startIndex
        });
      });
      const scheduleCount = schedules.length;
      const tableContent = generateTableContent(tableRows);
      
      return TEMPLATES.chat.messageContainer.withTable(
        `✅ 提供時間成功！您目前已提供 Giver 以下 ${scheduleCount} 個時段，請耐心等待對方確認回覆。`,
        tableContent,
        'success-provide-table table-hover'
      );
    },

    // 新增：Giver 已提供時間的複選模板
    giverAvailableTimesWithCheckboxes: () => `
      <div class="message giver-message">
        <div class="d-flex align-items-center">
          <img id="chat-giver-avatar-small" src="/static/images/icons/chat-avatar.svg" alt="Giver" class="chat-avatar-modal">
        </div>
        <div class="message-content">
          <p class="message-title">以下是 Giver 已提供、尚未被預約的日期：</p>
          <div class="chat-checkbox-options mt-2">
            <div class="form-check mb-2">
              <input class="form-check-input" type="checkbox" id="time-option-1" data-option="demo-time-1">
              <label class="form-check-label" for="time-option-1">
                ${getDemoTimeLabel('demo-time-1')}
              </label>
            </div>
            <div class="form-check mb-2">
              <input class="form-check-input" type="checkbox" id="time-option-2" data-option="demo-time-2">
              <label class="form-check-label" for="time-option-2">
                ${getDemoTimeLabel('demo-time-2')}
              </label>
            </div>
            <div class="form-check mb-2">
              <input class="form-check-input" type="checkbox" id="time-option-3" data-option="provide-my-time">
              <label class="form-check-label" for="time-option-3">
                ${CONFIG.UI_TEXT.BUTTONS.PROVIDE_MY_TIME_NOT_AVAILABLE}
              </label>
            </div>
          </div>
          <div class="form-check mb-3 d-flex justify-content-end gap-2">
            <button class="btn btn-outline-secondary btn-option" data-option="cancel">取消</button>
            <button class="btn btn-orange btn-option" id="confirm-selection-btn" disabled>確認</button>
          </div> 
        </div>
      </div>
    `,

    // 新增：提供我的時間選項模板
    provideMyTimeOptions: () => 
      TEMPLATES.chat.messageContainer.withAvatar(
        `好的！請選擇以下選項，提供您方便的時段：`,
        TEMPLATES.chat.buttonGroup(['single-time', 'multiple-times', 'cancel'])
      ),
    
    // 新增：預約成功訊息和表格模板
    reservationSuccessMessageAndTable: (demoTimeOptions, provideMyTimeOption) => {
      const totalCount = demoTimeOptions.length + (provideMyTimeOption ? 1 : 0);
      
      // 準備所有項目 - 處理 demoTimeOptions 的資料結構
      const allItems = [
        ...demoTimeOptions.map(option => ({
          option: option.option,
          timeSlot: getDemoTimeLabel(option.option),
          status: CONFIG.UI_TEXT.STATUS.TAKER_VIEW.PENDING
        })),
        ...(provideMyTimeOption ? [{
          option: 'provide-my-time',
          timeSlot: CONFIG.UI_TEXT.BUTTONS.PROVIDE_MY_TIME,
          status: CONFIG.UI_TEXT.STATUS.TAKER_VIEW.PENDING,
          buttonText: CONFIG.UI_TEXT.BUTTONS.CANCEL_OPTION
        }] : [])
      ];

      // 使用通用函數生成表格行
      const tableRows = generateReservationTableRows(allItems);

      const tableContent = generateTableContent(tableRows);
      
      return TEMPLATES.chat.messageContainer.withTable(
        CONFIG.UI_TEXT.RESERVATION_SUCCESS.TEXT,
        tableContent,
        'reservation-success-table table-hover'
      );
    },

    // 新增：已預約時間訊息和表格模板
    bookedTimesMessageAndTable: (bookedSchedules) => {
      
      // 使用通用函數生成表格行
      const tableRows = generateReservationTableRows(bookedSchedules);
      
      const tableContent = generateTableContent(tableRows);
      
      return TEMPLATES.chat.messageContainer.withTable(
        CONFIG.UI_TEXT.RESERVATION_SUCCESS.TEXT,
        tableContent,
        'reservation-success-table table-hover'
      );
    },

    // 新增：取消成功訊息和表格模板
    cancelSuccessMessageAndTable: (demoTimeOptions, provideMyTimeOption) => {
      console.log('TEMPLATES.chat.cancelSuccessMessageAndTable called', { demoTimeOptions, provideMyTimeOption });
      const totalCount = demoTimeOptions.length + (provideMyTimeOption ? 1 : 0);
      
      // 準備所有項目 - 處理 demoTimeOptions 的資料結構
      const allItems = [
        ...demoTimeOptions.map(option => ({
          option: option.option,
          timeSlot: getDemoTimeLabel(option.option),
          status: CONFIG.UI_TEXT.STATUS.TAKER_VIEW.PENDING
        })),
        ...(provideMyTimeOption ? [{
          option: 'provide-my-time',
          timeSlot: CONFIG.UI_TEXT.BUTTONS.PROVIDE_MY_TIME,
          status: CONFIG.UI_TEXT.STATUS.TAKER_VIEW.PENDING,
          buttonText: CONFIG.UI_TEXT.BUTTONS.CANCEL_OPTION
        }] : [])
      ];

      // 使用通用函數生成表格行
      const tableRows = generateReservationTableRows(allItems);
      
      const tableContent = generateTableContent(tableRows);
      
      return TEMPLATES.chat.messageContainer.withTable(
        `取消預約成功！您目前已預約 Giver 以下 ${totalCount} 個時段：`,
        tableContent,
        'reservation-success-table table-hover'
      );
    },
  },
};

// ======================================================
//   4-2. DOM 元素查詢工具 (DOM Element Query Utilities)
// ======================================================

const DOM = {
  // 基礎查詢方法
  getElement: (selector) => document.querySelector(selector),
  getElements: (selector) => document.querySelectorAll(selector),
  getById: (id) => document.getElementById(id),
  
  // 創建元素
  createElement: (tag, className = '', innerHTML = '') => {
    
    const element = document.createElement(tag);
    if (className) element.className = className;
    if (innerHTML) element.innerHTML = innerHTML;
    
    return element;
  },
  
  // 元素操作工具
  utils: {
    // 安全地設置文字內容（防止 XSS）
    setTextContent: (element, text) => {
      if (element) {
        element.textContent = text;
      } else {
      }
    },
    
    // 安全地設置 HTML 內容
    setInnerHTML: (element, html) => {
      if (element) {
        element.innerHTML = html;
      } else {
      }
    },
    
    // 添加事件監聽器
    addEventListener: (element, event, handler, options = {}) => {
      if (element) {
        element.addEventListener(event, handler, options);
      } else {
      }
    },
    
    // 移除事件監聽器
    removeEventListener: (element, event, handler, options = {}) => {
      if (element) {
        element.removeEventListener(event, handler, options);
      } else {
      }    
    },
    
    // 顯示元素
    show: (element) => {
      console.log('DOM.utils.show called', { element });
      if (element) {
        element.classList.remove('hidden');
        element.classList.add('visible');
      } else {
        console.error('無法顯示元素，元素不存在');
      }
    },
    
    // 隱藏元素
    hide: (element) => {
      console.log('DOM.utils.hide called', { element });
      if (element) {
        element.classList.remove('visible');
        element.classList.add('hidden');
      } else {
        console.error('無法隱藏元素，元素不存在');
      }
    },
    
    // 切換 CSS 類別
    toggleClass: (element, className) => {
      console.log('DOM.utils.toggleClass called', { element, className });
      if (element) {
        element.classList.toggle(className);
      } else {
        console.error(`[toggleClass] 元素不存在：無法切換 ${className} 類別`);
      }
    },
    
    // 添加 CSS 類別 
    addClass: (element, className) => {
      console.log('DOM.utils.addClass called', { element, className });
      if (element) {
        element.classList.add(className);
      } else {
        console.error(`[addClass] 無法添加 CSS 類別：元素不存在`);
      }
    },
    
    // 移除 CSS 類別
    removeClass: (element, className) => {
      console.log('DOM.utils.removeClass called', { element, className });
      if (element) {
        element.classList.remove(className);
      } else {
        console.error(`[removeClass] 無法移除 CSS 類別：元素不存在`);
      }
    },

    // 檢查橫向滾動是否超出容器
    checkTopicOverflow: (container, chevron) => {
      console.log('DOM.utils.checkTopicOverflow called', { container, chevron });
      if (!container || !chevron) {
        console.error(`[checkTopicOverflow] 無法檢查是否超出範圍：元素不存在`);
        return false;
      }
      const scrollWidth = container.scrollWidth;
      const clientWidth = container.clientWidth;
      return scrollWidth > clientWidth;
    },
    
    // 滾動到底部
    scrollToBottom: (element) => {
      console.log('DOM.utils.scrollToBottom called', { element });
      if (element) {
        element.scrollTo({
          top: element.scrollHeight,
          behavior: 'smooth'
        });
      } else {
        console.error(`[scrollToBottom] 無法滾動到底部：元素不存在`);
      }
    },
    
    // 清理 Modal
    cleanupModal: (modal) => {
      console.log('DOM.utils.cleanupModal called', { modal });
      if (modal) { 
        // 不要清空 modal 內容，只清理狀態
        modal.classList.remove('show');                // 移除 Bootstrap 的顯示 class
        modal.style.display = 'none';                  // 隱藏 modal 元素
        modal.removeAttribute('tabindex');             // 移除 tabindex 屬性
        modal.setAttribute('inert', '');               // 使用 inert 屬性
        
        // 使用 ModalCleanupUtils 清理 modal 相關元素和樣式
        ModalCleanupUtils.cleanupModal({ 
          removeBackdrop: true, 
          removeModalOpen: true, 
          clearOverflow: false, 
          clearPaddingRight: true 
        });
        
        // 強制處理焦點問題
        if (DOM.chat && DOM.chat.forceFocusToBody) {
          DOM.chat.forceFocusToBody();
        } else {
          // 備用方案
          document.body.focus();
        }
      } else {
        console.error(`[cleanupModal] 無法清理 Modal：元素不存在`);
      }
    }
  },
  
  // 聊天相關元素
  chatElements: {
    input: () => document.getElementById('chat-input-message'),
    sendBtn: () => document.getElementById('chat-send-btn'),
    messages: () => document.getElementById('chat-messages'),
    modal: () => document.getElementById('giver-modal'),
    header: () => document.querySelector('#giver-modal .modal-header'),
    title: () => document.getElementById('chatModalLabel'),
    modalElement: () => document.getElementById('giver-modal')
  },
  
  // 確認對話框相關元素
  confirm: {
    modal: () => document.getElementById('confirm-modal'),
    title: () => document.querySelector('#confirm-modal .modal-title'),
    message: () => document.querySelector('#confirm-modal .modal-body p.text-muted'),
    confirmBtn: () => document.getElementById('continue-btn'),
    cancelBtn: () => document.getElementById('leave-btn')
  },
  
  // Modal 相關元素
  modal: {
    backdrop: () => document.querySelector('.modal-backdrop'),
    giverModal: () => document.getElementById('giver-modal'),
    confirmModal: () => document.getElementById('confirm-modal')
  },
  
  // 服務項目相關元素
  topic: {
    containers: () => document.querySelectorAll('.giverCard__topic'),
    buttons: (container) => container.querySelectorAll('.btn-topic-sm'),
    chevron: (container) => container.querySelector('.fa-chevron-right')
  },
      
  // 聊天訊息建立工具
  message: {
    // 建立基礎訊息結構
    createBaseMessage: (type = 'user') => {
      const messageDiv = DOM.createElement('div', `message ${type}-message`);
      const messageContent = DOM.createElement('div', 'message-content');
      
      console.log('基礎訊息結構創建完成:', { messageDiv, messageContent });
      return { messageDiv, messageContent };
    },
    
    // 建立訊息文字內容
    createTextContent: (text, allowHTML = false) => {
      console.log('DOM.message.createTextContent called', { text, allowHTML });
      const p = DOM.createElement('p', 'mb-1');
      if (allowHTML) {
        p.innerHTML = text;
      } else if (text && text.includes('\n')) {
        const lines = text.split('\n');
        lines.forEach((line, index) => {
          if (index > 0) {
            p.appendChild(document.createElement('br'));
          }
          if (line.trim()) {
            const textNode = document.createTextNode(line);
            p.appendChild(textNode);
          }
        });
      } else {
        DOM.utils.setTextContent(p, text);
      }
      console.log('文字內容創建完成:', p);
      return p;
    },
    
    // 創建時間戳記
    createTimestamp: (timeString) => {
      console.log('DOM.message.createTimestamp called', { timeString });
      
      const timestampDiv = DOM.createElement('div', 'message-time');
      DOM.utils.setTextContent(timestampDiv, timeString);
      
      console.log('DOM.message.createTimestamp: 時間戳記創建完成', timestampDiv);
      return timestampDiv;
    },
    
    // 獲取當前時間字串
    getCurrentTimeString: () => {
      console.log('DOM.message.getCurrentTimeString called');
      const now = DateUtils.getToday();
      return DateUtils.formatToLocalTime(now);
    },
    
    // 建立 Giver 頭像
    createGiverAvatar: () => {
      console.log('DOM.message.createGiverAvatar called');
      
      const avatarContainer = DOM.createElement('div', 'd-flex align-items-center');
      const avatarImg = DOM.createElement('img');
      avatarImg.id = 'chat-giver-avatar-small';
              avatarImg.src = '/static/images/icons/chat-avatar.svg';
      avatarImg.alt = 'Giver';
      avatarImg.className = 'avatar-modal';
      avatarContainer.appendChild(avatarImg);
      
      console.log('Giver 頭像創建完成:', avatarContainer);
      return avatarContainer;
    },
    
    // 建立完整訊息
    createMessage: (text, type = 'user', allowHTML = false) => {
      console.log('DOM.message.createMessage called', { text, type, allowHTML });
      const { messageDiv, messageContent } = DOM.message.createBaseMessage(type);
      // 添加文字內容
      const textElement = DOM.message.createTextContent(text, allowHTML);
      messageContent.appendChild(textElement);
      // 創建時間戳記
      const timeString = DOM.message.getCurrentTimeString();
      const timestampElement = DOM.message.createTimestamp(timeString);
      console.log('DOM.message.createMessage: 時間戳記創建完成', timestampElement);
      messageContent.appendChild(timestampElement);
      // 如果是 Giver 訊息，添加頭像
      if (type === 'giver') {
        const avatar = DOM.message.createGiverAvatar();
        messageDiv.appendChild(avatar);
      }
      // 組合最終結構
      messageDiv.appendChild(messageContent);
      console.log('DOM.message.createMessage completed', { messageDiv });
      return messageDiv;
    },
    
    // 添加訊息到聊天區域
    addToChat: (messageElement) => {
      const chatMessages = DOM.chatElements.messages();
      if (!chatMessages) {
        console.error('聊天訊息區域未找到');
        return;
      }
      
      console.log('DOM.message.addToChat called', { messageElement });
      chatMessages.appendChild(messageElement);
      
      // 滾動到底部
      DOM.utils.scrollToBottom(chatMessages);
      console.log('DOM.message.addToChat completed');
    },
    
    // 清空聊天區域（保留初始訊息）
    clearChat: () => {
      const chatMessages = DOM.chatElements.messages();
      if (chatMessages) {
        // 清空聊天區域
        chatMessages.innerHTML = '';
        
        // 重新創建初始訊息
        const initialMessageHTML = TEMPLATES.chat.initialMessage();
        
        // 添加初始訊息到聊天區域
        chatMessages.innerHTML = initialMessageHTML;
        
        // 重新設定選項按鈕事件監聽器
        DOM.chat.setupOptionButtons();
        
        console.log('DOM.message.clearChat completed');
      }
    },
    
    // 獲取聊天區域中的所有訊息
    getAllMessages: () => {
      const chatMessages = DOM.chatElements.messages();
      console.log('DOM.message.getAllMessages called', { chatMessages });
      return chatMessages ? Array.from(chatMessages.children) : [];
    },
    
    // 獲取最後一條訊息
    getLastMessage: () => {
      const messages = DOM.message.getAllMessages();
      console.log('DOM.message.getLastMessage called', { messages });
      return messages.length > 0 ? messages[messages.length - 1] : null;
    },
    
    // 檢查訊息是否為特定類型
    isMessageType: (messageElement, type) => {
      console.log('DOM.message.isMessageType called', { messageElement, type });
      return messageElement && messageElement.classList.contains(`${type}-message`);
    },
    
    // 為訊息添加額外的 CSS 類別
    addMessageClass: (messageElement, className) => {
      console.log('DOM.message.addMessageClass called', { messageElement, className });
      if (messageElement) {
        DOM.utils.addClass(messageElement, className);
      }
    },
    
    // 移除訊息的 CSS 類別
    removeMessageClass: (messageElement, className) => {
      console.log('DOM.message.removeMessageClass called', { messageElement, className });
      if (messageElement) {
        DOM.utils.removeClass(messageElement, className);
      }
    }
  },
  
  // 事件監聽器管理工具
  events: {
    // 事件監聽器儲存
    listeners: new Map(),
    
    // 添加事件監聽器（帶管理功能）
    add: (element, event, handler, options = {}) => {
      console.log('DOM.events.add called', { element, event, handler, options });
      if (!element) return;
      
      // 生成唯一的事件識別碼
      const eventId = `${element.id || 'anonymous'}_${event}_${Date.now()}`;
      
      // 儲存事件監聽器資訊
      DOM.events.listeners.set(eventId, {
        element,
        event,
        handler,
        options,
        active: true
      });
      
      // 添加事件監聽器
      element.addEventListener(event, handler, options);
      
      return eventId;
    },
    
    // 移除事件監聽器
    remove: (eventId) => {
      console.log('DOM.events.remove called', { eventId });
      const listenerInfo = DOM.events.listeners.get(eventId);
      if (listenerInfo && listenerInfo.active) {
        listenerInfo.element.removeEventListener(
          listenerInfo.event, 
          listenerInfo.handler, 
          listenerInfo.options
        );
        listenerInfo.active = false;
        DOM.events.listeners.delete(eventId);
      }
    },
    
    // 移除元素的所有事件監聽器
    removeAll: (element) => {
      console.log('DOM.events.removeAll called', { element });
      for (const [eventId, listenerInfo] of DOM.events.listeners) {
        if (listenerInfo.element === element && listenerInfo.active) {
          DOM.events.remove(eventId);
        }
      }
    },
    
    // 移除特定事件類型的所有監聽器
    removeByEvent: (event) => {
      console.log('DOM.events.removeByEvent called', { event });
      for (const [eventId, listenerInfo] of DOM.events.listeners) {
        if (listenerInfo.event === event && listenerInfo.active) {
          DOM.events.remove(eventId);
        }
      }
    },
    
    // 移除特定元素的所有監聽器
    removeByElement: (element) => {
      console.log('DOM.events.removeByElement called', { element });
      for (const [eventId, listenerInfo] of DOM.events.listeners) {
        if (listenerInfo.element === element && listenerInfo.active) {
          DOM.events.remove(eventId);
        }
      }
    },
    
    // 獲取所有活動的事件監聽器
    getAll: () => {
      console.log('DOM.events.getAll called');
      return Array.from(DOM.events.listeners.entries())
        .filter(([_, info]) => info.active)
        .map(([id, info]) => ({ id, ...info }));
    },
    
    // 獲取元素的事件監聽器
    getByElement: (element) => {
      console.log('DOM.events.getByElement called', { element });
      return Array.from(DOM.events.listeners.entries())
        .filter(([_, info]) => info.element === element && info.active)
        .map(([id, info]) => ({ id, ...info }));
    },
    
    // 事件委派工具
    delegate: (parentElement, selector, event, handler, options = {}) => {
      console.log('DOM.events.delegate called', { parentElement, selector, event, handler, options });
      // 委派事件處理器（內部函式）
      const delegatedHandler = (e) => {
        const target = e.target.closest(selector);
        if (target && parentElement.contains(target)) {
          handler.call(target, e, target);
        }
      };
      
      return DOM.events.add(parentElement, event, delegatedHandler, options);
    },
    
    // 一次性事件監聽器
    once: (element, event, handler, options = {}) => {
      console.log('DOM.events.once called', { element, event, handler, options });
      // 一次性事件處理器（內部函式）
      const onceHandler = (e) => {
        handler(e);
        DOM.events.removeByElement(element);
      };
      
      return DOM.events.add(element, event, onceHandler, options);
    },
    
    // 防抖事件監聽器
    debounce: (element, event, handler, delay = 300, options = {}) => {
      console.log('DOM.events.debounce called', { element, event, handler, delay, options });
      let timeoutId;
      
      // 防抖事件處理器（內部函式）
      const debouncedHandler = (e) => {
        clearTimeout(timeoutId);
        timeoutId = setTimeout(() => handler(e), delay);
      };
      
      return DOM.events.add(element, event, debouncedHandler, options);
    },
    
    // 節流事件監聽器
    throttle: (element, event, handler, limit = 300, options = {}) => {
      console.log('DOM.events.throttle called', { element, event, handler, limit, options });
      let inThrottle;
      
      // 節流事件處理器（內部函式）
      const throttledHandler = (e) => {
        if (!inThrottle) {
          handler(e);
          inThrottle = true;
          setTimeout(() => inThrottle = false, limit);
        }
      };
      
      return DOM.events.add(element, event, throttledHandler, options);
    },
    
    // 事件監聽器管理工具
    utils: {      
      // 清理所有事件監聽器
      clearAll: () => {
        console.log('DOM.events.utils.clearAll called');
        const allListeners = DOM.events.getAll();
        allListeners.forEach(listener => {
          DOM.events.remove(listener.id);
        });
      },
      
      // 清理特定元素的所有事件監聽器
      clearElement: (element) => {
        console.log('DOM.events.utils.clearElement called', { element });
        DOM.events.removeAll(element);
      },
      
      // 清理特定事件類型的所有監聽器
      clearEvent: (event) => {
        console.log('DOM.events.utils.clearEvent called', { event });
        DOM.events.removeByEvent(event);
      },
      
      // 檢查元素是否有特定事件類型的監聽器
      hasEvent: (element, event) => {
        console.log('DOM.events.utils.hasEvent called', { element, event });
        const elementListeners = DOM.events.getByElement(element);
        return elementListeners.some(listener => listener.event === event);
      },
      
      // 獲取元素的事件監聽器數量
      getElementCount: (element) => {
        console.log('DOM.events.utils.getElementCount called', { element });
        return DOM.events.getByElement(element).length;
      },
      
      // 獲取特定事件類型的監聽器數量
      getEventCount: (event) => {
        console.log('DOM.events.utils.getEventCount called', { event });
        return DOM.events.getAll().filter(listener => listener.event === event).length;
      },
      
      // 調試：輸出所有事件監聽器資訊
      debug: () => {
        console.log('DOM.events.utils.debug called');
        const allListeners = DOM.events.getAll();
        console.group('事件監聽器調試資訊');
        console.log('總數量:', allListeners.length);
        
        allListeners.forEach(listener => {
          console.log(`- ${listener.id}: ${listener.element.tagName}(${listener.element.id || 'no-id'}) -> ${listener.event}`);
        });
        
        console.groupEnd();
        return allListeners;
      }
    }
  },
  
  // 聊天功能管理工具
  chat: {
    // 聊天狀態管理
    state: {
      currentGiver: null,
      isActive: false,
      messageHistory: [],
      lastMessageTime: null,
      providedSchedules: []
    },
    
    // 聊天初始化
    init: (giver) => {
      console.log('DOM.chat.init called', { giver });
      
      // 使用 ChatStateManager 初始化聊天會話
      ChatStateManager.initChatSession(giver);
      
      // 更新對話框標題
      const modalTitle = DOM.chatElements.title();
      if (!modalTitle) {
        console.error('DOM.chat.init: 聊天對話框標題元素未找到');
        return;
      }
      
      const titleText = `邀請 Giver - ${giver.name || '未知用戶'} 協助諮詢`;
      console.log('DOM.chat.init: 設定對話框標題:', titleText);
      DOM.utils.setTextContent(modalTitle, titleText);
      
      // 重新設定聊天區域的初始狀態
      DOM.message.clearChat();
      
      // 開啟 modal，設定 backdrop 為 static
      const modalElement = DOM.chatElements.modal();
      const modal = new bootstrap.Modal(modalElement, {
        backdrop: 'static',
        keyboard: false
      });
      modal.show();
      
      // 設定聊天功能
      DOM.chat.setup();
    },
    
    // 設定聊天功能
    setup: () => {
      console.log('DOM.chat.setup called');
      // 清理舊的事件監聽器，但不結束聊天會話
      DOM.chat.cleanupEventListeners();
      
      // 重新獲取元素引用
      const chatInput = DOM.chatElements.input();
      const sendBtn = DOM.chatElements.sendBtn();
      
      // 設定 UI 控制項
      DOM.chat.setupUIControls();
      
      // 設定輸入控制項
      DOM.chat.setupInputControls(chatInput, sendBtn);
      
      // 設定模態框事件
      DOM.chat.setupModalEvents();
      
      // 聚焦到輸入框
      chatInput.focus();
    },
    
    // 設定 UI 控制項
    setupUIControls: () => {
      const modalHeader = DOM.chatElements.header();
      if (!modalHeader) {
        console.error('DOM.chat.setupUIControls: 聊天對話框標題區域未找到');
        return;
      }
      
      console.log('DOM.chat.setupUIControls: 設定聊天 UI 控制項');
      
      // 檢查是否已經有關閉按鈕，避免重複添加
      const existingCloseBtn = DOM.getElement('.btn-close-header');
      if (!existingCloseBtn) {
        // 創建關閉按鈕 - 使用 CSS 類別而非內聯樣式
        const closeBtn = DOM.createElement('button', 'btn-close-base btn-close-header', '<i class="fa-solid fa-xmark"></i>');
        
        // 點擊關閉按鈕時顯示確認對話框
        DOM.events.add(closeBtn, 'click', () => {
          console.log('DOM.chat.setupUIControls: 關閉按鈕被點擊');
          DOM.chat.showCloseConfirmation();
        });
        
        // 將關閉按鈕添加到 modal-header 的右側
        modalHeader.appendChild(closeBtn);
        
        console.log('DOM.chat.setupUIControls: 關閉按鈕已添加');
      } else {
        console.log('DOM.chat.setupUIControls: 關閉按鈕已存在，重新綁定事件監聽器');
        // 使用 cloneNode 來移除所有舊的事件監聽器
        const newCloseBtn = existingCloseBtn.cloneNode(true);
        existingCloseBtn.parentNode.replaceChild(newCloseBtn, existingCloseBtn);
        
        // 重新綁定事件監聽器
        DOM.events.add(newCloseBtn, 'click', () => {
          console.log('DOM.chat.setupUIControls: 關閉按鈕被點擊');
          DOM.chat.showCloseConfirmation();
        });
      }
      
      // 設定選項按鈕事件監聽器
      DOM.chat.setupOptionButtons();
    },
    
    // 處理預約時間選項
    handleScheduleOption: async () => {
      console.log('DOM.chat.handleScheduleOption called');
      // 顯示 Giver 已提供的時間選項
      await nonBlockingDelay(DELAY_TIMES.CHAT.OPTION_SELECT, () => {
        DOM.chat.showGiverAvailableTimes();
      });
    },
    
    // 處理暫不預約選項
    handleSkipOption: async () => {
      console.log('DOM.chat.handleSkipOption called：處理暫不預約選項');
      
      // 模擬 Giver 回覆
      await nonBlockingDelay(DELAY_TIMES.CHAT.RESPONSE, () => {
        const response = '好的，您選擇暫不預約 Giver 時間。<br><br>如未來有需要預約 Giver 時間，請使用聊天輸入區域下方的功能按鈕。<br><br>有其他問題需要協助嗎？';
        DOM.chat.addGiverResponse(response);
      });
    },
    
    // 顯示預約選項按鈕
    showScheduleOptions: () => {
      console.log('DOM.chat.showScheduleOptions called：顯示預約選項按鈕');
      
      // 將訊息與按鈕組合在同一個訊息框
      const scheduleOptionsHTML = TEMPLATES.chat.scheduleOptions();
      
      // 插入到聊天區域
      const chatMessages = DOM_CACHE.chatMessages;
      if (chatMessages) {
        chatMessages.insertAdjacentHTML('beforeend', scheduleOptionsHTML);
        // 綁定事件
        DOM.chat.setupScheduleOptionButtons();
        // 滾動到底部
        chatMessages.scrollTop = chatMessages.scrollHeight;
      }
    },
    
    // 顯示 Giver 已提供的時間選項
    showGiverAvailableTimes: () => {
      console.log('DOM.chat.showGiverAvailableTimes called：顯示 Giver 已提供的時間選項');
      
      // 將訊息與複選選項組合在同一個訊息框
      const giverAvailableTimesHTML = TEMPLATES.chat.giverAvailableTimesWithCheckboxes();
      
      // 插入到聊天區域
      const chatMessages = DOM_CACHE.chatMessages;
      if (chatMessages) {
        chatMessages.insertAdjacentHTML('beforeend', giverAvailableTimesHTML);
        // 綁定複選選項事件
        DOM.chat.setupCheckboxOptions();
        // 滾動到底部
        chatMessages.scrollTop = chatMessages.scrollHeight;
      }
    },

    // 顯示提供我的時間選項（3個按鈕）
    showProvideMyTimeOptions: () => {
      console.log('DOM.chat.showProvideMyTimeOptions called：顯示提供我的時間選項');
      
      // 將訊息與按鈕組合在同一個訊息框
      const provideMyTimeOptionsHTML = TEMPLATES.chat.provideMyTimeOptions();
      
      // 插入到聊天區域
      const chatMessages = DOM_CACHE.chatMessages;
      if (chatMessages) {
        chatMessages.insertAdjacentHTML('beforeend', provideMyTimeOptionsHTML);
        // 綁定事件
        DOM.chat.setupScheduleOptionButtons();
        // 滾動到底部
        chatMessages.scrollTop = chatMessages.scrollHeight;
      }
    },
    
    // 設定聊天輸入區域的額外功能按鈕事件監聽器
    setupChatExtraButtons: () => {
      console.log('DOM.chat.setupChatExtraButtons called：設定聊天輸入區域的額外功能按鈕');
      const extraButtons = document.querySelectorAll('.chat-extra-buttons .btn[data-option]');
      
      extraButtons.forEach(button => {
        // 先移除舊的事件監聽器，避免重複綁定
        const newBtn = button.cloneNode(true);
        button.parentNode.replaceChild(newBtn, button);
        
        // 重新綁定事件監聽器
        DOM.events.add(newBtn, 'click', (e) => {
          e.preventDefault();
          e.stopPropagation();
          
          const option = newBtn.getAttribute('data-option');
          const optionText = newBtn.textContent.trim();
          console.log('聊天額外功能按鈕被點擊:', { option, optionText });
          
          // 添加使用者選擇的訊息
          DOM.chat.addUserMessage(optionText);
          
          // 處理不同的選項
          switch (option) {
            case 'view-giver-times':
              DOM.chat.handleViewTimes();
              break;
            case 'view-my-booked-times':
              DOM.chat.handleViewMyBookedTimes();
              break;
            case 'provide-single-time':
              DOM.chat.handleSingleTime();
              break;
            case 'provide-multiple-times':
              DOM.chat.handleMultipleTimes();
              break;
            case 'view-my-times':
              DOM.chat.handleViewAllSchedules();
              break;
            default:
              console.warn('未知的聊天額外功能選項:', option);
          }
        });
      });
    },

    // 設定預約選項按鈕事件監聽器
    setupScheduleOptionButtons: () => {
      console.log('DOM.chat.setupScheduleOptionButtons called：設定預約選項按鈕');
      const scheduleOptionButtons = document.querySelectorAll('.chat-option-btn[data-option]');
      
      scheduleOptionButtons.forEach(button => {
        const newBtn = button.cloneNode(true);
        button.parentNode.replaceChild(newBtn, button);
        
        // 再綁定新的事件監聽器
        DOM.events.add(newBtn, 'click', (e) => {
          e.preventDefault();
          e.stopPropagation();
          
          const option = newBtn.getAttribute('data-option');
          const optionText = newBtn.textContent.trim();
          console.log('預約選項按鈕被點擊:', { option, optionText });
          
          // 添加使用者選擇的訊息
          DOM.chat.addUserMessage(optionText);
          
          // 處理不同的選項
          switch (option) {
            case 'view-times':
              DOM.chat.handleViewTimes();
              break;
            case 'single-time':
              DOM.chat.handleSingleTime();
              break;
            case 'multiple-times':
              DOM.chat.handleMultipleTimes();
              break;
            case 'view-all':
              DOM.chat.handleViewAllSchedules();
              break;
            case 'cancel':
              DOM.chat.handleCancelSchedule();
              break;
            case 'submit-schedules':
              // 使用 EventManager 處理 submit-schedules 按鈕
              EventManager.handleOptionButton(newBtn, e);
              break;
            default:
              console.warn('未知的預約選項:', option);
          }
          
          // 禁用整個 Giver 訊息泡泡中的互動元素
          DOM.chat.disableGiverMessageInteractions(newBtn);
        });
      });
    },
    
    // 設定複選選項事件監聽器
    setupCheckboxOptions: () => {
      console.log('DOM.chat.setupCheckboxOptions called：設定複選選項');
      
      const checkboxes = document.querySelectorAll('.chat-checkbox-options input[type="checkbox"]');
      const confirmBtn = document.getElementById('confirm-selection-btn');
      
      // 為每個複選框添加事件監聽器
      checkboxes.forEach(checkbox => {
        DOM.events.add(checkbox, 'change', (e) => {
          console.log('複選框狀態改變:', { 
            id: checkbox.id, 
            option: checkbox.getAttribute('data-option'), 
            checked: checkbox.checked 
          });
          
          // 處理互斥選擇邏輯
          DOM.chat.handleMutualExclusion(checkbox);
          
          // 更新確認按鈕狀態
          DOM.chat.updateConfirmButtonState();
        });
      });
      
              // 為確認按鈕添加事件監聽器
        if (confirmBtn) {
          DOM.events.add(confirmBtn, 'click', async (e) => {
            e.preventDefault();
            e.stopPropagation();
            
            console.log('確認選擇按鈕被點擊');
            
            try {
              // 獲取選中的選項
              const selectedOptions = DOM.chat.getSelectedCheckboxOptions();
              console.log('選中的選項:', selectedOptions);
              
              // 處理選中的選項
              await DOM.chat.handleSelectedOptions(selectedOptions);
              
              // 禁用整個 Giver 訊息泡泡中的互動元素
              DOM.chat.disableGiverMessageInteractions(confirmBtn);
            } catch (error) {
              console.error('確認選擇按鈕處理時發生錯誤:', error);
            }
          });
        }
    },

    // 設定預約成功表格按鈕事件監聽器
    setupReservationTableButtons: () => {
      console.log('DOM.chat.setupReservationTableButtons called：設定預約成功表格按鈕');
      
      // 綁定取消預約時段按鈕
      const cancelReservationBtns = document.querySelectorAll('.cancel-reservation-btn');
      cancelReservationBtns.forEach(btn => {
        DOM.events.add(btn, 'click', (e) => {
          e.preventDefault();
          e.stopPropagation();
          
          const option = btn.getAttribute('data-option');
          console.log('取消預約時段按鈕被點擊:', { option });
          
          // 處理取消預約時段
          DOM.chat.handleCancelReservationTime(option, btn);
        });
      });
      
      // 綁定確認完畢和取消全部按鈕
      const confirmAllBtn = document.querySelector('[data-option="confirm-all"]');
      const cancelAllBtn = document.querySelector('[data-option="cancel-all"]');
      
      if (confirmAllBtn) {
        DOM.events.add(confirmAllBtn, 'click', (e) => {
          e.preventDefault();
          e.stopPropagation();
          
          console.log('確認完畢按鈕被點擊');
          DOM.chat.handleConfirmAllReservations();
        });
      }
      
      if (cancelAllBtn) {
        DOM.events.add(cancelAllBtn, 'click', (e) => {
          e.preventDefault();
          e.stopPropagation();
          
          console.log('取消全部預約按鈕被點擊');
          DOM.chat.handleCancelAllReservations();
        });
      }
    },

    // 取消預約時段
    handleCancelReservationTime: (option, button) => {
      console.log('DOM.chat.handleCancelReservationTime called：取消預約時段', { option });
      
      // 獲取時段名稱：根據 option 的值，設定 timeSlot 的值
      let timeSlot = '';
      if (option === 'demo-time-1') {
        timeSlot = getDemoTimeLabel('demo-time-1');
      } else if (option === 'demo-time-2') {
        timeSlot = getDemoTimeLabel('demo-time-2');
      } else if (option === 'provide-my-time') {
        timeSlot = `${CONFIG.UI_TEXT.BUTTONS.PROVIDE_MY_TIME}`;
      }
      
      // 跳出確認 modal：使用 UIComponents.confirmDialog 函式，顯示一個確認對話框，讓使用者可以確認是否取消預約。
      UIComponents.confirmDialog({
        title: '確認取消預約',
        message: `確定取消預約以下時段嗎？${timeSlot}`,
        confirmText: '取消預約',
        cancelText: '保留',
        onConfirm: () => {
          // 使用者確認取消預約
          console.log('使用者確認取消預約:', timeSlot);
          
          // 從 ChatStateManager 中移除被取消的預約時段
          const bookedSchedules = ChatStateManager.getBookedSchedules();
          const updatedBookedSchedules = bookedSchedules.filter(schedule => schedule.option !== option);
          ChatStateManager.set(ChatStateManager.CONFIG.STATE_KEYS.BOOKED_SCHEDULES, updatedBookedSchedules);
          console.log('DOM.chat.handleCancelReservationTime: 已從 ChatStateManager 移除預約時段', { option, remainingCount: updatedBookedSchedules.length });
          
          // 添加使用者訊息
          DOM.chat.addUserMessage(`您選擇取消：${timeSlot}`);
                    
          // 從 DOM 移除該行：只移除被取消的那一列，不會影響到其他列
          const tableRow = button.closest('tr'); // 獲取該按鈕所在的行：從當前元素（在這裡是 button 元素）開始，向上遍歷它的父元素，直到找到第一個 class 為 'tr' 的元素
          if (tableRow) {
            tableRow.remove();
          }

          // 取得最新的所有預約行（這時候畫面上只剩下還沒被取消的）
          const allRows = document.querySelectorAll('.reservation-success-table tbody tr, .reservation-table tbody tr');
          console.log('移除 tr 後，allRows:', allRows, allRows.length);

          // 先移除所有舊的表格訊息泡泡（.table-responsive.mt-2 外層的父元素：整個訊息泡泡）
          document.querySelectorAll('.table-responsive.mt-2').forEach(tableDiv => {
            if (tableDiv.parentElement) tableDiv.parentElement.remove(); 
          });

          if (allRows.length === 0) {
            // 如果沒有其他預約，顯示取消訊息
            DOM.chat.addGiverResponse('您已取消所有預約時段。<br><br>如果仍想預約 Giver 時間，請使用聊天輸入區域下方的功能按鈕。');
          } else {
            // 如果還有其他預約，直接使用現存的行（allRows），顯示取消成功訊息泡泡
            DOM.chat.addCancelSuccessMessage(allRows);
          }
        },
        onCancel: () => {
          // 使用者選擇保留，不做任何動作
          console.log('使用者選擇保留預約:', timeSlot);
        }
      });
    },

    // 在聊天對話框最下方新增一個新的訊息泡泡，顯示取消成功和剩餘的預約時段
    addCancelSuccessMessage: (visibleRows) => {
      console.log('DOM.chat.addCancelSuccessMessage called：新增取消成功訊息泡泡', { visibleRowsCount: visibleRows.length });
      
      // 從 ChatStateManager 獲取剩餘的預約時段
      const remainingBookedSchedules = ChatStateManager.getBookedSchedules();
      console.log('DOM.chat.addCancelSuccessMessage: 剩餘的預約時段', remainingBookedSchedules);
      
      if (remainingBookedSchedules.length === 0) {
        // 如果沒有剩餘時段，不生成任何訊息泡泡
        DOM.chat.addGiverResponse('您已取消所有預約時段。<br><br>如果仍想預約 Giver 時間，請使用聊天輸入區域下方的功能按鈕。');
        return;
      }
      
      // 將 ChatStateManager 中的資料轉換為模板需要的格式
      const remainingOptions = remainingBookedSchedules.map(schedule => ({
        option: schedule.option,
        label: schedule.timeSlot
      }));
      
      // 生成取消成功訊息泡泡 HTML
      const cancelSuccessHTML = TEMPLATES.chat.cancelSuccessMessageAndTable(remainingOptions);
        // 在聊天對話框最下方插入新的訊息泡泡
        const chatMessages = DOM_CACHE.chatMessages;
        if (chatMessages) {
          chatMessages.insertAdjacentHTML('beforeend', cancelSuccessHTML);
        // 綁定新的表格按鈕事件
        DOM.chat.setupReservationTableButtons();
        // 滾動到底部
        chatMessages.scrollTop = chatMessages.scrollHeight;
      }
    },

    // 處理確認完畢所有預約
    handleConfirmAllReservations: async () => {
      console.log('DOM.chat.handleConfirmAllReservations called：處理確認完畢所有預約');
      
      DOM.chat.addUserMessage('確認完畢，請協助送出給 Giver');
      
      await nonBlockingDelay(DELAY_TIMES.CHAT.RESPONSE, () => {
        const response = CONFIG.UI_TEXT.RESERVATION_SUCCESS.TEXT;
        DOM.chat.addGiverResponse(response);
      });
    },

    // 處理取消全部預約
    handleCancelAllReservations: () => {
      console.log('DOM.chat.handleCancelAllReservations called：處理取消全部預約');
      
      // 清空 ChatStateManager 中的預約時段
      ChatStateManager.clearBookedSchedules();
      console.log('DOM.chat.handleCancelAllReservations: 已清空所有預約時段');
      
      DOM.chat.handleCancelSchedule();
    },

    // 處理取消表單
    handleCancelScheduleForm: async (e) => {
      e.preventDefault();
      e.stopPropagation();
      
      
      // 隱藏表單
      const scheduleForm = document.getElementById('schedule-form');
      if (scheduleForm) {
        scheduleForm.classList.remove('schedule-form-visible');
        scheduleForm.classList.add('schedule-form-hidden');
      }
      
      // 添加使用者訊息
      DOM.chat.addUserMessage('取消提供時段');
      
      // 顯示取消訊息
      await nonBlockingDelay(DELAY_TIMES.CHAT.RESPONSE, () => {
        DOM.chat.addGiverResponse('已取消提供時段。<br><br>如果仍想預約 Giver 時間，請使用聊天輸入區域下方的功能按鈕。');
      });
    },  

    // 禁用整個 Giver 訊息泡泡中的互動元素
    disableGiverMessageInteractions: (button) => {
      console.log('DOM.chat.disableGiverMessageInteractions called：禁用 Giver 訊息泡泡中的互動元素');
      
      // 找到包含該按鈕的 Giver 訊息泡泡
      const giverMessage = button.closest('.giver-message');
      if (!giverMessage) {
        console.warn('DOM.chat.disableGiverMessageInteractions: 找不到 Giver 訊息泡泡');
        return;
      }
      
      // 定義需要禁用的元素類型和樣式
      const elementsToDisable = [
        { selector: 'input[type="checkbox"]', type: 'checkbox' },
        { selector: 'button', type: 'button' },
        { selector: 'label', type: 'label' }
      ];
      
      // 統一的禁用樣式設定
      const disableStyles = {
        pointerEvents: 'none',
        opacity: '0.6'
      };
      
      // 通用函數：禁用單個元素
      const disableElement = (element, elementType) => {
        console.log(`DOM.chat.disableGiverMessageInteractions: 禁用 ${elementType} 元素`, { element });
        
        // 設定禁用狀態（適用於表單元素）
        if (element.disabled !== undefined) {
          element.disabled = true;
        }
        
        // 應用統一的禁用樣式
        Object.assign(element.style, disableStyles);
      };
      
      // 遍歷所有需要禁用的元素類型
      elementsToDisable.forEach(({ selector, type }) => {
        const elements = giverMessage.querySelectorAll(selector);
        console.log(`DOM.chat.disableGiverMessageInteractions: 找到 ${elements.length} 個 ${type} 元素`);
        
        elements.forEach(element => {
          disableElement(element, type);
        });
      });
      
      console.log('DOM.chat.disableGiverMessageInteractions: 已禁用 Giver 訊息泡泡中的所有互動元素');
    },

    // 更新確認按鈕狀態
    updateConfirmButtonState: () => {
      const checkboxes = document.querySelectorAll('.chat-checkbox-options input[type="checkbox"]:not(:disabled)');
      const confirmBtn = document.getElementById('confirm-selection-btn');

      if (confirmBtn) {
        const hasSelection = Array.from(checkboxes).some(checkbox => checkbox.checked);
        confirmBtn.disabled = !hasSelection;
        
        // 確認按鈕一直保持橘色背景，只根據是否有選項來啟用/禁用
        confirmBtn.classList.remove('btn-secondary');
        confirmBtn.classList.add('btn-orange');
      }
    },

    // 獲取選中的複選框選項
    getSelectedCheckboxOptions: () => {
      const checkboxes = document.querySelectorAll('.chat-checkbox-options input[type="checkbox"]:checked:not(:disabled)');
      const selectedOptions = [];
      
      checkboxes.forEach(checkbox => {
        const option = checkbox.getAttribute('data-option');
        const label = checkbox.nextElementSibling.textContent.trim();
        selectedOptions.push({ option, label });
      });
      
      return selectedOptions;
    },

    // 處理選中的選項
    handleSelectedOptions: async (selectedOptions) => {
      console.log('DOM.chat.handleSelectedOptions called：處理選中的選項', selectedOptions);
      
      try {
        // 添加使用者選擇的訊息
        const selectedText = selectedOptions.map(option => option.label).join('、');
        DOM.chat.addUserMessage(`您選擇：${selectedText}`);
        
        // 分析選項組合並決定處理策略
        const optionAnalysis = DOM.chat.analyzeSelectedOptions(selectedOptions);
        console.log('DOM.chat.handleSelectedOptions: 選項分析結果', optionAnalysis);
        
        // 使用 switch-case 結構處理不同的選項組合
        switch (optionAnalysis.strategy) {
          case 'cancel':
            console.log('DOM.chat.handleSelectedOptions: 處理取消選項');
            await DOM.chat.handleCancelSchedule();
            break;
            
          case 'demo_with_provide':
            console.log('DOM.chat.handleSelectedOptions: 處理 Demo 時間 + 提供我的時間選項');
            await DOM.chat.handleMultipleDemoTimeSelection(optionAnalysis.demoTimeOptions, optionAnalysis.provideMyTimeOption);
            break;
            
          case 'demo_only':
            console.log('DOM.chat.handleSelectedOptions: 處理僅 Demo 時間選項');
            await DOM.chat.handleMultipleDemoTimeSelection(optionAnalysis.demoTimeOptions, null);
            break;
            
          case 'provide_only':
            console.log('DOM.chat.handleSelectedOptions: 處理僅提供我的時間選項');
            await DOM.chat.handleProvideMyTime();
            break;
            
          case 'unknown':
            console.warn('DOM.chat.handleSelectedOptions: 處理未知選項組合');
            selectedOptions.forEach(selectedOption => {
              console.warn('未知的選項:', selectedOption.option);
            });
            break;
            
          default:
            console.error('DOM.chat.handleSelectedOptions: 未定義的處理策略', optionAnalysis.strategy);
            break;
        }
        
        console.log('DOM.chat.handleSelectedOptions: 選項處理完成');
      } catch (error) {
        console.error('DOM.chat.handleSelectedOptions: 處理選項時發生錯誤', error);
        // 可以在這裡添加錯誤處理邏輯，例如顯示錯誤訊息給使用者
      }
    },
    
    // 分析選中的選項並決定處理策略
    analyzeSelectedOptions: (selectedOptions) => {
      console.log('DOM.chat.analyzeSelectedOptions called：分析選中的選項', selectedOptions);
      
      // 分類選中的選項
      const demoTimeOptions = selectedOptions.filter(option => 
        option.option === 'demo-time-1' || option.option === 'demo-time-2'
      );
      const provideMyTimeOption = selectedOptions.find(option => 
        option.option === 'provide-my-time'
      );
      const cancelOption = selectedOptions.find(option => 
        option.option === 'cancel'
      );
      
      // 決定處理策略
      let strategy = 'unknown';
      
      if (cancelOption) {
        strategy = 'cancel';
      } else if (demoTimeOptions.length > 0 && provideMyTimeOption) {
        strategy = 'demo_with_provide';
      } else if (demoTimeOptions.length > 0) {
        strategy = 'demo_only';
      } else if (provideMyTimeOption) {
        strategy = 'provide_only';
      }
      
      const analysis = {
        strategy,
        demoTimeOptions,
        provideMyTimeOption,
        cancelOption,
        totalOptions: selectedOptions.length
      };
      
      console.log('DOM.chat.analyzeSelectedOptions: 分析完成', analysis);
      return analysis;
    },

    // 處理 Demo 時間選擇
    handleDemoTimeSelection: async (timeSlot) => {
      console.log('DOM.chat.handleDemoTimeSelection called：處理 Demo 時間選擇', timeSlot);
      await nonBlockingDelay(DELAY_TIMES.CHAT.RESPONSE, () => {  
        const response = `您已成功預約 ${timeSlot}。<br><br>Giver 將在 24 小時內確認您的預約，請留意通知。<br><br>有其他問題需要協助嗎？`;
        DOM.chat.addGiverResponse(response);
      });
    },

    // 處理提供我的時間選項
    handleProvideMyTime: async () => {
      console.log('DOM.chat.handleProvideMyTime called：處理提供我的時間選項');
      await nonBlockingDelay(DELAY_TIMES.CHAT.RESPONSE, () => {
        // 顯示提供我的時間選項（3個按鈕）
        DOM.chat.showProvideMyTimeOptions();
      });
    },
    
    // 處理多個 Demo 時間選項
    handleMultipleDemoTimeSelection: async (demoTimeOptions, provideMyTimeOption) => {
      console.log('DOM.chat.handleMultipleDemoTimeSelection called：處理多個 Demo 時間選項', { demoTimeOptions, provideMyTimeOption });
      
      // 將預約資料儲存到 ChatStateManager
      const bookedSchedules = [];
      
      // 處理 Demo 時間選項
      demoTimeOptions.forEach(option => {
        const timeSlot = getDemoTimeLabel(option.option);
        
        bookedSchedules.push({
          type: 'demo',
          option: option.option,
          timeSlot: timeSlot,
          status: CONFIG.UI_TEXT.STATUS.TAKER_VIEW.PENDING
        });
      });
      
      // 處理提供我的時間選項
      if (provideMyTimeOption) {
        bookedSchedules.push({
          type: 'provide-my-time',
          option: 'provide-my-time',
          timeSlot: `${CONFIG.UI_TEXT.BUTTONS.PROVIDE_MY_TIME}`,
          status: CONFIG.UI_TEXT.STATUS.TAKER_VIEW.PENDING
        });
      }
      
      // 儲存預約資料
      ChatStateManager.addBookedSchedules(bookedSchedules);
      
      await nonBlockingDelay(DELAY_TIMES.CHAT.RESPONSE, () => {
        // 顯示預約成功訊息和表格
        const reservationSuccessHTML = TEMPLATES.chat.reservationSuccessMessageAndTable(demoTimeOptions, provideMyTimeOption);
        const chatMessages = DOM_CACHE.chatMessages;
        if (chatMessages) {
          chatMessages.insertAdjacentHTML('beforeend', reservationSuccessHTML);
          // 綁定表格按鈕事件
          DOM.chat.setupReservationTableButtons();
          // 滾動到底部
          chatMessages.scrollTop = chatMessages.scrollHeight;
        }
      });
    },
    
    // 處理查看時間選項
    handleViewTimes: async () => {
      console.log('DOM.chat.handleViewTimes called：處理查看時間選項');
      await delay(DELAY_TIMES.CHAT.RESPONSE);
      // 使用新的模板顯示「Giver 尚末提供提供方便的時間」訊息和按鈕
      const noGiverTimesHTML = TEMPLATES.chat.noGiverTimesWithButtons();
      const chatMessages = DOM_CACHE.chatMessages;
      if (chatMessages) {
        chatMessages.insertAdjacentHTML('beforeend', noGiverTimesHTML);
        // 綁定按鈕事件
        DOM.chat.setupScheduleOptionButtons();
        // 滾動到底部
        chatMessages.scrollTop = chatMessages.scrollHeight;
      }
    },
    
    // 處理查看我已預約的時間選項
    handleViewMyBookedTimes: async () => {
      console.log('DOM.chat.handleViewMyBookedTimes called：處理查看我已預約的時間選項');
      
      // 檢查是否有已預約的時間
      const bookedSchedules = ChatStateManager.getBookedSchedules();
      console.log('DOM.chat.handleViewMyBookedTimes: 已預約的時段', bookedSchedules);
      
      await delay(DELAY_TIMES.CHAT.RESPONSE);
      const chatMessages = DOM_CACHE.chatMessages;
      if (chatMessages) {
        if (bookedSchedules.length > 0) {
          // 有預約時段，顯示預約成功訊息和表格
          const bookedTimesHTML = TEMPLATES.chat.bookedTimesMessageAndTable(bookedSchedules);
          chatMessages.insertAdjacentHTML('beforeend', bookedTimesHTML);
          // 綁定表格按鈕事件
          DOM.chat.setupReservationTableButtons();
        } else {
          // 沒有預約時段，顯示「您目前還沒有預約任何 Giver 時間」訊息和按鈕
          const noBookedTimesHTML = TEMPLATES.chat.noBookedTimesWithButtons();
          chatMessages.insertAdjacentHTML('beforeend', noBookedTimesHTML);
          // 綁定按鈕事件
          DOM.chat.setupScheduleOptionButtons();
        }
        // 滾動到底部
        chatMessages.scrollTop = chatMessages.scrollHeight;
      }
    },
    
    // 處理單筆時段選項
    handleSingleTime: async (editIndex = null, editData = null) => {
      console.log('DOM.chat.handleSingleTime called：處理單筆時段選項', { editIndex, editData });

      // 處理參數格式：如果 editIndex 是數字，editData 是物件，則調整參數順序
      if (typeof editIndex === 'number' && editData && typeof editData === 'object' && editData.date) {
        // 這是新的呼叫格式：handleSingleTime(idx, editData)
        const actualEditIndex = editIndex;
        const actualEditData = editData;
        editIndex = actualEditIndex;
        editData = actualEditData;
        console.log('DOM.chat.handleSingleTime: 調整參數格式', { editIndex, editData });
      }
      await nonBlockingDelay(100, () => {
        console.log('DOM.chat.handleSingleTime: setTimeout 開始執行');
        // 顯示表單
        let scheduleForm = DOM_CACHE.scheduleForm;
        console.log('DOM.chat.handleSingleTime: 檢查現有表單', { scheduleForm });
        if (!scheduleForm) {
          console.log('DOM.chat.handleSingleTime: 沒有現有表單，準備動態創建');
          // 動態創建
          const chatMessages = DOM_CACHE.chatMessages;
          if (chatMessages) {
            console.log('DOM.chat.handleSingleTime: 找到 chat-messages，插入表單');
            const formHTML = TEMPLATES.chat.scheduleForm();
            chatMessages.insertAdjacentHTML('beforeend', formHTML);
            DOM_CACHE.resetScheduleForm(); // 重設快取
            scheduleForm = DOM_CACHE.scheduleForm;
            console.log('DOM.chat.handleSingleTime: 表單已創建', { scheduleForm });
          }
        }
        if (scheduleForm) {
          console.log('DOM.chat.handleSingleTime: 表單存在，開始設定');
          // 將表單移動到聊天記錄的最下方
          const chatMessages = DOM_CACHE.chatMessages;
          if (chatMessages) {
            chatMessages.appendChild(scheduleForm);
            console.log('DOM.chat.handleSingleTime: 表單已移動到底部');
          }
          // 初始化表單欄位事件（日期欄位可點擊彈出日曆 modal）
          const formElement = DOM_CACHE.timeScheduleForm;
          if (formElement) {
            console.log('DOM.chat.handleSingleTime: 初始化表單欄位');
            initScheduleFormInputs(formElement);
            // 清空所有錯誤訊息
            FormValidator.clearAllValidationErrors(formElement);
          }
          scheduleForm.classList.remove('schedule-form-hidden');
          scheduleForm.classList.add('schedule-form-visible');
          console.log('DOM.chat.handleSingleTime: 表單樣式已設定');
               
          // 帶入編輯資料
          const inputs = DOM_CACHE.getFormInputs();
          if (editData) {
            console.log('DOM.chat.handleSingleTime: 編輯模式，設定編輯資料', editData);
            
            // 使用通用設定器設定編輯資料
            const editConfigs = {
              dateInput: { defaultValue: editData.date },
              startTimeInput: { defaultValue: editData.startTime },
              endTimeInput: { defaultValue: editData.endTime },
              notesInput: { defaultValue: editData.notes || '' }
            };
            
            Object.entries(editConfigs).forEach(([key, config]) => {
              if (inputs[key]) {
                setupInputField(inputs[key], config);
              }
            });
          } else {
            console.log('DOM.chat.handleSingleTime: 新增模式，設定預設值');
            
            // 使用通用設定器設定預設值
            const defaultConfigs = {
              startTimeInput: { defaultValue: '' },
              endTimeInput: { defaultValue: '' },
              dateInput: { defaultValue: DateUtils.getNextWeekFormatted() },
              notesInput: { defaultValue: '' }
            };
            
            Object.entries(defaultConfigs).forEach(([key, config]) => {
              if (inputs[key]) {
                setupInputField(inputs[key], config);
              }
            });
          }
          // 設定表單事件
          console.log('DOM.chat.handleSingleTime: 設定表單事件');
          DOM.chat.setupScheduleForm(editIndex, editData);
                    
          // 滾動到底部
          if (chatMessages) {
            chatMessages.scrollTop = chatMessages.scrollHeight;
            console.log('DOM.chat.handleSingleTime: 已滾動到底部');
          }
          console.log('DOM.chat.handleSingleTime: 處理完成');
        } else {
          console.error('DOM.chat.handleSingleTime: 無法找到或創建表單');
        }
      }, 100);
    },
    
    // 設定表單事件
    setupScheduleForm: (editIndex = null, editData = null) => {
      const form = DOM_CACHE.timeScheduleForm;
      if (form) {
        // 設定編輯索引（用於事件委派處理）
        form.setAttribute('data-edit-index', editIndex);
        
        // 設定是否為草稿編輯
        if (editData && editData.isDraft) {
          form.setAttribute('data-edit-is-draft', 'true');
          console.log('DOM.chat.setupScheduleForm: 設定為草稿編輯模式');
        } else {
          form.setAttribute('data-edit-is-draft', 'false');
          console.log('DOM.chat.setupScheduleForm: 設定為正式提供編輯模式');
        }
        
        // 表單提交事件由 EventManager 統一處理
        // 取消按鈕事件也由 EventManager 統一處理
      }
    },
    
    // 顯示日期選擇器
    showDatePicker: () => {
      console.log('DOM.chat.showDatePicker called：顯示日期選擇器');
      
      // 防止重複調用
      if (DOM.chat._isShowingDatePicker) {
        console.log('DOM.chat.showDatePicker: 日期選擇器正在顯示中，跳過重複調用');
        return;
      }
      DOM.chat._isShowingDatePicker = true;
      
      // 強制清理殘留的 backdrop 和 body 狀態
      ModalCleanupUtils.quickCleanup();
      
      // 清除任何現有的錯誤訊息
      DOM.chat.clearDatePickerError();
      
      // 初始化日期選擇器
      DOM.chat.initDatePicker();
      
      // 查找 Modal 元素
      const datePickerModalElement = DOM_CACHE.datePickerModal;
      console.log('DOM.chat.showDatePicker: 查找日期選擇器 Modal', { datePickerModalElement });
      
      if (datePickerModalElement) {
        try {
          // 移除舊的事件監聽器
          datePickerModalElement.removeEventListener('shown.bs.modal', DOM.chat._onModalShown);
          datePickerModalElement.removeEventListener('hidden.bs.modal', DOM.chat._onModalHidden);
          
          // 顯示 Modal
          const datePickerModal = new bootstrap.Modal(datePickerModalElement, {
            backdrop: 'static',
            keyboard: false
          });
          console.log('DOM.chat.showDatePicker: 創建 Bootstrap Modal 實例', { datePickerModal });
          
          datePickerModal.show();
          console.log('DOM.chat.showDatePicker: Modal 顯示指令已執行');
          
          // 添加顯示完成的事件監聽器
          DOM.chat._onModalShown = () => {
            console.log('DOM.chat.showDatePicker: Modal 已完全顯示');
            // 重置標記，允許下次調用
            DOM.chat._isShowingDatePicker = false;
          };
          DOM.events.add(datePickerModalElement, 'shown.bs.modal', DOM.chat._onModalShown);
          
          // 添加隱藏完成的事件監聽器
          DOM.chat._onModalHidden = () => {
            console.log('DOM.chat.showDatePicker: Modal 已隱藏');
            
            // 清除錯誤訊息
            DOM.chat.clearDatePickerError();
            
            // 檢查是否是因為取消而關閉（沒有選擇日期）
            const dateInput = DOM_CACHE.dateInput;
            const hasSelectedDate = dateInput && dateInput.value.trim() !== '';
            
            if (!hasSelectedDate) {
              console.log('DOM.chat.showDatePicker: 檢測到取消操作，顯示系統訊息');
              // 延遲顯示系統訊息，確保 Modal 完全關閉
              setTimeout(() => {
                DOM.chat.addGiverResponse('您已取消提供單筆方便時段。<br><br>如果仍想提供方便時段，請使用聊天輸入區域下方的功能按鈕。');
              }, 300);
            }
            
            // 重置標記，允許下次調用
            DOM.chat._isShowingDatePicker = false;
            // 重置日期選擇器快取
            DOM_CACHE.resetDatePicker();
          };
          DOM.events.add(datePickerModalElement, 'hidden.bs.modal', DOM.chat._onModalHidden);
          
        } catch (error) {
          console.error('DOM.chat.showDatePicker: 顯示 Modal 時發生錯誤', error);
          
          // 備案：直接設定 Modal 為顯示狀態
          datePickerModalElement.classList.add('show');
          datePickerModalElement.style.display = 'block';
          document.body.classList.add('modal-open');
          
          // 添加 backdrop（靜態，不允許點擊關閉）
          const backdrop = document.createElement('div');
          backdrop.className = 'modal-backdrop fade show';
          backdrop.style.pointerEvents = 'none'; // 防止點擊 backdrop 關閉 modal
          document.body.appendChild(backdrop);
          
          console.log('DOM.chat.showDatePicker: 使用備案方式顯示 Modal');
          // 重置標記
          DOM.chat._isShowingDatePicker = false;
        }
      } else {
        console.error('DOM.chat.showDatePicker: 找不到日期選擇器 Modal 元素');
        // 重置標記
        DOM.chat._isShowingDatePicker = false;
      }
    },
    
    // 初始化日期選擇器
    initDatePicker: () => {
      console.log('DOM.chat.initDatePicker called：初始化日期選擇器');
      
      // 清除任何現有的錯誤訊息
      DOM.chat.clearDatePickerError();
      
      // 每次初始化都從當前日期開始，確保不會保留上次的狀態
      const currentDate = new Date();
      let currentMonth = currentDate.getMonth();
      let currentYear = currentDate.getFullYear();
      
      console.log('DOM.chat.initDatePicker: 重置為當前日期', { 
        currentMonth, 
        currentYear, 
        currentDate: currentDate.toDateString() 
      });
      
      // 設定關閉按鈕事件
      const closeBtn = document.getElementById('date-picker-close-btn');
      if (closeBtn) {
        // 移除舊的事件監聽器
        const newCloseBtn = closeBtn.cloneNode(true);
        if (closeBtn.parentNode) {
          closeBtn.parentNode.replaceChild(newCloseBtn, closeBtn);
        }
        DOM.events.add(newCloseBtn, 'click', () => {
          console.log('DOM.chat.initDatePicker: 關閉按鈕被點擊');
          const datePickerModal = bootstrap.Modal.getInstance(document.getElementById('date-picker-modal'));
          if (datePickerModal) {
            datePickerModal.hide();
          }
          // 強制清理 backdrop 和 body 狀態
          ModalCleanupUtils.delayedCleanup(200);
          // 重置日期選擇器快取，確保下次開啟時從當前月份開始
          setTimeout(() => {
            DOM_CACHE.resetDatePicker();
          }, 200);
        });
      }
      
      // 更新日期選擇器的月份年份顯示（內部函式）
      const updateMonthYear = () => {
        console.log('DOM.chat.initDatePicker: 更新月份年份顯示');
        const monthYearElement = DOM_CACHE.currentMonthYear;
        if (monthYearElement) {
                  monthYearElement.textContent = `${CONFIG.DATE_PICKER.MONTH_NAMES[currentMonth]} ${currentYear}`;
        }
      };
      
      // 生成日期選擇器的日曆內容（內部函式）
      const generateCalendar = () => {
        console.log('DOM.chat.initDatePicker: 生成日曆');
        const calendarElement = DOM_CACHE.datePickerCalendar;
        if (!calendarElement) return;
        
        calendarElement.innerHTML = '';
        
        const firstDay = new Date(currentYear, currentMonth, 1);
        const lastDay = new Date(currentYear, currentMonth + 1, 0);
        const startDate = new Date(firstDay);
        startDate.setDate(startDate.getDate() - firstDay.getDay());
        
        const today = new Date();
        const selectedDate = ChatStateManager.getSelectedDate();
        
        for (let i = 0; i < CONFIG.DATE_PICKER.CALENDAR.TOTAL_CELLS; i++) {
          const date = new Date(startDate);
          date.setDate(startDate.getDate() + i);
          
          const dateCell = document.createElement('div');
          dateCell.className = 'date-cell';
          dateCell.textContent = date.getDate();
          
          // 檢查是否為今天
          if (date.toDateString() === today.toDateString()) {
            dateCell.classList.add('today');
          }
          
          // 檢查是否為選中的日期
          if (selectedDate && date.toDateString() === selectedDate.toDateString()) {
            dateCell.classList.add('selected');
          }
          
          // 檢查是否為其他月份的日期
          if (date.getMonth() !== currentMonth) {
            dateCell.classList.add('other-month');
          }
          
          // 檢查是否為過去的日期
          if (date < today && date.toDateString() !== today.toDateString()) {
            dateCell.classList.add('disabled');
          } else {
            // 為所有非過去的日期添加點擊事件（包括超過3個月的日期）
            DOM.events.add(dateCell, 'click', () => {
              console.log('DOM.chat.initDatePicker: 日期被點擊', date);
              
              // 立即驗證選擇的日期
              if (!DateUtils.validateDateWithinAllowedMonths(date, false)) {
                // 驗證失敗，在日期選擇器 modal 內部顯示錯誤訊息
                DOM.chat.showDatePickerError(FormValidator.ERROR_MESSAGES.SCHEDULE_FORM.DATE_TOO_FAR);
                return; // 不設定日期，不關閉 modal，讓使用者重新選擇
              }
              
              // 移除其他選中的日期
              document.querySelectorAll('.date-cell.selected').forEach(cell => {
                cell.classList.remove('selected');
              });
              // 選中當前日期
              dateCell.classList.add('selected');
              ChatStateManager.setSelectedDate(date);
              // 直接寫入 input 並關閉 modal
              const dateInput = document.getElementById('schedule-date');
              if (dateInput) {
                const formattedDate = DateUtils.formatDate(date);
                dateInput.value = formattedDate;
                console.log('DOM.chat.initDatePicker: 日期已設定', formattedDate);
                
                // 清除任何現有的錯誤訊息
                FormValidator.clearValidationError(dateInput);
                // 清除日期選擇器 modal 內部的錯誤訊息
                DOM.chat.clearDatePickerError();
              }
              // 關閉 Modal
              const datePickerModal = bootstrap.Modal.getInstance(document.getElementById('date-picker-modal'));
              if (datePickerModal) {
                datePickerModal.hide();
              }
              // 強制清理 backdrop 和 body 狀態
              ModalCleanupUtils.delayedCleanup(200);
              // 重置日期選擇器快取，確保下次開啟時從當前月份開始
              setTimeout(() => {
                DOM_CACHE.resetDatePicker();
              }, 200);
            });
          }
          
          // 檢查是否超過允許的月份範圍（視覺上變灰，但仍可點擊）
          if (!DateUtils.validateDateWithinAllowedMonths(date)) {
            dateCell.classList.add('disabled', 'too-far');
          }
          
          calendarElement.appendChild(dateCell);
        }
      };
      
      // 上個月按鈕
      const prevMonthBtn = DOM_CACHE.prevMonthBtn;
      if (prevMonthBtn) {
        // 移除舊的事件監聽器
        const newPrevMonthBtn = prevMonthBtn.cloneNode(true);
        if (prevMonthBtn.parentNode) {
          prevMonthBtn.parentNode.replaceChild(newPrevMonthBtn, prevMonthBtn);
        }
        DOM.events.add(newPrevMonthBtn, 'click', () => {
          console.log('DOM.chat.initDatePicker: 上個月按鈕被點擊');
          currentMonth--;
          if (currentMonth < CONFIG.DATE_PICKER.CALENDAR.FIRST_MONTH_INDEX) {
            currentMonth = CONFIG.DATE_PICKER.CALENDAR.LAST_MONTH_INDEX;
            currentYear--;
          }
          updateMonthYear();
          generateCalendar();
        });
      }
      
      // 下個月按鈕
      const nextMonthBtn = DOM_CACHE.nextMonthBtn;
      if (nextMonthBtn) {
        // 移除舊的事件監聽器
        const newNextMonthBtn = nextMonthBtn.cloneNode(true);
        if (nextMonthBtn.parentNode) {
          nextMonthBtn.parentNode.replaceChild(newNextMonthBtn, nextMonthBtn);
        }
        DOM.events.add(newNextMonthBtn, 'click', () => {
          console.log('DOM.chat.initDatePicker: 下個月按鈕被點擊');
          currentMonth++;
          if (currentMonth > CONFIG.DATE_PICKER.CALENDAR.LAST_MONTH_INDEX) {
            currentMonth = CONFIG.DATE_PICKER.CALENDAR.FIRST_MONTH_INDEX;
            currentYear++;
          }
          updateMonthYear();
          generateCalendar();
        });
      }
      
      // 確定按鈕
      const confirmBtn = DOM_CACHE.confirmDateBtn;
      if (confirmBtn) {
        // 移除舊的事件監聽器
        const newConfirmBtn = confirmBtn.cloneNode(true);
        if (confirmBtn.parentNode) {
          confirmBtn.parentNode.replaceChild(newConfirmBtn, confirmBtn);
        }
        DOM.events.add(newConfirmBtn, 'click', () => {
          console.log('DOM.chat.initDatePicker: 確定按鈕被點擊');
          const selectedDate = ChatStateManager.getSelectedDate();
          if (selectedDate) {
            // 立即驗證選擇的日期
            if (!DateUtils.validateDateWithinAllowedMonths(selectedDate, false)) {
              // 驗證失敗，在日期選擇器 modal 內部顯示錯誤訊息
              DOM.chat.showDatePickerError(FormValidator.ERROR_MESSAGES.SCHEDULE_FORM.DATE_TOO_FAR);
              return; // 不關閉 modal，讓使用者重新選擇
            }
            
            // 驗證通過後才設定日期
            const dateInput = DOM_CACHE.dateInput;
            if (dateInput) {
              const formattedDate = DateUtils.formatDate(selectedDate);
              dateInput.value = formattedDate;
              console.log('DOM.chat.initDatePicker: 日期已設定', formattedDate);
              
              // 清除日期輸入欄位的錯誤訊息
              const errorElement = dateInput.parentNode.querySelector('.validation-error');
              if (errorElement) {
                errorElement.classList.remove('error-visible');
                errorElement.classList.add('error-hidden');
                errorElement.textContent = '';
              }
              // 清除日期選擇器 modal 內部的錯誤訊息
              DOM.chat.clearDatePickerError();
            }
          }
          
          // 關閉 Modal
          const confirmDatePickerModal = bootstrap.Modal.getInstance(document.getElementById('date-picker-modal'));
          if (confirmDatePickerModal) {
            confirmDatePickerModal.hide();
          }
          // 強制清理 backdrop 和 body 狀態
          ModalCleanupUtils.delayedCleanup(200);
          // 重置日期選擇器快取，確保下次開啟時從當前月份開始
          setTimeout(() => {
            DOM_CACHE.resetDatePicker();
          }, 200);
        });
      }
      
      // 初始化顯示
      updateMonthYear();
      generateCalendar();
    },
    
    // 在日期選擇器 modal 內部顯示錯誤訊息
    showDatePickerError: (message) => {
      console.log('DOM.chat.showDatePickerError called', { message });
      
      // 找到日期選擇器 modal
      const datePickerModal = document.getElementById('date-picker-modal');
      if (!datePickerModal) {
        console.warn('DOM.chat.showDatePickerError: 找不到日期選擇器 modal');
        return;
      }
      
      // 先清除現有的錯誤訊息
      DOM.chat.clearDatePickerError();
      
      // 創建錯誤訊息元素
      const errorDiv = document.createElement('div');
      errorDiv.className = 'validation-error text-danger small mt-2 date-picker-error';
      errorDiv.textContent = message;
      errorDiv.style.display = 'block';
      
      // 找到標題元素
      const modalTitle = datePickerModal.querySelector('.modal-title');
      if (modalTitle) {
        // 在標題後面插入錯誤訊息
        modalTitle.parentNode.insertBefore(errorDiv, modalTitle.nextSibling);
      } else {
        // 如果找不到標題，則插入到 modal 的最前面
        datePickerModal.insertBefore(errorDiv, datePickerModal.firstChild);
      }
      
      console.log('DOM.chat.showDatePickerError: 日期選擇器錯誤已顯示');
    },
    
    // 清除日期選擇器 modal 內部的錯誤訊息
    clearDatePickerError: () => {
      console.log('DOM.chat.clearDatePickerError called');
      
      const datePickerModal = document.getElementById('date-picker-modal');
      if (datePickerModal) {
        const existingError = datePickerModal.querySelector('.date-picker-error');
        if (existingError) {
          existingError.remove();
        }
      }
    },
    
    // 檢查多數人休息時間並顯示錯誤訊息
    checkBusinessHours: (input, formattedTime) => {
      console.log('DOM.chat.checkBusinessHours called：檢查多數人休息時間', { formattedTime });
      
      const businessStart = CONFIG.DATE_PICKER.BUSINESS_HOURS.START;
      const businessEnd = CONFIG.DATE_PICKER.BUSINESS_HOURS.END;
      
      if (DateUtils.compareTimes(formattedTime, businessStart) < 0 || 
          DateUtils.compareTimes(formattedTime, businessEnd) > 0) {
        FormValidator.showValidationError(FormValidator.ERROR_MESSAGES.SCHEDULE_FORM.TIME_BUSINESS_HOURS, input);
        return false;
      } else {
        // 只清除該輸入欄位的錯誤訊息，不清除表單下方的錯誤訊息
        const errorElement = input.parentNode.querySelector('.validation-error');
        if (errorElement) {
          errorElement.classList.remove('error-visible');
          errorElement.classList.add('error-hidden');
          errorElement.textContent = '';
        }
        return true;
      }
    },

    // 格式化時間輸入
    formatTimeInput: (input, forceFormat = false) => {
      console.log('DOM.chat.formatTimeInput called：格式化時間輸入', { 
        value: input.value, 
        forceFormat 
      });
      
      // input 事件時只允許數字，不自動補冒號
      let value = input.value.replace(/[^0-9]/g, ''); // 移除所有非數字字符
      if (!forceFormat) {
        input.value = value;
        return;
      }
      
      // blur 事件時才自動格式化
      DOM.chat.processTimeInput(input, value);
    },
    
    // 處理時間輸入的共用邏輯：格式化4位數字為 HH:MM 格式，驗證時間有效性，顯示相應錯誤訊息
    processTimeInput: (input, value) => {
      console.log('DOM.chat.processTimeInput called：處理時間輸入', { value });
      
      if (value.length === CONFIG.DATE_PICKER.TIME.TIME_INPUT_LENGTH) {
        const hours = parseInt(value.substring(CONFIG.DATE_PICKER.TIME.HOURS_START, CONFIG.DATE_PICKER.TIME.HOURS_END));
        const minutes = parseInt(value.substring(CONFIG.DATE_PICKER.TIME.MINUTES_START, CONFIG.DATE_PICKER.TIME.MINUTES_END));
        // 先格式化為 HH:MM 格式
        const formattedTime = `${String(hours).padStart(CONFIG.DATE_PICKER.FORMAT.PADDING_LENGTH, CONFIG.DATE_PICKER.FORMAT.PADDING_CHAR)}${CONFIG.DATE_PICKER.SEPARATORS.TIME}${String(minutes).padStart(CONFIG.DATE_PICKER.FORMAT.PADDING_LENGTH, CONFIG.DATE_PICKER.FORMAT.PADDING_CHAR)}`;
        input.value = formattedTime;
        
        if (hours >= CONFIG.DATE_PICKER.TIME.MIN_HOURS && hours <= CONFIG.DATE_PICKER.TIME.MAX_HOURS && 
            minutes >= CONFIG.DATE_PICKER.TIME.MIN_MINUTES && minutes <= CONFIG.DATE_PICKER.TIME.MAX_MINUTES) {
          DOM.chat.checkBusinessHours(input, formattedTime);
        } else {
          // 顯示錯誤訊息
          let errorMessage = '';
          if (hours > CONFIG.DATE_PICKER.TIME.MAX_HOURS) {
            errorMessage += `"時"數「${hours}」超過 ${CONFIG.DATE_PICKER.TIME.MAX_HOURS}，請輸入 00-${CONFIG.DATE_PICKER.TIME.MAX_HOURS} 之間的數字\n`;
          }
          if (minutes > CONFIG.DATE_PICKER.TIME.MAX_MINUTES) {
            errorMessage += `"分"數「${minutes}」超過 ${CONFIG.DATE_PICKER.TIME.MAX_MINUTES}，請輸入 00-${CONFIG.DATE_PICKER.TIME.MAX_MINUTES} 之間的數字\n`;
          }
          FormValidator.showValidationError(errorMessage, input);
          return; // 時間無效時直接返回，不進行後續處理
        }
      } else {
        // 非4位數字，保留原始輸入並顯示錯誤訊息
        input.value = value;
        FormValidator.showValidationError(`目前輸入內容非 ${CONFIG.DATE_PICKER.TIME.TIME_INPUT_LENGTH} 位數字，請輸入 ${CONFIG.DATE_PICKER.TIME.TIME_INPUT_LENGTH} 位數字`, input);
      }
    },
    
    // 驗證並格式化時間
    validateAndFormatTime: (input) => {
      console.log('DOM.chat.validateAndFormatTime called：驗證並格式化時間', { value: input.value });
      let value = input.value.trim();
      
      // 如果為空，保持空值
      if (!value) {
        input.value = '';
        return;
      }
      
      // 移除所有非數字字符
      const numbers = value.replace(/[^0-9]/g, '');
      
      if (numbers.length === 0) {
        input.value = '';
        return;
      }
      
      DOM.chat.processTimeInput(input, numbers);
    },
    
    // 驗證備註輸入
    validateNotesInput: (input) => {
      console.log('DOM.chat.validateNotesInput called：驗證備註輸入', { value: input.value });
      const value = input.value.trim();
      
      // 如果為空，清除該欄位的錯誤訊息
      if (!value) {
        ErrorElementUtils.clearInputError(input);
        return;
      }
      
      // 檢查長度限制
      if (value.length > FormValidator.RULES.SCHEDULE_FORM.NOTES.MAX_LENGTH) {
        FormValidator.showValidationError(FormValidator.ERROR_MESSAGES.SCHEDULE_FORM.NOTES_TOO_LONG, input);
      } else {
        // 清除該欄位的錯誤訊息
        ErrorElementUtils.clearInputError(input);
      }
    },
    
    // 驗證日期輸入
    validateDateInput: (input) => {
      console.log('DOM.chat.validateDateInput called：驗證日期輸入', { value: input.value });
      const value = input.value.trim();
      
      // 如果為空，清除該欄位的錯誤訊息
      if (!value) {
        ErrorElementUtils.clearInputError(input);
        return;
      }
      
      // 檢查日期格式
      if (!DateUtils.isValidDateFormat(value)) {
        FormValidator.showValidationError(FormValidator.ERROR_MESSAGES.SCHEDULE_FORM.DATE_INVALID, input);
        return;
      }
      
      // 檢查是否為過去日期
      const today = DateUtils.getToday();
      const selectedDate = new Date(value.replace(/\//g, '-'));
      if (selectedDate < new Date(today.getFullYear(), today.getMonth(), today.getDate())) {
        FormValidator.showValidationError(FormValidator.ERROR_MESSAGES.SCHEDULE_FORM.DATE_PAST, input);
        return;
      }
      
      // 檢查是否超過 3 個月
      if (!DateUtils.validateDateWithinAllowedMonths(selectedDate)) {
        FormValidator.showValidationError(FormValidator.ERROR_MESSAGES.SCHEDULE_FORM.DATE_TOO_FAR, input);
        return;
      }
      
      // 清除該欄位的錯誤訊息
      ErrorElementUtils.clearInputError(input);
    },
    
    // 提交表單
    submitScheduleForm: async () => {
      console.log('DOM.chat.submitScheduleForm called：提交表單');
      
      const formData = DOM_CACHE.getFormData();
      
      console.log('DOM.chat.submitScheduleForm: 表單資料', formData);
      
      // 使用 FormValidator 驗證表單
      const validationResult = FormValidator.validateScheduleForm(formData);
      
      if (!validationResult.isValid) {
        console.warn('DOM.chat.submitScheduleForm: 表單驗證失敗', validationResult);
        FormValidator.showValidationError(validationResult.message);
        return;
      }
      
      // 檢查重複時段
      const existingSchedules = ChatStateManager.getProvidedSchedules();
      const draftSchedules = ChatStateManager.get(ChatStateManager.CONFIG.STATE_KEYS.DRAFT_SCHEDULES) || [];
      const allExistingSchedules = [...existingSchedules, ...draftSchedules];
      // 將 formData 轉換為標準時段格式
      const newSchedule = {
        date: formData.date,
        startTime: formData.startTime,
        endTime: formData.endTime
      };

      const isDuplicate = checkScheduleOverlap(newSchedule, allExistingSchedules);
      
      if (isDuplicate) {
        console.warn('DOM.chat.submitScheduleForm: 檢測到重複或重疊時段', formData);
        const duplicateMessage = FormValidator.generateDuplicateScheduleMessage(formData, allExistingSchedules);
        FormValidator.showValidationError(duplicateMessage);
        return;
      }
      
      // 格式化輸出
      const formattedSchedule = DOM.chat.formatScheduleWithWeekday(formData.date, formData.startTime, formData.endTime);
      const notes = formData.notes.trim();
      
      console.log('DOM.chat.submitScheduleForm: 格式化後的資料', {
        formattedSchedule,
        notes
      });
      
      // 記錄時段資料到草稿狀態
      const addResult = ChatStateManager.addDraftSchedule({
        date: formData.date,
        startTime: formData.startTime,
        endTime: formData.endTime,
        notes: notes,
        formattedSchedule: formattedSchedule
      });
      
      if (!addResult) {
        console.warn('DOM.chat.submitScheduleForm: 時段添加失敗，可能是重複或重疊時段');
        FormValidator.showValidationError('抱歉，您輸入的時段與已提供的時段重複或重疊，請重新輸入。');
        return;
      }
      
      console.log('DOM.chat.submitScheduleForm: 草稿時段資料已記錄', ChatStateManager.get(ChatStateManager.CONFIG.STATE_KEYS.DRAFT_SCHEDULES));
      
      // 添加使用者訊息
      const userMessage = `提供方便時段：${formattedSchedule}${notes ? `\n備註：${notes}` : ''}`;
      DOM.chat.addUserMessage(userMessage);
      
      // 隱藏表單
      const scheduleForm = DOM_CACHE.scheduleForm;
      if (scheduleForm) {
        scheduleForm.style.display = 'none';
      }
      
      // 清空表單
      DOM_CACHE.clearFormInputs();
      
      // 重置選中的日期
      ChatStateManager.setSelectedDate(null);
      
      // 模擬 Giver 回覆
      await delay(DELAY_TIMES.CHAT.RESPONSE);  
        // 將訊息與按鈕組合在同一個訊息框
        const responseHTML = TEMPLATES.chat.afterScheduleOptions(formattedSchedule, notes);
        const chatMessages = document.getElementById('chat-messages');
        if (chatMessages) {
          chatMessages.insertAdjacentHTML('beforeend', responseHTML);
          // 按鈕事件由 EventManager 統一處理
          console.log('submitScheduleForm: 按鈕事件由 EventManager 統一處理');
          // 滾動到底部
          chatMessages.scrollTop = chatMessages.scrollHeight;
        }
    },
    
    // 處理多筆時段選項
    handleMultipleTimes: async () => {
      console.log('DOM.chat.handleMultipleTimes called：處理多筆時段選項');
      await delay(DELAY_TIMES.CHAT.MULTIPLE_TIMES);
        // 使用新的模板顯示訊息和按鈕
        const responseHTML = TEMPLATES.chat.multipleTimesUnderConstruction();
        const chatMessages = document.getElementById('chat-messages');
        if (chatMessages) {
          chatMessages.insertAdjacentHTML('beforeend', responseHTML);
          // 按鈕事件由 EventManager 統一處理
          console.log('handleMultipleTimes: 按鈕事件由 EventManager 統一處理');
          chatMessages.scrollTop = chatMessages.scrollHeight;
        }
        
        // 設定多筆時段輸入模式
        ChatStateManager.setMultipleTimesMode(true);
        console.log('DOM.chat.handleMultipleTimes: 已設定多筆時段輸入模式');
    },
    
    // 處理查看所有已提供時段選項
    handleViewAllSchedules: async () => {
      console.log('DOM.chat.handleViewAllSchedules called：處理查看所有已提供時段選項');
      
      // 獲取當前 Giver 和使用者 ID
      const currentGiver = ChatStateManager.getCurrentGiver();
      const currentUserId = ChatStateManager.getCurrentUserId();
      
      if (!currentGiver || !currentUserId) {
        console.warn('DOM.chat.handleViewAllSchedules: 缺少 Giver 或使用者 ID', { currentGiver, currentUserId });
        return;
      }
      
      console.log('DOM.chat.handleViewAllSchedules: 開始從資料庫載入時段', { giverId: currentGiver.id, userId: currentUserId });
      
      // 從資料庫載入使用者提供給該 Giver 的時段
      const databaseSchedules = await ChatStateManager.loadUserSchedulesFromDatabase(currentGiver.id, currentUserId);
      console.log('DOM.chat.handleViewAllSchedules: 從資料庫載入的時段', databaseSchedules);
      
      // 將資料庫中的時段合併到已提供的時段中（避免重複）
      const existingProvidedSchedules = ChatStateManager.getProvidedSchedules();
      const existingIds = new Set(existingProvidedSchedules.map(s => s.id));
      
      // 只添加資料庫中不存在於當前已提供時段中的時段
      const newSchedules = databaseSchedules.filter(schedule => !existingIds.has(schedule.id));
      
      if (newSchedules.length > 0) {
        console.log('DOM.chat.handleViewAllSchedules: 新增資料庫中的時段到已提供時段', newSchedules);
        // 將新的時段添加到已提供時段列表中
        newSchedules.forEach(schedule => {
          ChatStateManager.addSchedule(schedule);
        });
      }
      
      const providedSchedules = ChatStateManager.getProvidedSchedules();
      const draftSchedules = ChatStateManager.get(ChatStateManager.CONFIG.STATE_KEYS.DRAFT_SCHEDULES) || [];
      console.log('DOM.chat.handleViewAllSchedules: 合併後的已提供時段資料', providedSchedules);
      console.log('DOM.chat.handleViewAllSchedules: 草稿時段資料', draftSchedules);
      
      // 檢查是否有草稿時段
      const hasDraftSchedules = draftSchedules.length > 0;
      console.log('DOM.chat.handleViewAllSchedules: 是否有草稿時段', hasDraftSchedules);
      
      // 使用 case 語法處理不同的顯示邏輯
      let displayCase;
      if (providedSchedules.length === 0 && draftSchedules.length === 0) {
        displayCase = 'no-schedules';
      } else if (!hasDraftSchedules) {
        displayCase = 'no-draft-schedules';
      } else {
        displayCase = 'has-draft-schedules';
      }
      
      console.log('DOM.chat.handleViewAllSchedules: 顯示案例', displayCase);
      
      // 重繪表格（內部函式）：生成時段表格的 HTML 內容
      const renderTable = (includeButtons = false) => {
        console.log('renderTable() called: 重繪時段表格', { includeButtons });
        // 合併正式提供時段和草稿時段，但標記草稿時段
        const { allSchedules } = getAllSchedulesWithDraftStatus();
        console.log('renderTable() allSchedules:', allSchedules);
        
        // 使用共用函數生成表格
        const result = generateScheduleTable(allSchedules, includeButtons);
        
        console.log('renderTable() completed: 表格模板已生成');
        return result;
      };
      
      // 真正渲染與事件綁定（內部函式）：渲染表格並綁定相關事件
      const mountTable = (includeButtons = false) => {
        console.log('mountTable() called: 渲染與事件綁定表格', { includeButtons });
        const chatMessages = document.getElementById('chat-messages');
        if (!chatMessages) {
          console.warn('mountTable() error: 找不到 chat-messages 元素');
          return;
        }
        console.log('mountTable() 開始移除舊的時段表格訊息泡泡');
        // 先移除所有舊的時段表格訊息泡泡
        chatMessages.querySelectorAll('.giver-message .schedule-table').forEach(table => {
          const bubble = table.closest('.giver-message');
          if (bubble) bubble.remove();
        });
        console.log('mountTable() 插入新的表格訊息');
        // 插入新的表格訊息
        chatMessages.insertAdjacentHTML('beforeend', renderTable(includeButtons));
        // 綁定表格內按鈕事件
        const table = chatMessages.querySelector('.giver-message:last-child table');
        if (!table) {
          console.warn('mountTable() error: 找不到新插入的表格');
          return;
        }
        console.log('mountTable() 滾動到底部');
        // 滾動到底部
        chatMessages.scrollTop = chatMessages.scrollHeight;
        console.log('mountTable() completed: 表格渲染與事件綁定完成');
      };
      
      await delay(DELAY_TIMES.CHAT.VIEW_TIMES);
      
      // 使用 switch case 語法處理不同的顯示邏輯
      switch (displayCase) {
        case 'no-schedules':
          console.log('DOM.chat.handleViewAllSchedules: 案例 - 沒有時段');
          const html = TEMPLATES.chat.noSchedulesWithButtons();
          const chatMessages = document.getElementById('chat-messages');
          if (chatMessages) {
            chatMessages.insertAdjacentHTML('beforeend', html);
            DOM.chat.setupScheduleOptionButtons();
            chatMessages.scrollTop = chatMessages.scrollHeight;
          }
          break;
          
        case 'no-draft-schedules':
          console.log('DOM.chat.handleViewAllSchedules: 案例 - 沒有草稿時段');
          mountTable(false); // 不包含按鈕
          break;
          
        case 'has-draft-schedules':
          console.log('DOM.chat.handleViewAllSchedules: 案例 - 有草稿時段');
          mountTable(true); // 包含按鈕
          break;
          
        default:
          console.warn('DOM.chat.handleViewAllSchedules: 未知的顯示案例', displayCase);
          mountTable(false);
          break;
      }
    },
    
    // 處理取消預約選項
    handleCancelSchedule: async () => {
      console.log('DOM.chat.handleCancelSchedule called：處理取消預約選項');
      await delay(DELAY_TIMES.CHAT.CANCEL_MESSAGE);
      const response = '好的，已取消預約。<br><br>如未來有需要預約 Giver 時間，請使用聊天輸入區域下方的功能按鈕。<br><br>有其他問題需要協助嗎？';
      DOM.chat.addGiverResponse(response);
    },

    // 新增：處理成功提供時間選項
    handleSuccessProvideTime: async () => {
      console.log('DOM.chat.handleSuccessProvideTime called：處理成功提供時間選項');
      
      const providedSchedules = ChatStateManager.getProvidedSchedules();
      console.log('DOM.chat.handleSuccessProvideTime: 已提供的時段資料', providedSchedules);
      
      const chatMessages = document.getElementById('chat-messages');
      if (chatMessages) {
        // 先移除舊的成功提供表格（如果存在）
        const existingSuccessMessage = chatMessages.querySelector('.success-provide-table')?.closest('.giver-message');
        if (existingSuccessMessage) {
          console.log('DOM.chat.handleSuccessProvideTime: 移除舊的成功提供表格');
          existingSuccessMessage.remove();
        }
        
        // 每次都創建新的成功提供表格
        console.log('DOM.chat.handleSuccessProvideTime: 創建新的成功提供表格');
        const responseHTML = TEMPLATES.chat.successProvideTime(providedSchedules, 0);
        chatMessages.insertAdjacentHTML('beforeend', responseHTML);
        
        console.log('按鈕事件由 EventManager 統一處理');
        
        chatMessages.scrollTop = chatMessages.scrollHeight;
      }
    },
    
    // 格式化時段字串，包含星期幾
    formatScheduleWithWeekday: (date, startTime, endTime) => {
      console.log('DOM.chat.formatScheduleWithWeekday called', { date, startTime, endTime });
      
      // 解析日期字串 (YYYY/MM/DD)
      const dateParts = date.split(CONFIG.DATE_PICKER.SEPARATORS.DATE);
      if (dateParts.length !== 3) {
        console.warn('DOM.chat.formatScheduleWithWeekday: 日期格式不正確', { date });
        return `${date} ${startTime}${CONFIG.DATE_PICKER.SEPARATORS.PERIOD}${endTime}`;
      }
      
      const year = parseInt(dateParts[0]);
      const month = parseInt(dateParts[1]) - CONFIG.DATE_PICKER.CALCULATION.MONTH_OFFSET; // JavaScript 月份從 0 開始
      const day = parseInt(dateParts[2]);
      
      // 創建 Date 物件
      const dateObj = new Date(year, month, day);
      
      // 檢查日期是否有效
      if (isNaN(dateObj.getTime())) {
        console.warn('DOM.chat.formatScheduleWithWeekday: 無效的日期', { date });
        return `${date} ${startTime}${CONFIG.DATE_PICKER.SEPARATORS.PERIOD}${endTime}`;
      }
      
      // 星期幾陣列
      const weekdays = CONFIG.DATE_PICKER.WEEKDAYS;
      const weekday = weekdays[dateObj.getDay()];
      
      const formattedStartTime = DateUtils.formatTimeWithoutSeconds(startTime);
      const formattedEndTime = DateUtils.formatTimeWithoutSeconds(endTime);
      
      // 格式化輸出
      const formattedSchedule = `${date}（週${weekday}）${formattedStartTime}${CONFIG.DATE_PICKER.SEPARATORS.PERIOD}${formattedEndTime}`;
      console.log('DOM.chat.formatScheduleWithWeekday: 格式化結果', { formattedSchedule });
      
      return formattedSchedule;
    },
    
    // 設定輸入控制項
    setupInputControls: (chatInput, sendBtn) => {
      console.log('DOM.chat.setupInputControls called：設定輸入控制項', { chatInput, sendBtn });
      
      if (!chatInput || !sendBtn) {
        console.error('DOM.chat.setupInputControls: 聊天輸入框或發送按鈕未找到');
        return;
      }
      
      console.log('DOM.chat.setupInputControls: 設定聊天輸入控制項:', { chatInput, sendBtn });
      
      // 發送訊息函數（內部函式）：處理聊天訊息的發送邏輯
      const sendMessage = async () => {
        console.log('DOM.chat.setupInputControls.sendMessage called: 處理聊天訊息發送');
        const message = chatInput.value.trim();
        chatInput.value = '';
        
        if (!message) {
          console.log('DOM.chat.setupInputControls.sendMessage: 訊息為空，跳過發送');
          return;
        }
        
        // 先顯示用戶訊息（無論是否為多筆時段模式）
        console.log('DOM.chat.setupInputControls: 顯示用戶訊息', message);
        DOM.chat.addUserMessage(message);
        
        if (ChatStateManager.isMultipleTimesMode()) {
          // 處理多筆時段輸入
          console.log('DOM.chat.setupInputControls: 處理多筆時段輸入', message);
          DOM.chat.handleMultipleTimesSubmission(message);
        } else {
          // 模擬 Giver 回覆
          await delay(DELAY_TIMES.CHAT.RESPONSE);
          const giverResponse = DOM.chat.getGiverResponse(message);
          DOM.chat.addGiverResponse(giverResponse);
        }
      };
      
      // 按 Enter 鍵發送訊息
      DOM.events.add(chatInput, 'keypress', (e) => {
        console.log('DOM.chat.setupInputControls: 按鍵事件:', e.key);
        if (e.key === 'Enter') {
          sendMessage();
        }
      });
      
      // 點擊發送按鈕
      DOM.events.add(sendBtn, 'click', () => {
        console.log('DOM.chat.setupInputControls: 發送按鈕被點擊');
        sendMessage();
      });
    },
    
    // 設定模態框事件
    setupModalEvents: () => {
      console.log('DOM.chat.setupModalEvents called：設定模態框事件');
      const modalElement = DOM.chatElements.modalElement();
      if (modalElement) {
        // 監聽 modal 隱藏事件
        DOM.events.add(modalElement, 'hidden.bs.modal', () => {
          console.log('DOM.chat.setupModalEvents: Modal 已隱藏，清理聊天功能');
          DOM.chat.cleanup();
          
          // 強制處理焦點問題
          DOM.chat.forceFocusToBody();
          
          // 確保 backdrop 被清理
          ModalCleanupUtils.delayedCleanup(0);
        });
        
        // 監聽 modal 顯示事件
        DOM.events.add(modalElement, 'shown.bs.modal', () => {
          console.log('DOM.chat.setupModalEvents: Modal 已顯示');
          // 確保 modal 有正確的 tabindex
          modalElement.setAttribute('tabindex', '-1');
          modalElement.removeAttribute('inert');
          
          // 設定聊天輸入區域的額外功能按鈕事件監聽器
          DOM.chat.setupChatExtraButtons();
        });
      }
    },
    
    // 強制將焦點移到 body
    forceFocusToBody: () => {
      console.log('DOM.chat.forceFocusToBody called：強制將焦點移到 body');
      // 使用多種方法確保焦點正確轉移
      setTimeout(() => {
        // 移除所有可能的焦點
        const activeElement = document.activeElement;
        if (activeElement && activeElement !== document.body) {
          activeElement.blur();
        }
        
        // 移除 modal 的 tabindex 屬性
        const modalElement = DOM.chatElements.modal();
        if (modalElement) {
          modalElement.removeAttribute('tabindex');
          modalElement.setAttribute('inert', '');
        }
        
        // 強制焦點到 body
        document.body.focus();
        
        // 如果焦點仍然不在 body 上，再次嘗試
        setTimeout(() => {
          if (document.activeElement !== document.body) {
            document.body.focus();
          }
        }, 50);
      }, 0);
    },
    
    // 顯示關閉確認對話框
    showCloseConfirmation: () => {
      console.log('DOM.chat.showCloseConfirmation called：顯示關閉確認對話框');
      showConfirmDialog({
        title: '差幾步就能完成申請囉！',
        message: 'Giver 提供的名額即將額滿，現在離開下次需要重新申請哦！要繼續完成嗎？',
        confirmText: '繼續完成',
        cancelText: '忍痛離開',
        cleanupBackdrop: false, // 點擊繼續完成時不清理 backdrop
        onConfirm: () => {
          // 繼續聊天，不做任何操作
        },
        onCancel: () => {
          // 關閉聊天對話框
          const chatModal = bootstrap.Modal.getInstance(DOM.chatElements.modal());
          if (chatModal) {
            chatModal.hide();
          }
          // 清理 modal 和 backdrop
          setTimeout(() => {
            const modalElement = DOM.chatElements.modal();
            if (modalElement) {
              DOM.utils.cleanupModal(modalElement);
            }
            // 額外清理 backdrop
            ModalCleanupUtils.quickCleanup();
            
            // 強制處理焦點問題：當使用者關閉對話框時，強制將焦點移到 body，避免使用者無法操作其他元素。
            DOM.chat.forceFocusToBody(); 
          }, DELAY_TIMES.UI.MODAL_CLEANUP);
        }
      });
    },
    
    // 添加使用者訊息
    addUserMessage: (message) => {
      console.log('DOM.chat.addUserMessage called：添加使用者訊息', { message });
      
      const messageElement = DOM.message.createMessage(message, 'user');
      if (!messageElement) {
        console.error('DOM.chat.addUserMessage: 無法創建使用者訊息元素');
        return;
      }
      
      DOM.message.addToChat(messageElement); // 將使用者訊息添加到聊天區域
      
      // 使用 ChatStateManager 記錄訊息歷史
      ChatStateManager.addUserMessage(message);
      console.log('DOM.chat.addUserMessage: 使用者訊息已添加');
    },
    
    // 添加 Giver 回覆
    addGiverResponse: (message) => {
      console.log('DOM.chat.addGiverResponse called：添加 Giver 回覆', { message });
      const response = message;
      console.log('DOM.chat.addGiverResponse: Giver 回覆內容:', response);
      const messageElement = DOM.message.createMessage(response, 'giver', true);
      if (!messageElement) {
        console.error('DOM.chat.addGiverResponse: 無法創建 Giver 訊息元素');
        return;
      }
      DOM.message.addToChat(messageElement);
      ChatStateManager.addGiverMessage(response);
      console.log('DOM.chat.addGiverResponse: Giver 回覆已添加');
    },
    
    // 獲取 Giver 回覆
    getGiverResponse: (userMessage) => {
      console.log('DOM.chat.getGiverResponse called：獲取 Giver 回覆', { userMessage });
      return BusinessLogic.chat.generateResponse(userMessage);
    },
    
    // 清理事件監聽器（不結束聊天會話）
    cleanupEventListeners: () => {
      console.log('DOM.chat.cleanupEventListeners called：清理事件監聽器');
      
      // 清理所有聊天相關的事件監聽器
      const chatInput = DOM.chatElements.input();
      const sendBtn = DOM.chatElements.sendBtn();
      
      if (chatInput) {
        // 使用 DOM.events.removeAll 移除所有事件監聽器
        DOM.events.removeAll(chatInput);
      }
      
      if (sendBtn) {
        // 使用 DOM.events.removeAll 移除所有事件監聽器
        DOM.events.removeAll(sendBtn);
      }
      
      console.log('DOM.chat.cleanupEventListeners: 事件監聽器清理完成');
    },
    
    // 清理聊天功能
    cleanup: () => {
      console.log('DOM.chat.cleanup called：清理聊天功能');
      
      // 清空聊天區域並重新設定初始狀態
      DOM.message.clearChat();
      
      // 移除關閉按鈕
      const closeBtn = DOM.getElement('.btn-close-header');
      if (closeBtn) {
        closeBtn.remove();
      }
      
      // 隱藏並清理表單
      const scheduleForm = document.getElementById('schedule-form');
      if (scheduleForm) {
        scheduleForm.style.display = 'none';
        
        // 清空表單欄位
        const clearConfig = { defaultValue: '' };
        
        const formFields = [
          { id: 'schedule-date', element: document.getElementById('schedule-date') },
          { id: 'schedule-start-time', element: document.getElementById('schedule-start-time') },
          { id: 'schedule-end-time', element: document.getElementById('schedule-end-time') },
          { id: 'schedule-notes', element: document.getElementById('schedule-notes') }
        ];
        
        formFields.forEach(field => {
          if (field.element) {
            setupInputField(field.element, clearConfig);
          }
        });
      }
      
      // 清理日期選擇器狀態
      ChatStateManager.setSelectedDate(null);
      
      // 關閉日期選擇器 Modal
      const datePickerModal = bootstrap.Modal.getInstance(document.getElementById('date-picker-modal'));
      if (datePickerModal) {
        datePickerModal.hide();
        // 清除錯誤訊息
        DOM.chat.clearDatePickerError();
        // 重置日期選擇器快取，確保下次開啟時從當前月份開始
        DOM_CACHE.resetDatePicker();
      }
      
      // 清理聊天狀態（但保留 currentGiver 資訊，避免時段提交時無法確定目標 Giver）
      const currentGiver = ChatStateManager.get(ChatStateManager.CONFIG.STATE_KEYS.CURRENT_GIVER);
      ChatStateManager.setMultiple({
        [ChatStateManager.CONFIG.STATE_KEYS.IS_ACTIVE]: false,
        [ChatStateManager.CONFIG.STATE_KEYS.IS_MULTIPLE_TIMES_MODE]: false,
        [ChatStateManager.CONFIG.STATE_KEYS.SELECTED_DATE]: null
      });
      console.log('DOM.chat.cleanup: 保留 currentGiver 資訊', { currentGiver });
      
      // 清理所有聊天相關的事件監聽器
      const chatInput = DOM.chatElements.input();
      const sendBtn = DOM.chatElements.sendBtn();
      
      if (chatInput) {
        // 使用 DOM.events.removeAll 移除所有事件監聽器
        DOM.events.removeAll(chatInput);
      }
      
      if (sendBtn) {
        // 使用 DOM.events.removeAll 移除所有事件監聽器
        DOM.events.removeAll(sendBtn);
      }
      
      console.log('DOM.chat.cleanup: 聊天功能清理完成');
    },
    
    // 聊天功能工具
    utils: {      
      // 獲取聊天歷史
      getHistory: () => {
        console.log('DOM.chat.utils.getHistory called：獲取聊天歷史');
        return ChatStateManager.getMessageHistory();
      },
      
      // 清空聊天歷史
      clearHistory: () => {
        console.log('DOM.chat.utils.clearHistory called：清空聊天歷史');
        ChatStateManager.clearMessageHistory();
      },
      
      // 檢查聊天是否活躍
      isActive: () => {
        console.log('DOM.chat.utils.isActive called：檢查聊天是否活躍');
        return ChatStateManager.isActive();
      },
      
      // 獲取當前 Giver
      getCurrentGiver: () => {
        console.log('DOM.chat.utils.getCurrentGiver called：獲取當前 Giver');
        return ChatStateManager.getCurrentGiver();
      },
      
      // 調試聊天功能
      debug: () => {
        console.group('DOM.chat.utils.debug called：聊天功能調試資訊');
        ChatStateManager.debug();
        console.groupEnd();
      }
    },
    
    // 設定選項按鈕事件監聽器
    setupOptionButtons: () => {
      console.log('DOM.chat.setupOptionButtons called：設定選項按鈕');
      const optionButtons = DOM.getElements('.btn-option');
      optionButtons.forEach(button => {
        // 先移除舊的事件監聽器（用 cloneNode 替換）
        const newBtn = button.cloneNode(true);
        button.parentNode.replaceChild(newBtn, button);
        // 再綁定新的
        DOM.events.add(newBtn, 'click', (e) => {
          e.preventDefault();
          e.stopPropagation();
          const option = newBtn.getAttribute('data-option');
          const optionText = newBtn.textContent.trim();
          console.log('DOM.chat.setupOptionButtons: 選項按鈕被點擊:', { option, optionText });
          DOM.chat.addUserMessage(optionText);
          if (option === 'schedule') {
            DOM.chat.handleScheduleOption();
          } else if (option === 'skip') {
            DOM.chat.handleSkipOption();
          } else if (option === 'submit-schedules') {
            // 使用 EventManager 處理 submit-schedules 按鈕
            EventManager.handleOptionButton(newBtn, e);
          }
          // 隱藏選項按鈕
          const optionsContainer = newBtn.closest('.chat-options-buttons');
          if (optionsContainer) {
            optionsContainer.style.display = 'none';
          }
        });
      });
    },
    
    // 處理多筆時段提交
    handleMultipleTimesSubmission: async (message) => {
      console.log('DOM.chat.handleMultipleTimesSubmission called：處理多筆時段提交', { message });
      
      // 使用 FormValidator 驗證多筆時段
      const validationResult = FormValidator.validateMultipleSchedules(message);
      
      if (!validationResult.isValid) {
        console.warn('DOM.chat.handleMultipleTimesSubmission: 多筆時段驗證失敗', validationResult);
        await delay(DELAY_TIMES.ERROR.VALIDATION_ERROR);   
        DOM.chat.addGiverResponse(validationResult.message);
        return;
      }
      
      // 使用 DateUtils 解析多筆時段
      const { isValid, schedules } = DateUtils.parseMultipleSchedules(message);
      
      console.log('DOM.chat.handleMultipleTimesSubmission: 解析出的時段', schedules);
      
      if (!isValid) {
        // 沒有解析到有效時段
        await delay(DELAY_TIMES.ERROR.VALIDATION_ERROR);
        DOM.chat.addGiverResponse('抱歉，我無法解析您提供的時段格式。請使用以下格式：\n日期 時間範圍\n例如：\n2024/01/15 14:00-16:00\n2024/01/17 10:00-12:00');
        return;
      }
      
      // 檢查重複時段
      const existingSchedules = ChatStateManager.getProvidedSchedules();
      const draftSchedules = ChatStateManager.get(ChatStateManager.CONFIG.STATE_KEYS.DRAFT_SCHEDULES) || [];
      const allExistingSchedules = [...existingSchedules, ...draftSchedules];
      const duplicateSchedules = [];
      
      schedules.forEach(schedule => {
        const isDuplicate = checkScheduleOverlap(schedule, allExistingSchedules);
        
        if (isDuplicate) {
          duplicateSchedules.push(schedule);
        }
      });
      
      if (duplicateSchedules.length > 0) {
        console.warn('DOM.chat.handleMultipleTimesSubmission: 檢測到重複或重疊時段', duplicateSchedules);
        
        // 為每個重複的時段生成詳細錯誤訊息
        const duplicateMessages = duplicateSchedules.map(schedule => {
          const duplicateMessage = FormValidator.generateDuplicateScheduleMessage(schedule, allExistingSchedules);
          return `• ${schedule.formattedSchedule}：${duplicateMessage}`;
        });
        
        const errorMessage = `以下時段與已提供的時段重複或重疊：\n${duplicateMessages.join('\n')}`;
        
        FormValidator.showValidationError(errorMessage);
        return;
      }
      
      // 記錄時段資料到草稿狀態
      const addResult = ChatStateManager.addDraftSchedules(schedules);
      
      if (!addResult) {
        console.warn('DOM.chat.handleMultipleTimesSubmission: 時段添加失敗，可能是重複或重疊時段');
        FormValidator.showValidationError('抱歉，您輸入的時段中有與已提供的時段重複或重疊的部分，請重新輸入。');
        return;
      }
      
      // 退出多筆時段輸入模式
      ChatStateManager.setMultipleTimesMode(false);
      
      // 顯示提交結果
      await delay(DELAY_TIMES.CHAT.SUCCESS_MESSAGE);
        let scheduleList = '';
        schedules.forEach((schedule, index) => {
          const scheduleNumber = index + 1;
          scheduleList += `• 時段 ${scheduleNumber}：${schedule.formattedSchedule}\n`;
        });
        
        const scheduleCount = schedules.length;
        
        const responseHTML = TEMPLATES.chat.afterMultipleScheduleOptions();
        
        const chatMessages = document.getElementById('chat-messages');
        if (chatMessages) {
          chatMessages.insertAdjacentHTML('beforeend', responseHTML);
          // 按鈕事件由 EventManager 統一處理
          console.log('handleMultipleTimesSubmission: 按鈕事件由 EventManager 統一處理');
          // 滾動到底部
          chatMessages.scrollTop = chatMessages.scrollHeight;
        }
    },

    // 新增 showScheduleOptionsWithViewAll
    showScheduleOptionsWithViewAll: () => {
      console.log('DOM.chat.showScheduleOptionsWithViewAll called：顯示 5 按鈕預約選項');
      const scheduleOptionsHTML = TEMPLATES.chat.scheduleOptionsWithViewAll();
      const chatMessages = document.getElementById('chat-messages');
      if (chatMessages) {
        chatMessages.insertAdjacentHTML('beforeend', scheduleOptionsHTML);
        DOM.chat.setupScheduleOptionButtons();
        chatMessages.scrollTop = chatMessages.scrollHeight;
      }
    },

    // 處理互斥選擇邏輯
    handleMutualExclusion: (changedCheckbox) => {
      console.log('DOM.chat.handleMutualExclusion called：處理互斥選擇邏輯', { 
        option: changedCheckbox.getAttribute('data-option'), 
        checked: changedCheckbox.checked 
      });
      
      const allCheckboxes = document.querySelectorAll('.chat-checkbox-options input[type="checkbox"]');
      
      // 獲取當前所有選中的選項
      const selectedOptions = Array.from(allCheckboxes)
        .filter(checkbox => checkbox.checked)
        .map(checkbox => checkbox.getAttribute('data-option'));
      
      console.log('當前選中的選項:', selectedOptions);
      
      // 重置所有選項的狀態
      DOM.chat.resetCheckboxStates(allCheckboxes);
      
      // 根據當前所有選中的選項來決定哪些選項應該被禁用
      const hasDemoTime = selectedOptions.includes('demo-time-1') || selectedOptions.includes('demo-time-2');
      const hasProvideMyTime = selectedOptions.includes('provide-my-time');
      const hasCancel = selectedOptions.includes('cancel');
      
      // 應用互斥邏輯
      allCheckboxes.forEach(checkbox => {
        const option = checkbox.getAttribute('data-option');
        const shouldDisable = DOM.chat.shouldDisableCheckbox(option, hasDemoTime, hasProvideMyTime, hasCancel);
        
        if (shouldDisable) {
          DOM.chat.disableCheckbox(checkbox);
        }
      });
    },

    // 重置複選框狀態的通用函數
    resetCheckboxStates: (checkboxes) => {
      console.log('DOM.chat.resetCheckboxStates called：重置複選框狀態');
      
      checkboxes.forEach(checkbox => {
        const label = checkbox.nextElementSibling;
        if (label) {
          label.style.textDecoration = 'none';
          label.style.color = '';
        }
        checkbox.disabled = false;
      });
    },

    // 判斷是否應該禁用複選框的通用函數
    shouldDisableCheckbox: (option, hasDemoTime, hasProvideMyTime, hasCancel) => {
      console.log('DOM.chat.shouldDisableCheckbox called：判斷是否應該禁用複選框', { 
        option, hasDemoTime, hasProvideMyTime, hasCancel 
      });
      
      // 如果選中了 Demo 時間，禁用其他所有選項
      if (hasDemoTime && option !== 'demo-time-1' && option !== 'demo-time-2') {
        return true;
      }
      // 如果選中了提供我的時間，禁用 Demo 時間和取消選項
      else if (hasProvideMyTime && (option === 'demo-time-1' || option === 'demo-time-2' || option === 'cancel')) {
        return true;
      }
      // 如果選中了取消，禁用其他所有選項
      else if (hasCancel && option !== 'cancel') {
        return true;
      }
      
      return false;
    },

    // 禁用複選框的通用函數
    disableCheckbox: (checkbox) => {
      console.log('DOM.chat.disableCheckbox called：禁用複選框', { 
        option: checkbox.getAttribute('data-option') 
      });
      
      const label = checkbox.nextElementSibling;
      
      checkbox.disabled = true;
      checkbox.checked = false;
      
      if (label) {
        label.style.textDecoration = 'line-through';
        label.style.color = CONFIG.COLORS.DISABLED_TEXT;
      }
    },
  },
  
  // 資料載入管理工具
  dataLoader: {
    // 從 DOM 中提取 Giver 資料
    extractGiversFromDOM() {
      const giverCards = document.querySelectorAll('.giverCard[data-id]');
      const givers = [];
      
      giverCards.forEach(card => {
        const id = parseInt(card.getAttribute('data-id'));
        const name = card.querySelector('.giverCard__name span')?.textContent?.trim();
        const title = card.querySelector('.giverCard__title')?.textContent?.trim();
        const company = card.querySelector('.giverCard__company')?.textContent?.trim();
        const image = card.querySelector('.giverCard__avatar-img')?.src;
        
        // 提取統計資料
        const countValues = card.querySelectorAll('.giverCard__count-value');
        const consulted = countValues[0]?.textContent?.replace(/[^\d]/g, '') || '0';
        const average_responding_time = countValues[1]?.textContent?.replace(/[^\d]/g, '') || '0';
        const experience = countValues[2]?.textContent?.replace(/[^\d]/g, '') || '0';
        
        // 提取服務項目
        const topics = [];
        const topicElements = card.querySelectorAll('.giverCard__topic .btn-topic-sm');
        topicElements.forEach(topic => {
          topics.push(topic.textContent.trim());
        });
        
        givers.push({
          id,
          name,
          title,
          company,
          image,
          consulted,
          average_responding_time,
          experience,
          giverCard__topic: topics
        });
      });
      
      console.log('DOM.dataLoader.extractGiversFromDOM: 從 DOM 中提取到', givers.length, '筆 Giver 資料');
      return givers;
    },
    
    // 載入狀態管理
    state: {
      isLoading: false,
      lastLoadTime: null,
      loadCount: 0,
      errorCount: 0,
      cache: new Map(),
      retryCount: 0,
      loadingElement: null
    },
    
    // API 配置
    config: {
      baseURL: BASE_URL,
      timeout: 10000,
      retryDelay: 1000,
      maxRetries: 3,
      cacheExpiry: 5 * 60 * 1000 // 5分鐘
    },
    
    // 簡化的 Giver 資料載入（僅從 DOM 提取）
    loadGivers: async ({ onSuccess, onError, onComplete } = {}) => {
      console.log('DOM.dataLoader.loadGivers called：從伺服器端渲染的 DOM 中提取 Giver 資料');
      
      try {
        // 從已渲染的 HTML 中讀取 Giver 資料
        const giversData = DOM.dataLoader.extractGiversFromDOM();
        const totalCount = giversData.length;
        
        if (giversData.length === 0) {
          console.warn('DOM.dataLoader.loadGivers: 未找到 Giver 資料');
          onError?.(new Error('未找到 Giver 資料'));
          return [];
        }
        
        console.log('DOM.dataLoader.loadGivers: 成功提取', giversData.length, '筆 Giver 資料');
        
        // 更新應用狀態
        appState.givers = giversData;
        appState.totalGivers = totalCount;
        
        // 快取資料
        DOM.dataLoader.cacheData('givers', giversData);
        DOM.dataLoader.cacheData('givers_total', totalCount);
        
        // 渲染分頁器
        renderPaginator(totalCount);
        
        // 回調函數
        onSuccess?.(giversData);
        
        return giversData;
        
      } catch (error) {
        console.error('DOM.dataLoader.loadGivers: 提取 Giver 資料失敗:', error);
        onError?.(error);
        throw error;
      } finally {
        onComplete?.();
      }
    },
    
    // 簡化的特定 Giver 資料載入
    loadGiverById: async (giverId, options = {}) => {
      console.log('DOM.dataLoader.loadGiverById called：從應用狀態中查找 Giver 資料', { giverId });
      const { onSuccess = null, onError = null } = options;
      
      try {
        // 從已載入的應用狀態中查找
        const giverData = appState.givers?.find(giver => giver.id === parseInt(giverId));
        
        if (!giverData) {
          const error = new Error(`找不到 ID 為 ${giverId} 的 Giver`);
          console.error('DOM.dataLoader.loadGiverById:', error.message);
          onError?.(error);
          throw error;
        }
        
        console.log('DOM.dataLoader.loadGiverById: 成功找到 Giver 資料:', giverData.name);
        onSuccess?.(giverData);
        return giverData;
        
      } catch (error) {
        console.error('DOM.dataLoader.loadGiverById: 查找 Giver 資料失敗:', error);
        onError?.(error);
        throw error;
      }
    },
    
    // 發送 HTTP 請求
    makeRequest: async (cacheKey, requestConfig) => {
      console.log('DOM.dataLoader.makeRequest called：發送 HTTP 請求', { cacheKey, requestConfig });
      const config = {
        timeout: DOM.dataLoader.config.timeout,
        ...requestConfig
      };
      
      try {
        const response = await axios(config);
        return response;
        
      } catch (error) {
        // 重試邏輯
        if (DOM.dataLoader.state.retryCount < DOM.dataLoader.config.maxRetries) {
          DOM.dataLoader.state.retryCount++;
          console.log(`DOM.dataLoader.makeRequest: 請求失敗，重試第 ${DOM.dataLoader.state.retryCount} 次`);
          
          await new Promise(resolve => 
            setTimeout(resolve, DOM.dataLoader.config.retryDelay * DOM.dataLoader.state.retryCount)
          );
          
          return DOM.dataLoader.makeRequest(cacheKey, requestConfig);
        }
        
        throw error;
      }
    },
    
    // 錯誤處理
    handleError: (error, retryCallback) => {
      console.error('DOM.dataLoader.handleError: 資料載入錯誤:', error);
      
      // 顯示錯誤訊息
      DOM.dataLoader.showError(error.message || '資料載入失敗');
      
      // 如果還有重試次數，自動重試
      if (DOM.dataLoader.state.retryCount < DOM.dataLoader.config.maxRetries) {
        setTimeout(retryCallback, DOM.dataLoader.config.retryDelay);
      }
    },
    
    // 快取管理
    cacheData: (key, data) => {
      const cacheItem = {
        data,
        timestamp: Date.now(),
        expiry: Date.now() + DOM.dataLoader.config.cacheExpiry
      };
      
      DOM.dataLoader.state.cache.set(key, cacheItem);
      console.log('DOM.dataLoader.cacheData: 資料已快取:', key);
    },
    
    // 從快取中獲取資料，如果資料存在且未過期則返回資料，否則返回 null
    getCached: (key) => {
      const cacheItem = DOM.dataLoader.state.cache.get(key);
      if (cacheItem && Date.now() < cacheItem.expiry) {
        return cacheItem.data;
      }
      
      // 過期資料，從快取中移除
      DOM.dataLoader.state.cache.delete(key);
      return null;
    },
    
    // 檢查指定鍵值的資料是否存在於快取中且未過期
    isCached: (key) => {
      return DOM.dataLoader.getCached(key) !== null;
    },
    
    // 清除指定鍵值的資料或清除所有快取
    clearCache: (key = null) => {
      if (key) {
        DOM.dataLoader.state.cache.delete(key);
        console.log('DOM.dataLoader.clearCache: 清除快取:', key);
      } else {
        DOM.dataLoader.state.cache.clear();
        console.log('DOM.dataLoader.clearCache: 清除所有快取');
      }
    },
    
    // 載入狀態 UI
    showLoading: () => {
      console.log('DOM.dataLoader.showLoading called：顯示載入指示器');
      // 創建載入指示器
      const loadingIndicator = DOM.createElement('div', 'loading-indicator', `
        <div class="spinner-border text-primary" role="status">
          <span class="visually-hidden">載入中...</span>
        </div>
        <p class="mt-2">載入資料中...</p>
      `);
      
      document.body.appendChild(loadingIndicator);
      DOM.dataLoader.state.loadingElement = loadingIndicator;
    },
    
    // 隱藏載入指示器
    hideLoading: () => {
      console.log('DOM.dataLoader.hideLoading called：隱藏載入指示器');
      if (DOM.dataLoader.state.loadingElement) {
        DOM.dataLoader.state.loadingElement.remove();
        DOM.dataLoader.state.loadingElement = null;
      }
    },
    
    // 顯示錯誤訊息
    showError: async (message) => {
      console.log('DOM.dataLoader.showError called：顯示錯誤訊息', { message });
      // 創建錯誤訊息
      const errorElement = DOM.createElement('div', 'error-message', `
        <div class="alert alert-danger" role="alert">
          <i class="fas fa-exclamation-triangle me-2"></i>
          ${message}
          <button type="button" class="btn-close ms-auto" data-bs-dismiss="alert"></button>
        </div>
      `);
      
      document.body.appendChild(errorElement);
      
      // 自動移除錯誤訊息
      await delay(5000);
        if (errorElement.parentNode) {
          errorElement.remove();
        }
    },
    
    // 資料載入工具
    utils: {      
      // 檢查網路狀態
      checkNetworkStatus: () => {
        console.log('DOM.dataLoader.utils.checkNetworkStatus called：檢查網路狀態');
        return navigator.onLine;
      },
      
      // 預載入資料
      preloadData: async (dataTypes = ['givers']) => {
        console.log('DOM.dataLoader.utils.preloadData called：預載入資料', { dataTypes });
        
        const promises = dataTypes.map(type => {
          switch (type) {
            case 'givers':
              // 確保在載入 Giver 資料之前先清空靜態卡片
              const giverPanel = DOM.getElement(CONFIG.SELECTORS.GIVER_PANEL);
              if (giverPanel) {
                console.log('DOM.dataLoader.utils.preloadData: 清空靜態 Giver 卡片');
                giverPanel.innerHTML = '';
              }
              return DOM.dataLoader.loadGivers({ showLoading: false });
            default:
              return Promise.resolve();
          }
        });
        
        try {
          await Promise.all(promises);
          console.log('DOM.dataLoader.utils.preloadData: 資料預載入完成');
        } catch (error) {
          console.error('DOM.dataLoader.utils.preloadData: 資料預載入失敗:', error);
          if (typeof UIComponents !== 'undefined' && UIComponents.toast) {
            UIComponents.toast({ message: '資料預載入失敗，請稍後再試', type: 'error' });
          }
        }
      },
      
      // 清理過期快取
      cleanupExpiredCache: () => {
        console.log('DOM.dataLoader.utils.cleanupExpiredCache called：清理過期快取');
        const now = Date.now();
        let cleanedCount = 0;
        
        for (const [key, item] of DOM.dataLoader.state.cache) {
          if (now > item.expiry) {
            DOM.dataLoader.state.cache.delete(key);
            cleanedCount++;
          }
        }
        
        if (cleanedCount > 0) {
          console.log(`DOM.dataLoader.utils.cleanupExpiredCache: 清理了 ${cleanedCount} 個過期快取項目`);
        }
      },
      
      // 調試資料載入功能
      debug: () => {
        console.group('DOM.dataLoader.utils.debug called：資料載入調試資訊');
        console.log('DOM.dataLoader.utils.debug: 載入狀態:', DOM.dataLoader.state);
        console.log('DOM.dataLoader.utils.debug: 網路狀態:', DOM.dataLoader.utils.checkNetworkStatus());
        console.log('DOM.dataLoader.utils.debug: 快取項目:', Array.from(DOM.dataLoader.state.cache.keys()));
        console.groupEnd();
      }
    }
  },
  
  // Giver 相關功能
  giver: {
    
    // 設定卡片事件
    setupCardEvents: () => {
      console.log('DOM.giver.setupCardEvents called：設定卡片事件');
      // 移除原本為卡片設定的點擊事件，只保留按鈕事件
      
      // 設定諮詢按鈕事件
      const actionButtons = DOM.getElements(`.${CONFIG.CLASSES.GIVER_CARD_ACTION_BUTTON}`);
      actionButtons.forEach(button => {
        DOM.events.add(button, 'click', (e) => {
          e.preventDefault();
          e.stopPropagation(); // 防止事件冒泡
          
          const giverId = parseInt(button.dataset.id, 10); // 確保轉換為整數
          console.log('DOM.giver.setupCardEvents: 按鈕點擊', { 
            buttonDataId: button.dataset.id, 
            parsedGiverId: giverId,
            appStateGivers: appState.givers 
          });
          
          const giver = appState.givers.find(g => g.id === giverId); // 使用嚴格比較
          
          if (giver) {
            console.log('DOM.giver.setupCardEvents: 找到 Giver', { giver });
            // 呼叫 UIInteraction 開啟聊天對話框
            UIInteraction.openChatDialog(giver);
          } else {
            console.error('DOM.giver.setupCardEvents: 未找到對應的 Giver', { 
              giverId, 
              availableGivers: appState.givers.map(g => ({ id: g.id, name: g.name }))
            });
          }
        });
      });
    },

    // 檢查所有卡片的服務項目是否超出容器，並處理溢出
    checkAllTopicsOverflow: async () => {
      const topicContainers = DOM.getElements(`.${CONFIG.CLASSES.GIVER_CARD_TOPIC}`);
      
      topicContainers.forEach(async container => {
        const buttons = Array.from(container.querySelectorAll(`.${CONFIG.CLASSES.GIVER_CARD_TOPIC_BUTTON}`));
        const chevron = container.querySelector('.fa-chevron-right');

        if (!chevron || buttons.length === 0) return;

        // 1. 重設狀態，以便正確測量
        buttons.forEach(async btn => {
          btn.classList.remove('btn-hidden');
          btn.classList.add('btn-visible');
        });
        chevron.classList.remove('inline');
        chevron.classList.add('hidden');
        container.classList.remove('flex-wrap');
        container.classList.add('flex-nowrap');

        // 2. 延遲執行以等待 DOM 更新
        await delay(1000);  
          const containerWidth = container.clientWidth;

          // 如果沒有溢出，則恢復並跳出
          if (container.scrollWidth <= containerWidth) {
            chevron.classList.remove('inline');
            chevron.classList.add('hidden');
            container.classList.remove('flex-nowrap');
            container.classList.add('flex-wrap');
            return;
          }

          // 如果確定溢出，則顯示箭頭並計算可用空間
          chevron.classList.remove('hidden');
          chevron.classList.add('inline');
          const chevronWidth = chevron.offsetWidth;
          const gap = 8; // 根據 CSS --spacing-sm 變數設定
          const availableWidth = containerWidth - chevronWidth;
          let accumulatedWidth = 0;

          for (const btn of buttons) {
            const btnWidthWithGap = btn.offsetWidth + gap;
            if (accumulatedWidth + btnWidthWithGap > availableWidth) {
              btn.classList.remove('btn-visible');
              btn.classList.add('btn-hidden'); // 隱藏放不下的按鈕
            } else {
              accumulatedWidth += btnWidthWithGap;
              btn.classList.remove('btn-hidden');
              btn.classList.add('btn-visible'); // 確保按鈕可見
            }
          }

          // 3. 恢復容器的換行屬性
          container.classList.remove('flex-nowrap');
          container.classList.add('flex-wrap');
      });
    }
  },
  
  // 分頁相關功能
  pagination: {
    // 根據頁碼取得該頁的 Giver 資料
    getGiversByPage: (page) => {
      console.log('DOM.pagination.getGiversByPage called：取得第', page, '頁的 Giver 資料');
      
      if (!appState.givers || appState.givers.length === 0) {
        console.warn('沒有 Giver 資料');
        return [];
      }
      
      const startIndex = (page - 1) * CONFIG.PAGINATION.GIVERS_PER_PAGE;
      const endIndex = startIndex + CONFIG.PAGINATION.GIVERS_PER_PAGE;
      const pageGivers = appState.givers.slice(startIndex, endIndex);
      
      console.log('DOM.pagination.getGiversByPage: 第', page, '頁資料:', pageGivers.length, '筆');
      return pageGivers;
    },
    
    // 渲染分頁器
    renderPaginator: (totalCount) => {
      console.log('DOM.pagination.renderPaginator called：渲染分頁器，總數:', totalCount);
      
      const paginator = DOM.getElement(CONFIG.SELECTORS.PAGINATOR);
      console.log('DOM.pagination.renderPaginator: 分頁器元素:', paginator);
      
      if (!paginator) {
        console.error('DOM.pagination.renderPaginator: 分頁器元素未找到:', CONFIG.SELECTORS.PAGINATOR);
        console.error('DOM.pagination.renderPaginator: 嘗試手動查找元素');
        const manualPaginator = document.getElementById('paginator');
        console.error('DOM.pagination.renderPaginator: 手動查找結果:', manualPaginator);
        return;
      }
      
      const totalPages = Math.ceil(totalCount / CONFIG.PAGINATION.GIVERS_PER_PAGE);
      
      // 即使只有一頁也顯示分頁器，讓使用者知道這是第一頁
      if (totalPages <= 1) {
        // 顯示簡單的分頁器，只顯示當前頁碼
        let simplePaginatorHTML = TEMPLATES.paginator.container();
        simplePaginatorHTML += TEMPLATES.paginator.pageNumber(1, true); // 顯示第一頁為當前頁
        simplePaginatorHTML += '</ul>';
        paginator.innerHTML = simplePaginatorHTML;
        console.log('DOM.pagination.renderPaginator: 只有一頁，顯示簡單分頁器');
        return;
      }
      
      // 生成分頁 HTML
      let paginatorHTML = TEMPLATES.paginator.container();
      
      // 上一頁按鈕
      paginatorHTML += TEMPLATES.paginator.prevButton();
      
      // 頁碼按鈕
      const currentPage = appState.currentPage || 1;
      const maxPagesToShow = CONFIG.PAGINATION.MAX_PAGES_DISPLAY;
      
      let startPage = Math.max(1, currentPage - Math.floor(maxPagesToShow / 2));
      let endPage = Math.min(totalPages, startPage + maxPagesToShow - 1);
      
      // 調整起始頁碼
      if (endPage - startPage + 1 < maxPagesToShow) {
        startPage = Math.max(1, endPage - maxPagesToShow + 1);
      }
      
      // 第一頁
      if (startPage > 1) {
        paginatorHTML += TEMPLATES.paginator.item(1);
        if (startPage > 2) {
          paginatorHTML += TEMPLATES.paginator.ellipsis();
        }
      }
      
      // 頁碼
      for (let i = startPage; i <= endPage; i++) {
        const isActive = i === currentPage;
        paginatorHTML += TEMPLATES.paginator.pageNumber(i, isActive);
      }
      
      // 最後一頁
      if (endPage < totalPages) {
        if (endPage < totalPages - 1) {
          paginatorHTML += TEMPLATES.paginator.ellipsis();
        }
        paginatorHTML += TEMPLATES.paginator.item(totalPages);
      }
      
      // 下一頁按鈕
      paginatorHTML += TEMPLATES.paginator.nextButton();
      
      paginatorHTML += '</ul>';
      paginator.innerHTML = paginatorHTML;
      
      // 設定分頁事件
      DOM.pagination.setupPaginatorEvents();
      
      console.log('DOM.pagination.renderPaginator: 分頁器渲染完成，總頁數:', totalPages);
    },
    
    // 設定分頁事件
    setupPaginatorEvents: () => {
      console.log('DOM.pagination.setupPaginatorEvents called：設定分頁事件');
      const paginator = DOM.getElement(CONFIG.SELECTORS.PAGINATOR);
      if (!paginator) return;
      
      const pageLinks = paginator.querySelectorAll(`.${CONFIG.CLASSES.PAGINATOR_LINK}`);
      
      pageLinks.forEach(link => {
        DOM.events.add(link, 'click', (e) => {
          e.preventDefault();
          
          const page = link.dataset.page;
          const currentPage = appState.currentPage || 1;
          const totalPages = Math.ceil((appState.totalGivers || appState.givers.length) / CONFIG.PAGINATION.GIVERS_PER_PAGE);
          
          let targetPage = currentPage;
          
          if (page === 'prev') {
            targetPage = Math.max(1, currentPage - 1);
          } else if (page === 'next') {
            targetPage = Math.min(totalPages, currentPage + 1);
          } else {
            targetPage = parseInt(page);
          }
          
          if (targetPage !== currentPage && targetPage >= 1 && targetPage <= totalPages) {
            console.log('DOM.pagination.setupPaginatorEvents: 切換到第', targetPage, '頁');
            DOM.pagination.goToPage(targetPage);
          }
        });
      });
    },
    
    // 切換到指定頁面
    goToPage: async (page) => {
      console.log('DOM.pagination.goToPage called：切換到第', page, '頁');
      
      // 更新當前頁面
      appState.currentPage = page;
      
      try {
        // 確保 appState.givers 包含完整的資料集
        if (!appState.givers || appState.givers.length === 0) {
          appState.givers = DOM.dataLoader.extractGiversFromDOM();
        }
        
        // 使用本地資料進行分頁
        const pageGivers = DOM.pagination.getGiversByPage(page);
        
        console.log('DOM.pagination.goToPage: 載入第', page, '頁資料，共', pageGivers.length, '筆');
        
        // 顯示對應頁面的 Giver 卡片
        DOM.pagination.showPageGivers(pageGivers);
        
        // 重新渲染分頁器
        DOM.pagination.renderPaginator(appState.totalGivers || appState.givers.length);
        
        // 滾動到頂部
        window.scrollTo({ top: 0, behavior: 'smooth' });
        
      } catch (error) {
        console.error('DOM.pagination.goToPage: 載入頁面資料失敗:', error);
        // 如果載入失敗，顯示錯誤訊息
        DOM.pagination.showError('載入頁面資料失敗，請重新整理頁面');
      }
    },
    
    // 顯示指定頁面的 Giver 卡片
    showPageGivers: (pageGivers) => {
      console.log('DOM.pagination.showPageGivers called：顯示頁面 Giver 卡片', { count: pageGivers.length });
      
      const giverPanel = DOM.getElement(CONFIG.SELECTORS.GIVER_PANEL);
      if (!giverPanel) {
        console.error('DOM.pagination.showPageGivers: Giver 面板元素未找到');
        return;
      }
      
      // 隱藏所有 Giver 卡片（包括父容器）
      const allGiverCards = giverPanel.querySelectorAll('.giverCard[data-id]');
      allGiverCards.forEach(card => {
        // 隱藏整個卡片容器（包括 col-sm-3 包裝器）
        const cardContainer = card.closest('.col-sm-3');
        if (cardContainer) {
          cardContainer.style.display = 'none';
        } else {
          card.style.display = 'none';
        }
      });
      
      // 顯示當前頁面的 Giver 卡片
      pageGivers.forEach(giver => {
        const card = giverPanel.querySelector(`.giverCard[data-id="${giver.id}"]`);
        if (card) {
          // 顯示整個卡片容器（包括 col-sm-3 包裝器）
          const cardContainer = card.closest('.col-sm-3');
          if (cardContainer) {
            cardContainer.style.display = 'block';
          } else {
            card.style.display = 'block';
          }
        }
      });
      
      console.log('DOM.pagination.showPageGivers: 已顯示', pageGivers.length, '筆 Giver 卡片');
    },
    
    // 顯示錯誤訊息
    showError: (message) => {
      console.error('DOM.pagination.showError:', message);
      
      const giverPanel = DOM.getElement(CONFIG.SELECTORS.GIVER_PANEL);
      if (giverPanel) {
        giverPanel.innerHTML = `
          <div class="alert alert-warning text-center" role="alert">
            <i class="fas fa-exclamation-triangle me-2"></i>
            ${message}
          </div>
        `;
      }
    }
  },

  // 清理全域事件監聽器、定時器與快取
  cleanup: () => {
    // 1. 清理全域事件監聽器
    document.removeEventListener('click', EventManager.handleGlobalClick);
    document.removeEventListener('submit', EventManager.handleGlobalSubmit);
    document.removeEventListener('change', EventManager.handleGlobalChange);
    // 若有其他全域事件監聽器，請一併移除

    // 2. 清理定時器
    if (window.__DOM_INTERVALS__) {
      window.__DOM_INTERVALS__.forEach(clearInterval);
      window.__DOM_INTERVALS__ = [];
    }
    if (window.__DOM_TIMEOUTS__) {
      window.__DOM_TIMEOUTS__.forEach(clearTimeout);
      window.__DOM_TIMEOUTS__ = [];
    }

    // 3. 清理快取
    if (typeof DOM_CACHE === 'object' && typeof DOM_CACHE.resetAll === 'function') {
      DOM_CACHE.resetAll();
    }
    if (typeof ChatStateManager === 'object' && typeof ChatStateManager.reset === 'function') {
      ChatStateManager.reset();
    }
    // 4. 其他自定義清理
    // ...
    console.log('DOM.cleanup: 已清理全域事件監聽器、定時器與快取');
  },
};

// ======================================================
//   4-3. UI 互動模組 (UI Interaction Module)
// ======================================================

const UIInteraction = {
  // 開啟聊天對話框
  openChatDialog: (giver) => {
    console.log('UIInteraction.openChatDialog called', { giver });
    DOM.chat.init(giver);
  },
  
  // 顯示確認對話框
  showConfirmDialog: (options) => {
    console.log('UIInteraction.showConfirmDialog called', { options });
    const { // options 是一個物件，預設為以下屬性：
      title = '確認',
      message = '您確定要執行此操作嗎？',
      confirmText = '確定',
      cancelText = '取消',
      onConfirm = () => {}, // 預設為空函式
      onCancel = () => {}, // 預設為空函式
      cleanupBackdrop = true // 預設為 true，控制是否清理 backdrop 背景遮罩
    } = options;
    
    // 更新確認對話框內容
    const modalTitle = DOM.confirm.title();
    const modalMessage = DOM.confirm.message();
    const confirmBtn = DOM.confirm.confirmBtn();
    const cancelBtn = DOM.confirm.cancelBtn();
    
    if (modalTitle) DOM.utils.setTextContent(modalTitle, title);
    if (modalMessage) DOM.utils.setTextContent(modalMessage, message);
    if (confirmBtn) DOM.utils.setTextContent(confirmBtn, confirmText);
    if (cancelBtn) DOM.utils.setTextContent(cancelBtn, cancelText);
    
    // 確認按鈕事件監聽器（內部函式）：當使用者點擊確認按鈕時，會執行 onConfirm 函式，這通常是實際要執行的業務邏輯（如刪除資料、取消預約等）
    const confirmHandler = async () => {
      console.log('confirmHandler called');
      onConfirm(); // 執行傳入的 onConfirm 函式，這通常是實際要執行的業務邏輯（如刪除資料、取消預約等）
      const modal = bootstrap.Modal.getInstance(DOM.confirm.modal());
      if (modal) {
        modal.hide(); // 隱藏對話框
        // 只有在需要清理 backdrop 時才清理
        if (cleanupBackdrop) {
          await nonBlockingDelay(DELAY_TIMES.UI.MODAL_CLEANUP, () => {
            ModalCleanupUtils.quickCleanup();
            // 強制處理焦點問題
            document.body.focus();
          });
        }
      }
    };
    
    // 取消按鈕事件監聽器（內部函式）：當使用者點擊取消按鈕時，會執行 onCancel 函式，這通常是實際要執行的業務邏輯（如取消預約等）
    const cancelHandler = async () => {
      console.log('cancelHandler called');
      onCancel(); // 執行傳入的 onCancel 函式，這通常是實際要執行的業務邏輯（如取消預約等）
      const modal = bootstrap.Modal.getInstance(DOM.confirm.modal());
      if (modal) {
        modal.hide();
        // 確保 backdrop 被清理
        await nonBlockingDelay(DELAY_TIMES.UI.MODAL_CLEANUP, () => {
          ModalCleanupUtils.quickCleanup();
          // 強制處理焦點問題
          document.body.focus();
        });
      }
    };
    
    // 移除舊的事件監聽器：解決重覆綁定事件監聽器
    if (confirmBtn) { // 如果確認按鈕存在
      // 使用 cloneNode 來移除所有舊的事件監聽器
      const newConfirmBtn = confirmBtn.cloneNode(true); // 複製確認按鈕
      confirmBtn.parentNode.replaceChild(newConfirmBtn, confirmBtn); // 替換確認按鈕
      newConfirmBtn.addEventListener('click', confirmHandler); // 綁定確認按鈕的事件監聽器
    }
    
    if (cancelBtn) { // 如果取消按鈕存在
      const newCancelBtn = cancelBtn.cloneNode(true); // 複製取消按鈕
      cancelBtn.parentNode.replaceChild(newCancelBtn, cancelBtn); // 替換取消按鈕
      newCancelBtn.addEventListener('click', cancelHandler); // 綁定取消按鈕的事件監聽器
    }
    
    // 顯示確認對話框，讓使用者可以看到確認對話框並進行相應的操作。
    const modal = new bootstrap.Modal(DOM.confirm.modal());
    modal.show();
  }
};

// ======================================================
//   4-4. UI 組件模組 (UIComponents)
// ======================================================

const UIComponents = {
  // 產生按鈕
  button: ({ text = '', className = '', icon = '', attrs = {} } = {}) => {
    console.log('UIComponents.button called: 產生按鈕', { text, className, icon, attrs });
    const btn = document.createElement('button');
    btn.type = 'button';
    btn.className = className;
    if (icon) {
      const iconElem = document.createElement('i');
      iconElem.className = icon;
      btn.appendChild(iconElem);
      if (text) btn.appendChild(document.createTextNode(' '));
    }
    if (text) btn.appendChild(document.createTextNode(text));
    Object.entries(attrs).forEach(([k, v]) => btn.setAttribute(k, v));
    return btn;
  },

  // 產生確認對話框
  confirmDialog: ({ title = '', message = '', confirmText = '確定', cancelText = '取消', onConfirm, onCancel }) => {
    console.log('UIComponents.confirmDialog called: 產生確認對話框', { title, message, confirmText, cancelText });
    // 可根據現有 showConfirmDialog 實作
    return showConfirmDialog({ title, message, confirmText, cancelText, onConfirm, onCancel });
  },

  // 產生 Toast 訊息
  toast: ({ message = '', type = 'info', duration = 2000 }) => {
    console.log('UIComponents.toast called: 產生 Toast 訊息', { message, type, duration });
    const toast = document.createElement('div');
    toast.className = `ui-toast ui-toast-${type}`;
    toast.textContent = message;
    document.body.appendChild(toast);
    setTimeout(() => { toast.remove(); }, duration);
    return toast;
  },

  // 產生載入動畫
  spinner: ({ size = 'md', className = '' } = {}) => {
    console.log('UIComponents.spinner called: 產生載入動畫', { size, className });
    const spinner = document.createElement('div');
    spinner.className = `ui-spinner spinner-border spinner-border-${size} ${className}`;
    spinner.setAttribute('role', 'status');
    spinner.innerHTML = '<span class="visually-hidden">Loading...</span>';
    return spinner;
  },

  // 產生 icon
  icon: (iconClass = '', extraClass = '') => {
    console.log('UIComponents.icon called: 產生 icon', { iconClass, extraClass });
    const icon = document.createElement('i');
    icon.className = `${iconClass} ${extraClass}`.trim();
    return icon;
  }
};

// ======================================================================
//   5. 事件和狀態管理：依賴 UI 模組 (Event and State Management: Dependencies on UI Modules)
// ======================================================================

// ======================================================
//   5-1. 統一事件委派管理器 (Event Delegation Manager)
// ======================================================

const EventManager = {
  // 事件處理器映射
  handlers: new Map(),
  
  // 初始化事件委派
  init() {
    console.log('EventManager: 初始化事件委派系統');
    
    // 綁定全域點擊事件委派
    document.addEventListener('click', this.handleGlobalClick.bind(this));
    
    // 綁定全域提交事件委派
    document.addEventListener('submit', this.handleGlobalSubmit.bind(this));
    
    // 綁定全域變更事件委派
    document.addEventListener('change', this.handleGlobalChange.bind(this));
    
    console.log('EventManager: 事件委派系統初始化完成');
  },
  
  // 全域點擊事件委派處理
  handleGlobalClick(e) {
    const target = e.target;
    
    // 處理各種按鈕類型
    if (target.matches('.btn-option')) {
      this.handleOptionButton(target, e);
    } else if (target.matches('.edit-provide-btn, .schedule-edit-btn')) {
      this.handleEditButton(target, e);
    } else if (target.matches('.delete-provide-btn, .schedule-delete-btn')) {
      this.handleDeleteButton(target, e);
    } else if (target.matches('.cancel-reservation-btn')) {
      this.handleCancelReservation(target, e);
    } else if (target.matches('#cancel-schedule-form')) {
      this.handleCancelScheduleForm(target, e);
    } else if (target.matches('.calendar-day')) {
      this.handleCalendarDayClick(target, e);
    } else if (target.matches('.date-input')) {
      this.handleDateInputClick(target, e);
    }
  },
  
  // 全域提交事件委派處理
  handleGlobalSubmit(e) {
    console.log('EventManager: 全域提交事件觸發', { target: e.target.id });
    if (e.target.matches('#time-schedule-form')) {
      e.preventDefault();
      console.log('EventManager: 處理時間表單提交');
      this.handleScheduleFormSubmit(e.target, e);
    }
  },
  
  // 全域變更事件委派處理
  handleGlobalChange(e) {
    if (e.target.matches('.schedule-date, .schedule-start-time, .schedule-end-time')) {
      this.handleScheduleInputChange(e.target, e);
    }
  },
  
  // 處理選項按鈕
  handleOptionButton: createButtonHandler('option', {
    dataAttributes: ['data-option'],
    logMessage: '選項按鈕被點擊',
    
    // 預處理：跳過聊天模組專門處理的選項按鈕
    preprocess: (data, btn, e) => {
      if (btn.closest('.chat-options-buttons') && data.option === 'cancel') {
        console.log('EventManager: 跳過聊天模組專門處理的選項按鈕');
        return false;
      }
      return true;
    },
    
    // 主要處理邏輯
    handler: async (data, btn, e) => {
      const { option } = data;
      
      console.log('EventManager: 處理選項按鈕', { option, data });
      
      // 處理不同選項
      switch (option) {
        case 'schedule':
          DOM.chat.addUserMessage(`${CONFIG.UI_TEXT.BUTTONS.SCHEDULE}`);
          DOM.chat.handleSchedule();
          break;
        case 'skip':
          DOM.chat.addUserMessage(`${CONFIG.UI_TEXT.BUTTONS.SKIP}`);
          DOM.chat.handleSkip();
          break;
        case 'cancel':
          DOM.chat.addUserMessage(`${CONFIG.UI_TEXT.BUTTONS.CANCEL_SCHEDULE}`);
          DOM.chat.handleCancelSchedule();
          // 禁用整個 Giver 訊息泡泡中的互動元素
          DOM.chat.disableGiverMessageInteractions(btn);
          break;
        case 'view-times':
          DOM.chat.addUserMessage(`${CONFIG.UI_TEXT.BUTTONS.VIEW_GIVER_TIME}`);
          DOM.chat.handleViewGiverTime();
          break;  
        case 'view-my-schedules-reservation':
          DOM.chat.addUserMessage(`${CONFIG.UI_TEXT.BUTTONS.VIEW_MY_SCHEDULES_RESERVATION}`);
          DOM.chat.handleViewMySchedulesReservation();
          break;
        case 'view-all':
          DOM.chat.addUserMessage(`${CONFIG.UI_TEXT.BUTTONS.VIEW_MY_SCHEDULES_PROVIDE}`);
          DOM.chat.handleViewAllSchedules();
          break;
        case 'single-time':
          DOM.chat.addUserMessage(`${CONFIG.UI_TEXT.BUTTONS.PROVIDE_SINGLE_TIME}`);
          DOM.chat.handleSingleTime();
          break;
        case 'continue-single-time':
          DOM.chat.addUserMessage(`${CONFIG.UI_TEXT.BUTTONS.CONTINUE_PROVIDE_SINGLE_TIME}`);
          DOM.chat.handleSingleTime();
          break;
        case 'multiple-times':
          DOM.chat.addUserMessage(`${CONFIG.UI_TEXT.BUTTONS.PROVIDE_MULTIPLE_TIMES}`);
          DOM.chat.handleMultipleTimes();
          break;
        case 'continue-multiple-times':
          DOM.chat.addUserMessage(`${CONFIG.UI_TEXT.BUTTONS.CONTINUE_PROVIDE_MULTIPLE_TIMES}`);
          DOM.chat.handleMultipleTimes();
          break;
        case 'submit-schedules':
          console.log('EventManager: 進入 submit-schedules case');
          DOM.chat.addUserMessage(`${CONFIG.UI_TEXT.BUTTONS.SUBMIT_SCHEDULES}`);
          
          try {
            // 將草稿時段轉為正式提供時段
            const draftSchedules = ChatStateManager.get(ChatStateManager.CONFIG.STATE_KEYS.DRAFT_SCHEDULES) || [];
            console.log('EventManager: 檢查草稿時段', { draftSchedulesCount: draftSchedules.length, draftSchedules });
            
            if (draftSchedules.length > 0) {
              // 將草稿時段轉為正式提供時段（移除 isDraft 標記）
              const formalSchedules = draftSchedules.map(schedule => {
                const { isDraft, ...formalSchedule } = schedule;
                return formalSchedule;
              });
              console.log('EventManager: 草稿時段已轉換為正式時段', { formalSchedules });
              
              // 準備發送到後端的資料格式
              const currentGiver = ChatStateManager.get(ChatStateManager.CONFIG.STATE_KEYS.CURRENT_GIVER);
              
              // 檢查 currentGiver 是否存在
              if (!currentGiver) {
                console.error('EventManager: currentGiver 為 null，無法確定要發送給哪個 Giver');
                UIComponents.toast({ message: '無法確定要發送給哪個 Giver，請重新開始諮詢流程', type: 'error' });
                return;
              }
              
              const giverId = currentGiver.id; // 使用當前 Giver 的 ID
              console.log('EventManager: 使用 Giver ID', { giverId, giverName: currentGiver.name });
              
              const schedulesToSubmit = formalSchedules.map(schedule => ({
                giver_id: giverId,
                taker_id: 1, // 預設 【Demo】測試 Taker 的 user_id 為 1
                date: schedule.date.replace(/\//g, '-'), // 將日期格式從 YYYY/MM/DD 轉換為 YYYY-MM-DD
                start_time: schedule.startTime + ':00', // 添加秒數以符合 time 格式
                end_time: schedule.endTime + ':00', // 添加秒數以符合 time 格式
                note: schedule.notes || null
                // status 由後端根據 operator_role 自動決定
                // TAKER 建立 -> PENDING (等待 Giver 確認)
                // GIVER 建立 -> AVAILABLE (可預約)
              }));
              
              // 構建包含建立者資訊的請求體
              const requestBody = {
                schedules: schedulesToSubmit,
                created_by: 1, // 【Demo】測試 Taker 1 的 user_id  
                created_by_role: 'TAKER'
              };
              
              console.log('EventManager: 準備發送到後端的時段資料', { requestBody });
              
              // 發送 axios POST 請求到後端（統一後的端點，包含操作者資訊）
              const response = await APIClient.post('/api/v1/schedules', requestBody);
              console.log('EventManager: 後端回應', { response });
              
              // 將後端返回的 ID 更新到時段資料中
              const updatedFormalSchedules = formalSchedules.map((schedule, index) => {
                const backendSchedule = response[index];
                if (backendSchedule && backendSchedule.id) {
                  return {
                    ...schedule,
                    id: backendSchedule.id,
                    created_at: backendSchedule.created_at,
                    updated_at: backendSchedule.updated_at,
                    status: backendSchedule.status
                  };
                }
                return schedule;
              });
              
              console.log('EventManager: 更新後的時段資料', { 
                originalFormalSchedules: formalSchedules,
                updatedFormalSchedules: updatedFormalSchedules,
                backendResponse: response 
              });
              
              // 添加到正式提供時段列表
              const existingSchedules = ChatStateManager.getProvidedSchedules();
              const allSchedules = [...existingSchedules, ...updatedFormalSchedules];
              console.log('EventManager: 合併時段列表', { existingSchedulesCount: existingSchedules.length, updatedFormalSchedulesCount: updatedFormalSchedules.length, allSchedulesCount: allSchedules.length });
              ChatStateManager.set(ChatStateManager.CONFIG.STATE_KEYS.PROVIDED_SCHEDULES, allSchedules);
              
              // 清空草稿列表
              ChatStateManager.set(ChatStateManager.CONFIG.STATE_KEYS.DRAFT_SCHEDULES, []);
              console.log('EventManager: 草稿列表已清空');
              
              console.log('EventManager: 草稿時段已轉為正式提供時段並成功發送到後端', { 
                draftCount: draftSchedules.length, 
                totalFormalCount: allSchedules.length,
                backendResponse: response
              });
              
              // 顯示成功訊息
              UIComponents.toast({ message: '時段已成功送出給 Giver！', type: 'success' });
            } else {
              console.log('EventManager: 沒有草稿時段需要提交');
              UIComponents.toast({ message: '沒有新的時段需要提交', type: 'info' });
            }
            
          } catch (error) {
            console.error('EventManager: 提交時段到後端失敗', { error });
            
            // 檢查是否為時段重疊錯誤
            if (error.response && error.response.status === 400) {
              const errorDetail = error.response.data?.detail || error.response.data;
              if (typeof errorDetail === 'string' && errorDetail.includes('時段重複或重疊')) {
                // 顯示重疊錯誤訊息
                UIComponents.toast({ message: errorDetail, type: 'error' });
                console.log('EventManager: 檢測到時段重疊錯誤', { errorDetail });
              } else {
                UIComponents.toast({ message: errorDetail || '提交時段失敗，請稍後再試', type: 'error' });
              }
            } else {
              UIComponents.toast({ message: '提交時段失敗，請稍後再試', type: 'error' });
            }
          }
          
          // 先更新現有表格，確保編輯功能正常
          EventManager.updateScheduleDisplay();

          // 延遲顯示成功訊息泡泡
          console.log('EventManager: 準備延遲顯示成功訊息泡泡');
          await delay(DELAY_TIMES.CHAT.SUCCESS_MESSAGE);
          console.log('EventManager: 延遲完成，準備顯示成功訊息泡泡');
          DOM.chat.handleSuccessProvideTime();
          console.log('EventManager: submit-schedules case 處理完成');
          break;
        
        default:
          console.log('EventManager: 未知的選項按鈕', { option });
      }
    },
    
    // 成功回調：禁用整個 Giver 訊息泡泡中的互動元素
    onSuccess: (data, btn, e) => {      
      // 禁用整個 Giver 訊息泡泡中的互動元素
      DOM.chat.disableGiverMessageInteractions(btn);
    }
  }),
  
  // 處理編輯按鈕
  handleEditButton: createButtonHandler('edit', {
    dataAttributes: [],
    logMessage: '編輯按鈕被點擊',
    
    // 主要處理邏輯
    handler: async (data, btn, e) => {
      const { index, isScheduleTable, isSuccessProvideTable } = data;
      
      if (isScheduleTable) {
        // 處理包含草稿和正式時段的表格
        const providedSchedules = ChatStateManager.getProvidedSchedules();
        const draftSchedules = ChatStateManager.get(ChatStateManager.CONFIG.STATE_KEYS.DRAFT_SCHEDULES) || [];
        
        // 合併所有時段以找到要編輯的時段
        const { allSchedules } = getAllSchedulesWithDraftStatus();
        
        const scheduleToEdit = allSchedules[index];
        
        if (scheduleToEdit) {
          // 計算實際的編輯索引
          let actualEditIndex;
          if (scheduleToEdit.isDraft) {
            // 如果是草稿時段，計算在草稿陣列中的實際索引
            const draftIndex = index - providedSchedules.length;
            actualEditIndex = providedSchedules.length + draftIndex;
          } else {
            // 如果是正式提供時段，使用原始索引
            actualEditIndex = index;
          }
          
          // 傳遞編輯索引和時段資料，並標記是否為草稿
          const editData = {
            index: actualEditIndex,
            ...scheduleToEdit,
            isDraft: scheduleToEdit.isDraft
          };
          console.log('EventManager: 找到要編輯的時段', { 
            originalIndex: index, 
            actualEditIndex, 
            isDraft: scheduleToEdit.isDraft,
            editData 
          });
          DOM.chat.handleSingleTime(actualEditIndex, editData);
        } else {
          console.error('EventManager: 找不到要編輯的時段', { 
            index, 
            totalSchedules: allSchedules.length,
            providedSchedules: providedSchedules.length,
            draftSchedules: draftSchedules.length
          });
        }
      } else if (isSuccessProvideTable) {
        // 處理成功提供表格（只有正式提供時段）
        const schedules = ChatStateManager.getProvidedSchedules();
        const schedule = schedules[index];
        console.log('EventManager: 編輯成功提供表格中的時段', { index, schedule });
        
        if (schedule) {
          // 傳遞編輯索引和時段資料
          const editData = {
            index: index,
            ...schedule,
            isDraft: false
          };
          console.log('EventManager: 找到要編輯的成功提供時段', editData);
          DOM.chat.handleSingleTime(index, editData);
        } else {
          console.error('EventManager: 找不到要編輯的時段', { index, totalSchedules: schedules.length });
        }
      } else {
        // 處理其他表格（如成功提供表格）
        const schedules = ChatStateManager.getProvidedSchedules();
        const schedule = schedules[index];
        console.log('EventManager: 編輯正式提供時段', { index, schedule });
        DOM.chat.handleSingleTime(index, schedule);
      }
    }
  }),
  
  // 處理刪除按鈕
  handleDeleteButton: createButtonHandler('delete', {
    dataAttributes: [],
    logMessage: '刪除按鈕被點擊',
    
    // 主要處理邏輯
    handler: async (data, btn, e) => {
      const { index, isProvideTable, isScheduleTable } = data;
      
      const dialogConfig = isProvideTable ? {
        title: '取消提供時間',
        message: '確定要取消提供此時間嗎？',
        confirmText: '取消提供',
        cancelText: '保留'
      } : {
        title: '刪除時段',
        message: '確定要刪除此時段嗎？',
        confirmText: '刪除',
        cancelText: '取消'
      };
      
      return new Promise((resolve) => {
        UIComponents.confirmDialog({
          ...dialogConfig,
          onConfirm: async () => {
            console.log('EventManager: 刪除按鈕被點擊', { index, isProvideTable, isScheduleTable });
      
            // 強制重設快取
            if (DOM_CACHE) DOM_CACHE.resetScheduleForm();

            // 獲取當前顯示的所有時段（包含正式提供和草稿）
            const providedSchedules = ChatStateManager.getProvidedSchedules();
            const draftSchedules = ChatStateManager.get(ChatStateManager.CONFIG.STATE_KEYS.DRAFT_SCHEDULES) || [];
            
            // 合併所有時段以找到要刪除的時段
            const { allSchedules } = getAllSchedulesWithDraftStatus();
            
            const scheduleToDelete = allSchedules[index];
            
            if (scheduleToDelete) {
              if (scheduleToDelete.isDraft) {
                // 刪除草稿時段
                const updatedDraftSchedules = draftSchedules.filter((_, idx) => {
                  const draftIndex = providedSchedules.length + idx;
                  return draftIndex !== index;
                });
                ChatStateManager.set(ChatStateManager.CONFIG.STATE_KEYS.DRAFT_SCHEDULES, updatedDraftSchedules);
                console.log('EventManager: 草稿時段已刪除', { deletedSchedule: scheduleToDelete, remainingDrafts: updatedDraftSchedules.length });
              } else {
                // 刪除正式提供時段 - 需要發送 API 請求到後端
                try {
                  // 獲取當前使用者和 Giver 資訊
                  const currentUserId = ChatStateManager.getCurrentUserId();
                  const currentGiver = ChatStateManager.getCurrentGiver();
                  
                  if (!currentUserId || !currentGiver) {
                    console.error('EventManager: 無法獲取使用者或 Giver 資訊', { currentUserId, currentGiver });
                    UIComponents.toast({ message: '刪除失敗：無法獲取使用者資訊', type: 'error' });
                    return;
                  }
                  
                  // 發送刪除請求到後端
                  const deleteRequest = {
                    deleted_by: currentUserId,
                    deleted_by_role: scheduleToDelete.role || 'TAKER'  
                  };
                  
                  console.log('EventManager: 發送刪除請求到後端', { 
                    scheduleId: scheduleToDelete.id, 
                    deleteRequest 
                  });
                  
                  // 使用 APIClient 發送 DELETE 請求
                  await APIClient.delete(`/api/v1/schedules/${scheduleToDelete.id}`, {
                    data: deleteRequest,
                    headers: { 'Content-Type': 'application/json' }
                  });
                  
                  // 刪除成功後，更新前端狀態
                  const updatedProvidedSchedules = providedSchedules.filter((_, idx) => idx !== index);
                  ChatStateManager.set(ChatStateManager.CONFIG.STATE_KEYS.PROVIDED_SCHEDULES, updatedProvidedSchedules);
                  console.log('EventManager: 正式提供時段已刪除', { deletedSchedule: scheduleToDelete, remainingProvided: updatedProvidedSchedules.length });
                  
                  UIComponents.toast({ message: '時段已成功刪除', type: 'success' });
                  
                } catch (error) {
                  console.error('EventManager: 刪除時段失敗', error);
                  UIComponents.toast({ message: '刪除失敗：' + (error.response?.data?.detail || error.message), type: 'error' });
                  return; // 不更新前端狀態
                }
              }
            }
            
            // 檢查是否還有任何時段
            const remainingProvided = ChatStateManager.getProvidedSchedules();
            const remainingDrafts = ChatStateManager.get(ChatStateManager.CONFIG.STATE_KEYS.DRAFT_SCHEDULES) || [];
            
            if (remainingProvided.length === 0 && remainingDrafts.length === 0) {
              DOM.chat.addGiverResponse('已取消所有提供時間。<br><br>如未來有需要預約 Giver 時間，請使用聊天輸入區域下方的功能按鈕。<br><br>有其他問題需要協助嗎？');
            } else {
              // 使用 updateScheduleDisplay 方法更新所有相關表格
              EventManager.updateScheduleDisplay();
              console.log('EventManager: 所有時段表格已更新');
            }
            resolve();
          }
        });
      });
    }
  }),
  
  // 處理取消預約按鈕
  handleCancelReservation: createButtonHandler('cancelReservation', {
    dataAttributes: ['data-schedule-id'],
    logMessage: '取消預約按鈕被點擊',
    
    // 主要處理邏輯
    handler: async (data, btn, e) => {
      const { scheduleId } = data;
      
      return new Promise((resolve) => {
        UIComponents.confirmDialog({
          title: '取消預約',
          message: '確定要取消此預約嗎？',
          confirmText: '取消預約',
          cancelText: '保留',
          onConfirm: () => {
            // 從狀態管理中移除預約
            const bookedSchedules = ChatStateManager.get(ChatStateManager.CONFIG.STATE_KEYS.BOOKED_SCHEDULES) || [];
            const updatedSchedules = bookedSchedules.filter(schedule => schedule.id !== scheduleId);
            ChatStateManager.set(ChatStateManager.CONFIG.STATE_KEYS.BOOKED_SCHEDULES, updatedSchedules);
            
            // 更新顯示
            DOM.chat.updateBookedSchedulesDisplay(updatedSchedules);
            
            console.log('EventManager: 預約已取消', { scheduleId, remainingCount: updatedSchedules.length });
            resolve();
          }
        });
      });
    }
  }),
  
  // 處理取消表單按鈕
  handleCancelScheduleForm: createButtonHandler('cancelScheduleForm', {
    dataAttributes: [],
    logMessage: '取消表單按鈕被點擊',
    
    // 主要處理邏輯
    handler: async (data, btn, e) => {
      // 隱藏表單
      const scheduleForm = DOM_CACHE.scheduleForm;
      if (scheduleForm) {
        scheduleForm.classList.remove('schedule-form-visible');
        scheduleForm.classList.add('schedule-form-hidden');
      }
      
      // 清空表單
      DOM_CACHE.clearFormInputs();

      // 清空表單所有錯誤訊息
      FormValidator.clearAllValidationErrors(DOM_CACHE.scheduleForm);
          
      // 重置選中的日期
      ChatStateManager.setSelectedDate(null);
      
      // 顯示取消訊息
      DOM.chat.addGiverResponse('您已取消新增時段。<br><br>如果仍想提供方便時段，請使用聊天輸入區域下方的功能按鈕。<br><br>有其他問題需要協助嗎？');
    }
  }),
  
  // 處理表單提交
  async handleScheduleFormSubmit(form, e) {
    
    const formData = DOM_CACHE.getFormData();
    
    
    // 驗證表單
    const validationResult = FormValidator.validateScheduleForm(formData);
    if (!validationResult.isValid) {
      console.warn('EventManager: 表單驗證失敗', validationResult);
      
      // 過濾掉隱藏的錯誤訊息
      const visibleErrors = validationResult.errors.filter(error => error !== '__HIDDEN_ERROR__');
      
      if (visibleErrors.length > 0) {
        // 時間邏輯錯誤顯示在表單下方，多數人休息時間錯誤使用彈出顯示
        if (validationResult.message && validationResult.message !== '__HIDDEN_ERROR__' && 
            validationResult.message.includes('多數人休息時間')) {
          FormValidator.showValidationError(validationResult.message);
        } else if (visibleErrors.length > 0) {
          // 根據錯誤訊息類型，顯示在對應的欄位下方
          const errorMessage = visibleErrors[0];
          let targetElement = form; // 預設顯示在表單上
          
          // 檢查錯誤訊息類型，決定顯示位置
          if (errorMessage.includes('日期格式不正確') || 
              errorMessage.includes('不能選擇過去的日期') || 
              errorMessage.includes('不能預約 3 個月後的日期')) {
            targetElement = document.getElementById('schedule-date');
          } else if (errorMessage.includes('請輸入開始時間') || 
                     errorMessage.includes('目前輸入內容非 4 位數字')) {
            targetElement = document.getElementById('schedule-start-time');
          } else if (errorMessage.includes('請輸入結束時間')) {
            targetElement = document.getElementById('schedule-end-time');
          } else if (errorMessage.includes('備註不能超過')) {
            targetElement = document.getElementById('schedule-notes');
          }
          
          FormValidator.showValidationError(errorMessage, targetElement);
        }
      }
      return;
    }
    
    // 檢查重複時段
    const existingSchedules = ChatStateManager.getProvidedSchedules();
    const editIndex = form.getAttribute('data-edit-index');
    const isEditMode = editIndex !== null && editIndex !== undefined && editIndex !== 'null' && editIndex !== '';

    const isDuplicate = checkScheduleOverlap(formData, existingSchedules, editIndex);
    
    // 檢測重複或重疊時段
    if (isDuplicate) {
      console.warn('EventManager: 檢測到重複或重疊時段', formData);
      const duplicateMessage = FormValidator.generateDuplicateScheduleMessage(formData, existingSchedules);
      FormValidator.showValidationError(duplicateMessage);
      return;
    }
    
    // 處理編輯模式
    if (isEditMode) {
      console.log('EventManager: 編輯模式，覆蓋原本的時段', isEditMode);
      
      // 檢查是否為草稿時段的編輯
      const isDraftEdit = form.getAttribute('data-edit-is-draft') === 'true';
      
      // 獲取所有現有時段（除了正在編輯的時段）
      const providedSchedules = ChatStateManager.getProvidedSchedules();
      const draftSchedules = ChatStateManager.get(ChatStateManager.CONFIG.STATE_KEYS.DRAFT_SCHEDULES) || [];
      
      // 創建不包含正在編輯時段的列表
      const otherSchedules = [];
      
      if (isDraftEdit) {
        // 編輯草稿時段：排除正在編輯的草稿時段
        const actualDraftIndex = parseInt(editIndex) - providedSchedules.length;
        providedSchedules.forEach((schedule, index) => {
          otherSchedules.push(schedule);
        });
        draftSchedules.forEach((schedule, index) => {
          if (index !== actualDraftIndex) {
            otherSchedules.push(schedule);
          }
        });
      } else {
        // 編輯正式提供時段：排除正在編輯的正式時段
        providedSchedules.forEach((schedule, index) => {
          if (index !== parseInt(editIndex)) {
            otherSchedules.push(schedule);
          }
        });
        draftSchedules.forEach((schedule, index) => {
          otherSchedules.push(schedule);
        });
      }
      
      // 檢查修改後的時段是否與其他時段重複或重疊
      const isDuplicate = checkScheduleOverlap(formData, otherSchedules, editIndex);
      
      // 檢測重複或重疊時段
      if (isDuplicate) {
        console.warn('EventManager: 編輯模式檢測到重複或重疊時段', formData);
        const duplicateMessage = FormValidator.generateDuplicateScheduleMessage(formData, otherSchedules);
        if (duplicateMessage) {
          FormValidator.showValidationError(duplicateMessage);
        } else {
          // 如果無法生成詳細訊息，使用預設錯誤訊息
          const errorMessage = '抱歉，您修改的時段與其他時段重複或重疊，請重新輸入。';
          FormValidator.showValidationError(errorMessage);
        }
        return;
      }
      
      // 沒有重複，執行更新
      if (isDraftEdit) {
        // 編輯草稿時段
        const actualDraftIndex = parseInt(editIndex) - providedSchedules.length;
        
        if (actualDraftIndex >= 0 && actualDraftIndex < draftSchedules.length) {
          draftSchedules[actualDraftIndex] = { 
            ...draftSchedules[actualDraftIndex], 
            ...formData,
            formattedSchedule: DOM.chat.formatScheduleWithWeekday(formData.date, formData.startTime, formData.endTime)
          };
          ChatStateManager.set(ChatStateManager.CONFIG.STATE_KEYS.DRAFT_SCHEDULES, draftSchedules);
          console.log('EventManager: 草稿時段已更新', { actualDraftIndex, updatedSchedule: draftSchedules[actualDraftIndex] });
        }
      } else {
        // 編輯正式提供時段
        providedSchedules[editIndex] = { 
          ...providedSchedules[editIndex], 
          ...formData,
          formattedSchedule: DOM.chat.formatScheduleWithWeekday(formData.date, formData.startTime, formData.endTime)
        };
        ChatStateManager.set(ChatStateManager.CONFIG.STATE_KEYS.PROVIDED_SCHEDULES, providedSchedules);
        console.log('EventManager: 正式提供時段已更新', { editIndex, updatedSchedule: providedSchedules[editIndex] });
      }
      
      // 隱藏表單
      const scheduleForm = document.getElementById('schedule-form');
      if (scheduleForm) {
        scheduleForm.classList.remove('schedule-form-visible');
        scheduleForm.classList.add('schedule-form-hidden');
      }
      
      // 更新顯示
      console.log('EventManager.handleScheduleFormSubmit: 編輯完成，準備更新表格顯示');
      this.updateScheduleDisplay();
      
      // 確保表格更新後，滾動到適當位置
      await nonBlockingDelay(DELAY_TIMES.CHAT.FORM_SUBMIT, () => {
        const chatMessages = DOM_CACHE.chatMessages;
        if (chatMessages) {
          chatMessages.scrollTop = chatMessages.scrollHeight;
        }
      });
      
      return;
    }
    
    // 新增模式
    const formattedSchedule = DOM.chat.formatScheduleWithWeekday(formData.date, formData.startTime, formData.endTime);
    
    // 檢查重複時段（在新增前就檢查）
    // 首先從資料庫載入已提供的時段
    const currentGiver = ChatStateManager.getCurrentGiver();
    const currentUserId = ChatStateManager.getCurrentUserId();
    
    if (currentGiver && currentUserId) {
      console.log('EventManager.handleScheduleFormSubmit: 載入資料庫中的已提供時段', { giverId: currentGiver.id, userId: currentUserId });
      
      const databaseSchedules = await ChatStateManager.loadUserSchedulesFromDatabase(currentGiver.id, currentUserId);
      console.log('EventManager.handleScheduleFormSubmit: 從資料庫載入的時段', databaseSchedules);
      
      // 將資料庫中的時段合併到已提供的時段中（避免重複）
      const existingProvidedSchedules = ChatStateManager.getProvidedSchedules();
      const existingIds = new Set(existingProvidedSchedules.map(s => s.id));
      
      // 只添加資料庫中不存在於當前已提供時段中的時段
      const newSchedules = databaseSchedules.filter(schedule => !existingIds.has(schedule.id));
      
      if (newSchedules.length > 0) {
        console.log('EventManager.handleScheduleFormSubmit: 新增資料庫中的時段到已提供時段', newSchedules);
        // 將新的時段添加到已提供時段列表中
        newSchedules.forEach(schedule => {
          ChatStateManager.addSchedule(schedule);
        });
      }
    }
    
    const existingSchedulesAfterLoad = ChatStateManager.getProvidedSchedules();
    const draftSchedulesAfterLoad = ChatStateManager.get(ChatStateManager.CONFIG.STATE_KEYS.DRAFT_SCHEDULES) || [];
    const allExistingSchedulesAfterLoad = [...existingSchedulesAfterLoad, ...draftSchedulesAfterLoad];
    
    // 將 formData 轉換為標準時段格式
    const newScheduleForCheck = {
      date: formData.date,
      startTime: formData.startTime,
      endTime: formData.endTime
    };

    console.log('EventManager.handleScheduleFormSubmit: 開始重疊檢查', {
      newSchedule: newScheduleForCheck,
      existingSchedulesCount: allExistingSchedulesAfterLoad.length,
      allExistingSchedules: allExistingSchedulesAfterLoad
    });

    const isDuplicateSchedule = checkScheduleOverlap(newScheduleForCheck, allExistingSchedulesAfterLoad);
    
    if (isDuplicateSchedule) {
      console.warn('EventManager.handleScheduleFormSubmit: 檢測到重複或重疊時段', formData);
      const duplicateMessage = FormValidator.generateDuplicateScheduleMessage(formData, allExistingSchedulesAfterLoad);
      FormValidator.showValidationError(duplicateMessage);
      return;
    }
    
    // 改為加入草稿狀態，而不是直接加入已提供時段列表
    const draftSchedule = {
      date: formData.date,
      startTime: formData.startTime,
      endTime: formData.endTime,
      notes: formData.notes.trim(),
      formattedSchedule: formattedSchedule,
      isDraft: true // 標記為草稿
    };
    
    // 使用 ChatStateManager.addDraftSchedule 方法添加草稿時段
    const addResult = ChatStateManager.addDraftSchedule({
      date: formData.date,
      startTime: formData.startTime,
      endTime: formData.endTime,
      notes: formData.notes.trim(),
      formattedSchedule: formattedSchedule
    });
    
    if (!addResult) {
      console.warn('EventManager.handleScheduleFormSubmit: 草稿時段添加失敗');
      FormValidator.showValidationError('抱歉，您輸入的時段添加失敗，請重新輸入。');
      return;
    }
    
    // 隱藏表單並清空
    const scheduleForm = DOM_CACHE.scheduleForm;
    if (scheduleForm) {
      scheduleForm.classList.remove('schedule-form-visible');
      scheduleForm.classList.add('schedule-form-hidden');
    }
    
    // 清除重複時段錯誤
    FormValidator.clearDuplicateScheduleError();
    
    DOM_CACHE.clearFormInputs();
    
    // 重置選中的日期
    ChatStateManager.setSelectedDate(null);
    
    // 模擬 Giver 回覆
    await nonBlockingDelay(DELAY_TIMES.CHAT.FORM_SUBMIT, () => {
      const responseHTML = TEMPLATES.chat.afterScheduleOptions(formattedSchedule, formData.notes);
      const chatMessages = DOM_CACHE.chatMessages;
      if (chatMessages) {
        chatMessages.insertAdjacentHTML('beforeend', responseHTML);
        chatMessages.scrollTop = chatMessages.scrollHeight;
      }
    });
  },
  
  // 處理日曆日期點擊
  handleCalendarDayClick(dayElement, e) {
    const date = dayElement.getAttribute('data-date');
    
    // 立即驗證選擇的日期
    if (date && !DateUtils.validateDateWithinAllowedMonths(date, true)) {
      return; // 不設定選中的日期，讓使用者重新選擇
    }
    
    ChatStateManager.setSelectedDate(date);
  },
  
  // 處理日期輸入框點擊
  handleDateInputClick(input, e) {
    DOM.chat.showDatePicker();
  },
  
  // 處理表單輸入變更
  handleScheduleInputChange(input, e) {
    const field = input.id;
    const value = input.value;
    
    // 當使用者修改任何輸入欄位時，清除重複時段錯誤
    FormValidator.clearDuplicateScheduleError();
    
    // 可以在這裡添加即時驗證邏輯
  },
  
  // 更新時段顯示
  updateScheduleDisplay() {
    const chatMessages = DOM_CACHE.chatMessages;
    if (!chatMessages) return;
    
    // 獲取最新的時段資料
    const providedSchedules = ChatStateManager.getProvidedSchedules();
    const draftSchedules = ChatStateManager.get(ChatStateManager.CONFIG.STATE_KEYS.DRAFT_SCHEDULES) || [];
    
    // 合併所有時段
    const { allSchedules } = getAllSchedulesWithDraftStatus();
    
    console.log('EventManager.updateScheduleDisplay: 更新時段顯示', { 
      providedSchedules: providedSchedules.length, 
      draftSchedules: draftSchedules.length,
      allSchedules: allSchedules.length 
    });
    
    // 檢查是否有草稿時段
    const hasDraftSchedules = draftSchedules.length > 0;
    
    // 更新所有相關的表格
    // 1. 更新成功提供時間表格（只顯示正式提供的時段）
    const successMessages = chatMessages.querySelectorAll('.success-provide-table');
    successMessages.forEach(successTable => {
      const giverMessage = successTable.closest('.giver-message');
      if (giverMessage) {
        // 計算正式提供時段在全域索引中的起始位置
        // 由於成功提供表格只顯示正式提供時段，所以起始索引為 0
        const startIndex = 0;
        const updatedHTML = TEMPLATES.chat.successProvideTime(providedSchedules, startIndex);
        giverMessage.outerHTML = updatedHTML;
        console.log('EventManager.updateScheduleDisplay: 成功提供表格已更新', { startIndex });
      }
    });
    
    // 2. 更新查看所有時段表格（顯示所有時段，包含草稿）
    const scheduleTables = chatMessages.querySelectorAll('.schedule-table');
    scheduleTables.forEach(scheduleTable => {
      const giverMessage = scheduleTable.closest('.giver-message');
      if (giverMessage) {
        // 根據是否有草稿時段決定是否顯示按鈕
        const includeButtons = hasDraftSchedules;
        
        // 使用共用函數生成表格
        const updatedHTML = generateScheduleTable(allSchedules, includeButtons);
        
        giverMessage.outerHTML = updatedHTML;
        console.log('EventManager.updateScheduleDisplay: 查看所有時段表格已更新', { includeButtons });
        
        // 重新設定選項按鈕事件監聽器
        const newGiverMessage = chatMessages.querySelector('.giver-message:last-child');
        if (newGiverMessage) {
          DOM.chat.setupOptionButtons();
        }
      }
    });
    
    // 3. 更新所有包含時段資料的 giver-message（以防有其他類型的表格）
    const giverMessages = chatMessages.querySelectorAll('.giver-message');
    giverMessages.forEach(giverMessage => {
      // 檢查是否包含時段相關的內容
      const hasScheduleContent = giverMessage.querySelector('.schedule-table, .success-provide-table, .schedule-item');
      if (hasScheduleContent && !giverMessage.querySelector('.schedule-table, .success-provide-table')) {
        // 如果包含時段內容但沒有主要表格，可能是其他類型的時段顯示
        // 這裡可以根據需要添加其他表格類型的更新邏輯
        console.log('EventManager.updateScheduleDisplay: 發現其他類型的時段顯示，可能需要更新');
      }
    });
    
    // 滾動到底部
    chatMessages.scrollTop = chatMessages.scrollHeight;
  }
};

// ======================================================
//   5-2. 錯誤處理模組 (Error Handling Module)
// ======================================================

// 錯誤型別常數
const ERROR_TYPES = {
  NETWORK: 'NETWORK_ERROR',
  VALIDATION: 'VALIDATION_ERROR',
  DOM: 'DOM_ERROR',
  BUSINESS: 'BUSINESS_ERROR',
  UNKNOWN: 'UNKNOWN_ERROR'
};

// 錯誤處理器：包含多個處理函數的集合，用於處理不同類型的錯誤
const errorHandlers = {
  [ERROR_TYPES.NETWORK]: (error) => {
    console.error('DOM.errorHandler.handle: 網路錯誤:', error);
    return {
      type: ERROR_TYPES.NETWORK,
      message: CONFIG.MESSAGES.ERROR.NETWORK,
      originalError: error,
      timestamp: new Date(),
      retryable: true
    };
  },
  [ERROR_TYPES.VALIDATION]: (error) => {
    console.error('DOM.errorHandler.handle: 驗證錯誤:', error);
    return {
      type: ERROR_TYPES.VALIDATION,
      message: CONFIG.MESSAGES.ERROR.VALIDATION,
      originalError: error,
      timestamp: new Date(),
      retryable: false
    };
  },
  [ERROR_TYPES.DOM]: (error) => {
    console.error('DOM.errorHandler.handle: DOM 錯誤:', error);
    return {
      type: ERROR_TYPES.DOM,
      message: 'DOM 操作失敗',
      originalError: error,
      timestamp: new Date(),
      retryable: false
    };
  },
  [ERROR_TYPES.BUSINESS]: (error) => {
    console.error('DOM.errorHandler.handle: 業務邏輯錯誤:', error);
    return {
      type: ERROR_TYPES.BUSINESS,
      message: error.message || '業務邏輯錯誤',
      originalError: error,
      timestamp: new Date(),
      retryable: false
    };
  },
  [ERROR_TYPES.UNKNOWN]: (error) => {
    console.error('DOM.errorHandler.handle: 未知錯誤:', error);
    return {
      type: ERROR_TYPES.UNKNOWN,
      message: CONFIG.MESSAGES.ERROR.UNKNOWN,
      originalError: error,
      timestamp: new Date(),
      retryable: false
    };
  }
};

// 錯誤處理器：單一的錯誤處理物件，包含錯誤歷史、錯誤處理器、錯誤類型等
const ErrorHandler = {
  ERROR_TYPES,
  handlers: errorHandlers,

  // 錯誤歷史記錄
  errorHistory: [],

  // 處理錯誤
  handle: (error, type = ERROR_TYPES.UNKNOWN, context = {}) => {
    console.log('ErrorHandler.handle called: 處理錯誤', { error, type, context });
    const handler = ErrorHandler.handlers[type];
    if (!handler) {
      console.error('DOM.errorHandler.handle: 未找到錯誤處理器:', type);
      return ErrorHandler.handlers[ERROR_TYPES.UNKNOWN](error);
    }

    const processedError = handler(error);
    processedError.context = context;

    // 記錄錯誤歷史
    ErrorHandler.errorHistory.push(processedError);

    // 限制錯誤歷史記錄數量
    if (ErrorHandler.errorHistory.length > 100) {
      ErrorHandler.errorHistory = ErrorHandler.errorHistory.slice(-50);
    }

    return processedError;
  },

  // 顯示錯誤訊息
  showError: async (error, options = {}) => {
    console.log('ErrorHandler.showError called: 顯示錯誤訊息', { error, options });
    const {
      duration = CONFIG.UI.ERROR_DISPLAY_TIME,
      showNotification = true,
      logToConsole = true
    } = options;

    if (logToConsole) {
      console.error('DOM.errorHandler.showError: 顯示錯誤:', error);
    }

    if (showNotification) {
      // 創建錯誤通知元素
      const errorElement = DOM.createElement('div', 'error-notification', `
        <div class="alert alert-danger alert-dismissible fade show" role="alert">
          <i class="fas fa-exclamation-triangle me-2"></i>
          ${error.message || CONFIG.MESSAGES.ERROR.UNKNOWN}
          <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
        </div>
      `);

      // 添加到頁面
      document.body.appendChild(errorElement);

      // 自動移除
      await delay(duration);
        if (errorElement.parentNode) {
          errorElement.remove();
        }
    }
  },

  // 顯示成功訊息
  showSuccess: async (message, options = {}) => {
    console.log('ErrorHandler.showSuccess called: 顯示成功訊息', { message, options });
    const {
      duration = CONFIG.UI.ERROR_DISPLAY_TIME,
      showNotification = true
    } = options;

    if (showNotification) {
      const successElement = DOM.createElement('div', 'success-notification', `
        <div class="alert alert-success alert-dismissible fade show" role="alert">
          <i class="fas fa-check-circle me-2"></i>
          ${message}
          <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
        </div>
      `);

      document.body.appendChild(successElement);

      await delay(duration);
        if (successElement.parentNode) {
          successElement.remove();
        }
    }
  },

  // 顯示資訊訊息
  showInfo: async (message, options = {}) => {
    console.log('ErrorHandler.showInfo called: 顯示資訊訊息', { message, options });
    const {
      duration = CONFIG.UI.ERROR_DISPLAY_TIME,
      showNotification = true
    } = options;

    if (showNotification) {
      const infoElement = DOM.createElement('div', 'info-notification', `
        <div class="alert alert-info alert-dismissible fade show" role="alert">
          <i class="fas fa-info-circle me-2"></i>
          ${message}
          <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
        </div>
      `);

      document.body.appendChild(infoElement);

      await delay(duration);
        if (infoElement.parentNode) {
          infoElement.remove();
        }
    }
  },

  // 工具方法
  utils: {

    // 清理錯誤歷史
    clearHistory: () => {
      console.log('ErrorHandler.utils.clearHistory called: 清理錯誤歷史');
      ErrorHandler.errorHistory = [];
    },


    // 檢查是否有特定類型的錯誤
    hasErrorType: (type) => {
      console.log('ErrorHandler.utils.hasErrorType called: 檢查是否有特定類型的錯誤', { type });
      return ErrorHandler.errorHistory.some(error => error.type === type);
    },

    // 調試錯誤處理器
    debug: () => {
      console.group('DOM.errorHandler.utils.debug called：錯誤處理器調試資訊');
      console.log('DOM.errorHandler.utils.debug: 錯誤歷史:', ErrorHandler.errorHistory);
      console.groupEnd();
    }
  }
};

// ======================================================================
//   6. API 和外部服務：API 請求模組 (API and External Services: API Request Module)
// ======================================================================

// ======================================================
//   6-1. API 請求模組 (APIClient)
// ======================================================

const APIClient = {
  // GET 請求
  get: async (url, options = {}) => {
    console.log('APIClient.get called: GET 請求', { url, options });
    try {
      const res = await axios.get(url, options);
      return await APIClient._handleResponse(res);
    } catch (err) {
      APIClient._handleError(err);
      throw err;
    }
  },

  // POST 請求
  post: async (url, data = {}, options = {}) => {
    console.log('APIClient.post called: POST 請求', { url, data, options });
    try {
      const res = await axios.post(url, data, {
        ...options,
        headers: { 'Content-Type': 'application/json', ...(options.headers || {}) }
      });
      return await APIClient._handleResponse(res);
    } catch (err) {
      APIClient._handleError(err);
      throw err;
    }
  },

  // PUT 請求
  put: async (url, data = {}, options = {}) => {
    console.log('APIClient.put called: PUT 請求', { url, data, options });
    try {
      const res = await axios.put(url, data, {
        ...options,
        headers: { 'Content-Type': 'application/json', ...(options.headers || {}) }
      });
      return await APIClient._handleResponse(res);
    } catch (err) {
      APIClient._handleError(err);
      throw err;
    }
  },

  // DELETE 請求
  delete: async (url, options = {}) => {
    console.log('APIClient.delete called: DELETE 請求', { url, options });
    try {
      const res = await axios.delete(url, options);
      return await APIClient._handleResponse(res);
    } catch (err) {
      APIClient._handleError(err);
      throw err;
    }
  },

  // 統一處理回應
  _handleResponse: async (res) => {
    console.log('APIClient._handleResponse called: 處理 API 回應', { status: res.status, statusText: res.statusText });
    // axios 會自動處理 HTTP 錯誤狀態，所以這裡只需要回傳資料
    return res.data;
  },

  // 統一錯誤處理
  _handleError: (err) => {
    console.log('APIClient._handleError called: 處理 API 錯誤', { error: err.message });
    console.error('APIClient 請求錯誤:', err);
    // 可在這裡加上全域錯誤提示、上報等
    UIComponents.toast({ message: '伺服器連線失敗，請稍後再試', type: 'error' });
  }
};


// ======================================================================
//   7. 初始化和全域函式 (Initialization and Global Functions)
// ======================================================================

// ======================================================
//   7-1. 初始化模組 (Initialization Module)
// ======================================================

const Initializer = {  
  init: async () => {
    console.log('DOM.Initializer.init called：開始初始化應用程式');
    
    try {
      
      // 從已渲染的 DOM 中提取 Giver 資料並設定到應用狀態
      const giversData = DOM.dataLoader.extractGiversFromDOM();
      if (giversData.length > 0) {
        console.log('DOM.Initializer.init: 從伺服器端渲染的 HTML 中提取到', giversData.length, '筆 Giver 資料');
        appState.givers = giversData;
        appState.totalGivers = giversData.length;
        
        // 設定卡片事件（重要：伺服器端渲染的卡片需要設定事件）
        DOM.giver.setupCardEvents();
        
        // 顯示第一頁的資料
        const firstPageGivers = DOM.pagination.getGiversByPage(1);
        DOM.pagination.showPageGivers(firstPageGivers);
        
        // 渲染分頁器
        DOM.pagination.renderPaginator(giversData.length);
      } else {
        // 如果沒有找到已渲染的資料，則嘗試載入
        console.log('DOM.Initializer.init: 未找到已渲染的 Giver 資料，嘗試載入');
        await DOM.dataLoader.utils.preloadData(['givers']);
      }
      
      // 設定定期清理
      setInterval(() => {
        DOM.dataLoader.utils.cleanupExpiredCache();
      }, DOM.dataLoader.config.cacheExpiry);
      
      console.log('應用程式初始化完成');
      
    } catch (error) {
      console.error('DOM.Initializer.init: 應用程式初始化失敗:', error);
      ErrorHandler.handle(error, ERROR_TYPES.UNKNOWN, { context: 'Initializer.init' });
    }
  }
};

// ======================================================
//   7-2. 全域函式 (Global Functions)：為了向後相容，保留舊的函式引用
// ======================================================

const renderPaginator = DOM.pagination.renderPaginator;
const getGiversByPage = DOM.pagination.getGiversByPage;
const checkTopicOverflow = DOM.utils.checkTopicOverflow;
const scrollToBottom = DOM.utils.scrollToBottom;
const cleanupModal = DOM.utils.cleanupModal;
const openChatDialog = UIInteraction.openChatDialog;
const showConfirmDialog = UIInteraction.showConfirmDialog;

// ======================================================
//   7-3. 頁面載入時設定全域事件監聽器 (Setting Global Event Listeners on Page Load)
// ======================================================

DOM.events.add(document, 'DOMContentLoaded', async function() {
  
  // 初始化事件委派管理器
  EventManager.init();
  
  // 使用初始化模組進行完整初始化 - 等待完成
  await Initializer.init();

  // 設定 resize 事件監聽器，用於處理服務項目溢出
  let resizeTimeout;
  window.addEventListener('resize', () => {
    console.log('DOM.events.add: 設定 resize 事件監聽器');
    clearTimeout(resizeTimeout);
    resizeTimeout = setTimeout(() => {
      if (DOM.giver && typeof DOM.giver.checkAllTopicsOverflow === 'function') {
        DOM.giver.checkAllTopicsOverflow();
      }
    }, DELAY_TIMES.UI.MODAL_CLEANUP);  
  });

  // --- 手動初始化聊天對話框，並將實例存到全域變數中 ---
  const giverModalElement = DOM.getById(CONFIG.SELECTORS.GIVER_MODAL);
  if (giverModalElement) {
    console.log('DOM.events.add: 手動初始化聊天對話框');
    // 初始化 Modal 實例，並設定點擊外部不可關閉
    CONFIG.INSTANCES.GIVER_MODAL = new bootstrap.Modal(giverModalElement, {
      backdrop: 'static', // 點擊背景不會關閉 Modal
      keyboard: false     // 按下 ESC 鍵不會關閉 Modal
    });

    // 監聽 'shown.bs.modal' 事件，此事件在對話框完全顯示後觸發
    giverModalElement.addEventListener('shown.bs.modal', () => {
      console.log('DOM.events.add: 監聽 shown.bs.modal 事件');
      const modalDialog = giverModalElement.querySelector('.modal-dialog');
      const modalContent = giverModalElement.querySelector('.modal-content');
      const modalBody = giverModalElement.querySelector('.modal-body');

      if (modalDialog && modalContent && modalBody) {
        // --- 最終解決方案：用 JS 動態應用 Flexbox ---

        // 1. 設定對話框本身的最大高度，確保它不會超出視窗
        modalDialog.style.height = '90vh';
        modalContent.style.height = '100%';
        
        // 2. 將 modal-content 設為 Flex 容器，讓其子元素可以彈性分配空間
        modalContent.style.display = 'flex';
        modalContent.style.flexDirection = 'column';

        // 3. 讓 modal-body (內容區) 自動填滿所有剩餘空間
        modalBody.style.flexGrow = '1';
        modalBody.style.overflowY = 'auto'; // 讓內容區內部可以滾動
      }
    });
  }
});

// ======================================================================
//   7-4. 初始化時段表單的輸入欄位 (Initializing Input Fields for Time Schedule Form)：設定預設值、事件監聽器、日期、開始時間、結束時間的輸入事件和驗證
// ======================================================================

// 通用輸入欄位設定器 (Universal Input Field Setup)
// =================================================================

// 通用輸入欄位設定器
const setupInputField = (inputElement, config) => {
  if (!inputElement) {
    return false;
  }


  // 設定預設值
  inputElement.value = config.defaultValue || '';

  // 綁定 input 事件
  if (config.onInput) {
    inputElement.addEventListener('input', (e) => {
      try {
        config.onInput(e.target);
      } catch (error) {
      }
    });
  }

  // 綁定 blur 事件
  if (config.onBlur) {
    inputElement.addEventListener('blur', (e) => {
      try {
        config.onBlur(e.target);
      } catch (error) {
      }
    });
  }

  // 綁定 click 事件
  if (config.onClick) {
    inputElement.addEventListener('click', (e) => {
      try {
        e.preventDefault();
        e.stopPropagation();
        config.onClick(e.target);
      } catch (error) {
      }
    });
  }

  // 綁定 focus 事件
  if (config.onFocus) {
    inputElement.addEventListener('focus', (e) => {
      try {
        e.preventDefault();
        config.onFocus(e.target);
      } catch (error) {
      }
    });
  }

  // 綁定 change 事件
  if (config.onChange) {
    inputElement.addEventListener('change', (e) => {
      try {
        config.onChange(e.target);
      } catch (error) {
      }
    });
  }

  return true;
};

// 批量設定輸入欄位
const setupMultipleInputFields = (formElement, fieldConfigs) => {
  if (!formElement) {
    return false;
  }


  // 清除所有錯誤訊息
  const inputs = formElement.querySelectorAll('input, textarea');
  inputs.forEach(input => {
    FormValidator.clearValidationError(input);
  });

  // 設定每個欄位
  const results = {};
  for (const [selector, config] of Object.entries(fieldConfigs)) {
    const element = formElement.querySelector(selector);
    results[selector] = setupInputField(element, config);
  }

  return results;
};

// 初始化表單欄位
const initScheduleFormInputs = (formElement) => {
  
  // 定義所有輸入欄位的配置
  const fieldConfigs = {
    // 日期輸入欄位
    '#schedule-date': {
      defaultValue: DateUtils.getTodayFormatted(),
      onClick: (target) => {
        DOM.chat.showDatePicker();
      },
      onFocus: (target) => {
        DOM.chat.showDatePicker();
      },
      onChange: (target) => {
        DOM.chat.validateDateInput(target);
      },
      onBlur: (target) => {
        DOM.chat.validateDateInput(target);
      }
    },
    
    // 開始時間輸入欄位
    '#schedule-start-time': {
      defaultValue: '',
      onInput: (target) => {
        DOM.chat.formatTimeInput(target);
      },
      onBlur: (target) => {
        DOM.chat.formatTimeInput(target, true); // blur 時自動格式化
        DOM.chat.validateAndFormatTime(target);
      }
    },
    
    // 結束時間輸入欄位
    '#schedule-end-time': {
      defaultValue: '',
      onInput: (target) => {
        DOM.chat.formatTimeInput(target, false); // 只做數字過濾
      },
      onBlur: (target) => {
        DOM.chat.formatTimeInput(target, true); // blur 時自動格式化
        DOM.chat.validateAndFormatTime(target);
      }
    },
    
    // 備註輸入欄位
    '#schedule-notes': {
      defaultValue: '',
      onInput: (target) => {
        DOM.chat.validateNotesInput(target);
      },
      onBlur: (target) => {
        DOM.chat.validateNotesInput(target);
      }
    }
  };

  // 使用通用設定器批量設定所有欄位
  const results = setupMultipleInputFields(formElement, fieldConfigs);
  
  return results;
}

// ...
// 在 handleSingleTime 動態產生表單後呼叫
// ...
// 於動態產生表單後加上：
const formElement = document.getElementById('time-schedule-form');
if (formElement) {
  initScheduleFormInputs(formElement);
}
// ...
// setupScheduleForm 只負責表單提交事件即可