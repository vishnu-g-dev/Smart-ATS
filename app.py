import streamlit as st
from google import genai
import PyPDF2 as pdf
import os
from dotenv import load_dotenv

# 1. Unlock the secret .env vault
load_dotenv()

# 2. Grab the secret key from the vault and save it in a variable
my_secret_key = os.getenv("GOOGLE_API_KEY")

# 3. Connect to Google using that secret key securely!
client = genai.Client(api_key=my_secret_key)

# Function to ask the AI a question
def get_ai_response(prompt):
    # We use the brand new, highly capable flash model
    response = client.models.generate_content(
        model='gemini-2.5-flash', 
        contents=prompt
    )
    return response.text

# Function to extract text from the uploaded PDF resume
def read_pdf(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        text += str(page.extract_text())
    return text

# The instructions we give to the AI robot
prompt_template = """
Act like a highly experienced Applicant Tracking System (ATS). 
Your task is to evaluate the student's resume based on the provided job description.
Think about what recruiters look for and provide a helpful, honest review.

Resume text: {resume_text}
Job Description: {job_description}

Please provide your answer in this exact format:
1. Job Match: [Give a percentage]
2. Missing Keywords: [List the important words from the job description missing in the resume]
3. Profile Summary: [Give brief feedback on how to improve]
"""

# Setting up the webpage title and description
st.title("🎓 Smart ATS Resume Analyzer")
st.write("Upload your resume to see how well it matches the job description!")

# Creating a text box for the job description
job_description = st.text_area("Paste the Job Description here:")

# Creating a button to upload the PDF
uploaded_file = st.file_uploader("Upload Your Resume (PDF)", type="pdf")

# Creating a submit button
submit = st.button("Analyze My Resume")

# What happens when we click submit?
if submit:
    if uploaded_file is not None and job_description:
        st.write("Analyzing... 🤖")
        
        # 1. Read the PDF
        resume_text = read_pdf(uploaded_file)
        
        # 2. Fill in the blanks in our prompt template
        final_prompt = prompt_template.format(resume_text=resume_text, job_description=job_description)
        
        # 3. Send it to the AI and get the result
        response = get_ai_response(final_prompt)
        
        # 4. Show the result on the screen
        st.subheader("Analysis Results:")
        st.write(response)
        
    else:
        st.error("Oops! Please make sure to provide both a job description and a resume.")