import streamlit as st
import glob
import os 

PAGE_TITLE = "Projects | Arya"
PAGE_ICON = "🏛"
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON,layout="wide")


with st.sidebar:
    #st.subheader('**Project lists**')
    projects = st.selectbox('**Lists of Projects**', (
                                                'Food Calorie and Weight Estimation for school E.R.P system',
                                                'Gender Classification using CNN & OpenCV',
                                                'Career Buddy - Career Guidance AI Chatbot',
                                                'Web Application for Stock Price Analysis & Prediction',
                                                'NLP-Powered Document Summarizer',
                                                )
                                                )

if projects == 'Career Buddy - Career Guidance AI Chatbot':
    chatbot_url = "Images/Project Images/Chatbot/chatbot.png"
    col1,col2,col3 = st.columns([0.5,2,0.1])
    with col2:
        st.subheader(f'**:green[{projects}]**')
    col4,col5,col6 = st.columns([1,2,1])
    
    with col5:
        st.image(chatbot_url,  width=450)
        st.link_button("Repository", "https://github.com/Arya920/Career-Guidance-AI-bot")
    with open("Images/Project Images/Chatbot/chatbot.md",'r') as f:
        st.markdown(f.read(),unsafe_allow_html=True)
    with st.popover('Give Feedback'):
        user_name = st.text_input('Name')
        user_mail = st.text_input('Gmail')
        user_msg = st.text_area('Your Feedback')
        submitted = st.button('Submit')
    if submitted:
        if user_name and user_mail and user_msg:
            st.toast('Feedback Received ✅')

#==================================================================== Food calorie Project=================================

if projects == 'Food Calorie and Weight Estimation for school E.R.P system':
    foodcalorie_url = "Images/Project Images/FoodCalorie/logo.jpg"
    foodcalorie_pipeline = "Images/Project Images/FoodCalorie/FOOD-CALORIE-PIPELINE.png"
    foodimage1 = "Images/Project Images/FoodCalorie/FoodImage1.jpg"
    foodimage2 = "Images/Project Images/FoodCalorie/FoodImage2.jpg"
    foodimage3 = "Images/Project Images/FoodCalorie/FoodImage3.jpeg"
    foodimage4 = "Images/Project Images/FoodCalorie/FoodImage4.jpeg"
    foodimage_loss_curve = "Images/Project Images/FoodCalorie/results.png"
    foodimage_cm = "Images/Project Images/FoodCalorie/confusion_matrix.png"
    col1,col2,col3 = st.columns([0.5,2,0.1])
    with col2:
        st.subheader(f'**:green[{projects}]**')
    col4,col5,col6 = st.columns([1,2,1])
    
    with col5:
        st.image(foodcalorie_url,  width=450)
        repo = st.button("Repository")
        if repo:
            st.toast('Sorry I have not uploaded the code yet')

    with open("Images/Project Images/FoodCalorie/foodcalorie1.md",'r') as a:
        st.markdown(a.read(),unsafe_allow_html=True)
    
    col7,col8,col9 = st.columns([1,2,1])
    with col8:
        st.image(foodcalorie_pipeline,width=500)
    
    with open("Images/Project Images/FoodCalorie/foodcalorie2.md",'r') as b:
        st.markdown(b.read(),unsafe_allow_html=True)

    st.markdown("""
        ### Example Images      
     """)

    col10,col11,col12,col13 = st.columns([1,2,2,1])
    with col11:
        st.image(foodimage1,width=200)
        st.image(foodimage3,width=200)
    with col12:
        st.image(foodimage2,width=160)
        st.image(foodimage4,width=170)
    st.markdown("""
        ### Loss Curve & Confusion Matrix of YOLO Model
    """)

    col7,col8,col9 = st.columns([1,2,1])
    with col8:
        st.image(foodimage_loss_curve,width=500)
        st.image(foodimage_cm,width=500)

    st.markdown(""" 
                ### Conclusion
                In this endeavor, we created an extensive system to estimate the calories and weight of food items
                    from images and videos. Utilizing the advanced features of the YOLO V8 model for object detection
                    and classification, we precisely identified and localized food items within the images. The fine-tuned
                    YOLO V8 model, trained on a varied dataset encompassing 15 different food categories, showed strong
                    performance in the classification of food items.
                    The detected food items’ subsequent weight estimation was carried out using a K-Nearest Neighbors
                    (KNN) model. This model predicted the weight based on the area of the food items, generating precise
                    weight estimates that were subsequently used to compute the total calorie content. The combination
                    of these models allowed us to obtain dependable and accurate assessments of food calorie and weight,
                    fulfilling an essential requirement in dietary evaluation and nutrition management.
                    The findings of this project highlight the value of integrating advanced machine learning models with
                    well-organized datasets to tackle intricate real-world challenges. Future research could investigate broad-
                    ening the range of food categories, enhancing model precision, and incorporating real-time processing
                    functionalities to improve the system’s usability and relevance. In sum, this project marks a critical
                    advancement towards automated dietary assessment tools that can help foster healthier eating behaviors
                    and greater nutritional awareness. """)
    with st.popover('Give Feedback'):
        user_name = st.text_input('Name')
        user_mail = st.text_input('Gmail')
        user_msg = st.text_area('Your Feedback')
        submitted = st.button('Submit')
    if submitted:
        if user_name and user_mail and user_msg:
            st.toast('Feedback Received ✅')

