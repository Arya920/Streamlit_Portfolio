import streamlit as st
from functions import layout


PAGE_TITLE = "Work Experiences | Arya"
PAGE_ICON = "🏛"
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON,layout="wide")
st.title("Professional Experiences")

# col1,col2 = st.columns(2)
# button_label = 'Description'
# with col1:

#     with st.expander('ISNARTECH PVT LTD.',):
#         isnartech_logo_url = "logos/Isnartech_logo.jpeg"
#         st.image(isnartech_logo_url, width=300)

#         st.markdown('Job Role : **:orange[AI DEVELOPER]**')
#         st.write('Duration : JAN 2024 - PRESENT')

#         #if st.button('Job descriptions',key='jobbutton1'):
#         st.markdown("""
                    
#                 ✅ To handle front-end back-end algorithm development, optimization and improvements.  
#                 ✅ Handle end to end development & deployment.  
#                 ✅ Maintain coordination.  
#                 ✅ Data preparation, handling.  
#                 ✅ Do research work about latest developments in AI, image processing, computer vision, deep learning.  
#                 ✅ Maintain database & API integration.  
#                 ✅ Inform to Company authority if you find something unusual or something not as per rules and regulations of Company.  
#                     """)
    

# with col2:
#     with st.expander('EXPOSYS DATA LABS'):
#         EDL_logo = "logos/EDL_logo.jpeg"
#         st.image(EDL_logo, width=200)

#         st.write('Job Role : **:orange[DATA SCIENCE INTERN]**')
#         st.write('Duration : AUG. 2023 - SEP. 2023')

#         #if st.button('Job descriptions',key='jobbutton2'):
#         st.markdown("""
                    
#                 ✅ Analyzed diabetes prediction using 9 Machine Learning methods and proposed a deep learning model.  
#                 ✅ Created a web app for personalized health tracking and real-time risk assessment.  
#                 ✅ Proposed model outperformed existing models by attaining a 10 percent higher accuracy in diabetes prediction.  
#                 ✅ Constructed projects in a well-documented manner, ensuring clarity and ease of understanding for future reference and collaboration.   
#                     """)



layout.txt('''### Lead AI Developer / Data Scientist''','')

col1, col2 = st.columns([3,2])
with col1:
    st.markdown('''
    **Gurgaon, Haryana**
    - Training design & implement ML Algorithms.
    - Training on Python, SQL...
    - Data analysis, machine learning, scraping...
    - End to End LLM RAG Pipeline implementation
    - Build and deployed a Complete Enterprise Resource Planing system (ERP) for a Private School
    - Created a real time air quality predictor application using machine learning algorithms like XGBoost, Random Forest and ANN.
    - Public Works : [Air Quality Prediction ](https://github.com/Arya920/AirQualityPredictionFlask), [Natural Language to SQL Code Conversion](https://github.com/Arya920/Natural_Language_To_SQL_Queries)
    ''')
with col2:
    layout.txt('<h5 class=years>Jan 2024 - July 2024</h5>','')
    st.image('logos/isnartech_logo.jpeg')

st.markdown('---')

###### Rise Up #######
layout.txt('''### Data Science Intern / AI Intern''','')

col1, col2 = st.columns([3,2])
with col1:
    st.markdown('''
    **Remote**
    - Implemented more than 10 ML models for Diabetes Disease prediction.
    - Created a state of the art streamlit web app for impleenting this project
    - Created a proper explained 
    - Reference : (Diabetes Disease Prediction)[https://github.com/Arya920/Desease-prediction]
    ''')
with col2:
    layout.txt("<h5 class=years> Aug 2023 - Oct 2023</h5>","")
    st.image('logos/EDL_logo.jpeg')