from pathlib import Path
from typing import Optional


ALLOWED_EXTENSIONS = {".pdf", ".jpg", ".jpeg", ".png"}
MAX_FILE_SIZE = 10 * 1024 * 1024


def validate_upload(uploaded_file) -> Optional[str]:
    """Return a user-facing validation error, or None when valid."""
    if uploaded_file is None:
        return "Please choose a medical report first."

    suffix = Path(uploaded_file.name).suffix.lower()
    if suffix not in ALLOWED_EXTENSIONS:
        return "Unsupported file type. Please upload a PDF, JPG, JPEG, or PNG file."

    if uploaded_file.size > MAX_FILE_SIZE:
        return "The file is larger than 10 MB. Please upload a smaller report."

    return None
