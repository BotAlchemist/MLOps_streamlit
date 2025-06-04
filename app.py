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
