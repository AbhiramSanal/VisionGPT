import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def explain_answer(question, caption, answer):

    prompt = f"""
You are analyzing an image.

Image description:
{caption}

Question about the image:
{question}

Short model answer:
{answer}

Provide a clear and natural explanation in 1-2 sentences.
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role":"user","content":prompt}]
    )

    return response.choices[0].message.content