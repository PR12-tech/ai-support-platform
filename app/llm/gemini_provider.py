import os

from google import genai
from dotenv import load_dotenv

from app.llm.base_provider import BaseLLMProvider

load_dotenv()

class GeminiProvider(BaseLLMProvider):

    def __init__(self):

        self.client = genai.Client(
            api_key=os.getenv("GEMINI_API_KEY")
        )

        self.model = "gemini-2.5-flash"


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

