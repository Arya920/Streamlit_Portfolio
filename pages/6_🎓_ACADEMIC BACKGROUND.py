import streamlit as st



VIT_DESCRIPTION = """My Academic Journey was always influenced by my love for maths and coding Starting from my Data science degree down to my latest experience"""
vit_logo_url = "Images/Other/vit.png"
cols = st.columns(2, gap='small')

with cols[0]:
    st.markdown("""
            ### VIT AP  **:orange[2022 - 2024]**          
                """)
    st.image(vit_logo_url)

with cols[1]:
    #st.title("VIT-AP")
    st.write(VIT_DESCRIPTION)
    #st.write('MSc Data Science')
    st.markdown(""" 
            - Degree: **:orange[MSc Data Science]**
            -  CGPA: **:orange[8.9]**
            - Subjects: **:orange[Python, Data structures, Machine learning, Deep learning, Information retrieval techniques.]**
                """)

st.divider()

KU_DESCRIPTION = """Here I started my journey of Statistics and got immense knowledge of theoretrical aspect of the data science and my love grew towards this subject"""
ku_logo_url = "Images/Other/KU.jpg"
cols = st.columns(2, gap='small')

with cols[0]:
    st.markdown("""
            ### Kalyani University **:orange[2019 - 2022]**              
                """)
    st.image(ku_logo_url)

with cols[1]:
    #st.title("VIT-AP")
    st.write(KU_DESCRIPTION)
    #st.write('B.Sc. Statistics')
    st.markdown(""" 
            - Degree: **:orange[B.Sc. Statistics]**
            -  CGPA: **:orange[8.26]**
            - Subjects: **:orange[Hypothesis testing, Probability theory, Time series analysis, Regression analysis.]**
                """)


st.divider()

CDMHS_DESCRIPTION = """Here I spent 12 years of my school life. Learned, faught laughed and most of all here I built the mentality to never stop the urge of learning new things and never to stop asking questions."""
ku_logo_url = "Images/Other/CDMHS.jpg"
cols = st.columns(2, gap='small')

with cols[0]:
    st.markdown("""
            ### Chinsurah Deshbandhu Memorial High School **:orange[2007 - 2019]**              
                """)
    st.image(ku_logo_url)

with cols[1]:
    #st.title("VIT-AP")
    st.write(KU_DESCRIPTION)
    #st.write('B.Sc. Statistics')
    st.markdown(""" 
            - Main Combination: **:orange[P.C.M.S]**
            -  Percentage: [ Class 10 : **:orange[90%]** ] & [ Class 12 : **:orange[81%]** ]
            - Subjects: **:orange[Physics, Chemistry, Math, Statistics (11 & 12), Bengali, English and many more.]**
                """)