# ==============================================================================Gender Classification Project==========================
elif projects == 'Gender Classification using CNN & OpenCV':
    gender_classification_url = "Images/Project Images/GenderClassification/gender.jpg"
    col1,col2,col3 = st.columns([0.5,2,0.1])
    with col2:
        st.subheader(f'**:green[{projects}]**')
    col4,col5,col6 = st.columns([1,2,1])
    
    with col5:
        st.image(gender_classification_url,  width=450)
        st.link_button("Repository", "https://github.com/Arya920/Gender-Detection-Project")
    with open("Images/Project Images/GenderClassification/genderclassification.md",'r') as c:
        st.markdown(c.read(),unsafe_allow_html=True)
    with st.popover('Give Feedback'):
        user_name = st.text_input('Name')
        user_mail = st.text_input('Gmail')
        user_msg = st.text_area('Your Feedback')
        submitted = st.button('Submit')
    if submitted:
        if user_name and user_mail and user_msg:
            st.toast('Feedback Received ✅')


elif projects == 'NLP-Powered Document Summarizer':
    st.warning('Will Upload soon')

elif projects == 'Web Application for Stock Price Analysis & Prediction':
    st.warning('Will Upload soon')

















# st.title('My Projects')

# def project_descriptions(index):
#     project_description_list = ["""Unlock the power of Natural Language Processing (NLP) with our Automatic Document Summarization Model (ADSM), designed to effortlessly
#                                     distill the essence of lengthy articles and research papers. Tired of drowning in information overload? Let our ADSM be your guide,
#                                     providing crisp and coherent summaries, saving you valuable time and effort.
#                                 """,
                                
#                                 """This project focuses on classifying the gender of individuals from facial images. It employs a combination of techniques including transfer learning,
#                                     fine-tuning, and custom CNN models.
#                                 """,
                                
#                                 """This project presents the development of a career counseling bot that utilizes Quora data to provide users with valuable insights
#                                     and recommendations for their career choices.
#                                 """,
                                
#                                 """The application allows users to analyze historical stock data, perform technical & statistical analysis, and even predict future 
#                                     stock prices using deep learning models.
#                                 """]        

#     for word in project_description_list[index].split(" "):
#         yield word + " "
#         time.sleep(0.05)
      

# button_label = 'Small description'
# col5,col6 = st.columns(2)

# with col5:
#     st.subheader('**:green[NLP-Powered Document Summarizer ]**')
#     summarizer_url = "Images/summarizer.png"
#     st.image(summarizer_url, use_column_width=True)
#     st.link_button("Repository", "https://github.com/Arya920/Document_Summarizer")
#     if st.button(button_label, key='button1'):
#         # st.markdown("""Unlock the power of Natural Language Processing (NLP) with our Automatic Document Summarization Model (ADSM), designed to effortlessly
#         #         distill the essence of lengthy articles and research papers. Tired of drowning in information overload? Let our ADSM be your guide,
#         #         providing crisp and coherent summaries, saving you valuable time and effort. """)
#         st.write_stream(project_descriptions(0))


#     st.subheader('**:green[Gender Classification using CNN & OpenCV ]**')
#     gender_url = "Images/gender.jpg"
#     st.image(gender_url, use_column_width=True)
#     st.link_button("Repository", "https://github.com/Arya920/Gender-Detection-Project")
    
#     if st.button(button_label,key='button2'):
#         # st.markdown("""This project focuses on classifying the gender of individuals from facial images. It employs a combination of techniques including transfer learning,
#         #         fine-tuning, and custom CNN models. """)
#         st.write_stream(project_descriptions(1))
    

# with col6:
#     st.subheader("**:green[Career Buddy - Career Guidance AI Chatbot]**")
#     chatbot_url = "Images/chatbot.png"
#     st.image(chatbot_url, use_column_width=True)
#     st.link_button("Repository", "https://github.com/Arya920/Career-Guidance-AI-bot")
#     if st.button(button_label, key='button3'):
#         # st.markdown("""This project presents the development of a career counseling bot that utilizes Quora data to provide users with valuable insights
#         #         and recommendations for their career choices """)
#         st.write_stream(project_descriptions(2))
        
#     st.subheader('**:green[Web Application for Stock Price Analysis & Prediction ]**')
#     sp_url = "Images/sp2.jpg"
#     st.image(sp_url, width= 406)
#     st.link_button("Repository", "https://github.com/Arya920/StockPriceForecasting")
#     if st.button(button_label, key='button4'):
#         # st.markdown("""The application allows users to analyze historical stock data, perform technical & statistical analysis, and even predict future 
#         #             stock prices using deep learning models.""")
#         st.write_stream(project_descriptions(3))