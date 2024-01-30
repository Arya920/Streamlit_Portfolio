import streamlit as st 
from services import services,skills,experiences,education,projects
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