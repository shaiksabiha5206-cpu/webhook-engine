from pydantic import BaseModel
class Settings(BaseModel):
    app_name :str = "webhook-engine"
    log_level : str = "INFO"
    max_retries:int = 3
settings = Settings()