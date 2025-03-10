from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Mobile Factory API"
    VERSION: str = "1.0"
    DEBUG: bool = False
    ORDER_ID_PREFIX: str = "MFC"
    
    class Config:
        env_file = ".env"

settings = Settings()
