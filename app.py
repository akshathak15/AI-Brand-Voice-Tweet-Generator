import streamlit as st
from groq import Groq

import os
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.set_page_config(page_title="AI Brand Tweet Generator")

st.title("AI Brand Voice Tweet Generator")
st.success("Tweets generated successfully!")
st.write("Generate 10 tweets based on brand voice.")

st.sidebar.header("Brand Information")

brand_name = st.sidebar.text_input("Brand Name")
industry = st.sidebar.text_input("Industry")

campaign = st.sidebar.selectbox(
    "Campaign Objective",
    ["Engagement", "Promotion", "Awareness"]
)

brand_desc = st.sidebar.text_area("Describe the brand")

if st.sidebar.button("Generate Tweets"):

    with st.spinner("Analyzing brand voice and generating tweets..."):

        prompt = f"""
You are a social media strategist.

Analyze the brand voice.

Brand: {brand_name}
Industry: {industry}
Campaign Objective: {campaign}
Description: {brand_desc}

Step 1: Identify
- tone
- target audience
- communication style
- content themes

Step 2: Generate 10 tweets matching the brand voice.
"""

    response = client.chat.completions.create(
    messages=[{"role": "user", "content": prompt}],
    model="llama-3.1-8b-instant"
)

    st.write(response.choices[0].message.content)
    st.markdown("---")
st.caption("Built with Streamlit + Groq AI | Internship Assignment Project")