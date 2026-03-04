# VisionGPT – Multimodal Image Understanding Assistant

VisionGPT is a multimodal AI system that can **describe images and answer natural language questions about them**.
The system integrates **computer vision models, multimodal transformers, and a large language model** to generate intelligent responses about visual scenes.

---

# Features

• Automatic **image caption generation**
• **Visual Question Answering (VQA)** on uploaded images
• **LLM-powered explanations** for human-like responses
• GPU-accelerated inference using PyTorch
• Interactive web interface built with Streamlit

---

# System Architecture

Image → Caption Generation → Question Input → Visual Question Answering → LLM Explanation

Pipeline:

1. User uploads an image
2. BLIP model generates a descriptive caption
3. User asks a question about the image
4. ViLT model predicts a short answer
5. Llama LLM expands the answer into a natural explanation
6. Streamlit displays the final AI response

---

# Tech Stack

Python
PyTorch
HuggingFace Transformers
Streamlit
Pillow
Groq API (Llama LLM)

Models Used:

BLIP – Image Captioning
ViLT – Visual Question Answering
Llama – Language Reasoning Layer

---

# Project Structure

VisionGPT

app.py

[models]
caption_model.py , 
vqa_model.py

[llm]
groq_llama.py

requirements.txt

---

# Installation

Clone the repository

```
git clone https://github.com/AbhiramSanal/VisionGPT.git
cd VisionGPT
```

Install dependencies

```
pip install -r requirements.txt
```

---

# Running the Application

Start the Streamlit app:

```
streamlit run app.py
```

Then open the local URL shown in the terminal.

---

# Example Interaction

User uploads an image of a dog catching a frisbee.

Question:
"What is the dog doing?"

AI Response:
"The dog appears to be jumping into the air to catch a frisbee, suggesting it is playing in an open grassy area."

---

# Future Improvements

Chat-style multimodal interaction
Image similarity retrieval
Multiple image reasoning
Docker deployment

---

# Author

Developed as a multimodal AI project demonstrating computer vision, natural language processing, and large language model integration.
