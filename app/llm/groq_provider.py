import os

from groq import Groq
from dotenv import load_dotenv

from app.llm.base_provider import BaseLLMProvider

load_dotenv()

class GroqProvider(BaseLLMProvider):

    def __init__(self):

        self.client = Groq(
            api_key=os.getenv("GROQ_API_KEY")
        )

        self.model = "llama-3.3-70b-versatile"

    def generate_content(
            self,
            prompt: str
    ) -> str | None:

        try:

            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            text = response.choices[0].message.content

            if text is None or not text.strip():
                return None

            return text.strip()

        except Exception:

            return None