from typing import Literal
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import model_validator

class Settings(BaseSettings):

    DATABASE_URL: str

    LLM_PROVIDER: Literal["gemini", "groq"] = "gemini"

    GEMINI_API_KEY: str = ""

    GROQ_API_KEY: str = ""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    @model_validator(mode="after")
    def validate_api_keys(self):
        if not self.GEMINI_API_KEY.strip():
            raise ValueError("GEMINI_API_KEY cannot be empty.")

        if not self.GROQ_API_KEY.strip():
            raise ValueError("GROQ_API_KEY cannot be empty.")

        return self

settings = Settings()
