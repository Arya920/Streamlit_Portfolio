import streamlit as st 
from streamlit_extras.stylable_container import stylable_container
from pathlib import Path
from PIL import Image,ImageDraw
from html_codes import html_code_for_social2




def user():

    st.write("")
    st.write("")
    image1 = Image.open("Images\PF2.jpg")
    mask = Image.new('L', image1.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, image1.width, image1.height), fill=255)
    circular_image = Image.new('RGBA', image1.size, (0, 0, 0, 0))
    circular_image.paste(image1, mask=mask)



    col1,col2 = st.columns(2)
    with col1:
        st.markdown('''Data scientist and ML/DL enthusiast with a flair for crafting captivating web apps that turn complex datasets into actionable insights.
                    ''')
        st.markdown(':white_check_mark: Want to work together?')
        st.markdown('Send me an email 👉 [Mail me here](aryachakraborty.official@gmail.com)')
        st.markdown('Or you can contact me here 👇')
        st.markdown(html_code_for_social2, unsafe_allow_html=True )

        current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
        resume_path  = current_dir / "documents" / "Resume_DS.pdf"

        with stylable_container(
            key="green_button",
            css_styles="""
                button {
                    background-color: green;
                    color: white;
                    border-radius: 20px;
                }
                """,
        ):
            with open(resume_path, "rb") as pdf_file:
                PDFbyte = pdf_file.read()
            st.download_button(
                label=" 📄 Download Resume",
                data=PDFbyte,
                file_name=resume_path.name,
                mime="application/octet-stream",
            )
    with col2:
        st.image(circular_image, width=220)