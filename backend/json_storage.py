import json
from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4


def save_results(result, results_folder):
    results_folder = Path(results_folder)
    results_folder.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    filename = f"{timestamp}_{uuid4().hex}.json"
    output_path = results_folder / filename
    json_text = json.dumps(result, ensure_ascii=False, indent=2)

    with output_path.open("x", encoding="utf-8") as output_file:
        output_file.write(json_text + "\n")

    return output_path
