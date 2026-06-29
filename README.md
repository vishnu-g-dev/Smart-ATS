# 🎓 Smart ATS Resume Analyzer

A secure, modern web application powered by Generative AI that helps job seekers optimize their resumes against specific job descriptions. Built using Python, Streamlit, and Google's advanced Gemini 2.5 Flash model.

🌐 **Live Demo:** [Insert your live Streamlit URL here!]

---

## 🚀 Features
* **AI-Powered Matching:** Evaluates the overall alignment between a resume (PDF) and a job description.
* **Keyword Gap Analysis:** Automatically extracts crucial keywords missing from the candidate's profile.
* **Actionable Feedback:** Provides a professional profile summary detailing clear steps for resume improvement.
* **Enterprise Security:** Keeps API credentials secure using system environment variables (`.env`).

---

## 🛠️ Tech Stack & Architecture

The application handles file parsing and AI inference through a modular local pipeline before deployment to cloud infrastructure:

* **Frontend UI:** Streamlit
* **AI Brain:** Google Gemini 2.5 Flash (via `google-genai` SDK)
* **PDF Extraction:** PyPDF2
* **Environment Management:** python-dotenv

---

## 📦 Installation & Local Setup

Want to run this robot friend on your own laptop? Follow these steps:

### 1. Clone the Repository
```bash
git clone [https://github.com/your-username/Smart-ATS.git](https://github.com/your-username/Smart-ATS.git)
cd Smart-ATS
