import streamlit as st
from functions import layout
import streamlit.components.v1 as components
import plotly.graph_objects as go

PAGE_TITLE = "My Skills | Arya"
PAGE_ICON = "🏛"
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON,layout="wide")

# st.title("SKILLS")
# col1,col2,col3 = st.columns(3)

# with col1:
#     with st.expander('Mathematical Skills :1234:'):
#         st.markdown('''
#                     ✅ **:gray[Statistical Analysis]**  
#                     ✅ **:gray[Multivariate Analysis]**  
#                     ✅ **:gray[Time Series Analysis]**  
#                     ''')
        
#     with st.expander('Analytical Skills 📈'):
#         st.markdown("""
#                     ✅ **:gray[Pandas]**  
#                     ✅ **:gray[Seaborn]**  
#                     ✅ **:gray[NumPy]**  
#                     ✅ **:gray[MatplotLib]**  
#                     ✅ **:gray[Plotly]**  

#                     """)
    
# with col2:
#     with st.expander('B.I. Tools'):
#         st.markdown("""
#                     ✅ **:gray[Excel]**  
#                     ✅ **:gray[Power BI]**  
                
#                     """)
    
#     with st.expander('Programming Languages 🐍'):
#         st.markdown(""" 
#                     ✅ **:gray[Python]**  
#                     ✅ **:gray[R]**  
#                     ✅ **:gray[SQL]**        
#                     """)
        
#     with st.expander('Web Frameworks 📱'):
#         st.markdown("""                    
#                     ✅ **:gray[Streamlit]**  
#                     ✅ **:gray[Flask]**  
#                     """)
    
# with col3: 
#     with st.expander('Machine Learning & Deep Learning 🧑‍💻🤖'):
#         st.markdown("""
#                     ✅ **:gray[Keras]**  
#                     ✅ **:gray[Tensorflow]**  
#                     ✅ **:gray[Natural Language Processing (NLP)]**  
#                     ✅ **:gray[Computer Vision]**  
#                     ✅ **:gray[OpenCV]**  
#                     ✅ **:gray[Artificial Neural Network]**  
#                     ✅ **:gray[Recurrent Neural Network]**  
#                     ✅ **:gray[Convolutional Neural Network]**  
#                     """)


col1, col2 = st.columns([5,3])
with col1:
    st.markdown('''
    # Hard Skills
    ''')
    st.divider()
    layout.txt3('**Mathematical Skills** :1234:', ' **:gray[Statistical Analysis | Multivariate Analysis | Time Series ]**')
    layout.txt3('**Programming** 🐍', '**:gray[Python | R | HTML | CSS]**')
    layout.txt3('**Data processing/wrangling**', '**:gray[SQL | pandas | numpy]**')
    layout.txt3('**Database Management System 🫙**', '**:gray[MySQL | SQLite]**')
    layout.txt3('**Scraping** 📈', '**:gray[BeautifulSoup | Scrapy]**')
    layout.txt3('**Data visualization** 📈', '**:gray[matplotlib | plotly |  seaborn ]**')
    layout.txt3('**Business Intelligence** ', '**:gray[ Power BI |  Excel |  Tableau ]**')
    layout.txt3('**Machine Learning** 🧑‍💻', '**:gray[ scikit-learn]**')
    layout.txt3('**Deep Learning** 🤖', '**:gray[ tensorflow-keras |  PyTorch |  Neural Networks |  Natural Language Processing |  Computer Vision |  Open CV]**')
    layout.txt3('**Large Language Model** 🤖', '**:gray[ Transformers |  P.E.F.T. |  L.O.R.A |  Quantization]**')
    layout.txt3('**Model deployment** 📱', '**:gray[ Streamlit |  Flask |  Gradio]**')


with col2:
    ###### Skills ######
    st.markdown('''
    # Soft Skills
    ''')
    st.divider()
    layout.txt3('**Speaking**', '**:gray[At ease in speaking | patient | good communicator | able to pass on knowledge and popularize.]**')
    layout.txt3('**Emotional intelligence**', '**:gray[Ease of understanding others and adapting to my audience]**')
    layout.txt3('**Good executive**', '**:gray[Adaptable | multidisciplinary | resilient]**')



programming_skills = {
    'Python': 5,
    'SQL': 4,
    'R': 3,
    'Streamlit': 5,
    'Flask': 5
}

ai_skills = {
    'Deep Learning': 5,
    'Generative AI': 3,
    'Machine Learning': 5,
    'NLP': 5,
    'Computer Vision': 3
}

# Create radar charts
fig1 = go.Figure()
fig1.add_trace(go.Scatterpolar(
    r=list(programming_skills.values()),
    theta=list(programming_skills.keys()),
    fill='toself',
    name='Programming Skills'
))
fig1.update_layout(
    polar=dict(
        bgcolor="#407887",
        radialaxis=dict(
            visible=True,
            range=[0, 5],
            tickfont=dict(size=15, color="white", family="Arial", weight="bold")
        ),
        angularaxis=dict(
            tickfont=dict(size=12, color="black", family="Arial", weight="bold")
        )
    ),
    showlegend=False,
    title={
        'text': "Proficiency in Programming Languages & Frameworks",
        'font': {'size': 15, 'color': 'black'}
    }
)

fig2 = go.Figure()
fig2.add_trace(go.Scatterpolar(
    r=list(ai_skills.values()),
    theta=list(ai_skills.keys()),
    fill='toself',
    name='AI/ML & DL Skills'
))
fig2.update_layout(
    polar=dict(
        bgcolor="#407887",
        radialaxis=dict(
            visible=True,
            range=[0, 5],
            tickfont=dict(size=15, color="white", family="Arial", weight="bold")
        ),
        angularaxis=dict(
            tickfont=dict(size=12, color="black", family="Arial", weight="bold")
        )
    ),
    showlegend=False,
    title={
        'text': "Proficiency in Machine Learning & Artificial Intelligence",
        'font': {'size': 15, 'color': 'black'}
    }
)

st.divider()
col3, col4, col5, col6 = st.columns([0.01, 3.1, 3.5, 0.01])
with col4:
    st.plotly_chart(fig1)
with col5:
    st.plotly_chart(fig2)

