from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=r".env")
    DB_USER: str = ""
    DB_PORT: str = ""
    DB_NAME: str = ""
    DB_PASS: str = ""
    DB_HOST: str = ""
    JWT_SECRET_KEY: str = ""
    JWT_ALGORITHM: str = ""
    GOOGLE_API_KEY: str = ""
    
settings = Settings()