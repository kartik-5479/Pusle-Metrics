from html import escape
from typing import Dict

import streamlit as st

from components.header import render_header
from utils.helpers import status_class


MEDICAL_TERM_GUIDE = {
    "hyperglycemia": "a higher-than-usual blood sugar level; this term alone is not a diagnosis",
    "hypoglycemia": "a lower-than-usual blood sugar level; this term alone is not a diagnosis",
    "hemoglobin": "a protein in red blood cells that carries oxygen around the body",
    "anemia": "a condition in which the blood may not carry enough oxygen, with causes that need professional assessment",
    "cholesterol": "a waxy substance in the blood that the body uses, but which is interpreted in context and in different forms",
    "hyperlipidemia": "higher-than-usual levels of certain fats in the blood; this term alone is not a diagnosis",
    "creatinine": "a waste product commonly measured to help assess kidney function",
    "bilirubin": "a substance produced when red blood cells are broken down, often considered when assessing liver or blood-related findings",
}


def _term_definitions(text: str) -> list[str]:
    """Return plain-language definitions for recognized terms in an explanation."""
    lowered = text.lower()
    return [
        f"{term.title()}: {definition}."
        for term, definition in MEDICAL_TERM_GUIDE.items()
        if term in lowered
    ]


def _plain_language_explanation(parameter: Dict) -> str:
    """Build a clearer explanation when an older analysis returned a short one."""
    name = str(parameter.get("name", "This parameter"))
    value = str(parameter.get("value", "Not available"))
    unit = str(parameter.get("unit", "")).strip()
    reference_range = str(parameter.get("reference_range", "Not available"))
    status = str(parameter.get("status", "Not available"))
    original = str(parameter.get("explanation", "Not available")).strip()

    definitions = _term_definitions(original)
    definition_text = " " + " ".join(definitions) if definitions else ""
    if len(original.split()) >= 24:
        return f"{original}{definition_text}"

    reported_value = f"{value} {unit}".strip()
    if status == "Normal":
        comparison = f"The reported value of {reported_value} is within the supplied reference range of {reference_range}."
        meaning = "This means the result is not flagged as outside the laboratory range shown in this report."
    elif status == "Borderline":
        comparison = f"The reported value of {reported_value} is close to or slightly outside the supplied reference range of {reference_range}."
        meaning = "Borderline results need context and should be discussed with a qualified healthcare professional."
    elif status == "Abnormal":
        comparison = f"The reported value of {reported_value} appears outside the supplied reference range of {reference_range}."
        meaning = "This can be associated with different causes and does not by itself establish a diagnosis."
    else:
        comparison = f"The report lists a value of {reported_value}, but a usable reference range is not available."
        meaning = "Without a reference range, this result cannot be reliably classified from the report alone."

    if original and original != "Not available":
        return f"{original} {comparison} {meaning}{definition_text} Please discuss this result with a qualified healthcare professional if you have concerns."
    return f"This report lists {name} as a measured parameter. {comparison} {meaning}{definition_text} Please discuss this result with a qualified healthcare professional if you have concerns."


def render(analysis: Dict, sample: bool = False) -> None:
    render_header()
    if st.button("← Back to Home"):
        st.session_state.page = "Home"
        st.rerun()

    st.title("Detailed Analysis" + (" · SAMPLE DATA" if sample else ""))
    if sample:
        st.info("This is sample data for demonstration only. It is not from your medical report.")
    st.caption("Review the information identified in the report. This is educational information, not a diagnosis.")
    patient = analysis.get("patient_information", {})
    summary = analysis.get("summary", {})
    stats = analysis.get("statistics", {})

    st.markdown("### Patient and Report Information")
    info_columns = st.columns(5)
    for column, label, key in zip(
        info_columns,
        ["Name", "Age", "Gender", "Report Type", "Date"],
        ["name", "age", "gender", "report_type", "date"],
    ):
        column.markdown(f'<div class="pm-card"><div class="pm-muted">{label}</div><strong>{escape(str(patient.get(key, "Not available")))}</strong></div>', unsafe_allow_html=True)

    st.markdown("### Overall Summary")
    st.markdown(f'<div class="pm-card"><span class="pm-eyebrow">Overall Health Status</span><h2>{escape(str(summary.get("overall_status", "Not available")))}</h2><p class="pm-muted">{escape(str(summary.get("summary_text", "Not available")))}</p></div>', unsafe_allow_html=True)

    st.markdown("### Report Breakdown")
    breakdown = analysis.get("breakdown", [])
    if breakdown:
        for item in breakdown:
            st.markdown(f'<div class="pm-card pm-list-item" style="margin-bottom:.7rem">{escape(str(item))}</div>', unsafe_allow_html=True)
    else:
        st.info("No additional report breakdown was returned.")

    st.markdown("### Precautions and Recommendations")
    precautions = analysis.get("precautions", [])
    recommendations = analysis.get("recommendations", [])
    for label, items in [("Precaution", precautions), ("Recommendation", recommendations)]:
        for item in items:
            st.markdown(f'<div class="pm-card pm-list-item" style="margin-bottom:.7rem"><strong>{label}</strong><br>{escape(str(item))}</div>', unsafe_allow_html=True)
    if not precautions and not recommendations:
        st.info("No additional precautions or recommendations were returned.")

    st.markdown("### Statistics")
    stat_columns = st.columns(3)
    for column, label, key in zip(stat_columns, ["Normal", "Borderline", "Abnormal"], ["normal", "borderline", "abnormal"]):
        column.metric(label, stats.get(key, 0))

    st.markdown("### Parameter Analysis")
    parameters = analysis.get("parameters", [])
    if not parameters:
        st.info("No parameter-level results are available.")
        return

    rows = []
    for parameter in parameters:
        status = str(parameter.get("status", "Not available"))
        status_markup = f'<span class="pm-status {status_class(status)}">{escape(status)}</span>'
        rows.append(
            "<tr>"
            f"<td>{escape(str(parameter.get('name', 'Not available')))}</td>"
            f"<td>{escape(str(parameter.get('value', 'Not available')))}</td>"
            f"<td>{escape(str(parameter.get('unit', 'Not available')))}</td>"
            f"<td>{escape(str(parameter.get('reference_range', 'Not available')))}</td>"
            f"<td>{status_markup}</td>"
            "<td>See plain-language explanation below.</td>"
            "</tr>"
        )
    table = """<div class="pm-table-wrap"><table class="pm-table"><thead><tr>
        <th>Parameter</th><th>Value</th><th>Unit</th><th>Reference Range</th><th>Status</th><th>Explanation</th>
        </tr></thead><tbody>""" + "".join(rows) + "</tbody></table></div>"
    st.markdown(table, unsafe_allow_html=True)

    st.markdown("### Plain-language explanations")
    st.caption("These explanations describe the reported result in simple terms. They are educational and do not provide a diagnosis.")
    for parameter in parameters:
        name = escape(str(parameter.get("name", "Not available")))
        status = str(parameter.get("status", "Not available"))
        value = escape(str(parameter.get("value", "Not available")))
        explanation = escape(_plain_language_explanation(parameter))
        st.markdown(
            f"""<article class="pm-explanation-card">
            <div class="pm-explanation-heading"><h4>{name}</h4>
            <span class="pm-status {status_class(status)}">{escape(status)}</span></div>
            <div class="pm-explanation-value">Reported result: <strong>{value}</strong></div>
            <p>{explanation}</p>
            </article>""",
            unsafe_allow_html=True,
        )
