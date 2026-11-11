from pathlib import Path

from json_storage import save_results
from process_pdf import process_pdf


def main():
    file_path = input("Enter the path to the PDF file: ").strip()
    result = process_pdf(file_path)

    project_root = Path(__file__).resolve().parent.parent
    output_path = save_results(result, project_root / "results")

    print(f"Total entries found: {result['entries_count']}")
    print(f"Results saved to {output_path}")


if __name__ == "__main__":
    main()
