"""Version 2: add text input and a button."""

import streamlit as st


def run() -> None:
    st.set_page_config(page_title="AI Study Buddy v2")
    st.title("AI Study Buddy")
    st.write("Now the app can take input from the user.")

    name = st.text_input("What is your name?", placeholder="Enter your name")

    if st.button("Say hello"):
        if name.strip():
            st.success(f"Hello, {name}! Welcome to the AI lab.")
        else:
            st.warning("Please type your name first.")


if __name__ == "__main__":
    run()
