from typing import Any, Dict


DEFAULT_VALUE = "Not available"


def clean_text(value: Any) -> str:
    """Convert optional values into safe display text."""
    if value is None or str(value).strip() == "":
        return DEFAULT_VALUE
    return str(value).strip()


def clean_list(value: Any) -> list[str]:
    """Normalize a model list while ignoring malformed entries."""
    if not isinstance(value, list):
        return []
    return [clean_text(item) for item in value if item and clean_text(item) != DEFAULT_VALUE]


def normalize_analysis(data: Dict[str, Any]) -> Dict[str, Any]:
    """Normalize Gemini output so UI code can safely consume it."""
    patient = data.get("patient_information") or {}
    summary = data.get("summary") or {}
    parameters = data.get("parameters") or []

    normalized_parameters = []
    for item in parameters if isinstance(parameters, list) else []:
        if not isinstance(item, dict):
            continue
        raw_status = clean_text(item.get("status")).lower()
        status = {
            "normal": "Normal",
            "borderline": "Borderline",
            "abnormal": "Abnormal",
        }.get(raw_status, "Not available")
        normalized_parameters.append({
            "name": clean_text(item.get("name")),
            "value": clean_text(item.get("value")),
            "unit": clean_text(item.get("unit")),
            "reference_range": clean_text(item.get("reference_range")),
            "status": status,
            "explanation": clean_text(item.get("explanation")),
        })

    counts = {"normal": 0, "borderline": 0, "abnormal": 0}
    for item in normalized_parameters:
        status = item["status"].lower()
        if status in counts:
            counts[status] += 1

    breakdown = clean_list(data.get("breakdown"))
    if not breakdown:
        breakdown = [
            f"{item['name']} is marked {item['status']} based on the information and reference range shown in the report."
            for item in normalized_parameters
            if item["status"] != DEFAULT_VALUE
        ]

    precautions = clean_list(data.get("precautions"))
    recommendations = clean_list(data.get("recommendations"))
    if not precautions and (counts["borderline"] or counts["abnormal"]):
        precautions = [
            "Discuss borderline or abnormal findings with a qualified healthcare professional, especially if they persist or occur with symptoms.",
            "Do not change prescribed treatment based on this educational analysis alone.",
        ]
    if not recommendations and (counts["borderline"] or counts["abnormal"]):
        recommendations = [
            "Ask a qualified healthcare professional whether repeat testing or follow-up is appropriate for the reported findings.",
            "Bring the original report and any relevant symptoms or medicines to your healthcare discussion.",
        ]

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
            "normal": counts["normal"],
            "borderline": counts["borderline"],
            "abnormal": counts["abnormal"],
        },
        "parameters": normalized_parameters,
        "breakdown": breakdown,
        "key_insights": [clean_text(item) for item in data.get("key_insights", []) if item],
        "precautions": precautions,
        "recommendations": recommendations,
    }


def status_class(status: str) -> str:
    return status.lower().replace(" ", "-")
