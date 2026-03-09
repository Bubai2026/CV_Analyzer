import os
import google.generativeai as genai
from backend.core.prompts import RESUME_ANALYSER_PROMPT

# Use your hardcoded key or fixed .env logic here
api_key = "API_Key" 
genai.configure(api_key=api_key)

def analyze_resume_with_ai(resume_text, job_description):
    try:
        # UPDATED MODEL NAME: gemini-1.5-flash -> gemini-2.5-flash
        model = genai.GenerativeModel('gemini-2.5-flash')
        
        full_prompt = f"{RESUME_ANALYSER_PROMPT}\n\nJob Description:\n{job_description}\n\nResume Text:\n{resume_text}"
        
        response = model.generate_content(full_prompt)
        return response.text
    except Exception as e:
        # If gemini-2.5-flash is restricted in your region, try 'gemini-1.5-flash-latest'
        return f"AI Engine Error: {str(e)}"