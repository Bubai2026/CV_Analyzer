import streamlit as st
import requests
import re

# 1. Page Configuration
st.set_page_config(page_title="AI Resume Analyzer 2026", page_icon="🎯", layout="wide")

st.title("🎯 GenAI Resume-JD Matcher")
st.markdown("---")

# 2. Layout: Two Columns for Input
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.subheader("📋 Job Description")
    jd_input = st.text_area(
        "Paste the Job Description here...", 
        height=300, 
        placeholder="e.g., We are looking for a Python Developer with Gemini experience..."
    )

with col2:
    st.subheader("📤 Upload Resume")
    resume_file = st.file_uploader("Choose a PDF file", type=["pdf"])
    st.info("Ensure the PDF is text-based for the best results.")

# 3. Execution Logic
if st.button("🚀 Analyze Compatibility"):
    if not jd_input or not resume_file:
        st.warning("Kindly provide both the Job Description and a Resume PDF.")
    else:
        with st.spinner("Gemini 2.5 is evaluating your profile..."):
            try:
                # Prepare data for API
                files = {"resume": (resume_file.name, resume_file.getvalue(), "application/pdf")}
                data = {"job_description": jd_input}

                # Call the FastAPI Backend
                response = requests.post("http://127.0.0.1:8000/analyze", data=data, files=files)
                
                # Parse JSON safely
                res_data = response.json()

                if response.status_code == 200:
                    # Check if backend sent an internal error message
                    if "error" in res_data:
                        st.error(f"Backend Logic Error: {res_data['error']}")
                    else:
                        analysis_text = res_data.get("analysis", "")
                        
                        st.success("Analysis Complete!")
                        st.divider()

                        # --- SMART UI: Extract Score ---
                        # Looks for a pattern like "85%" in the AI text
                        score_match = re.search(r"(\d+)%", analysis_text)
                        
                        res_col1, res_col2 = st.columns([1, 3])
                        
                        with res_col1:
                            if score_match:
                                score = int(score_match.group(1))
                                st.metric("Match Score", f"{score}%")
                                st.progress(score / 100)
                            else:
                                st.metric("Match Score", "N/A")
                        
                        with res_col2:
                            st.markdown("### 📝 Detailed Feedback")
                            st.markdown(analysis_text)
                
                else:
                    st.error(f"Server Error ({response.status_code}): {res_data.get('detail', 'The server failed to respond.')}")

            except requests.exceptions.ConnectionError:
                st.error("Could not connect to the Backend. Is Uvicorn running on port 8000?")
            except Exception as e:
                st.error(f"An unexpected frontend error occurred: {e}")

st.markdown("---")
st.caption("Powered by FastAPI & Gemini 2.5 Flash • 2026")