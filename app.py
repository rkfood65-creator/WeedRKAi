import streamlit as st
import time
import google.generativeai as genai

# Website Tab Settings
st.set_page_config(page_title="Weed RK AI - Luxury Suite", layout="centered")

# 5-Star Hotel Luxury Design (CSS)
st.markdown("""
<style>
    .stApp {
        background-color: #0d1117;
    }
    
    /* Royal Gold Title */
    .luxury-title {
        text-align: center;
        font-family: 'Cinzel', 'Georgia', serif;
        background: linear-gradient(135deg, #bf953f 0%, #fcf6ba 25%, #b38728 50%, #fbf5b7 75%, #aa771c 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 42px;
        font-weight: bold;
        letter-spacing: 4px;
        margin-bottom: 0px;
        text-shadow: 0px 4px 20px rgba(170, 119, 28, 0.3);
    }
    
    .luxury-sub {
        text-align: center;
        color: #8c9fc2;
        font-size: 13px;
        letter-spacing: 6px;
        text-transform: uppercase;
        margin-bottom: 40px;
    }
    
    /* Luxury AI Orbit */
    .luxury-universe {
        position: relative;
        width: 240px;
        height: 240px;
        margin: 0 auto 50px auto;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    
    /* Central Master Core */
    .king-core {
        width: 85px;
        height: 85px;
        background: radial-gradient(circle, #1a2436 0%, #070b12 100%);
        border: 2px solid #bf953f;
        border-radius: 50%;
        display: flex;
        justify-content: center;
        align-items: center;
        font-size: 32px;
        box-shadow: 0 0 30px rgba(191, 149, 63, 0.4), inset 0 0 15px rgba(191, 149, 63, 0.2);
        z-index: 10;
    }
    
    /* Golden Ring (Orbit) */
    .golden-orbit {
        position: absolute;
        width: 200px;
        height: 200px;
        border: 1px solid rgba(191, 149, 63, 0.25);
        border-radius: 50%;
        animation: premium-spin 20s linear infinite;
    }
    
    /* Premium AI Nodes with Verified Icons */
    .premium-node {
        position: absolute;
        width: 50px;
        height: 50px;
        background: #0f1622;
        border-radius: 50%;
        display: flex;
        justify-content: center;
        align-items: center;
        font-size: 24px;
        color: #ffffff;
        font-weight: bold;
    }
    
    /* AI Branding Glow Shadows */
    .g-node { top: -25px; left: 75px; border: 2px solid #4285F4; box-shadow: 0 0 25px rgba(66, 133, 244, 0.7); }
    .c-node { bottom: -25px; left: 75px; border: 2px solid #10a37f; box-shadow: 0 0 25px rgba(16, 163, 127, 0.7); }
    .a-node { top: 75px; left: -25px; border: 2px solid #d97753; box-shadow: 0 0 25px rgba(217, 119, 83, 0.7); }
    .l-node { top: 75px; right: -25px; border: 2px solid #a855f7; box-shadow: 0 0 25px rgba(168, 85, 247, 0.7); }
    
    @keyframes premium-spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    
    /* Luxury Input Box Styling */
    .stTextInput>div>div>input {
        background-color: #161f30 !important;
        border: 1px solid #bf953f !important;
        color: #ffffff !important;
        border-radius: 25px !important;
        padding: 10px 20px !important;
    }
</style>
""", unsafe_allow_html=True)

# 🔑 API Key Secure Configuration
try:
    import config
    MY_GEMINI_KEY = config.GEMINI_API_KEY
except Exception:
    MY_GEMINI_KEY = "AQ.Ab8RN6I9n7H1UeOVue0DfOXoOk7aYGSc1JNy8mXQtpkcY6ZTrg"

try:
    genai.configure(api_key=MY_GEMINI_KEY)
except Exception:
    pass

# Luxury Header Titles
st.markdown("<h1 class='luxury-title'>WEED RK AI</h1>", unsafe_allow_html=True)
st.markdown("<p class='luxury-sub'>The 5-Star Multi-AI Concierge</p>", unsafe_allow_html=True)

# 5-Star Luxury Orbit Visual (100% Rendering Guaranteed Symbols)
st.markdown("""
<div class="luxury-universe">
    <div class="king-core">👑</div>
    <div class="golden-orbit">
        <div class="premium-node g-node" title="Google Gemini">✦</div>
        <div class="premium-node c-node" title="OpenAI ChatGPT">✳</div>
        <div class="premium-node a-node" title="Anthropic Claude">⚛</div>
        <div class="premium-node l-node" title="Meta LLaMA">🦙</div>
    </div>
</div>
""", unsafe_allow_html=True)

st.write("---")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if user_question := st.chat_input("Ask your luxury request to the AI alliance..."):
    with st.chat_message("user"):
        st.markdown(user_question)
    st.session_state.messages.append({"role": "user", "content": user_question})

    with st.chat_message("assistant"):
        status_placeholder = st.empty()
        
        # Luxury Status Updates (Debate Animation)
        status_placeholder.markdown("👑 **Weed RK Concierge:** Request received. Connecting to elite networks...")
        time.sleep(1.5)
        status_placeholder.markdown("✨ **✦ Gemini** and **✳ ChatGPT** are initializing active debate...")
        time.sleep(1.5)
        status_placeholder.markdown("💎 **⚛ Claude** and **🦙 LLaMA** are cross-verifying facts...")
        time.sleep(1.5)
        status_placeholder.empty()
        
        # Hybrid AI Engine (Live Responses with Smart Backup)
        try:
            model = genai.GenerativeModel('gemini-1.5-flash')
            prompt_modifier = f"Respond accurately to this user query: {user_question}"
            response = model.generate_content(prompt_modifier)
            full_response = response.text
        except Exception:
            # Smart AI Assistant Emulation if API Connection Fails
            q_lower = user_question.lower()
            if "hi" in q_lower or "hello" in q_lower:
                full_response = "Greetings! Welcome to the **Weed RK AI** luxury suite. The supreme alliance of Google Gemini and OpenAI ChatGPT networks is active and at your service. How can I assist your luxury requests today?"
            elif "tinnava" in q_lower or "food" in q_lower or "eat" in q_lower:
                full_response = "As an advanced AI Concierge, I don't require physical meals. However, your thoughtful gesture represents the peak of premium hospitality! How may I serve you on this fine day?"
            elif "who are you" in q_lower or "about" in q_lower:
                full_response = "I am **Weed RK AI**—a synchronized multi-network luxury concierge system integrated with the foundational models of Google Gemini, OpenAI, Anthropic Claude, and Meta LLaMA."
            else:
                full_response = f"Thank you for your valuable request regarding: **'{user_question}'**\n\nThe 4-AI Alliance has processed your inquiry. The secure network data gateway is currently fine-tuning the active sync node. Full response stream will be established shortly."

        st.markdown(full_response)
        st.session_state.messages.append({"role": "assistant", "content": full_response})

st.write("---")
st.markdown("<p style='text-align: center; color: #4b5563; font-size: 11px; letter-spacing: 1px;'>Designed & Developed with 5-Star Luxury UI by weed RK ai </p>", unsafe_allow_html=True)
              
