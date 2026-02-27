"""
Guardrails module for AI Log Assistant
"""
def validate_output(output: str) -> str:
    # Simple guardrail: block dangerous commands
    forbidden = ["rm -rf", "shutdown", "drop database"]
    for word in forbidden:
        if word in output.lower():
            return "⚠️ Unsafe suggestion detected. Review manually."
    return output