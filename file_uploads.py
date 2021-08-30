import streamlit as st
# File Processing packages
from PIL import Image
import pandas as pd
import docx2txt 
from PyPDF4 import PdfFileReader # (Method 1)
import pdfplumber # (Method 2)

# Load images
@st.cache
def load_image(image_file):
    img = Image.open(image_file)
    return img

def read_pdf(file):
    pdfReader = PdfFileReader(file)
    count = pdfReader.numPages
    all_page_text = ""
    for i in range(count):
        page = pdfReader.pages[i]
        all_page_text += page.extractText()

    return all_page_text


st.title("Files Upload tutorial")

menu = ["Home", "Dataset", "DocumentFiles", "About"]
choice = st.sidebar.selectbox("Menu",menu)

if choice == "Home":          # (For uploading Image: PIL,OpenCV)                                           
    st.subheader("Home")                                                 
    image_file = st.file_uploader("Upload Images",                       
        type = ["png", "jpg", "jpeg"])

    if image_file is not None:  # (To see in-depth details)
        #st.write(type(image_file))
        #st.write(dir(image_file))  # (Method 1)

        file_details = {"filename": image_file.name, # (Method 2)
        "filetype": image_file.type, "filesize": image_file.size}
        st.write(file_details)   

        st.image(load_image(image_file)) 
 
elif choice == "Dataset":             # (For uploading CSV files: Pandas,CSV)
    st.subheader("Dataset")
    data_file = st.file_uploader("Upload CSV", type = ["csv"])

    if data_file is not None:
        st.write(type(data_file))
        file_details = {"filename": data_file.name, 
        "filetype": data_file.type, "filesize": data_file.size}
        st.write(file_details)
        df = pd.read_csv(data_file)
        st.dataframe(df)

elif choice == "DocumentFiles":       # (For uploading Docx and PDF files: doc2txt, python-docx, PyPDF2, Pdfplumber, textract)
    st.subheader("DocumentFiles")
    docx_file = st.file_uploader("Upload Document",
        type = ["pdf", "docx", "doc", "txt"])
    if st.button("Process"):
        try:
            if docx_file is not None:
                file_details = {"filename": docx_file.name, 
            "filetype": docx_file.type, "filesize": docx_file.size}
            st.write(file_details)
        finally:
            st.write("Please select file")
            
    if docx_file.type == "text/plain": 
        #raw_text = docx_file.read() # (Read as bytes) Method 1  
        #st.write(raw_text) # (Works but in Bytes)
        #st.text(raw_text) # (works but also reads the text in a straight line) 

        #Read as string (decode bytes to string) Method 2
        raw_text = str(docx_file.read(), "utf-8")
        #st.write(raw_text) # (Works)
        st.text(raw_text)  # (Works)

    elif docx_file.type =="application/pdf":      # (To read Docx format)
        # try:
        #     with pdfplumber.open(docx_file) as pdf:
        #         pages = pdf.pages[0]
        #         st.write(pages.extract_text())

        # except:
        #     st.write("None")
            
     #Using PyPDF
       raw_text = read_pdf(docx_file)
       st.write(raw_text)   

    else:                                        
        raw_text = docx2txt.process(docx_file)  
        st.write(raw_text) #(Works)
        #st.text(raw_text)  #(Works)



else:
    st.subheader("About")