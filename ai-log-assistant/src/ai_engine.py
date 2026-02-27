from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate

class AIEngine:
    def __init__(self, model: str = "llama2"):
        self.llm = OllamaLLM(model=model)

    def analyze_logs(self, logs: str) -> str:
        prompt = PromptTemplate.from_template("""
        You are a DevOps assistant. Analyze the logs:
        1. Summarize main errors
        2. Suggest root causes
        3. Recommend next steps

        Logs:
        {logs}
        """)
        # Use .invoke instead of calling the object
        return self.llm.invoke(prompt.format(logs=logs))