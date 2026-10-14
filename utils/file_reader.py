# utils/file_reader.py

import json
import os

def load_json_data(file_path):
    """
    Safely reads a JSON file using try/except/finally exception handling.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Test data file not found at: {file_path}")

    file_obj = None
    try:
        file_obj = open(file_path, "r", encoding="utf-8")
        data = json.load(file_obj)
        return data
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON format in file {file_path}: {e}")
    except Exception as e:
        raise RuntimeError(f"An unexpected error occurred while reading {file_path}: {e}")
    finally:
        # Ensures file handle is closed even if an exception occurs
        if file_obj:
            file_obj.close()