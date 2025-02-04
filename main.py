from dotenv import load_dotenv
import os
import google.generativeai as genai
import streamlit as st

load_dotenv(override=True)
API_KEY = os.getenv('API_KEY')

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

def generate_recipe(ingredients):
    res = model.generate_content(f"Give me recipe with {ingredients}")
    return res.text

st.title("Recipe Generator")

ingredients = st.text_input("Enter Ingredients (csv): ")

if st.button("Get Recipe"):
    if ingredients:
        recipe = generate_recipe(ingredients)
        st.markdown(recipe)
    else:
        st.warning("Please enter some value.")