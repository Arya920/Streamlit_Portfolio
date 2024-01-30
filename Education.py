import streamlit as st 


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
        

