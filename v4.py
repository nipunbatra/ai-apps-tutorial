"""Version 4: add a sidebar, columns, metrics, and progress."""

import streamlit as st


def run() -> None:
    st.set_page_config(page_title="AI Study Buddy v4", layout="wide")

    st.sidebar.header("Controls")
    hours = st.sidebar.slider("Practice hours", 0, 20, 8)
    goal = st.sidebar.number_input("Weekly goal", min_value=1, max_value=20, value=10)
    topic = st.sidebar.selectbox("Focus topic", ["Python", "Git", "Pandas", "Streamlit"])

    completion = min(100, int((hours / goal) * 100))

    st.title("AI Study Buddy")
    st.write("This version adds layout and dashboard-style elements.")

    col1, col2, col3 = st.columns(3)
    col1.metric("Focus topic", topic)
    col2.metric("Planned hours", hours)
    col3.metric("Goal completion", f"{completion}%")

    st.progress(completion / 100)

    if completion >= 100:
        st.success("Goal reached.")
    else:
        st.info("You can still add more practice time this week.")


if __name__ == "__main__":
    run()
