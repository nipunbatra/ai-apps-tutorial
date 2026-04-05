"""Version 7: simple text analysis in a Streamlit app."""

from collections import Counter

import pandas as pd
import streamlit as st


def clean_words(text: str) -> list[str]:
    words = []
    for raw_word in text.lower().split():
        word = raw_word.strip(".,!?;:-()[]{}\"'")
        if word:
            words.append(word)
    return words


def run() -> None:
    st.set_page_config(page_title="AI Study Buddy v7", layout="wide")
    st.title("AI Study Buddy")
    st.write("This version analyzes text without calling any external API.")

    idea = st.text_area(
        "Describe a simple AI app idea",
        placeholder="Example: A small app that lets students upload marks and visualize progress.",
        height=180,
    )

    if not idea.strip():
        st.info("Type some text to see the analysis.")
        return

    words = clean_words(idea)
    top_words = Counter(words).most_common(5)

    col1, col2, col3 = st.columns(3)
    col1.metric("Characters", len(idea))
    col2.metric("Words", len(words))
    col3.metric("Sentences", idea.count(".") + idea.count("!") + idea.count("?"))

    if top_words:
        top_words_df = pd.DataFrame(top_words, columns=["word", "count"])
        st.dataframe(top_words_df, use_container_width=True, hide_index=True)


if __name__ == "__main__":
    run()
