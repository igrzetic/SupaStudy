from pathlib import Path

from dotenv import load_dotenv

from ai_extractor import extract_document
from evaluate_schedule import evaluate_document
from json_storage import save_results
from result_builder import build_document_result

BACKEND_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = BACKEND_DIR.parent


def main():
    load_dotenv(BACKEND_DIR / ".env")

    file_path = Path(
        input("Enter the path to the document: ").strip()
    ).expanduser().resolve()

    print("[1/3] Extracting information from the document...")
    extracted_data = extract_document(file_path)
    result = build_document_result(file_path, extracted_data)

    print("[2/3] Saving extracted information...")
    output_path = save_results(result, PROJECT_ROOT / "results")
    print(f"Results saved to: {output_path}")

    print("[3/3] Evaluating the result against the original document...")

    try:
        report = evaluate_document(file_path, extracted_data)
    except Exception as error:
        print(f"Evaluation failed ({type(error).__name__}): {error}")
        print("The extracted JSON is saved, but has not been evaluated.")
        return

    print(f"Evaluation model: {report['evaluation_model']}")
    print(f"Evaluation score (0–1): {report['score']}")
    print(f"Evaluation explanation: {report['reason']}")
    print("Processing completed.")


if __name__ == "__main__":
    main()
