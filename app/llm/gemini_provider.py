import os

from google import genai
from app.core.config import settings
from app.llm.base_provider import BaseLLMProvider
from app.logger import logger

class GeminiProvider(BaseLLMProvider):

    def __init__(self):

        self.client = genai.Client(
            api_key=settings.GEMINI_API_KEY
        )

        self.model = settings.GEMINI_MODEL


    def generate_content(
            self,
            prompt: str

    ) -> str | None:

        try:

            response = self.client.models.generate_content(
                model=self.model,
                contents=prompt
            )

            if (
                    response is None
                    or response.text is None
                    or not response.text.strip()
            ):
                return None

            return response.text.strip()

        except Exception:

            return None

