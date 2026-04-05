"""Version 8: remember values with st.session_state."""

import streamlit as st


def run() -> None:
    st.set_page_config(page_title="AI Study Buddy v8", layout="wide")
    st.title("AI Study Buddy")
    st.write("This version stores a list in session state.")

    if "ideas" not in st.session_state:
        st.session_state.ideas = []

    new_idea = st.text_input("Add a lab or app idea")

    col1, col2 = st.columns(2)

    if col1.button("Save idea"):
        if new_idea.strip():
            st.session_state.ideas.append(new_idea.strip())
            st.success("Idea saved in session state.")
        else:
            st.warning("Type something before saving.")

    if col2.button("Clear ideas"):
        st.session_state.ideas = []
        st.info("Session ideas cleared.")

    st.subheader("Saved ideas")
    if st.session_state.ideas:
        for index, idea in enumerate(st.session_state.ideas, start=1):
            st.write(f"{index}. {idea}")
    else:
        st.write("No ideas saved yet.")


if __name__ == "__main__":
    run()
