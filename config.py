import os

# Ollama Configuration
# CHANGE THE ENDPOINT AND MODEL NAME TO WHATEVER IS ON YOUR COMPUTER
OLLAMA_ENDPOINT = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.2:1b"
TEMPERATURE = 0.2  # Lower = more deterministic

# CHANGE THE INPUT DIRECTORY TO YOUR COMPUTER
INPUT_DIR = "C:/Users/lemay/PycharmProjects/CS442-Project/pythonProject/Blender-Python-Procedural-Level-Generation-master"
OUTPUT_DIR = os.path.join(INPUT_DIR, "docs")
