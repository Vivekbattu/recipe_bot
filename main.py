from dotenv import load_dotenv
import os
import google.generativeai as genai
import streamlit as st

load_dotenv(override=True)
API_KEY = os.getenv('API_KEY')

if not API_KEY:
    st.error("API Key not found. Please check your .env file.")
else:
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel("gemini-1.5-flash")

    def generate_recipe(ingredients):
        try:
            res = model.generate_content(f"Give me a recipe with {ingredients}")
            return res.text
        except Exception as e:
            st.error(f"Error generating recipe: {str(e)}")
            return ""

    st.title("Recipe Generator")
    ingredients = st.text_input("Enter Ingredients (comma-separated): ")

    if st.button("Get Recipe"):
        if ingredients:
            recipe = generate_recipe(ingredients)
            if recipe:
                st.markdown(recipe)
        else:
            st.warning("Please enter some ingredients.")
