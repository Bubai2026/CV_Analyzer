from fastapi import APIRouter, UploadFile, File, Form
from backend.utils.document_parser import extract_text_from_pdf
from backend.utils.data_cleaner import clean_resume_text
from backend.core.llm_engine import analyze_resume_with_ai
import os
import shutil

router = APIRouter()

@router.post("/analyze")
async def analyze_resume(
    job_description: str = Form(...), 
    resume: UploadFile = File(...)
):
    try:
        # 1. CRITICAL: Ensure the directory exists to avoid 500 Error
        upload_dir = os.path.join("data", "sample_resumes")
        os.makedirs(upload_dir, exist_ok=True)
        
        temp_path = os.path.join(upload_dir, resume.filename)

        # 2. Save the file
        with open(temp_path, "wb") as buffer:
            shutil.copyfileobj(resume.file, buffer)

        # 3. Extract and Clean
        raw_text = extract_text_from_pdf(temp_path)
        if not raw_text or len(raw_text.strip()) == 0:
            return {"error": "Could not read PDF. Please ensure it is a text-based PDF."}
        
        clean_text = clean_resume_text(raw_text)

        # 4. AI Analysis
        analysis_result = analyze_resume_with_ai(clean_text, job_description)

        # 5. Cleanup
        os.remove(temp_path)

        return {"analysis": analysis_result}

    except Exception as e:
        # This will send the actual error message to the frontend instead of just '500'
        return {"error": str(e)}