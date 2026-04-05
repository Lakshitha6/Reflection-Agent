"""" Setup fixtures for testing. """

import pytest
from src.agents.graph import app
from src.services.llm import LLMFactory
import yaml

@pytest.fixture
def agent_app():
    return app

@pytest.fixture
def llm_service():
    with open("config/settings.yaml", "r") as f:
        config = yaml.safe_load(f)
    
    return LLMFactory.create(config=config)