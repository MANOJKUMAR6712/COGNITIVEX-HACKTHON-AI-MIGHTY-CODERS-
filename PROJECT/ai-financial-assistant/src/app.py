import streamlit as st
from ui.chat import chat_interface
from ui.sidebar import user_profile_sidebar
from ui.tool_cards import financial_tool_cards

# Set Streamlit page config
st.set_page_config(
    page_title="INR AI Financial Assistant",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 3D animation video background (local or hosted mp4)
video_url = "https://www.w3schools.com/howto/rain.mp4"  # Replace with your 3D animation video URL or local path

st.markdown(
    f"""
    <style>
    .stApp {{
        background: transparent;
        position: relative;
    }}
    #bgvid {{
        position: fixed;
        right: 0;
        bottom: 0;
        min-width: 100vw;
        min-height: 100vh;
        z-index: -1;
        object-fit: cover;
    }}
    </style>
    <video autoplay muted loop id="bgvid">
        <source src="{video_url}" type="video/mp4">
    </video>
    """,
    unsafe_allow_html=True,
)

# Sidebar: User profile and customization
user_profile = user_profile_sidebar()

# Main UI: Chatbot and financial tools
st.title("💸 INR AI Financial Assistant")
st.write("Personalized financial advice, budget insights, and more — powered by AI.")

col1, col2 = st.columns([2, 1])

with col1:
    chat_interface(user_profile)

with col2:
    financial_tool_cards(user_profile)