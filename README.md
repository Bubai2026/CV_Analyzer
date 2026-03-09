# 🎯 AI-Powered Resume & JD Analyzer

A sophisticated Generative AI application that evaluates resumes against job descriptions (JD) using **Google Gemini 2.5 Flash**. This tool provides a compatibility score, highlights key strengths, identifies missing requirements, and offers actionable optimization advice.

---

## 🚀 Key Features

* **Deep Semantic Analysis**: Goes beyond keyword matching to understand the context of experience.
* **Real-time Scoring**: Provides a percentage-based match score between the Resume and JD.
* **Gap Analysis**: Automatically identifies missing technical and soft skills.
* **FastAPI Backend**: High-performance asynchronous API for handling document parsing and AI requests.
* **Streamlit UI**: A clean, interactive dashboard for easy file uploads and visualization.

---

## 🛠️ Tech Stack

* **Frontend**: [Streamlit](https://streamlit.io/)
* **Backend**: [FastAPI](https://fastapi.tiangolo.com/)
* **AI Engine**: [Google Gemini 2.5 Flash API](https://ai.google.dev/)
* **PDF Parsing**: [PyMuPDF (Fitz)](https://pymupdf.readthedocs.io/)
* **Environment**: Python 3.10+

---

## 📂 Project Structure

```text
genai_resume_analyzer/
├── backend/
│   ├── api/
│   │   └── routes.py         # API Endpoints
│   ├── core/
│   │   ├── llm_engine.py     # Gemini AI Integration
│   │   └── prompts.py        # System Prompts
│   ├── utils/
│   │   ├── document_parser.py # PDF Extraction
│   │   └── data_cleaner.py    # Text Preprocessing
│   └── main.py               # FastAPI Entry Point
├── frontend/
│   └── app.py                # Streamlit UI Dashboard
├── .env                      # API Keys (Local Only - Hidden from Git)
├── .gitignore                # Files to ignore in Git
└── requirements.txt          # Project Dependencies