import streamlit as st
import google.generativeai as genai

st.title("🔑 Quick Gemini API Test")

# Check if key exists
if "GEMINI_API_KEY" not in st.secrets:
    st.error("❌ No API key found in secrets!")
    st.stop()

api_key = st.secrets["GEMINI_API_KEY"]
st.success(f"✅ Key found: {api_key[:4]}...{api_key[-4:]}")

# Test the API
if st.button("Test API"):
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-2.5-flash")
        response = model.generate_content("Say hello in 5 words")
        
        st.success("✅ API WORKS!")
        st.write(f"Response: {response.text}")
        
    except Exception as e:
        st.error(f"❌ FAILED: {e}")
