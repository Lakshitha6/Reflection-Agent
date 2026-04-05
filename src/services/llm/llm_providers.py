from langchain_groq import ChatGroq
from .llm_base import BaseLLMService
import os
from dotenv import load_dotenv

load_dotenv()

class GroqService(BaseLLMService):
    
    def __init__(self, model_name: str, temperature: float, max_tokens: int):
        api_key = os.getenv("Groq_API_KEY")

        if not api_key:
            raise ValueError("Groq_API_KEY not found in .env file")

        self._llm = ChatGroq(
            api_key=api_key,
            model=model_name,
            temperature=temperature,
            max_tokens=max_tokens
        )

    
    def generate(self, user_query:str, system_prompt : str = "") -> str:
        
        messages = [
            ("system", system_prompt),
            ("human", user_query)
        ]

        response = self._llm.invoke(messages)

        return response.content