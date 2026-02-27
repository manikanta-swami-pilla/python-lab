import logging

class Agent:
    def __init__(self, ai_engine):
        self.ai_engine = ai_engine

    def process_logs(self, logs: str) -> str:
        summary = self.ai_engine.analyze_logs(logs)
        logging.info("AI Summary generated")
        return summary