import streamlit as st 





##------------------------------------------------------------SERVICES--------------------------------------------------------------------------------------------------------------------------------------
def services():
    col3,col4 = st.columns(2)

    with col3:
        stat_logo_url = "logos/stat.svg"
        st.image(stat_logo_url, width=40)
        st.subheader('**:green[Statistician]**')
        st.markdown("""Master the art of data interpretation and analysis, providing statistical insights to guide critical business decisions.
                    Employ rigorous methodologies and mathematical models to uncover hidden patterns and trends within your data.""")

        st.write("")

        PBI_logo_url = "logos/language.svg"
        st.image(PBI_logo_url, width=40)
        st.subheader('**:green[NLP Engineer]**')
        st.markdown("""Unlock the potential of natural language processing to extract meaningful information from textual data.
                    Develop innovative solutions for text analysis, sentiment analysis, and language understanding, empowering your applications with human-like comprehension capabilities.""")

    with col4:
        AI_logo_url = "logos/AI.svg"
        st.image(AI_logo_url, width=45)
        st.subheader('**:green[AI Developer]**')
        st.markdown("""TCraft cutting-edge artificial intelligence solutions tailored to your specific needs,
                    From predictive analytics to natural language processing, harness the power of AI to revolutionize your business operations""")

        st.write("")
        st.write("")
    
        sql_logo_url = "logos/sql.svg"
        st.image(sql_logo_url, width=45)
        st.subheader('**:green[SQL Developer]**')
        st.markdown("""Design robust and secure databases to store and retrieve data efficiently. Leverage expert SQL coding techniques to streamline
                    data management processes and enhance data integrity, facilitating seamless integration with your applications and systems.""")


##-----------------------------------------------------------------SKILLS--------------------------------------------------------------------------------------------------------


def skills():

    col1,col2,col3 = st.columns(3)

    with col1:
        with st.expander('Mathematical Skills :1234:'):
            st.markdown('''
                        ✅ **:gray[Statistical Analysis]**  
                        ✅ **:gray[Multivariate Analysis]**  
                        ✅ **:gray[Time Series Analysis]**  
                        ''')
            
        with st.expander('Analytical Skills 📈'):
            st.markdown("""
                        ✅ **:gray[Pandas]**  
                        ✅ **:gray[Seaborn]**  
                        ✅ **:gray[NumPy]**  
                        ✅ **:gray[MatplotLib]**  
                        ✅ **:gray[Plotly]**  

                        """)
        
    with col2:
        with st.expander('B.I. Tools'):
            st.markdown("""
                        ✅ **:gray[Excel]**  
                        ✅ **:gray[Power BI]**  
                 
                        """)
        
        with st.expander('Programming Languages 🐍'):
            st.markdown(""" 
                        ✅ **:gray[Python]**  
                        ✅ **:gray[R]**  
                        ✅ **:gray[SQL]**        
                        """)
            
        with st.expander('Web Dev 📱'):
            st.markdown("""                    
                        ✅ **:gray[Streamlit]**  
                        ✅ **:gray[Flask]**  
                        """)
        
    with col3: 
        with st.expander('Machine Learning & Deep Learning 🧑‍💻🤖'):
            st.markdown("""
                        ✅ **:gray[Keras]**  
                        ✅ **:gray[Tensorflow]**  
                        ✅ **:gray[Natural Language Processing (NLP)]**  
                        ✅ **:gray[Computer Vision]**  
                        ✅ **:gray[OpenCV]**  
                        ✅ **:gray[Artificial Neural Network]**  
                        ✅ **:gray[Recurrent Neural Network]**  
                        ✅ **:gray[Convolutional Neural Network]**  
                        """)
        



## ---------------------------------------------------------------EXPERIENCE-----------------------------------------------------------------------------------------------------

