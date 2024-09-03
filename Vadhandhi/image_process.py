import streamlit as st
from PIL import Image
from text_process import process_text_input
import easyocr
reader = easyocr.Reader(['en'])
import numpy as np

# Function to process image input
def process_image_input():
    flag=1
    up_image = st.file_uploader("Upload an image containing text", type=["png", "jpg", "jpeg"])

    if up_image is not None:
        image = np.array(Image.open(up_image))
        # Convert file to numpy array

        with st.spinner("Processing image..."):
            # Use OCR to extract text from image
            res = reader.readtext(image ,detail = 0)
           # extracted_text = pytesseract.image_to_string(image)
            st.write("**Extracted Text from Image:**")
            extracted_text=""
            for i in res:
                extracted_text += i+" "
            print(extracted_text)
            st.write(extracted_text)

            # Continue processing with the extracted text
            if extracted_text.strip():
                process_text_input(extracted_text,flag)
