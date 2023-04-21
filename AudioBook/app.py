import pyttsx3
import PyPDF2
import streamlit as st
import tempfile

st.title('My Audio Book')
st.info('This Audio Book Takes a pdf file and Reads it out for You')
file = st.file_uploader("Pick a Pdf file",type="pdf")
if file is not None:
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(file.read())
        book = open(tmp_file.name, 'rb')
        # book = open('PCA_Implementation.pdf', mode='rb')
        pdf_Reader = PyPDF2.PdfReader(book)
        pages = len(pdf_Reader.pages)
        s = st.number_input("Starting PageNo.",min_value=1,max_value=pages)
        e = st.number_input("ending PageNo.",min_value=1,max_value=pages)
        speaker = pyttsx3.init()
        button = st.button('Press to start')
        if button:
            for num in range(s-1, e):
                page = pdf_Reader.pages[num]
                text = page.extract_text()
                speaker.say(text)
                st.write(text)
                speaker.runAndWait()