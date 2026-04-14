import streamlit as st
import PyPDF2
import re
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# -------------------------
# CLEAN TEXT
# -------------------------
def clean_text(text):
    text = text.lower()
    text = re.sub(r'\W', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text

# -------------------------
# SKILLS
# -------------------------
skills_list = [
    "python", "java", "machine learning", "data analysis",
    "sql", "excel", "deep learning", "nlp", "tensorflow",
    "pandas", "communication", "project management"
]

def extract_skills(text):
    return [skill for skill in skills_list if skill in text]

def skill_match_score(cv_skills, job_skills):
    if len(job_skills) == 0:
        return 0
    return len(set(cv_skills) & set(job_skills)) / len(job_skills)

# -------------------------
# PDF READER
# -------------------------
def extract_text_from_pdf(file):
    text = ""
    reader = PyPDF2.PdfReader(file)
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text()
    return text

# -------------------------
# UI
# -------------------------
st.title("📄 CV Screening App (AI Powered)")

job_text = st.text_area("📝 Enter Job Description")

uploaded_files = st.file_uploader("📂 Upload CVs (PDF)", accept_multiple_files=True)

if st.button("🚀 Analyze"):
    if job_text and uploaded_files:

        job_clean = clean_text(job_text)
        job_skills = extract_skills(job_clean)

        results = []

        for file in uploaded_files:
            text = extract_text_from_pdf(file)
            clean = clean_text(text)

            cv_skills = extract_skills(clean)

            vectorizer = TfidfVectorizer()
            vectors = vectorizer.fit_transform([clean, job_clean])

            tfidf_score = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]

            skill_score = skill_match_score(cv_skills, job_skills)

            final_score = 0.7 * tfidf_score + 0.3 * skill_score

            missing = list(set(job_skills) - set(cv_skills))

            results.append({
                "file": file.name,
                "score": final_score,
                "skills": cv_skills,
                "missing": missing
            })

        results = sorted(results, key=lambda x: x['score'], reverse=True)

        st.subheader("🏆 Results")

        for r in results:
            st.write(f"📄 {r['file']}")
            st.write(f"⭐ Score: {round(r['score'],2)}")
            st.write(f"✅ Skills: {r['skills']}")
            st.write(f"❌ Missing: {r['missing']}")
            st.write("---")