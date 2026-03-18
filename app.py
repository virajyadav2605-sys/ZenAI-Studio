import streamlit as st
import google.generativeai as genai

# Page Config
st.set_page_config(page_title="Zen Creator Studio", page_icon="🎬")

# Connect to Gemini
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
else:
    st.error("Missing API Key in Secrets!")

# Modern UI
st.title("🎬 Zen Creator Studio")
st.markdown("---")
st.write("Welcome VR! Let's generate a viral YouTube script.")

# User Input
topic = st.text_input("Enter your video topic:", placeholder="e.g. MrBeast $10,000 Challenge")

if st.button("Generate Script 🚀"):
    if topic:
        with st.spinner("AI is brainstorming your next hit..."):
            try:
                # Latest stable model for speed
                model = genai.GenerativeModel("gemini-1.5-flash")
                
                # Instruction
                prompt = f"Act as a professional YouTuber. Write a viral Title and a high-energy script in Hinglish for: {topic}"
                
                response = model.generate_content(prompt)
                
                st.markdown("### 🔥 Your Content:")
                st.write(response.text)
            except Exception as e:
                st.error(f"System Error: {str(e)}")
    else:
        st.warning("Please type a topic first!")
