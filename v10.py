"""Version 10: a small final app that combines the main ideas."""

from collections import Counter
from io import StringIO

import pandas as pd
import streamlit as st


@st.cache_data
def get_demo_data(multiplier: int) -> pd.DataFrame:
    df = pd.DataFrame(
        {
            "day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
            "hours": [1, 2, 2, 3, 2, 4, 3],
        }
    )
    df["hours"] = df["hours"] * multiplier
    return df


def clean_words(text: str) -> list[str]:
    words = []
    for raw_word in text.lower().split():
        word = raw_word.strip(".,!?;:-()[]{}\"'")
        if word:
            words.append(word)
    return words


def run() -> None:
    st.set_page_config(page_title="AI Lab Starter App", layout="wide")

    if "ideas" not in st.session_state:
        st.session_state.ideas = []

    st.sidebar.header("App controls")
    student_name = st.sidebar.text_input("Student name", placeholder="Enter your name")
    topic = st.sidebar.selectbox("Focus topic", ["Python", "Git", "Pandas", "Streamlit"])
    multiplier = st.sidebar.slider("Study intensity", 1, 4, 1)
    use_demo_data = st.sidebar.checkbox("Use demo study data", value=True)

    st.title("AI Lab Starter App")
    st.write("A small app that combines widgets, data, charts, state, and text analysis.")

    if student_name.strip():
        st.success(f"Hello, {student_name}. Your focus topic is {topic}.")

    planner_tab, ideas_tab, export_tab = st.tabs(["Study planner", "Idea analyzer", "Export"])

    with planner_tab:
        sample_df = get_demo_data(multiplier)
        sample_csv = sample_df.to_csv(index=False)

        st.download_button(
            "Download sample CSV",
            data=sample_csv,
            file_name="study_log.csv",
            mime="text/csv",
        )

        uploaded_file = st.file_uploader("Upload your own study log", type="csv")

        if uploaded_file is not None and not use_demo_data:
            df = pd.read_csv(uploaded_file)
            source_label = "uploaded CSV"
        else:
            df = pd.read_csv(StringIO(sample_csv))
            source_label = "demo data"

        required_columns = {"day", "hours"}
        if not required_columns.issubset(df.columns):
            st.error("The study log must contain the columns: day, hours")
            return

        col1, col2, col3 = st.columns(3)
        col1.metric("Rows", len(df))
        col2.metric("Total hours", float(df["hours"].sum()))
        col3.metric("Data source", source_label)

        st.dataframe(df, use_container_width=True, hide_index=True)
        st.bar_chart(df.set_index("day"))

    with ideas_tab:
        idea = st.text_area(
            "Describe a simple AI app idea",
            placeholder="Example: A tool that shows student attendance and marks in one dashboard.",
            height=180,
        )

        if st.button("Save this idea"):
            if idea.strip():
                st.session_state.ideas.append(idea.strip())
                st.success("Idea saved.")
            else:
                st.warning("Type an idea before saving.")

        if idea.strip():
            words = clean_words(idea)
            top_words = Counter(words).most_common(5)

            col1, col2, col3 = st.columns(3)
            col1.metric("Characters", len(idea))
            col2.metric("Words", len(words))
            col3.metric("Top unique words", len(set(words)))

            if top_words:
                top_words_df = pd.DataFrame(top_words, columns=["word", "count"])
                st.dataframe(top_words_df, use_container_width=True, hide_index=True)

        st.subheader("Saved ideas in this session")
        if st.session_state.ideas:
            for index, saved_idea in enumerate(st.session_state.ideas, start=1):
                st.write(f"{index}. {saved_idea}")
        else:
            st.write("No saved ideas yet.")

    with export_tab:
        summary_lines = [
            "AI Lab Starter App summary",
            f"Student name: {student_name or 'not provided'}",
            f"Focus topic: {topic}",
            f"Study intensity: {multiplier}",
            f"Saved ideas: {len(st.session_state.ideas)}",
        ]
        summary_text = "\n".join(summary_lines)

        st.code(summary_text)
        st.download_button(
            "Download summary",
            data=summary_text,
            file_name="app_summary.txt",
            mime="text/plain",
        )


if __name__ == "__main__":
    run()
