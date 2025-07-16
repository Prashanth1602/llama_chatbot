import streamlit as st
from chatbot import get_response

st.set_page_config(page_title="AI Assistant", page_icon=":robot_face:", layout="centered")

st.title("AI Assistant")

st.write("Ask me anything about science, technology, innovation, startups, and research and development!")  

question = st.text_input("What's Your Question:", "")

if st.button("Get Answer"):
    if question:
        with st.spinner("Thinking..."):
            response = get_response(question)
            st.markdown(response)
    else:
        st.error("Please enter a question before clicking the button.")