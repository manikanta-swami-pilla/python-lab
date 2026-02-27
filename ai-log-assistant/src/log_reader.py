import logging

"""
This module is responsible for reading log data from log files or other sources. It provides functionality to parse and extract relevant information from logs for further analysis.
"""

def read_logs(path: str) -> str:
    try:
        with open(path, "r") as file:
            return file.read()
    except Exception as e:
        logging.error(f"Error reading log file: {e}")
        return ""