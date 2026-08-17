import os
import time
import re

from groq import Groq
from dotenv import load_dotenv

from app.llm.base_provider import BaseLLMProvider

load_dotenv()

class GroqProvider(BaseLLMProvider):

    def __init__(self):

        self.client = Groq(
            api_key=os.getenv("GROQ_API_KEY"),
            max_retries=1,
            timeout=20.0
        )

        self.model = os.getenv("GROQ_MODEL", "openai/gpt-oss-120b")

    def generate_content(
            self,
            prompt: str
    ) -> str | None:

        max_attempts = 3
        backoff = 1.0

        for attempt in range(max_attempts):
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

            except Exception as e:
                err_msg = str(e)
                print(f"GROQ ERROR (attempt {attempt + 1}/{max_attempts}): {err_msg}")

                if "rate limit" in err_msg.lower() or "429" in err_msg.lower():
                    # Parse try again time (e.g., "try again in 2.535s")
                    match = re.search(r"try again in ([\d\.]+)s", err_msg.lower())
                    wait_time = float(match.group(1)) + 0.5 if match else backoff
                    if wait_time > 10.0:
                        wait_time = 10.0
                    print(f"Rate limit hit. Waiting {wait_time:.2f} seconds before retry...")
                    time.sleep(wait_time)
                    backoff *= 2
                    continue

                return None

        return None