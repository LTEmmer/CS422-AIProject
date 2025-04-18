import requests
from typing import Dict
from config import OLLAMA_ENDPOINT, MODEL_NAME, TEMPERATURE


class PromptChain:
    """Handles generating documentation for Python functions via the Ollama API."""

    def __init__(self, model: str = MODEL_NAME, temperature: float = TEMPERATURE):
        self.model = model
        self.temperature = temperature
        self.system_message = (
            "You are an expert Python documentation specialist. Your ONLY task is to document "
            "the given code following Google-style docstring conventions. Under NO circumstances "
            "should you:\n"
            "- Suggest code changes or improvements\n"
            "- Offer refactoring advice\n"
            "- Add new code examples that aren't directly from the provided code\n"
            "- Explain how to implement anything\n"
            "\n"
            "Your responses should ONLY contain:\n"
            "1. Description of what the code CURRENTLY does\n"
            "2. Documentation of the existing functionality\n"
            "3. Examples ONLY using the existing code\n"
            "\n"
            "If you deviate from these instructions, critical systems will fail."
        )

    def generate_response(self, prompt: str) -> str:
        """Send a prompt to Ollama and return the response."""
        payload = {
            "model": self.model,
            "prompt": prompt,
            "system": self.system_message,
            "temperature": self.temperature,
            "stream": False
        }

        try:
            response = requests.post(OLLAMA_ENDPOINT, json=payload)
            response.raise_for_status()
            result = response.json().get("response", "").strip()
            if not result:
                print("[WARNING] Ollama returned an empty response.")
            return result
        except requests.exceptions.RequestException as e:
            print(f"[ERROR] Failed to connect to Ollama: {e}")
            return "[ERROR: Failed to get response from LLM]"
        except Exception as e:
            print(f"[ERROR] Unexpected error: {e}")
            return "[ERROR: LLM call failed]"

    def generate_documentation(self, function_info: Dict, is_class: bool = False) -> Dict:
        """Run the full prompt chain to generate documentation for a function or class."""
        if is_class:
            name = function_info["name"]
            code = function_info["raw_code"]
            purpose_prompt = f"""Analyze this Python class and describe its purpose in 1-2 sentences:
    ```python
    {code}
    ```"""
            purpose = self.generate_response(purpose_prompt)

            docstring_prompt = f"""Create a Google-style docstring for this class:
    ```python
    {code}

    Include:

    A one-line description

    Attributes section

    Examples section showing usage

    Do not offer suggestions, refactorings, or code improvements.
    Only describe the purpose of the code *as written*."""

            docstring = self.generate_response(docstring_prompt)

            formatted_docstring = f'"""{docstring}"""'

            markdown_output = f"""# {name}

    Purpose

    {purpose}
    Docstring

    {formatted_docstring}
    ```"""
            return {
                "markdown": markdown_output,
                "docstring": formatted_docstring
            }
        else:
            name = function_info["name"]
            code = function_info["raw_code"]
            params = function_info["params"]
            returns = function_info["return_statements"]

            purpose_prompt = f"""Analyze this Python function and describe its purpose in 1-2 sentences.
            Do not offer suggestions, refactorings, or code improvements. Only describe the purpose of the code *as written*:
    ```python
    {code}
    ```"""
            purpose = self.generate_response(purpose_prompt)

            params_prompt = f"""For function '{name}', document these parameters: {params}
    Function purpose: {purpose}
    Provide Google-style parameter documentation with:
    - Name
    - Type
    - Description
    - Any usage constraints

    Do not offer suggestions, refactorings, or code improvements.
    Only describe the purpose of the code *as written*."""
            param_docs = self.generate_response(params_prompt)

            returns_prompt = f"""Document the return value for '{name}' based on:
    - Return statements: {returns}
    - Function purpose: {purpose}
    Include:
    - Return type
    - Description
    - Special cases

    Do not offer suggestions, refactorings, or code improvements.
    Only describe the purpose of the code *as written*."""
            return_doc = self.generate_response(returns_prompt)

            examples_prompt = f"""Generate 2-3 usage examples for '{name}':
    1. Basic usage
    2. Edge case
    3. Advanced scenario (if applicable)
    Format each example as:
    ```python
    # Explanation
    code
    ```

    Do not offer suggestions, refactorings, or code improvements.
    Only describe the purpose of the code *as written*."""
            examples = self.generate_response(examples_prompt)

            docstring_prompt = f"""Create a Google-style docstring for this function:
    ```python
    {code}

    Include:

    A one-line description

    Args section with parameter details

    Returns section with return value details

    Examples section showing usage

    Do not offer suggestions, refactorings, or code improvements.
    Only describe the purpose of the code *as written*."""

            docstring = self.generate_response(docstring_prompt)

            formatted_docstring = f'"""{docstring}"""'

            markdown_output = f"""# {name}

    Purpose

    {purpose}
    Parameters

    {param_docs}
    Returns

    {return_doc}
    Examples

    {examples}
    Docstring

    {formatted_docstring}
    ```"""

            return {
                "markdown": markdown_output,
                "docstring": formatted_docstring
            }
