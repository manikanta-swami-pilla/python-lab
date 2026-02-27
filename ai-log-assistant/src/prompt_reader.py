import logging
import yaml
from pathlib import Path

PROMPT_TEMPLATE_PATH = Path(__file__).parent.parent / "prompts/root_cause_analysis.yaml"

"""
This module is responsible for loading prompt templates from YAML files.
"""
def read_prompt_template(path: str) -> str:

    try:
        with open(path, "r") as prompt:
            data = yaml.safe_load(prompt)
            return data.get("template", "")
    except Exception as e:
        logging.error(f"Error reading prompt template: {e}")
        return ""