# 💧 Water Conservation Advisor

![MIT License](https://img.shields.io/badge/License-MIT-green.svg)

This Streamlit-based application offers personalized water-saving tips based on your household information. By leveraging OpenAI's GPT model, it delivers eco-friendly and actionable suggestions to help you reduce water usage and save on your water bill.

## 🛠 Features
- Input household details like family size, shower habits, and water usage
- Uses GPT-3.5-turbo to generate customized tips
- User-friendly interface with interactive sliders and dropdowns
- Secure handling of OpenAI API key via Streamlit secrets

## 🚀 How to Run Locally
1. Install requirements:
   ```bash
   pip install streamlit openai
   
2. Add your OpenAI API key to .streamlit/secrets.toml:
   ```bash
   [OPENAI_API_KEY]
   key = "your-api-key"
3. Run the app:

   ```bash
   streamlit run app.py
✨ Example Inputs
   Family size: 4

   Shower time: 15 minutes

   Garden watering: Yes

   Washing machine: Yes

   Monthly bill: ₹500

👤 Author
Prasanna Korada

