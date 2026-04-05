from .llm_providers import GroqService

class LLMFactory:

    @staticmethod
    def create(config: dict):
        active_provider = config["llm"]["active_provider"]
        spec = config["llm"]["providers"][active_provider]

        if active_provider == "groq":
            return GroqService(
                model_name=spec["model"],
                temperature=spec["temperature"],
                max_tokens=spec["max_tokens"]
            )
        else:
            raise ValueError(f"LLM Provider {active_provider} not supported.")