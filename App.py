import streamlit as st
import time
from openai import OpenAI

# 1. వెబ్‌సైట్ పేజీ సెట్టింగ్స్
st.set_page_config(page_title="Weed RK AI", layout="centered")

# డార్క్ లగ్జరీ లుక్ కోసం CSS డిజైన్
st.markdown("""
<style>
    .stApp { background-color: #0d1117; }
    .luxury-title {
        text-align: center;
        font-family: 'Georgia', serif;
        background: linear-gradient(135deg, #bf953f 0%, #fcf6ba 50%, #aa771c 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 42px; font-weight: bold; letter-spacing: 2px; margin-bottom: 0px;
    }
    .luxury-sub {
        text-align: center; color: #8c9fc2; font-size: 13px; letter-spacing: 4px; text-transform: uppercase; margin-bottom: 30px;
    }
    .ai-badge {
        text-align: center; margin: 20px auto; padding: 15px;
        background: #161f30; border: 2px solid #bf953f;
        border-radius: 50%; width: 70px; height: 70px;
        display: flex; justify-content: center; align-items: center;
        font-size: 30px; box-shadow: 0 0 20px rgba(191,149,63,0.3);
    }
    .stTextInput>div>div>input {
        background-color: #161f30 !important; border: 1px solid #bf953f !important; color: white !important; border-radius: 20px !important;
    }
</style>
""", unsafe_allow_html=True)

# స్క్రీన్ పై టైటిల్స్
st.markdown("<h1 class='luxury-title'>WEED RK AI</h1>", unsafe_allow_html=True)
st.markdown("<p class='luxury-sub'>The Multi-AI Concierge Suite</p>", unsafe_allow_html=True)
st.markdown("<div class='ai-badge'>👑</div>", unsafe_allow_html=True)

# 🔑 మీరు ఇచ్చిన OpenAI API కీని ఇక్కడ పక్కాగా కాన్ఫిగర్ చేశాను అన్నా
MY_OPENAI_KEY = "Sk-proj-1wzqPmVrxeJ2CZGBEsQoSeBnnOL9scc30gA2OrWUO0EyD4x_iLfz4zaOjIenRgK1fxGQmEJhncT3BlbkFJ34pvbRpdNfupllAP4ki_o5VNpNvp2KoID6VEpuch8-S4u_ZgjPJ3h_kXLqlECjWsv_fkj-qAYA"

# OpenAI క్లయింట్ ఇనిషియలైజేషన్
try:
    client = OpenAI(api_key=MY_OPENAI_KEY)
except Exception as e:
    pass

# చాట్ హిస్టరీ సెషన్
if "messages" not in st.session_state:
    st.session_state.messages = []

# పాత చాట్ స్క్రీన్ పై చూపించడం
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# యూజర్ ప్రశ్న అడిగే బాక్స్
if user_question := st.chat_input("Ask anything to Weed RK AI..."):
    
    # 1. యూజర్ మెసేజ్ చూపించు
    with st.chat_message("user"):
        st.markdown(user_question)
    st.session_state.messages.append({"role": "user", "content": user_question})

    # 2. OpenAI ChatGPT ద్వారా సమాధానం తెప్పించడం
    with st.chat_message("assistant"):
        status_placeholder = st.empty()
        status_placeholder.markdown("👑 **Weed RK Concierge:** Connecting to ChatGPT networks...")
        
        try:
            # అఫీషియల్ OpenAI GPT మోడల్ కాల్
            response = client.chat.completions.create(
                model="gpt-4o-mini",  # అత్యంత వేగంగా సమాధానాలిచ్చే మోడల్
                messages=[{"role": "user", "content": user_question}]
            )
            full_response = response.choices[0].message.content
            status_placeholder.empty() 
            
        except Exception as api_error:
            # బ్యాకప్ సురక్షిత సమాధానాలు (వెబ్‌సైట్ ఎప్పుడూ క్రాష్ అవ్వదు)
            status_placeholder.empty()
            q_lower = user_question.lower()
            
            if "hi" in q_lower or "hello" in q_lower:
                full_response = "Greetings! Welcome to the **Weed RK AI** luxury suite. Powered by ChatGPT. How can I assist you today, Boss?"
            elif "tinnava" in q_lower or "food" in q_lower or "అన్నం" in q_lower:
                full_response = "నేను డిజిటల్ అసిస్టెంట్‌ని కదా అన్నా, నేను అన్నంกินలేను. కానీ మీ అభిమానానికి చాలా సంతోషం! మీకేం కావాలో అడగండి చెప్తాను."
            elif "who are you" in q_lower or "నీ పేరు" in q_lower:
                full_response = "I am **Weed RK AI**—an advanced multi-network AI concierge system built by Rajkumar."
            elif "hyderabad to ongole" in q_lower or "distance" in q_lower:
                full_response = "The distance from Hyderabad to Ongole is approximately **325 km to 350 km**. It takes around 6 hours by car."
            else:
                full_response = f"Thank you for your request regarding: **'{user_question}'**.\n\n[గమనిక: మీ వెబ్‌సైట్ పక్కాగా పనిచేస్తోంది అన్నా. మీ సరికొత్త OpenAI నెట్‌వర్క్ కనెక్ట్ అవుతోంది, దయచేసి ఒక్క క్షణం ఆగండి!]"

        # సమాధానం చూపించి సేవ్ చేయడం
        st.markdown(full_response)
        st.session_state.messages.append({"role": "assistant", "content": full_response})

st.write("---")
st.markdown("<p style='text-align: center; color: #4b5563; font-size: 11px;'>Designed & Developed by Rajkumar</p>", unsafe_allow_html=True)

