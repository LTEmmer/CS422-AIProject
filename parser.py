import re
from typing import Dict


def extract_function_info(function_code: str) -> Dict:
    """Parse metadata from a function's code."""
    first_line = function_code.split('\n')[0]
    name_match = re.search(r'def\s+(\w+)\(', first_line)
    params_match = re.search(r'def\s+\w+\((.*?)\)', first_line)
    docstring_match = re.search(r'"""(.*?)"""', function_code, re.DOTALL)
    return_statements = re.findall(r'return\s+.*', function_code)

    return {
        "name": name_match.group(1) if name_match else "unknown",
        "params": [p.strip() for p in params_match.group(1).split(',')] if params_match and params_match.group(
            1) else [],
        "docstring": docstring_match.group(1).strip() if docstring_match else None,
        "return_statements": return_statements,
        "raw_code": function_code.strip()
    }
