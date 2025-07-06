# 📄 Resume Skill Gap Analyzer

A powerful AI-powered Streamlit web app that analyzes your resume against a job description using **Gemini Pro** and gives you:

✅ Matched vs Missing Skills  
✅ Personalized Learning Roadmap  
✅ Match Rating Score  
✅ Visual Pie Chart of your skill alignment  

---

## 🚀 Demo

🔗 [[Live App on Streamlit Cloud](https://resume-skill-gap-analyzer-223.streamlit.app/)]

---

## 📸 Screenshots

| Upload Resume & JD | Result with Rating & Chart |
|--------------------|----------------------------|
| ![upload](assets/upload.png) | ![result](assets/result.png) |

---

## 📂 Features

- 📎 Upload your resume (PDF/DOCX)
- 📝 Paste any job description
- 🧠 AI compares and extracts:
  - Skills in your resume
  - Skills required by the JD
  - Missing skills
  - Learning roadmap
- ⭐ Resume match rating (/100)
- 🥧 Skill match pie chart
- 📥 Downloadable report

---

## 💻 Tech Stack

| Tool | Purpose |
|------|---------|
| [Streamlit](https://streamlit.io) | Web app framework |
| [Google Gemini API](https://ai.google.dev) | AI for skill analysis |
| Python | Backend logic |
| Matplotlib | Pie chart visualization |
| dotenv | Manage API secrets |
| PyMuPDF/docx2txt | Resume text extraction |

---

## 🧠 Gemini Prompt

```text
You are an AI designed to extract structured data. Analyze the following RESUME and JOB DESCRIPTION. 
Return your response in EXACTLY the following format:

Skills in Resume: [skill1, skill2, skill3]
Skills Required: [skillA, skillB, skillC]
Missing Skills: [missing1, missing2]
Learning Roadmap:
- Point 1
- Point 2
- Point 3
- Point 4
```
🛠️ Setup Instructions (for local use)
```
git clone https://github.com/10-trix/resume-skill-gap-analyzer.git
cd resume-skill-gap-analyzer
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

Create a .env file and add:
GOOGLE_API_KEY=your_google_gemini_api_key_here

Then run:
streamlit run app.py
```
🌐 Deployment
This app is deployed on Streamlit Cloud. To deploy:

1.Push your code to GitHub

2.Go to Streamlit Cloud

3.Connect your repo

4.Add GOOGLE_API_KEY in Secrets

5.Click Deploy

🙋‍♂️ Author
Tanmay Ranjan
🧑‍💻 [GitHub](https://github.com/10-trix)
📧 [Email](ishutan223@gmail.com)
📍 India
📄 License
MIT License. Free to use with attribution.
