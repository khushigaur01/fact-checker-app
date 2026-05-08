import streamlit as st

from extractor import extract_text_from_pdf
from extractor import extract_claims
from verifier import verify_claim
from utils import create_dataframe


st.set_page_config(page_title="AI Fact Checker")

st.title("AI Fact-Checking Web App")

st.write("Upload a PDF and verify claims automatically.")

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded_file is not None:

    with st.spinner("Extracting text from PDF..."):
        text = extract_text_from_pdf(uploaded_file)

    st.success("PDF text extracted successfully")

    with st.spinner("Extracting claims..."):
        claims = extract_claims(text)

    st.subheader("Extracted Claims")

    for idx, claim in enumerate(claims):
        st.write(f"{idx+1}. {claim}")

    results = []

    if st.button("Start Fact Checking"):

        progress_bar = st.progress(0)

        for idx, claim in enumerate(claims):

            verification = verify_claim(claim)

            results.append({
                "claim": claim,
                "status": verification["status"],
                "evidence": verification["evidence"]
            })

            progress = (idx + 1) / len(claims)
            progress_bar.progress(progress)

        st.success("Fact checking completed")

        df = create_dataframe(results)

        st.dataframe(df)

        st.subheader("Detailed Results")

        for result in results:

            st.markdown("---")

            st.write("### Claim")
            st.write(result["claim"])

            st.write("### Status")
            st.write(result["status"])

            st.write("### Evidence")
            st.write(result["evidence"])