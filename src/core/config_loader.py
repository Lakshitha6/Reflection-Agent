import yaml
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent # Goes up to Project Root
CONFIG_PATH = BASE_DIR / "config" / "settings.yaml"

def load_config(path=CONFIG_PATH):
    # Check if file exists
    if not os.path.exists(path):
        raise FileNotFoundError(f"Configuration file not found at: {os.path.abspath(path)}")
        
    with open(path, "r") as f:
        # Use safe_load to prevent execution of arbitrary code in the YAML file
        config = yaml.safe_load(f)

    return config


# Test config loading is working

# config = load_config()
# print(config["embeddings"]["active_provider"])