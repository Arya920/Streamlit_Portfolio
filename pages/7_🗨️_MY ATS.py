import streamlit as st
import re
import json

from functions import DonutChart
st.markdown(" # My Customized ATS")

st.warning("""This System only works on local system as it uses LLAMA CPP which is not designed to be deployed so for that reason to use this ATS you have to fork this repository and follow the below process. """)

st.warning("""To run This Web based ATS Checker I have used an open sourced Information Extraction model called **:green[`NuMind/NuExtract`]**. 
           Please Download the model **:green[`NuExtract-Q4_K_L.gguf`]** at first and keep that model in the **:green[`models`]** folder. Use the following link 👇""")
st.link_button("Model Download Link", "https://huggingface.co/bartowski/NuExtract-GGUF/tree/main")

def word_count(text):
    text = re.sub(r'\n', '',text)
    words = text.split()
    return len(words)

my_resume_key_points = {
    "Bio data": {
        "Name": "ARYA CHAKRABORTY",
        "Phone Number": "+91 6290686301",
        "Email id": "aryachakraborty.official@gmail.com"
    },
    "Education": {
        "UG College": "Kalyani Mahavidyalaya",
        "UG CGPA": "8.26",
        "PG College": "Vellore Institute of Technology",
        "PG CGPA": "8.81"
    },
    "Skills": {
        "Skills": [
            "Statistical analysis",
            "Time Series analysis",
            "Probability",
            "Python",
            "R",
            "SQL",
            "Power Bi",
            "Excel",
            "Transformers",
            "Streamlit",
            "Version control systems",
            "GitHub",
            "AWS Sagemaker",
            "Natural Language Processing NLP",
            "Computer Vision",
            "Large Language Models",
            "Gen AI",
            "Machine Learning",
            "Deep Learning",
            "Artificial Neural Network",
            "Recurrent Neural Network",
            "Convolutional Neural Network"
        ]
    }
}

def skill_match_analysis(resume, job_description):
    resume_skills = set(skill.lower() for skill in resume["Skills"]["Skills"])
    jd_skills = set(skill.lower() for skills in job_description.values() for skill in skills)
    
    matched_skills = resume_skills.intersection(jd_skills)
    missing_skills = jd_skills - resume_skills
    
    match_percentage = (len(matched_skills) / len(jd_skills)) * 100
    
    return matched_skills, missing_skills, match_percentage




st.markdown(
    """
    <style>
    .stTextArea textarea {
        border: 1px solid  #ee8228 ;  /* Adjust the border color as needed */
        border-radius: 5px;        /* Optional: Adjust the border radius */
        background-color: #407887; /* Ensure background color matches your theme */
        color: #FFFFFF;            /* Text color */
    }
    </style>
    """,
    unsafe_allow_html=True
)
jd = st.text_area("Copy and Paste yor Job Description here")
word_count_text = f"Word count: {word_count(jd)} / 512"
st.caption(word_count_text)
submit_button = st.button("Submit")


try:

    from Information_Extraction import extract_information

    if 'jd_information' not in st.session_state:
        st.session_state.jd_information = {}

    if 'percentage' not in st.session_state:
        st.session_state.percentage = ''

    if submit_button:
        if jd !="":
            jd = re.sub(r'\n', '',jd)
            if word_count(jd) <= 512:
                #global jd_information
                jd_information = extract_information( jd, example=["","",""])

                print('jd👇',jd_information)
                
                jd_information = json.loads(jd_information)
                st.session_state.jd_information = jd_information


                matched, missing, percentage = skill_match_analysis(my_resume_key_points, jd_information)

                st.session_state.percentage = round(percentage, 2)
                #st.write("Programming Skills👉",jd_information['Programming Languages'])
                #st.write("Technical Skills👉",jd_information['Technical Skills'])
                #st.write("Soft Skills👉",jd_information['Soft Skills'])
                
            else:
                st.warning("Word count exceeds the limit of 670 words. Please shorten your input.")

        col1, col2 = st.columns([3,2])
        with col1:
            
            DonutChart.doughnut_plot(float(st.session_state.percentage))
        with col2:
            if st.session_state.jd_information:
                if 'Programming Languages' in st.session_state.jd_information:
                    st.write("Programming Skills👉", st.session_state.jd_information['Programming Languages'])
                else:
                    st.write("Programming Skills: Not specified in the job description")

                if 'Technical Skills' in st.session_state.jd_information:
                    st.write("Technical Skills👉", st.session_state.jd_information['Technical Skills'])
                else:
                    st.write("Technical Skills: Not specified in the job description")
            else:
                st.write("Please submit a job description to see the required skills.")
    
except Exception as e:
    st.warning('This is still under development. If you know how to deploy Llama CPP on cloud please let me know at my mail id: aryachakraborty.official@gmail.com')
