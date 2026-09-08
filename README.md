# Pulse Metrics

Pulse Metrics is a Streamlit healthcare dashboard that turns supported medical reports into structured, plain-language information for discussion with a qualified healthcare professional. It is an educational tool, not a diagnostic system.

## Features

- Native collapsible Streamlit sidebar with page navigation
- PDF text extraction with PyMuPDF
- Image report analysis through Gemini multimodal input
- Structured Gemini output with guarded parsing and missing-value handling
- Normal, borderline, and abnormal parameter summaries
- Session-based report analysis without persistent medical-report storage
- Educational guides and privacy-focused messaging
- Responsive light/dark dashboard styling

## Technology

Python, Streamlit, Pandas, NumPy, Pillow, PyMuPDF, Google GenAI SDK, and python-dotenv.

## Setup

1. Activate the existing virtual environment.
2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Copy or edit `.env` and provide your own key:

```text
GEMINI_API_KEY=your_key_here
GEMINI_MODEL=gemini-3.6-flash
```

The key is loaded with `python-dotenv` and is never displayed or logged. Do not commit `.env`.

## Run

```powershell
py -m streamlit run app.py
```

## Analysis flow

Reports are validated at 10 MB and limited to PDF, JPG, JPEG, and PNG. Text-based PDFs are read in memory with PyMuPDF. Images are validated with Pillow and sent to Gemini as image bytes. Gemini is instructed to return a strict JSON structure; the response is normalized before display. Original report contents are not written to disk.

## Privacy and safety

Uploaded reports are processed in memory and are not written to disk by the application. This analysis is for informational purposes only and is not a medical diagnosis. Please consult a qualified healthcare professional for medical advice. Pulse Metrics does not recommend prescription medication.

## Future improvements

Possible next steps include authenticated storage, encrypted deployment storage, OCR for image-only PDFs, clinician-reviewed terminology, and automated integration tests.
