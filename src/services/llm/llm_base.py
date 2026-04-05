from abc import ABC, abstractmethod

class BaseLLMService(ABC):

    @abstractmethod
    def generate(self, user_query: str, system_prompt: str = "") -> str:
        """Takes a prompt and returns the LLM's text response."""
        pass