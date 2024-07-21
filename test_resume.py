import streamlit as st 
import pdfplumber
import re 

def extract_text_with_pdfplumber(pdf_path):
    pdf_text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            pdf_text += page.extract_text()

    lines = pdf_text.split('\n')
    lines = [line.strip() for line in lines if line.strip()]
    formatted_text = '\n'.join(lines)
    return formatted_text


#extracted_text = extract_text_with_pdfplumber(pdf_path)
#print(extracted_text)

def clean_extracted_text(pdf_path):
    extracted_text = extract_text_with_pdfplumber(pdf_path)
    text = re.sub(r'[^A-Za-z0-9\s,.\'@|:\-\n]', '', extracted_text)
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'\n+', '\n', text)
    text = text.strip()
    
    return text

#print(clean_extracted_text(pdf_path))