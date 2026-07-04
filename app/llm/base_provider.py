from abc import ABC, abstractmethod


class BaseLLMProvider(ABC):

    @abstractmethod
    def generate_content(
            self,
            prompt: str
    ) -> str | None:
        """
        Generate a response from the LLM.

        Returns:
             str: Generate text.
             None: If the provider request fails.
        """

        pass