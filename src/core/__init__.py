from .config_loader import load_config
from .data_loader import DocumentLoader
from .text_splitter import TextSplitter

config = load_config()

__all__ = ["config", "load_config", "DocumentLoader", "TextSplitter"]