import streamlit as st 
from streamlit_extras.stylable_container import stylable_container
from pathlib import Path
from PIL import Image,ImageDraw
from services import services
from Projects import projects
from skills import skills
from Education import education
from Experiences import experiences
from html_codes import html_code_for_social2
from user_details import user


st.set_page_config(
    page_title="ARYA CHAKRABORTY - PORTFOLIO🤘",
    page_icon="🚀",
    layout="centered"
)

st.title("**:rainbow[HI, I'm Arya Chakraborty]**")

if __name__ == "__main__":
    user()                     ## Check -----> "user_detals.py"

    tab1,tab2,tab3,tab4,tab5 = st.tabs(['**:green[SERVICES]** 🙋‍♂️', '**:green[EXPERIENCES]** 📋','**:green[PROJECTS]** 🌐', '**:green[SKILLS]** 👨🏻‍🔧', '**:green[EDUCATION]** 🎓'])

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