from io import BytesIO
from pathlib import Path
from typing import Dict

import fitz
from PIL import Image


class DocumentProcessingError(Exception):
    """Raised when a report cannot be read safely."""


def process_document(file_name: str, content: bytes) -> Dict[str, object]:
    """Extract text from PDFs and validate image reports for multimodal analysis."""
    extension = Path(file_name).suffix.lower()
    if extension == ".pdf":
        return _process_pdf(content)
    if extension in {".jpg", ".jpeg", ".png"}:
        return _process_image(content, extension)
    raise DocumentProcessingError("This file format is not supported.")


def _process_pdf(content: bytes) -> Dict[str, object]:
    try:
        document = fitz.open(stream=content, filetype="pdf")
        text = "\n".join(page.get_text("text") for page in document).strip()
        page_count = document.page_count
        document.close()
    except Exception as exc:
        raise DocumentProcessingError("The PDF could not be read.") from exc

    if not text:
        raise DocumentProcessingError(
            "This PDF does not contain selectable text. Image-only PDFs are not supported yet."
        )
    return {"kind": "text", "text": text, "page_count": page_count}


def _process_image(content: bytes, extension: str) -> Dict[str, object]:
    try:
        image = Image.open(BytesIO(content))
        image.load()
    except Exception as exc:
        raise DocumentProcessingError("The image could not be read.") from exc

    return {
        "kind": "image",
        "image_bytes": content,
        "mime_type": "image/png" if extension == ".png" else "image/jpeg",
        "dimensions": image.size,
    }
