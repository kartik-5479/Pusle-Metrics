import json
import os
from typing import Any, Dict

from dotenv import load_dotenv

from utils.helpers import normalize_analysis

load_dotenv(override=True)

MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-3.6-flash")


class GeminiConfigurationError(Exception):
    """Raised when Gemini is not configured."""


class GeminiAnalysisError(Exception):
    """Raised when Gemini cannot return a valid analysis."""


def _get_client():
    api_key = os.getenv("GEMINI_API_KEY", "").strip()
    if not api_key:
        raise GeminiConfigurationError(
            "Gemini API key is not configured. Please add GEMINI_API_KEY to your .env file."
        )
    try:
        from google import genai
        return genai.Client(api_key=api_key)
    except Exception as exc:
        raise GeminiConfigurationError("Gemini could not be initialized.") from exc


def analyze_report(document: Dict[str, Any]) -> Dict[str, Any]:
    """Analyze extracted report data using the current Google GenAI SDK."""
    client = _get_client()
    prompt = _analysis_prompt(document)
    from google.genai import types

    parts = [types.Part.from_text(text=prompt)]
    if document.get("kind") in {"image", "pdf"}:
        content_key = "image_bytes" if document["kind"] == "image" else "pdf_bytes"
        parts.append(
            types.Part.from_bytes(
                data=document[content_key],
                mime_type=document["mime_type"],
            )
        )
    contents = [types.Content(role="user", parts=parts)]

    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=contents,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                temperature=0.1,
            ),
        )
        raw_text = getattr(response, "text", "") or ""
        if not raw_text.strip():
            raise GeminiAnalysisError("Gemini returned an empty analysis.")
        parsed = json.loads(raw_text)
    except GeminiConfigurationError:
        raise
    except GeminiAnalysisError:
        raise
    except json.JSONDecodeError as exc:
        raise GeminiAnalysisError(
            "Gemini returned an invalid analysis format. Please try again."
        ) from exc
    except Exception as exc:
        message = str(exc).lower()
        if "api key" in message or "permission" in message or "unauthorized" in message:
            user_message = "Gemini rejected the API key. Please verify GEMINI_API_KEY in your .env file."
        elif "quota" in message or "rate limit" in message or "resource exhausted" in message:
            user_message = "Gemini usage limit reached. Please wait and try again."
        else:
            user_message = "Gemini could not analyze this report. Please try again."
        raise GeminiAnalysisError(user_message) from exc

    if not isinstance(parsed, dict):
        raise GeminiAnalysisError("Gemini returned an unexpected response format.")
    return normalize_analysis(parsed)


def _analysis_prompt(document: Dict[str, Any]) -> str:
    extracted_text = document.get("text", "")
    return f"""
You are a cautious medical-report analysis assistant. This is informational education,
not diagnosis. Extract only facts present in the supplied report. Never invent patient
information, values, diagnoses, or reference ranges. Use \"Not available\" when absent.
Classify parameters only when a provided reference range, explicit report flag, or stated
laboratory interpretation supports it. Use exactly Normal, Borderline, or Abnormal when
classification is justified; otherwise use Not available. Do not recommend prescription
medicines. Use cautious wording such as may indicate, could be associated with, appears
outside the provided reference range, and discuss with a qualified healthcare professional.

Write for a person without medical training. For every parameter that has a value, make
the explanation 2 to 4 short sentences. First state what the test generally measures in
simple language, then compare the reported value with the report's own reference range,
then explain why the result may matter without diagnosing. Mention when the result appears
within range. Do not use unexplained jargon; if a medical term is necessary, define it in
plain language immediately, for example: \"Hyperglycemia means a higher-than-usual blood
sugar level; this word alone is not a diagnosis.\" Do not make recommendations based on
ranges that are not in the report.

After the parameter analysis, provide a report breakdown that connects the main findings
to the supplied values and ranges in 2 or 3 short bullets. Return no more than 3 key
insights, 2 precautions, and 3 recommendations. Each item must be specific to a finding
in this report and must add new information; do not repeat the summary, parameter
explanation, or the same generic healthcare disclaimer in every list. If there are no
supported insights or recommendations, return an empty list rather than filler text.
Precautions should identify what the person should be careful about when interpreting the
finding. Recommendations should be practical, general, and clearly tied to the report;
never prescribe medication, suggest changing treatment, or invent lifestyle advice that
the report does not support.
Return JSON only with this exact shape:
{{
  "patient_information": {{"name":"", "age":"", "gender":"", "report_type":"", "date":""}},
  "summary": {{"overall_status":"", "summary_text":""}},
  "statistics": {{"normal":0,"borderline":0,"abnormal":0}},
    "parameters": [{{"name":"","value":"","unit":"","reference_range":"","status":"","explanation":"2 to 4 simple sentences explaining what this test measures and what this reported result may mean."}}],
    "breakdown": ["A short, simple explanation of the main finding supported by the report."],
  "key_insights": [],
    "precautions": ["A general, educational precaution supported by the reported findings."],
  "recommendations": []
}}
Report text (may be empty for an image):
{extracted_text}
"""
