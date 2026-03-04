import streamlit as st
from PIL import Image

from models.caption_model import generate_caption
from models.vqa_model import answer_question
from llm.groq_llama import explain_answer

st.title("Multimodal Image Captioning + Visual Q&A")

uploaded_file = st.file_uploader("Upload an image", type=["jpg","png","jpeg"])

if uploaded_file:

    image = Image.open(uploaded_file).convert("RGB")

    st.image(image, caption="Uploaded Image", use_column_width=True)

    caption = generate_caption(image)

    st.subheader("Generated Caption")

    st.write(caption)

    question = st.text_input("Ask a question about the image")

    if question:

        answer = answer_question(image, question)
        explanation = explain_answer(question, caption, answer)

        st.subheader("AI Response")
        st.write(explanation)