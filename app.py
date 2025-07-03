import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv
from utils.parser import extract_text_from_resume

# Load environment
load_dotenv()
genai.configure(api_key=os.getenv("AIzaSyCJ5QoOvrmr14DQnIofdVNOAT52cS5P7hk"))

# --------------- Page Config ---------------
st.set_page_config(
    page_title="Resume Skill Gap Analyzer",
    page_icon="📄",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --------------- Title & Intro ---------------
st.markdown(
    """
    <h1 style='text-align: center;'>📄 Resume Skill Gap Analyzer</h1>
    <p style='text-align: center; font-size: 18px; color: grey;'>
        Analyze your resume against a job description using <strong>Gemini Pro AI</strong> and get a personalized learning roadmap.
    </p>
    """,
    unsafe_allow_html=True
)

st.divider()

# --------------- Resume + JD Input ---------------
col1, col2 = st.columns(2)
with col1:
    resume_file = st.file_uploader("📎 Upload Your Resume", type=["pdf", "docx"])
with col2:
    jd_text = st.text_area("📝 Paste the Job Description", height=250, placeholder="Paste job description here...")

# --------------- Analyze Button ---------------
if resume_file and jd_text:
    if st.button("🔍 Analyze Skill Gap"):
        with st.spinner("⚙️ Analyzing resume... please wait"):
            resume_text = extract_text_from_resume(resume_file)

            prompt = f"""
Compare the following RESUME and JOB DESCRIPTION and return:
1. Skills found in the resume
2. Skills required by the job
3. Missing skills
4. A personalized learning roadmap

RESUME:
{resume_text}

JOB DESCRIPTION:
{jd_text}
"""

            model = genai.GenerativeModel(model_name="models/gemini-1.5-flash-latest")
            response = model.generate_content(prompt)
            analysis = response.text

        st.success("✅ Analysis Complete!")
        st.markdown("### 📋 Gemini AI Analysis")
        st.markdown(analysis)

        st.download_button(
            label="📥 Download Skill Gap Report",
            data=analysis,
            file_name="SkillGapAnalysis.txt",
            mime="text/plain"
        )
else:
    st.info("Upload a resume and paste a job description to begin analysis.")

# --------------- Footer ---------------
st.divider()
st.markdown(
    "<p style='text-align: center; color: grey;'>Made by Tanmay | Powered by Gemini Pro</p>",
    unsafe_allow_html=True
)
