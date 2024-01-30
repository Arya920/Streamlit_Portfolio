import streamlit as st 

def services():
    col3,col4 = st.columns(2)

    with col3:
        stat_logo_url = "logos\stat.svg"
        st.image(stat_logo_url, width=40)
        st.subheader('**:green[Statistician]**')
        st.markdown("""Master the art of data interpretation and analysis, providing statistical insights to guide critical business decisions.
                    Employ rigorous methodologies and mathematical models to uncover hidden patterns and trends within your data.""")

        st.write("")

        PBI_logo_url = "logos\language.svg"
        st.image(PBI_logo_url, width=40)
        st.subheader('**:green[NLP Engineer]**')
        st.markdown("""Unlock the potential of natural language processing to extract meaningful information from textual data.
                    Develop innovative solutions for text analysis, sentiment analysis, and language understanding, empowering your applications with human-like comprehension capabilities.""")

    with col4:
        AI_logo_url = "logos\AI.svg"
        st.image(AI_logo_url, width=45)
        st.subheader('**:green[AI Developer]**')
        st.markdown("""TCraft cutting-edge artificial intelligence solutions tailored to your specific needs,
                    From predictive analytics to natural language processing, harness the power of AI to revolutionize your business operations""")

        st.write("")
        st.write("")
    
        sql_logo_url = "logos\sql.svg"
        st.image(sql_logo_url, width=45)
        st.subheader('**:green[SQL Developer]**')
        st.markdown("""Design robust and secure databases to store and retrieve data efficiently. Leverage expert SQL coding techniques to streamline
                    data management processes and enhance data integrity, facilitating seamless integration with your applications and systems.""")
