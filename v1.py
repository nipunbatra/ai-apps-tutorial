"""Version 1: the smallest possible Streamlit app."""

import streamlit as st


def run() -> None:
    st.set_page_config(page_title="AI Study Buddy v1")
    st.title("AI Study Buddy")
    st.write("This is our first Streamlit app.")
    st.info("A Python script becomes a web app with one command: streamlit run v1.py")


if __name__ == "__main__":
    run()
