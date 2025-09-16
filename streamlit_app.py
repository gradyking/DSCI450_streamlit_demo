import streamlit as st
from google import genai
import tempfile

st.write("Gemini API GUI")

api_key = st.text_input("Google AI Studio API key", '1NS3RTAP1K3YH3R3T0TZW0NT5TEALY0URT0K3NZ')
picture = st.camera_input("Take a picture")
text = st.text_input("Gemini text prompt", "Can you identify what is in this picture?")

if picture:
    client = genai.Client(api_key=api_key)
    with st.spinner("Requesting response..."):
  
        # Save the captured image to a temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmpfile:
            tmpfile.write(picture.getvalue())
            tmp_path = tmpfile.name

        uploaded_file = client.files.upload(file=tmp_path)

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[text, uploaded_file]
        )

        st.write(response.text)