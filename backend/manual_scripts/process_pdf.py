from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

from pdf_reader import read_pdf_tables
from schedule_parser import parse_schedule_tables


def process_pdf(file_path):
    tables = read_pdf_tables(file_path)
    entries = parse_schedule_tables(tables)
    processed_at = datetime.now(ZoneInfo("Europe/Zagreb"))

    return {
        "schema_version": 1,
        "source_file": Path(file_path).name,
        "processed_at": processed_at.strftime("%d.%m.%Y %H:%M"),
        "entries_count": len(entries),
        "entries": entries,
    }
