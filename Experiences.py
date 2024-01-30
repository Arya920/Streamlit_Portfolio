import streamlit as st 

def experiences():
    col1,col2 = st.columns(2)
    button_label = 'Description'
    with col1:

        with st.expander('ISNARTECH PVT LTD.'):
            isnartech_logo_url = "logos\Isnartech_logo.jpeg"
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
            EDL_logo = "logos\EDL_logo.jpeg"
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
