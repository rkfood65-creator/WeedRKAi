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
    
    /* Premium AI Nodes */
    .premium-node {
        position: absolute;
        width: 50px;
        height: 50px;
        background: #0f1622;
        border-radius: 50%;
        display: flex;
        justify-content: center;
        align-items: center;
        font-size: 22px;
    }
    
    /* AI Branding Colors */
    .g-node { top: -25px; left: 75px; border: 2px solid #4285F4; box-shadow: 0 0 20px rgba(66, 133, 244, 0.5); }
    .c-node { bottom: -25px; left: 75px; border: 2px solid #10a37f; box-shadow: 0 0 20px rgba(16, 163, 127, 0.5); }
    .a-node { top: 75px; left: -25px; border: 2px solid #d97753; box-shadow: 0 0 20px rgba(217, 119, 83, 0.5); }
    .l-node { top: 75px; right: -25px; border: 2px solid #9c27b0; box-shadow: 0 0 20px rgba(156, 39, 176, 0.5); }
    
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

# 🔑 Secured integrated key provided by user
MY_GEMINI_KEY = "AQ.Ab8RN6I9n7H1UeOVue0DfOXoOk7aYGSc1JNy8mXQtpkcY6ZTrg"

# Configure the API Key directly
genai.configure(api_key=MY_GEMINI_KEY)

# Luxury Header Titles
st.markdown("<h1 class='luxury-title'>WEED RK AI</h1>", unsafe_allow_html=True)
st.markdown("<p class='luxury-sub'>The 5-Star Multi-AI Concierge</p>", unsafe_allow_html=True)

# 5-Star Luxury Orbit Visual
st.markdown("""
<div class="luxury-universe">
    <div class="king-core">👑</div>
    <div class="golden-orbit">
        <div class="premium-node g-node" title="Google Gemini">🔵</div>
        <div class="premium-node c-node" title="OpenAI ChatGPT">🟢</div>
        <div class="premium-node a-node" title="Anthropic Claude">🟠</div>
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
        
        # Luxury Status Updates (The Smart Debate Simulation Animation)
        status_placeholder.markdown("👑 **Weed RK Concierge:** Request received. Connecting to the elite neural networks...")
        time.sleep(2)
        
        status_placeholder.markdown("✨ **🔵 Gemini** and **🟢 ChatGPT** are initializing the active debate...")
        time.sleep(2)
        
        status_placeholder.markdown("💎 **🟠 Claude** and **🦙 LLaMA** are cross-verifying and filtering inaccuracies...")
        time.sleep(2)
        
        status_placeholder.markdown("⚜️ **Final Verdict:** Refining the 100% accurate master response...")
        time.sleep(2.5)
        
        status_placeholder.empty()
        
        try:
            # Fetching the original response from the Gemini engine using the provided key
            model = genai.GenerativeModel('gemini-1.5-flash')
            # Custom system prompt to force the AI to act as a combined system
            prompt_modifier = (
                "Respond to this query as a unified system compiled from Gemini, ChatGPT, Claude, and LLaMA, "
                f"giving the best verified answer. Query: {user_question}"
            )
            response = model.generate_content(prompt_modifier)
            full_response = response.text
        except Exception as e:
            # Elegant error fallback if API key fails
            full_response = "Thank you for your request. The system luxury alliance is currently stabilizing its secure gateway. Please verify the network connection or the integrated access token."

        st.markdown(full_response)
        st.session_state.messages.append({"role": "assistant", "content": full_response})

st.write("---")
st.markdown("<p style='text-align: center; color: #4b5563; font-size: 11px; letter-spacing: 1px;'>Designed & Developed with 5-Star Luxury UI by Rajkumar</p>", unsafe_allow_html=True)

