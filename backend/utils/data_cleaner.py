import re
import string

def clean_resume_text(text: str) -> str:
    """
    Cleans raw text extracted from a PDF to make it suitable for Gen AI analysis.
    """
    if not text:
        return ""

    # 1. Remove non-printable/ASCII characters
    text = "".join(filter(lambda x: x in string.printable, text))

    # 2. Replace multiple newlines or tabs with a single space
    text = re.sub(r'[\t\n\r\f\v]+', ' ', text)

    # 3. Remove URLs (Optional: sometimes useful to keep for LinkedIn)
    # text = re.sub(r'http\S+\s*', ' ', text)

    # 4. Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()

    return text

def summarize_text_if_long(text: str, max_chars: int = 10000) -> str:
    """
    Trims text if it exceeds a certain length to stay within token limits.
    10,000 characters is usually more than enough for a standard CV.
    """
    if len(text) > max_chars:
        return text[:max_chars] + "..."
    return text