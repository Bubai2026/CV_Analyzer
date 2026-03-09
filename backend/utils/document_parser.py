import fitz  # PyMuPDF

def extract_text_from_pdf(file_path):
    """
    Extracts all text from a given PDF file path.
    """
    try:
        doc = fitz.open(file_path)
        text = ""
        for page in doc:
            text += page.get_text()
        return text
    except Exception as e:
        print(f"Error parsing PDF: {e}")
        return None