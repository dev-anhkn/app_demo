from pathlib import Path
from typing import Any

import yaml

from src.config.application_config import ApplicationConfig


def load_yaml_config(filepath: Path) -> dict[str, Any]:
    """
    Load a YAML configuration file and return its contents as a dictionary.

    Args:
        filepath (Path): Path to YAML file.

    Returns:
        dict[str, Any]: Parsed YAML content. Returns an empty dict if file is empty.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the YAML is invalid or cannot be parsed.
    """
    filepath = Path(filepath)  # bảo đảm luôn là Path
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            data = yaml.safe_load(file)
            if data is None:
                return {}  # tránh trả về None khi file rỗng
            if not isinstance(data, dict):
                raise ValueError(
                    f"YAML content at {filepath} must be a mapping (dict), got {type(data).__name__}"
                )
            return data
    except FileNotFoundError:
        raise FileNotFoundError(f"Config file not found: {filepath}")
    except yaml.YAMLError as exc:
        raise ValueError(f"Error parsing YAML file {filepath}: {exc}")


def get_settings() -> ApplicationConfig:
    """
    Load settings from a YAML config file and return as an ApplicationConfig instance.

    Returns:
        ApplicationConfig: Settings object built from the YAML file.
    """
    config_path = Path(__file__).resolve().parent.parent.parent / "src" / "config" / "application.yaml"
    yaml_config = load_yaml_config(config_path)
    return ApplicationConfig(**yaml_config)


# Khởi tạo config toàn cục
application_config = get_settings()
