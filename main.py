from documenter import document_python_file, find_python_files
import time
import os
from config import INPUT_DIR, OUTPUT_DIR


def main():
    """Main function to document all Python files, creating a separate bpplgm-qwen-docs folder for each file."""
    if not os.path.isdir(INPUT_DIR):
        print(f"Error: Input directory not found - {INPUT_DIR}")
        return

    start_time = time.time()
    total_files = 0
    total_definitions = 0

    python_files = find_python_files(INPUT_DIR)

    for file_path in python_files:
        file_start_time = time.time()
        rel_path = os.path.relpath(file_path, INPUT_DIR)
        print(f"\n📄 Processing file: {rel_path}")

        # Create a dedicated bpplgm-qwen-docs folder for this Python file
        file_name = os.path.splitext(os.path.basename(file_path))[0]
        file_output_dir = os.path.join(OUTPUT_DIR, f"{file_name}_docs")
        os.makedirs(file_output_dir, exist_ok=True)

        generated_files = document_python_file(file_path, file_output_dir)

        file_time = time.time() - file_start_time
        print(f"⏱️  Time to process: {file_time:.2f} seconds")
        print(f"📝 Generated {len(generated_files)} documentation files in {file_output_dir}")

        total_files += 1
        total_definitions += len(generated_files)

    total_time = time.time() - start_time
    print("\n" + "=" * 50)
    print(f"🏁 Documentation generation complete!")
    print(f"📂 Total files processed: {total_files}")
    print(f"📝 Total definitions documented: {total_definitions}")
    print(f"⏱️  Total time elapsed: {total_time:.2f} seconds")
    print("=" * 50)


if __name__ == "__main__":
    main()

