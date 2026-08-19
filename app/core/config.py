from typing import Literal
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import model_validator

class Settings(BaseSettings):

    DATABASE_URL: str

    SECRET_KEY: str

    ALGORITHM: str = "HS256"

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    FRONTEND_URL: str = "http://localhost:5173"

    LLM_PROVIDER: Literal["gemini", "groq"] = "gemini"

    GEMINI_API_KEY: str = ""

    GEMINI_MODEL: str = "gemini-2.5-flash"

    GROQ_API_KEY: str = ""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    @model_validator(mode="after")
    def validate_api_keys(self):
        if self.LLM_PROVIDER == "gemini":
            if not self.GEMINI_API_KEY.strip():
                raise ValueError(
                    "GEMINI_API_KEY cannot be empty when LLM='gemini'."
                )

        elif self.LLM_PROVIDER == "groq":
            if not self.GROQ_API_KEY.strip():
                raise ValueError(
                    "GROQ_API_KEY cannot be empty when LLM_PROVIDER='groq'."
                )

        return self

settings = Settings()
