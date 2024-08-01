import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


PAGE_TITLE = "My Services | Arya"
PAGE_ICON = "🏛"
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON,layout="wide")

st.title("Want to Hire Me ? ")
st.text("These are the services I provide")
st.markdown("---")

#def services():
col3,col4 = st.columns(2)

with col3:
    stat_logo_url = "logos/stat.svg"
    st.image(stat_logo_url, width=40)
    st.subheader('**:green[Statistician]**')
    st.write("""Master the art of data interpretation and analysis, providing statistical insights to guide critical business decisions.
                Employ rigorous methodologies and mathematical models to uncover hidden patterns and trends within your data.""")

    st.write("")
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
    st.markdown("""Craft cutting-edge artificial intelligence solutions tailored to your specific needs,
                From predictive analytics to natural language processing, harness the power of AI to revolutionize your business operations""")

    st.write("")
    #st.write("")

    sql_logo_url = "logos/sql.svg"
    st.image(sql_logo_url, width=45)
    st.subheader('**:green[Data Scientist]**')
    st.markdown(""" I have led diverse data science projects and collaborated seamlessly with clients and partners to automate complex databases. My current
                    role as an AI Developer at Isnartech PVT. has further solidified my expertise in machine
                    learning, deep learning, and AI-driven solutions""")
                        
st.markdown("---")


# st.markdown(
#     """
#     <style>
#     .stTextArea textarea {
#         border: 1px solid  #ee8228 ;  /* Adjust the border color as needed */
#         border-radius: 5px;        /* Optional: Adjust the border radius */
#         background-color: #407887; /* Ensure background color matches your theme */
#         color: #000000;            /* Text color */
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

st.text("Drop a message here if you want to hire me or have any suggestion.")

with st.popover("Contact Me"):
    user_name = st.text_input('Name')
    user_mail = st.text_input('Gmail')
    user_msg = st.text_area('Your message to me')
    submitted = st.button('Submit')
    
if submitted:
    if user_name and user_mail and user_msg:
        # Email content
        from_email = "aryachakraborty.official@gmail.com"
        to_email = "aryachakraborty.official@gmail.com"
        subject = f"New contact form submission from {user_name}"
        message = f"Name: {user_name}\nEmail: {user_mail}\n\nMessage:\n{user_msg}"

        # Create message object
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        try:
            # Connect to the server and send the email
            server = smtplib.SMTP('smtp.gmail.com', 587)  # Update with your SMTP server details
            server.starttls()
            server.login(from_email, "arya 920")
            print('problem here')
            text = msg.as_string()
            print('server connected 🥳')
            server.sendmail(from_email, to_email, text)
            print('server connected 🥳')
            server.quit()
            st.success("Your message has been sent successfully!")
        except Exception as e:
            st.warning(f"Failed to send message: This issue is from my side. You can still mail me on my mail address ~ **:orange[aryachakraborty.official@gmail.com]**")
    else:
        st.warning("Please fill out all fields.")