from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # MongoDB Configuration
    MONGO_URI: str
    MONGO_NAME: str

    # Server Configuration
    SERVER_HOST: str = "0.0.0.0"
    SERVER_PORT: int = 8000
    SERVER_RELOAD: bool = False

    # API Configuration
    API_PREFIX: str = "/api/v1"

    class Config:
        env_file = ".env"
        extra = "ignore"
        arbitrary_types_allowed = True


settings = Settings()
