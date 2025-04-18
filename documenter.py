import os
from typing import List
from config import INPUT_DIR, OUTPUT_DIR
from extractor import extract_definitions
from parser import extract_function_info
from prompt_chain import PromptChain


def document_python_file(file_path: str, output_dir: str) -> List[str]:
    """Main workflow to document a Python file into a dedicated output directory."""
    if not os.path.exists(file_path):
        print(f"Error: File not found - {file_path}")
        return []

    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    definitions = extract_definitions(file_path)

    if not definitions:
        print(f"No classes or functions found in {file_path}.")
        return []

    chain = PromptChain()
    generated_files = []

    for defn in definitions:
        if defn["type"] == "function":
            func_info = extract_function_info(defn["code"])
            docs = chain.generate_documentation(func_info, is_class=False)
            md_path = os.path.join(output_dir, f"{defn['name']}.md")
        elif defn["type"] == "class":
            class_info = {
                "name": defn["name"],
                "raw_code": defn["code"]
            }
            docs = chain.generate_documentation(class_info, is_class=True)
            md_path = os.path.join(output_dir, f"{defn['name']}.md")
        elif defn["type"] == "method":
            continue

        with open(md_path, 'w', encoding="utf-8") as f:
            f.write(docs["markdown"])
        generated_files.append(md_path)

        print(f"✅ Generated documentation: {md_path}")

    return generated_files


def find_python_files(directory: str) -> List[str]:
    """Recursively find all Python files in a directory."""
    python_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py") and file != os.path.basename(__file__):
                python_files.append(os.path.join(root, file))
    return python_files
