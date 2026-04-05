"""Version 3: add sliders, select boxes, and simple logic."""

import streamlit as st


def run() -> None:
    st.set_page_config(page_title="AI Study Buddy v3")
    st.title("AI Study Buddy")
    st.write("This version uses widgets to collect choices.")

    hours = st.slider("How many hours will you practice this week?", 0, 20, 6)
    topic = st.selectbox(
        "Which topic do you want to revise?",
        ["Python", "Git", "Pandas", "Streamlit"],
    )
    mood = st.radio("How do you feel today?", ["curious", "okay", "confused"], horizontal=True)

    bonus = 10 if mood == "curious" else 0
    practice_score = min(100, hours * 5 + bonus)

    st.write(f"Planned topic: {topic}")
    st.write(f"Practice score: {practice_score}/100")

    if practice_score >= 60:
        st.success("Nice. This looks like a strong week.")
    else:
        st.info("Small steps are fine. Try adding a little more practice time.")


if __name__ == "__main__":
    run()
