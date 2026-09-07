from typing import Any, Dict


DEFAULT_VALUE = "Not available"


def clean_text(value: Any) -> str:
    """Convert optional values into safe display text."""
    if value is None or str(value).strip() == "":
        return DEFAULT_VALUE
    return str(value).strip()


def normalize_analysis(data: Dict[str, Any]) -> Dict[str, Any]:
    """Normalize Gemini output so UI code can safely consume it."""
    patient = data.get("patient_information") or {}
    summary = data.get("summary") or {}
    statistics = data.get("statistics") or {}
    parameters = data.get("parameters") or []

    normalized_parameters = []
    for item in parameters if isinstance(parameters, list) else []:
        if not isinstance(item, dict):
            continue
        status = clean_text(item.get("status"))
        if status.lower() not in {"normal", "borderline", "abnormal"}:
            status = "Not available"
        normalized_parameters.append({
            "name": clean_text(item.get("name")),
            "value": clean_text(item.get("value")),
            "unit": clean_text(item.get("unit")),
            "reference_range": clean_text(item.get("reference_range")),
            "status": status,
            "explanation": clean_text(item.get("explanation")),
        })

    def count(name: str) -> int:
        value = statistics.get(name, 0)
        return value if isinstance(value, int) and value >= 0 else 0

    return {
        "patient_information": {
            "name": clean_text(patient.get("name")),
            "age": clean_text(patient.get("age")),
            "gender": clean_text(patient.get("gender")),
            "report_type": clean_text(patient.get("report_type")),
            "date": clean_text(patient.get("date")),
        },
        "summary": {
            "overall_status": clean_text(summary.get("overall_status")),
            "summary_text": clean_text(summary.get("summary_text")),
        },
        "statistics": {
            "normal": count("normal"),
            "borderline": count("borderline"),
            "abnormal": count("abnormal"),
        },
        "parameters": normalized_parameters,
        "key_insights": [clean_text(item) for item in data.get("key_insights", []) if item],
        "recommendations": [clean_text(item) for item in data.get("recommendations", []) if item],
    }


def status_class(status: str) -> str:
    return status.lower().replace(" ", "-")
