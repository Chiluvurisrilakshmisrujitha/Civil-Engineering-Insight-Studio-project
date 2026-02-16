import streamlit as st
from PIL import Image
from google import genai

# 🔑 Paste your API key directly here
API_KEY = "AIzaSyCGcVQUZADYckPbFWLZCVVDJ06NyfYLLmY"

# Initialize Gemini Client
client = genai.Client(api_key=API_KEY)

# Streamlit UI
st.set_page_config(page_title="Civil Engineering Insight Studio")
st.title("🏗️ Civil Engineering Insight Studio")

st.write("""
Upload an image of a building, bridge, or construction site.
The AI will analyze materials, structure, and progress.
""")

uploaded_file = st.file_uploader(
    "Upload construction image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(image, caption="Uploaded Image", use_column_width=True)

    with st.spinner("Analyzing image... Please wait ⏳"):

        prompt = """
        You are a civil engineering expert.

        Analyze this image and provide:
        1) Materials used
        2) Structural elements
        3) Construction progress
        4) Any structural concerns

        Write clearly and professionally.
        """

        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=[prompt, image]
        )

    st.subheader("🔍 AI Analysis Result")
    st.write(response.text)
