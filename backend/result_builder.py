from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo


def build_document_result(file_path, extracted_data):
    processed_at = datetime.now(ZoneInfo("Europe/Zagreb"))

    return {
        "source_file": Path(file_path).name,
        "processed_at": processed_at.strftime("%d.%m.%Y %H:%M"),
        "entries_count": len(extracted_data["schedule"]),
        "schedule": extracted_data["schedule"],
        "uncertainties": extracted_data["uncertainties"],
    }
