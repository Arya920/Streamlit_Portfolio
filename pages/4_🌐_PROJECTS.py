import streamlit as st
import time

PAGE_TITLE = "Projects | Arya"
PAGE_ICON = "🏛"
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON,layout="wide")

st.title('My Projects')

def project_descriptions(index):
    project_description_list = ["""Unlock the power of Natural Language Processing (NLP) with our Automatic Document Summarization Model (ADSM), designed to effortlessly
                                    distill the essence of lengthy articles and research papers. Tired of drowning in information overload? Let our ADSM be your guide,
                                    providing crisp and coherent summaries, saving you valuable time and effort.
                                """,
                                
                                """This project focuses on classifying the gender of individuals from facial images. It employs a combination of techniques including transfer learning,
                                    fine-tuning, and custom CNN models.
                                """,
                                
                                """This project presents the development of a career counseling bot that utilizes Quora data to provide users with valuable insights
                                    and recommendations for their career choices.
                                """,
                                
                                """The application allows users to analyze historical stock data, perform technical & statistical analysis, and even predict future 
                                    stock prices using deep learning models.
                                """]        

    for word in project_description_list[index].split(" "):
        yield word + " "
        time.sleep(0.05)
      

button_label = 'Small description'
col5,col6 = st.columns(2)

with col5:
    st.subheader('**:green[NLP-Powered Document Summarizer ]**')
    summarizer_url = "Images/summarizer.png"
    st.image(summarizer_url, use_column_width=True)
    st.link_button("Repository", "https://github.com/Arya920/Document_Summarizer")
    if st.button(button_label, key='button1'):
        # st.markdown("""Unlock the power of Natural Language Processing (NLP) with our Automatic Document Summarization Model (ADSM), designed to effortlessly
        #         distill the essence of lengthy articles and research papers. Tired of drowning in information overload? Let our ADSM be your guide,
        #         providing crisp and coherent summaries, saving you valuable time and effort. """)
        st.write_stream(project_descriptions(0))


    st.subheader('**:green[Gender Classification using CNN & OpenCV ]**')
    gender_url = "Images/gender.jpg"
    st.image(gender_url, use_column_width=True)
    st.link_button("Repository", "https://github.com/Arya920/Gender-Detection-Project")
    
    if st.button(button_label,key='button2'):
        # st.markdown("""This project focuses on classifying the gender of individuals from facial images. It employs a combination of techniques including transfer learning,
        #         fine-tuning, and custom CNN models. """)
        st.write_stream(project_descriptions(1))
    

with col6:
    st.subheader("**:green[Career Buddy - Career Guidance AI Chatbot]**")
    chatbot_url = "Images/chatbot.png"
    st.image(chatbot_url, use_column_width=True)
    st.link_button("Repository", "https://github.com/Arya920/Career-Guidance-AI-bot")
    if st.button(button_label, key='button3'):
        # st.markdown("""This project presents the development of a career counseling bot that utilizes Quora data to provide users with valuable insights
        #         and recommendations for their career choices """)
        st.write_stream(project_descriptions(2))
        
    st.subheader('**:green[Web Application for Stock Price Analysis & Prediction ]**')
    sp_url = "Images/sp2.jpg"
    st.image(sp_url, width= 406)
    st.link_button("Repository", "https://github.com/Arya920/StockPriceForecasting")
    if st.button(button_label, key='button4'):
        # st.markdown("""The application allows users to analyze historical stock data, perform technical & statistical analysis, and even predict future 
        #             stock prices using deep learning models.""")
        st.write_stream(project_descriptions(3))