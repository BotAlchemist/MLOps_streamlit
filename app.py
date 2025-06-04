import streamlit as st

st.set_page_config(page_title="CI/CD Demo App", layout="centered")

st.title("🚀 Welcome to My Streamlit CI/CD Demo App")
st.write("This is a minimal app to demonstrate GitHub Actions CI integration.")

if st.button("Click Me"):
    st.success("🎉 Button clicked! CI is working!")

# New feature: user input
name = st.text_input("Enter your name")
if name:
    st.write(f"Hello, {name}! 👋")


st.subheader("🔢 Square a Number")

num = st.number_input("Enter a number", min_value=0.0, format="%.2f")

if st.button("Calculate Square"):
    st.success(f"The square of {num} is {num ** 2}")

