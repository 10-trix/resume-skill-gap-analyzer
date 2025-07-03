import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv
from utils.parser import extract_text_from_resume
import matplotlib.pyplot as plt
import ast  # <-- Added for safe literal evaluation

# Load environment
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))  # 🔐 Securely load from .env

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

st.markdown("")

# Utility: Safe extractor for Gemini list strings
def safe_extract_list(text, start_key, end_key):
    try:
        raw = analysis.split(start_key)[1].split(end_key)[0].strip()
        if not raw.startswith("[\"") and not raw.startswith("['"):
            raw = "[" + ", ".join(f'"{item.strip()}"' for item in raw.strip("[]").split(",")) + "]"
        return ast.literal_eval(raw)
    except Exception:
        return []

# --------------- Analyze Button Logic ---------------
if st.button("🔍 Analyze Skill Gap"):
    if resume_file and jd_text:
        with st.spinner("⚙️ Analyzing resume... please wait"):
            resume_text = extract_text_from_resume(resume_file)

            prompt = f"""
Compare the following RESUME and JOB DESCRIPTION. Return the output in this format exactly:

Skills in Resume: [skill1, skill2, ...]
Skills Required: [skillA, skillB, ...]
Missing Skills: [missing1, missing2, ...]
Learning Roadmap: (in 4-5 bullet points)

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

        # ------ Skill Matching Visualization ------
        try:
            skills_in_resume = safe_extract_list(analysis, "Skills in Resume:", "Skills Required:")
            required_skills = safe_extract_list(analysis, "Skills Required:", "Missing Skills:")
            missing_skills = safe_extract_list(analysis, "Missing Skills:", "Learning Roadmap:")

            matched_skills = list(set(skills_in_resume).intersection(set(required_skills)))
            match_percent = int((len(matched_skills) / len(required_skills)) * 100) if required_skills else 0

            # ⭐ Show Match Score
            st.markdown(f"### ⭐ Resume Match Rating: **{match_percent}/100**")

            # 🥧 Pie Chart
            labels = ['Matched Skills', 'Missing Skills']
            values = [len(matched_skills), len(missing_skills)]

            fig, ax = plt.subplots()
            ax.pie(values, labels=labels, autopct='%1.1f%%', colors=['#00b894', '#d63031'])
            ax.axis('equal')
            st.pyplot(fig)

        except Exception as e:
            st.warning("⚠️ Couldn't generate visualizations. Please try again or check input formatting.")
            st.exception(e)

        # 📥 Download Button
        st.download_button(
            label="📥 Download Skill Gap Report",
            data=analysis,
            file_name="SkillGapAnalysis.txt",
            mime="text/plain"
        )
    else:
        st.warning("⚠️ Please upload a resume and paste a job description before analyzing.")

# --------------- Footer ---------------
st.divider()
st.markdown(
    "<p style='text-align: center; color: grey;'>Made by Tanmay | Powered by Gemini Pro</p>",
    unsafe_allow_html=True
)
