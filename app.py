import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Weed RK ai", page_icon="🤖", layout="centered")

st.markdown("<h1 style='text-align: center; color: #00ffcc;'>🤖 Weed RK ai</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #888888;'>Your AI Assistant</p>", unsafe_allow_html=True)
st.write("---")

GOOGLE_API_KEY = "AQ.Ab8RN6IWKCXIBQlCRsVioRx_IRIyxkPfkyriwjPpC1HyY2MhdA"

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if user_question := st.chat_input("Ask a question..."):
    with st.chat_message("user"):
        st.markdown(user_question)
    st.session_state.messages.append({"role": "user", "content": user_question})

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        try:
            response = model.generate_content(user_question)
            full_response = response.text
            message_placeholder.markdown(full_response)
        except Exception as e:
            full_response = "Error connecting to the server."
            message_placeholder.markdown(full_response)
    
    st.session_state.messages.append({"role": "assistant", "content": full_response})

st.write("---")
st.markdown("<p style='text-align: center; color: #555555; font-size: 12px;'>Designed & Developed with AI by Rajkumar</p>", unsafe_allow_html=True)

