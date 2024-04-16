import streamlit as st
from openai import OpenAI

with open("keys/.openai_api_key.txt", "r") as f:
    OPENAI_API_KEY = f.read().strip()

client = OpenAI(api_key=OPENAI_API_KEY)

st.title("Code Reviewer with OpenAI")

st.header("Enter Your Python Code",divider='rainbow')
prompt = st.text_area("Enter your Python code here:", height=200)

if st.button("Review the Code"):
    st.markdown("<h2 style='color:blue;'>Review Result</h2>", unsafe_allow_html=True)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": """You are a Code Reviewer. 
                                         Review the given python code and note down all the bugs and errors in the code and 
                                         give fixed code by correcting the code."""},
            {"role": "user", "content": prompt}
        ],
        max_tokens=500
    )
    
    generated_text = response.choices[0].message.content
    st.write(generated_text)