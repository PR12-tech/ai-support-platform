import os

from dotenv import load_dotenv

from app.llm.gemini_provider import GeminiProvider

load_dotenv()


def get_provider():

    provider = os.getenv(
        "LLM_PROVIDER",
        "gemini"
    ).lower()

    if provider == "gemini":
       return GeminiProvider()

    raise ValueError(
        f"Unsupported LLM provider: {provider}"
    )