import streamlit as st
from services import services, skills, experiences, education, projects
from user_details import user
from PIL import Image
import os
import tempfile
from test_resume import clean_extracted_text

# Add this import for the chatbot functionality
from chatbot import get_response

page_icon = Image.open('logos/favicon2.ico')
st.set_page_config(
    page_title="Arya Chakraborty - PORTFOLIO🤘",
    page_icon=page_icon,
    layout="centered"
)

# with open("./styles/style.css") as f:
#     st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
st.title("**HI, I'm Arya Chakraborty**")

if __name__ == "__main__":
    user()  ## Check -----> "user_detals.py"
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(['**:orange[SERVICES]** 🙋‍♂️', '**:orange[EXPERIENCES]** 📋',
                                                  '**:orange[PROJECTS]** 🌐', '**:orange[SKILLS]** 👨🏻‍🔧', 
                                                  '**:orange[EDUCATION]** 🎓', '**:orange[CHECK JOB COMPATIBILITY]** ❄️'])
    with tab1:
        services()
    with tab2:
        experiences()
    with tab3:
        projects()    
    with tab4:
        skills()
    with tab5:
        education()
    with tab6:
        jd_type = st.radio("How you want to upload your JoB Description",
                            ["***Copy and Paste Your Text***","***Upload PDF***"],
                            index=None,)
        if jd_type == "***Copy and Paste Your Text***":
            st.markdown(
                """
                <style>
                .stTextArea textarea {
                    border: 1px solid  #ee8228 ;  /* Adjust the border color as needed */
                    border-radius: 5px;        /* Optional: Adjust the border radius */
                    background-color: #152238; /* Ensure background color matches your theme */
                    color: #FFFFFF;            /* Text color */
                }
                </style>
                """,
                unsafe_allow_html=True
            )
            jd = st.text_area("Job Description")
        elif jd_type == "***Upload PDF***":
            jd_pdf = st.file_uploader("Upload your PDF file",type='pdf')
            if jd_pdf is not None:
                with tempfile.TemporaryDirectory() as tmpdirname:
                    jd_file_path = os.path.join(tmpdirname, jd_pdf.name)
                    my_resume_path = "documents/Resume_DS_latest.pdf"

                    with open(jd_file_path, "wb") as file:
                        file.write(jd_pdf.getbuffer())
                    st.popover(f"File saved to {jd_file_path}")
                    
                    jd_extracted_text = clean_extracted_text(jd_file_path)
                    resume_extracted_text = clean_extracted_text(my_resume_path)
    