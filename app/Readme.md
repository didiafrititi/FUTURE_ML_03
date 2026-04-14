# 📄 AI-Powered CV Screening System

## 🚀 Project Overview

Recruitment teams often receive hundreds of CVs for a single job position. Manually reviewing each CV is time-consuming, inconsistent, and prone to human error.

This project presents an AI-powered CV screening system that automatically:

- Analyzes resumes (PDF/Text)
- Extracts relevant skills
- Matches candidates with job descriptions
- Ranks candidates based on suitability
- Identifies missing skills

This solution simulates real-world HR Tech tools used in recruitment platforms.

---

## 🎯 Features

✔ Text preprocessing and cleaning  
✔ Skill extraction using NLP techniques  
✔ Job description analysis  
✔ TF-IDF similarity scoring  
✔ Skill-based matching score  
✔ Final ranking of candidates  
✔ Missing skills identification  
✔ Interactive web application (Streamlit)

---

## 🧠 How It Works

The system uses a hybrid scoring approach:

### 1. Text Similarity (TF-IDF)
Measures how similar a CV is to the job description.

### 2. Skill Matching Score
Evaluates how many required skills from the job are present in the CV.


## 📊 Score Interpretation

The scoring system produces values between **0 and 1**, where:

- **0** indicates no similarity between the CV and the job description
- **1** indicates a perfect match

### 🧠 How the Score is Computed

The final score is a weighted combination of two components:

1. **Text Similarity (TF-IDF + Cosine Similarity)**
   - Measures how similar the resume content is to the job description
   - Output range: 0 to 1

2. **Skill Matching Score**
   - Measures how many required job skills are present in the CV
   - Formula:
     ```
     Skill Score = (Number of matching skills) / (Total job skills)
     ```


### 📈 Score Meaning

- **0.8 – 1.0** → Excellent match  
- **0.6 – 0.8** → Good match  
- **0.4 – 0.6** → (Average match)  
- **0.2 – 0.4** → Weak match  
- **0.0 – 0.2** → Very poor match  

This hybrid scoring approach ensures that both semantic similarity and skill relevance are considered.

### Final Score Formula:
Final Score = 0.7 * TF-IDF Score + 0.3 * Skill Match Score


This ensures both semantic similarity and skill relevance are considered.

---

## 

## 📂 Project Structure
FUTURE_ML_03/
│
├── app.py # Streamlit web app
├── requirements.txt # Dependencies
├── README.md # Project documentation
│
├── notebooks/
│ └── cv_screening.ipynb # NLP pipeline & experiments



---

## 💻 Installation

Clone the repository:
https://github.com/didiafrititi/FUTURE_ML_03.git


Install dependencies:
pip install -r requirements.txt


---

## ▶️ Run the Application
streamlit run app/app.py



---

## 🌐 Live Demo



---

## 📊 Example Output

- Candidate ranking based on score
- Extracted skills
- Missing required skills
- Clear explanation for each result

---

## 🧪 Technologies Used

- Python
- NLP (Natural Language Processing)
- TF-IDF (Scikit-learn)
- Streamlit
- Pandas / NumPy

---

## 💡 Future Improvements

- Advanced NLP models (BERT)
- Skill weighting system
- Visual dashboards (charts)
- Database integration
- API deployment

---

## Working datasets link

https://www.kaggle.com/datasets/snehaanbhawal/resume-dataset
https://www.kaggle.com/datasets/ravindrasinghrana/job-description-dataset
https://www.kaggle.com/datasets/PromptCloudHQ/us-jobs-on-monstercom

## 👩‍💻 Author

**Didia Voule-Frititi**

AI & Data Enthusiast  
Passionate about solving real-world problems using Machine Learning.

---

## ⭐ Why This Project Matters

This project demonstrates:

- Practical NLP skills
- Machine Learning for decision support
- Real-world application development
- End-to-end project delivery

It is directly applicable to HR Tech, recruitment platforms, and hiring automation systems.