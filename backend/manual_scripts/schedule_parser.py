from datetime import datetime


def complete_shared_values(row, previous_row):
    completed_row = row.copy()

    if previous_row is None:
        return completed_row

    if completed_row[0] is None:
        completed_row[0] = previous_row[0]

        previous_end = previous_row[2].split("-")[-1].strip()
        current_start = (completed_row[2] or "").split("-")[0].strip()

        if not completed_row[1] and current_start == previous_end:
            completed_row[1] = previous_row[1]

    return completed_row


def parse_schedule_row(row):
    if len(row) != 8:
        return None

    cells = []

    for cell in row:
        text = cell or ""
        cleaned_text = " ".join(text.split())
        cells.append(cleaned_text)

    week, date_text, time_text, location, topic, outcomes, teaching_type, professor = cells

    if not date_text:
        return None

    if week and not week.isdecimal():
        return None

    try:
        date_value = datetime.strptime(date_text, "%d.%m.%Y")
        start_text, end_text = time_text.split("-")
        start_time = datetime.strptime(start_text.strip(), "%H:%M")
        end_time = datetime.strptime(end_text.strip(), "%H:%M")
    except ValueError:
        return None

    week_number = None

    if week:
        week_number = int(week)

    return {
        "week": week_number,
        "date": date_value.strftime("%d.%m.%Y"),
        "start_time": start_time.strftime("%H:%M"),
        "end_time": end_time.strftime("%H:%M"),
        "location": location,
        "topic": topic,
        "learning_outcomes": outcomes,
        "teaching_type": teaching_type,
        "professor": professor,
    }

# def collect_row_warnings(row, completed_row, source):
#     warnings = []

#     fields = (
#         "week",
#         "date",
#         "time",
#         "location",
#         "topic",
#         "learning_outcomes",
#         "teaching_type",
#         "professor",
#     )

#     def add_warning(code, field, message, value):
#         warnings.append


def parse_schedule_tables(tables):
    entries = []

    for table in tables:
        previous_row = None

        for row in table["rows"]:
            if len(row) != 8:
                previous_row = None
                continue

            completed_row = complete_shared_values(row, previous_row)
            entry = parse_schedule_row(completed_row)

            if entry is not None:
                entries.append(entry)
                previous_row = completed_row
            else:
                previous_row = None

    return entries
