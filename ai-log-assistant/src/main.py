
import logging
import yaml
from log_reader import read_logs
from ai_engine import AIEngine
from agent import Agent
from guardrails import validate_output
from typing import Any
from pathlib import Path


PROJECT_ROOT = Path(__file__).parent
CONFIG_PATH = PROJECT_ROOT.parent / "config/settings.yaml"


logging.basicConfig(level=logging.INFO)


def main():
    # Load config
    with open(CONFIG_PATH, "r") as f:
        config = yaml.safe_load(f)

    logs = read_logs(config["log_source"])
    if not logs:
        logging.error("No logs found.")
        return

    ai_engine = AIEngine(model=config["model"])
    agent = Agent(ai_engine)

    summary = agent.process_logs(logs)
    safe_summary = validate_output(summary)

    print("=== AI Summary ===")
    print(safe_summary)

if __name__ == "__main__":
    main()