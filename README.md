# 🎓 Smart ATS Resume Analyzer

A secure, modern web application powered by Generative AI that helps job seekers optimize their resumes against specific job descriptions. Built using Python, Streamlit, and Google's advanced Gemini 2.5 Flash model.

🌐 **Live Link:** [https://smart-ats-resume-analyzer-genai.streamlit.app/]

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
git clone [https://github.com/vishnu-g-dev/Smart-ATS.git](https://github.com/vishnu-g-dev/Smart-ATS.git)
cd Smart-ATS
```

### 2. Install Superpowers (Dependencies)
Ensure you have Python installed, then run:
```bash
pip install -r requirements.txt
```

### 3. Setup Your Secret Vault (API Key)
Create a `.env` file in the root directory and securely add your Google AI Studio API key:
```text
GOOGLE_API_KEY="your_actual_gemini_api_key_here"
```

### 4. Ignite the Engine
Launch your local web server:
```bash
streamlit run app.py
```

---

## 💡 How It Works
1. **Upload:** Paste the target job description and drop in your resume in PDF format.
2. **Parsing:** The application opens the PDF layout and extracts its raw text data.
3. **AI Evaluation:** The prompt pipeline structures the data into an enterprise ATS simulation payload and submits it to the Gemini inference engine.
4. **Insight:** Get an instant percentage match score, critical keyword requirements, and optimization advice.

---

## 🔒 Security Note
This project adheres to professional security compliance standards. The private API key is entirely isolated using environment variable injection via `.env` and is strictly explicitly ignored by cloud setups through Streamlit Advanced Secrets management to prevent credential leaks.
---
*Designed and Developed by [Vishnu G](https://www.linkedin.com/in/vishnu-g-eee164) | Electrical and Electronics Engineering, NSS College of Engineering*
