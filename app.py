import streamlit as st
import google.generativeai as genai

# Page Config
st.set_page_config(page_title="Zen Creator Studio", page_icon="🎬")

# Connect to Gemini with specific version handling
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
else:
    st.error("Missing API Key in Secrets!")

# UI Header
st.title("🎬 Zen Creator Studio")
st.markdown("---")
st.write("Welcome VR! Your AI Video Assistant is Ready.")

# User Input
topic = st.text_input("Enter your video topic:", placeholder="e.g. MrBeast $10,000 Challenge")

if st.button("Generate Script 🚀"):
    if topic:
        with st.spinner("AI is brainstorming your next hit..."):
            try:
                # Using 'gemini-pro' which is the most stable for this version
                model = genai.GenerativeModel("gemini-pro")
                
                # Professional Prompt
                prompt = f"Write a viral YouTube title and a high-energy script in Hinglish for this topic: {topic}. Style: Engaging, Fast-paced, like MrBeast."
                
                response = model.generate_content(prompt)
                
                st.markdown("### 🔥 Your Viral Content:")
                st.write(response.text)
                st.success("Done! Now go make that video, VR!")
            except Exception as e:
                # Clear error message for debugging
                st.error(f"Error: {str(e)}")
    else:
        st.warning("Please type a topic first!")
