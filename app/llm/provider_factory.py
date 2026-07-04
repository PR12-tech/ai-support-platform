import os

from dotenv import load_dotenv

from app.llm.gemini_provider import GeminiProvider
from app.llm.groq_provider import GroqProvider

load_dotenv()


def get_provider():

    provider = os.getenv(
        "LLM_PROVIDER",
        "gemini"
    ).lower()

    if provider == "gemini":

       return GeminiProvider()

    if provider == "groq":

        return GroqProvider()

    raise ValueError(
        f"Unsupported LLM provider: {provider}"
    )