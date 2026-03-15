import streamlit as st
from optimizer import optimize_copy


st.set_page_config(
    page_title="AI Conversion Optimizer",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 AI Landing Page Conversion Optimizer")
st.caption("Improve marketing copy using AI")

text = st.text_area("Paste your landing page text here", height=200)

if st.button("Optimize Copy"):

    if text.strip() == "":
        st.warning("Please enter some text")

    else:

      
        with st.spinner("Optimizing your copy..."):
            result = optimize_copy(text)

        st.divider()

    
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Original Copy")
            st.write(text)

        with col2:
            st.subheader("Optimized Copy")
            st.markdown(result)


        st.download_button(
            "Download Optimized Copy",
            result,
            file_name="optimized_copy.txt"
        )


st.divider()
st.caption("Built with Streamlit + Groq AI")