"""應用程式配置管理模組。

使用 Pydantic BaseSettings 集中管理所有應用程式配置，包括路徑、應用程式資訊、API 設定等。
"""

# ===== 標準函式庫 =====
import logging
from pathlib import Path
import tomllib
from typing import Any

# ===== 第三方套件 =====
from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

# 日誌記錄功能初始化，只顯示 INFO 級別以上的事件。
logging.basicConfig(level=logging.INFO)
# 建立日誌記錄器：可在日誌中看到訊息從哪個模組來，利於除錯與維運
logger = logging.getLogger(__name__)


def get_project_version() -> str:
    """從 pyproject.toml 檔案中讀取專案版本號。

    如果讀取失敗，返回預設版本號。"""
    try:
        pyproject_path = Path(__file__).parent.parent.parent / "pyproject.toml"
        with open(pyproject_path, "rb") as f:
            pyproject_data = tomllib.load(f)
            return str(pyproject_data["tool"]["poetry"]["version"])
    except (FileNotFoundError, KeyError, tomllib.TOMLDecodeError) as e:
        logger.warning(f"無法從 pyproject.toml 讀取專案版本號。錯誤: {e}")
        return "0.1.0"  # 預設版本號


class Settings(BaseSettings):
    """應用程式設定管理類別。"""

    # Pydantic 設定配置
    model_config = SettingsConfigDict(
        env_file=".env",  # 自動載入 .env 檔案
        env_file_encoding="utf-8",  # 檔案編碼
        case_sensitive=False,  # 環境變數名稱不區分大小寫
        extra="ignore",  # 忽略未定義的環境變數
        env_parse_none_str=None,  # 禁用複雜值解析：環境變數的值是字串 "None" 時，不自動轉換成 Python 的 None 物件
    )

    # ===== 基礎路徑配置 =====
    project_root: Path = Field(
        default_factory=lambda: Path(__file__).parent.parent.parent,
        description="專案的根目錄，用來定位 pyproject.toml 等檔案",
    )
    app_dir: Path = Field(
        default_factory=lambda: Path(__file__).parent.parent,
        description="應用程式目錄，用來定位 templates 等檔案",
    )

    # ===== 應用程式基本配置 =====
    app_name: str = Field(
        default="104 Resume Clinic Scheduler", description="應用程式名稱"
    )
    app_description: str = Field(
        default="104 履歷診療室 - 站內諮詢時間媒合系統。\n\n讓 Giver（診療服務提供者）與 Taker（診療服務接受者）能在平台內，方便地設定可面談時段並完成配對媒合，同時提供即時通知，以減少等待回應時的不確定與焦慮感。",
        description="應用程式描述",
    )
    app_version: str = Field(
        default_factory=get_project_version, description="應用程式版本號"
    )

    # ===== 環境設定 =====
    app_env: str = Field(
        default="development",
        description="應用程式環境 (development, staging, production)",
    )
    # ⚠️ 正式環境記得將 .env 設定成 DEBUG=false
    # 如果 .env 或系統中結果是小寫字串 "true"，就回傳 True，開啟「除錯模式（debug mode）」
    # 如果 .env 或系統中沒有 DEBUG，預設回傳 False（布林值）
    debug: bool = Field(default=False, description="是否啟用除錯模式")
    testing: bool = Field(default=False, description="是否處於測試環境")
    secret_key: SecretStr | None = Field(
        default=None,  # 使用 None 作為預設值，強制從 `.env` 檔案讀取避免硬編碼
        description="應用程式密鑰",
    )

    # ===== API 文件配置 =====
    docs_url: str = Field(default="/docs", description="API 文件 URL")
    redoc_url: str = Field(default="/redoc", description="ReDoc 文件 URL")
    openapi_url: str = Field(
        default="/openapi.json", description="OpenAPI 規範文件 URL"
    )

    # ===== 伺服器配置 =====
    server_url: str = Field(
        default="http://localhost:8000", description="API 伺服器 URL"
    )
    server_description: str = Field(default="開發環境", description="伺服器環境描述")

    # ===== 靜態檔案配置 =====
    static_url: str = Field(default="/static", description="靜態檔案 URL 路徑")
    static_name: str = Field(default="static", description="靜態檔案掛載名稱")

    # ===== 日誌配置 =====
    log_level: str = Field(
        default="INFO",
        description="日誌級別 (DEBUG, INFO, WARNING, ERROR, CRITICAL)",
    )
    log_api_requests: bool = Field(default=True, description="是否記錄 API 請求日誌")
    log_static_requests: bool = Field(
        default=False, description="是否記錄靜態資源請求日誌"
    )
    log_file: str = Field(default="logs/app.log", description="日誌檔案路徑")

    # ===== 資料庫配置 =====
    # MySQL 配置
    mysql_host: str = Field(default="localhost", description="MySQL 主機地址")
    mysql_port: int = Field(default=3306, description="MySQL 連接埠")
    mysql_user: str | None = Field(
        default=None,
        description="MySQL 使用者名稱（建議使用專用應用程式帳號，不要使用 root）",
    )
    mysql_password: SecretStr | None = Field(
        default=None,  # 使用 None 作為預設值，強制從 `.env` 檔案讀取避免硬編碼
        description="MySQL 密碼",
    )
    mysql_database: str = Field(default="scheduler_db", description="MySQL 資料庫名稱")
    mysql_charset: str = Field(default="utf8mb4", description="MySQL 字符集")

    # SQLite 配置（用於測試環境）
    sqlite_database: str = Field(
        default=":memory:", description="SQLite 資料庫路徑（測試環境使用記憶體資料庫）"
    )

    # MongoDB 配置
    mongodb_uri: str = Field(
        default="mongodb://localhost:27017", description="MongoDB 連接 URI"
    )
    mongodb_database: str = Field(
        default="scheduler_db", description="MongoDB 資料庫名稱"
    )

    # Redis 配置
    redis_host: str = Field(default="localhost", description="Redis 主機地址")
    redis_port: int = Field(default=6379, description="Redis 連接埠")
    redis_db: int = Field(default=0, description="Redis 資料庫編號")
    redis_password: SecretStr | None = Field(
        default=None,  # 使用 None 作為預設值，強制從 `.env` 檔案讀取避免硬編碼
        description="Redis 密碼",
    )

    # ===== AWS 配置 =====
    aws_access_key_id: str | None = Field(default=None, description="AWS 存取金鑰 ID")
    aws_secret_access_key: SecretStr | None = Field(
        default=None,  # 使用 None 作為預設值，強制從 `.env` 檔案讀取避免硬編碼
        description="AWS 秘密存取金鑰",
    )
    aws_region: str = Field(default="ap-northeast-1", description="AWS 區域")
    aws_s3_bucket: str | None = Field(default=None, description="AWS S3 儲存桶名稱")

    # ===== 104 API 配置 =====
    api_104_base_url: str | None = Field(default=None, description="104 API 基礎 URL")
    api_104_client_id: str | None = Field(default=None, description="104 API 客戶端 ID")
    api_104_client_secret: SecretStr | None = Field(
        default=None,  # 使用 None 作為預設值，強制從 `.env` 檔案讀取避免硬編碼
        description="104 API 客戶端密鑰",
    )

    # ===== API 超時配置 =====
    api_timeout: int = Field(default=10, description="API 請求總超時時間（秒）")
    api_connect_timeout: int = Field(default=5, description="API 連接超時時間（秒）")
    api_read_timeout: int = Field(default=10, description="API 讀取超時時間（秒）")

    # ===== 安全配置 =====
    cors_origins: str = Field(
        default="http://localhost:8000", description="CORS 允許的來源（逗號分隔）"
    )
    session_secret: SecretStr | None = Field(
        default=None,  # 使用 None 作為預設值，強制從 `.env` 檔案讀取避免硬編碼
        description="會話密鑰",
    )

    # ===== 郵件配置 =====
    smtp_host: str | None = Field(default=None, description="SMTP 主機地址")
    smtp_port: int = Field(default=587, description="SMTP 連接埠")
    smtp_user: str | None = Field(default=None, description="SMTP 使用者名稱")
    smtp_password: SecretStr | None = Field(
        default=None,  # 使用 None 作為預設值，強制從 `.env` 檔案讀取避免硬編碼
        description="SMTP 密碼",
    )

    @property
    def cors_origins_list(self) -> list[str]:
        """取得 CORS 來源列表。"""
        return [
            origin.strip() for origin in self.cors_origins.split(",") if origin.strip()
        ]

    @property
    def static_dir(self) -> Path:
        """靜態檔案目錄。"""
        return self.project_root / "static"

    @property
    def templates_dir(self) -> Path:
        """模板目錄。"""
        return self.app_dir / "templates"

    @property
    def is_development(self) -> bool:
        """是否為開發環境。"""
        return self.app_env == "development"

    @property
    def is_production(self) -> bool:
        """是否為生產環境。"""
        return self.app_env == "production"

    @property
    def is_staging(self) -> bool:
        """是否為測試環境。"""
        return self.app_env == "staging"

    @property
    def mysql_connection_string(self) -> str:
        """Mysql 連接字串。"""
        password = (
            self.mysql_password.get_secret_value()
            if self.mysql_password is not None
            else ""
        )
        return (
            f"mysql+pymysql://{self.mysql_user}:{password}"
            f"@{self.mysql_host}:{self.mysql_port}/{self.mysql_database}"
            f"?charset={self.mysql_charset}"
        )

    @property
    def sqlite_connection_string(self) -> str:
        """SQLite 連接字串（用於測試環境）。"""
        return f"sqlite:///{self.sqlite_database}"

    @property
    def redis_connection_string(self) -> str:
        """Redis 連接字串。"""
        if self.redis_password:
            password = self.redis_password.get_secret_value()
            return (
                f"redis://:{password}@{self.redis_host}:"
                f"{self.redis_port}/{self.redis_db}"
            )
        return f"redis://{self.redis_host}:{self.redis_port}/{self.redis_db}"

    @property
    def smtp_config(self) -> dict[str, Any]:
        """取得 SMTP 配置。"""
        if not all([self.smtp_host, self.smtp_user, self.smtp_password]):
            return {}

        return {
            "host": self.smtp_host,
            "port": self.smtp_port,
            "username": self.smtp_user,
            "password": (
                self.smtp_password.get_secret_value() if self.smtp_password else ""
            ),
            "use_tls": True,
        }

    @property
    def has_smtp_config(self) -> bool:
        """檢查是否有完整的 SMTP 配置。"""
        return all([self.smtp_host, self.smtp_user, self.smtp_password])

    @property
    def has_aws_config(self) -> bool:
        """檢查是否有完整的 AWS 配置。"""
        return all(
            [self.aws_access_key_id, self.aws_secret_access_key, self.aws_region]
        )

    @property
    def has_104_api_config(self) -> bool:
        """檢查是否有完整的 104 API 配置。"""
        return all(
            [self.api_104_base_url, self.api_104_client_id, self.api_104_client_secret]
        )

    # ===== 安全相關的便利屬性 =====
    @property
    def secret_key_value(self) -> str:
        """安全地取得應用程式密鑰。"""
        return self.secret_key.get_secret_value() if self.secret_key else ""

    @property
    def session_secret_value(self) -> str:
        """安全地取得會話密鑰。"""
        return self.session_secret.get_secret_value() if self.session_secret else ""

    @property
    def aws_secret_key_value(self) -> str:
        """安全地取得 AWS 秘密金鑰。"""
        return (
            self.aws_secret_access_key.get_secret_value()
            if self.aws_secret_access_key
            else ""
        )

    @property
    def api_104_secret_value(self) -> str:
        """安全地取得 104 API 密鑰。"""
        return (
            self.api_104_client_secret.get_secret_value()
            if self.api_104_client_secret
            else ""
        )


# 全域設定實例
settings = Settings()
