import json
import os
from typing import Any, Dict

from dotenv import load_dotenv

from utils.helpers import normalize_analysis

load_dotenv(override=True)

MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")


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
    contents = [prompt]
    if document.get("kind") == "image":
        from google.genai import types
        contents.append(types.Part.from_bytes(
            data=document["image_bytes"],
            mime_type=document["mime_type"],
        ))

    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=contents,
            config={"response_mime_type": "application/json"},
        )
        raw_text = getattr(response, "text", "") or ""
        parsed = json.loads(raw_text)
    except GeminiConfigurationError:
        raise
    except Exception as exc:
        raise GeminiAnalysisError(
            "Gemini could not analyze this report. Please check your API configuration and try again."
        ) from exc

    if not isinstance(parsed, dict):
        raise GeminiAnalysisError("Gemini returned an unexpected response format.")
    return normalize_analysis(parsed)


def _analysis_prompt(document: Dict[str, Any]) -> str:
    extracted_text = document.get("text", "")
    return f"""
You are a cautious medical-report analysis assistant. This is informational education,
not diagnosis. Extract only facts present in the supplied report. Never invent patient
information, values, diagnoses, or reference ranges. Use \"Not available\" when absent.
Classify parameters only when a provided reference range or clear report context supports
it. Use exactly Normal, Borderline, or Abnormal when classification is possible;
otherwise use Not available. Do not recommend prescription medicines. Use cautious wording
such as may indicate, could be associated with, and discuss with a healthcare professional.
Return JSON only with this exact shape:
{{
  "patient_information": {{"name":"", "age":"", "gender":"", "report_type":"", "date":""}},
  "summary": {{"overall_status":"", "summary_text":""}},
  "statistics": {{"normal":0,"borderline":0,"abnormal":0}},
  "parameters": [{{"name":"","value":"","unit":"","reference_range":"","status":"","explanation":""}}],
  "key_insights": [],
  "recommendations": []
}}
Report text (may be empty for an image):
{extracted_text}
"""
