SCHEDULE_FIELDS = {
    "page": {"type": ["integer", "null"]},
    "week": {"type": ["integer", "null"]},
    "date": {"type": ["string", "null"]},
    "start_time": {"type": ["string", "null"]},
    "end_time": {"type": ["string", "null"]},
    "location": {"type": ["string", "null"]},
    "topic": {"type": ["string", "null"]},
    "learning_outcomes": {"type": ["string", "null"]},
    "teaching_type": {"type": ["string", "null"]},
    "professor": {"type": ["string", "null"]},
}

SCHEDULE_SCHEMA = {
    "type": "object",
    "properties": {
        "schedule": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": SCHEDULE_FIELDS,
                "required": list(SCHEDULE_FIELDS),
                "additionalProperties": False,
            },
        },
        "uncertainties": {
            "type": "array",
            "items": {"type": "string"},
        },
    },
    "required": ["schedule", "uncertainties"],
    "additionalProperties": False,
}
