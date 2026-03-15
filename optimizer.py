import os
from groq import Groq
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

api_key = os.getenv("GROQ_API_KEY") or st.secrets["GROQ_API_KEY"]

client = Groq(api_key=api_key)


def optimize_copy(text):

    prompt = f"""
You are a conversion optimization expert.

Improve the following landing page copy.

Original text:
{text}

Return ONLY the following fields.

Headline:
Description:
Call To Action:

Do NOT include explanations.
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content