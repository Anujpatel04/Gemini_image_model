import os
import google.generativeai as genai
import streamlit as st
from PIL import Image
import base64
from io import BytesIO

google_api_key = 'AIzaSyBm1AppYECEOWE_vhMi7NrBl6Y3T718XLk'
genai.configure(api_key=google_api_key)

st.title("Image Describer with Gemini Image Model")
st.write("Upload an image, and the AI will generate a response.")

uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    buffered = BytesIO()
    image.save(buffered, format="JPEG")
    img_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")

    input_blob = {
        "mime_type": "image/jpeg",
        "data": img_base64
    }

    try:
        model_name = "gemini-1.5-flash-8b-exp-0924" 
        model = genai.GenerativeModel(model_name)

        response = model.generate_content({
            "parts": [{"mime_type": "image/jpeg", "data": img_base64}]
        })

        st.markdown("### AI Response:")
        st.write(response.text)  

    except Exception as e:
        st.error(f"An error occurred: {e}")
