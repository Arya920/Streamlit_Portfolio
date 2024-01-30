import streamlit as st 


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
        
