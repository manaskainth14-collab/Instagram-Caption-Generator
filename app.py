import streamlit as st
from openai import OpenAI
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
st.title("Instagram Caption Generator📹")
topic = st.text_input("Enter your topic")
if st.button("Generate"):
    response = client.responses.create(
        model = "gpt-4o-mini",
        input = f"Generate a catchy caption for {topic}"
    )
    st.subheader("Caption")
    st.write(response.output_text)