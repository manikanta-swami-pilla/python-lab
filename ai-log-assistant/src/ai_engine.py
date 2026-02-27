from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
from pathlib import Path
from prompt_reader import read_prompt_template

PROMPT_TEMPLATE_PATH = Path(__file__).parent.parent / "prompts/root_cause_analysis.yaml"

class AIEngine:
    def __init__(self, model: str = "llama2"):
        self.llm = OllamaLLM(model=model)

    def analyze_logs(self, logs: str) -> str:
        try:
            prompt = PromptTemplate.from_template(read_prompt_template(PROMPT_TEMPLATE_PATH))
            return self.llm.invoke(prompt.format(logs=logs))
        except Exception as e:
            return f"Error analyzing logs: {e}"