def experiences():
    col1,col2 = st.columns(2)
    button_label = 'Description'
    with col1:

        with st.expander('ISNARTECH PVT LTD.'):
            isnartech_logo_url = "logos/Isnartech_logo.jpeg"
            st.image(isnartech_logo_url, width=150)

            st.write('Job Role : AI DEVELOPER')
            st.write('Duration : JAN 2024 - PRESENT')

            if st.button('Job descriptions',key='jobbutton1'):
                st.markdown("""
                            
                        ✅ To handle front-end back-end algorithm development, optimization and improvements.  
                        ✅ Handle end to end development & deployment.  
                        ✅ Maintain coordination.  
                        ✅ Data preparation, handling.  
                        ✅ Do research work about latest developments in AI, image processing, computer vision, deep learning.  
                        ✅ Maintain database & API integration.  
                        ✅ Inform to Company authority if you find something unusual or something not as per rules and regulations of Company.  
                            """)
       

    with col2:
        with st.expander('EXPOSYS DATA LABS'):
            EDL_logo = "logos/EDL_logo.jpeg"
            st.image(EDL_logo, width=95)

            st.write('Job Role : DATA SCIENCE INTERN')
            st.write('Duration : AUG. 2023 - SEP. 2023')

            if st.button('Job descriptions',key='jobbutton2'):
                st.markdown("""
                            
                        ✅ Analyzed diabetes prediction using 9 Machine Learning methods and proposed a deep learning model.  
                        ✅ Created a web app for personalized health tracking and real-time risk assessment.  
                        ✅ Proposed model outperformed existing models by attaining a 10 percent higher accuracy in diabetes prediction.  
                        ✅ Constructed projects in a well-documented manner, ensuring clarity and ease of understanding for future reference and collaboration.   
                            """)




## ----------------------------------------------EDUCATION------------------------------------------------------------------------------------------------------------------
                
def education():
    col1,col2 = st.columns(2)
    with col1:
        st.subheader("**:green[Vellore Institute of Technology, Amaravati]**")
        st.write('MSc Data Science')
        st.markdown(""" 
                -  CGPA: 8.78
                - Subjects: Python, Data structures, Machine learning, Deep learning, Information retrieval techniques.
                  """)
        
        with col2:
            st.write('Expected July 2024')



    col3, col4 = st.columns(2)
    with col3:
        st.subheader("**:green[Kalyani Mahavidyalaya, Nadia]**")
        st.write('BSc Statistics')
        st.markdown(""" 
                -  CGPA: 8.26
                - Subjects: Hypothesis testing, Probability theory, Time series analysis, Regression analysis.
                  """)
    with col4:
        st.write("June 2022")





##-------------------------------------------------------PROJECTS-----------------------------------------------------------------------------------------------------
        
def projects():
    button_label = 'Small description'
    col5,col6 = st.columns(2)

    with col5:
        st.subheader('**:green[NLP-Powered Document Summarizer ]**')
        summarizer_url = "Images/summarizer.png"
        st.image(summarizer_url, use_column_width=True)
        st.link_button("Repository", "https://github.com/Arya920/Document_Summarizer")
        if st.button(button_label, key='button1'):
            st.markdown("""Unlock the power of Natural Language Processing (NLP) with our Automatic Document Summarization Model (ADSM), designed to effortlessly
                    distill the essence of lengthy articles and research papers. Tired of drowning in information overload? Let our ADSM be your guide,
                    providing crisp and coherent summaries, saving you valuable time and effort. """)
        


        st.subheader('**:green[Gender Classification using CNN & OpenCV ]**')
        gender_url = "Images/gender.jpg"
        st.image(gender_url, use_column_width=True)
        st.link_button("Repository", "https://github.com/Arya920/Gender-Detection-Project")
        
        if st.button(button_label,key='button2'):
            st.markdown("""This project focuses on classifying the gender of individuals from facial images. It employs a combination of techniques including transfer learning,
                    fine-tuning, and custom CNN models. """)
        

    with col6:
        st.subheader("**:green[Career Buddy - Career Guidance AI Chatbot]**")
        chatbot_url = "Images/chatbot.png"
        st.image(chatbot_url, use_column_width=True)
        st.link_button("Repository", "https://github.com/Arya920/Career-Guidance-AI-bot")
        if st.button(button_label, key='button3'):
            st.markdown("""This project presents the development of a career counseling bot that utilizes Quora data to provide users with valuable insights
                    and recommendations for their career choices """)
            
        st.subheader('**:green[Web Application for Stock Price Analysis & Prediction ]**')
        sp_url = "Images/sp2.jpg"
        st.image(sp_url, width= 406)
        st.link_button("Repository", "https://github.com/Arya920/StockPriceForecasting")
        if st.button(button_label, key='button4'):
            st.markdown("""The application allows users to analyze historical stock data, perform technical & statistical analysis, and even predict future 
                        stock prices using deep learning models.""")