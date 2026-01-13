import streamlit as st
from generate import generate_description
from templates import ELECTRONICS_TEMPLATES
from safety import is_safe

st.set_page_config(
    page_title="AI Product Description Generator",
    layout="centered"
)

st.title("🛍️ AI Product Description Generator")
st.markdown(
    "Generate **professional, sales-ready product descriptions** for electronics, gadgets, and appliances."
)

category = st.selectbox(
    "Select product category:",
    list(ELECTRONICS_TEMPLATES.keys())
)

features = st.text_area(
    "Describe the product features:",
    placeholder="e.g. 5000mAh battery, fast charging, AMOLED display, lightweight design"
)

if st.button("Generate Description"):
    if not features.strip():
        st.warning("Please enter product features.")
    elif not is_safe(features):
        st.error("⚠️ Unsafe or restricted content detected.")
    else:
        prompt = ELECTRONICS_TEMPLATES[category].format(features=features)

        with st.spinner("Generating description..."):
            result = generate_description(prompt)

        st.subheader("📄 Generated Product Description")
        st.success(result)
