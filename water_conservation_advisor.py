
import streamlit as st
import openai

# --- CONFIG ---
st.set_page_config(page_title="Water Conservation Advisor", layout="centered")
st.title("💧 Water Conservation Advisor")
st.markdown("Get personalized tips to save water at home.")

# --- API KEY ---
openai.api_key = st.secrets["OPENAI_API_KEY"]  # Add this in Streamlit Cloud secrets or use your local env

# --- User Input ---
st.subheader("🏠 Household Information")
family_size = st.slider("Number of people in your household", 1, 10, 3)
shower_length = st.slider("Average shower length (in minutes)", 1, 30, 10)
water_garden = st.selectbox("Do you water your garden?", ["Yes", "No"])
use_washing_machine = st.selectbox("Do you use a washing machine?", ["Yes", "No"])
monthly_bill = st.number_input("Your monthly water bill (₹ or $)", min_value=0.0, step=10.0)

# --- Prompt Template ---
def generate_prompt():
    return f"""
You are a Water Conservation Advisor bot. A user has the following profile:
- Family size: {family_size}
- Shower length: {shower_length} minutes
- Water garden: {water_garden}
- Washing machine: {use_washing_machine}
- Monthly bill: {monthly_bill}

Give 4 practical and customized water-saving tips for this household. Make the language friendly and actionable.
"""

# --- Generate Tips ---
st.subheader("💡 Personalized Tips")
if st.button("Generate Tips"):
    with st.spinner("Thinking..."):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful and eco-friendly water conservation assistant."},
                    {"role": "user", "content": generate_prompt()}
                ]
            )
            tips = response["choices"][0]["message"]["content"]
            st.success("Here are your tips:")
            st.markdown(tips)
        except Exception as e:
            st.error(f"Error: {e}")

# --- Footer ---
st.markdown("---")
st.caption("Created as part of a sustainability capstone project.")
