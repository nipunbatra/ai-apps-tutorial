"""Version 8: use markdown, LaTeX, and a checkbox."""

import streamlit as st


def run() -> None:
    st.set_page_config(page_title="AI Study Buddy v8", layout="wide")
    st.title("AI Study Buddy")
    st.write("This version shows how Streamlit can display styled text and math.")

    st.markdown(
        """
        ### Why this is useful
        - `st.markdown()` is good for formatted notes
        - `st.latex()` is good for equations
        - `st.checkbox()` lets users show or hide details
        """
    )

    show_formula = st.checkbox("Show the formula details", value=True)

    st.subheader("A simple line")
    a = st.slider("Choose slope a", 0.0, 5.0, 2.0, 0.5)
    b = st.slider("Choose intercept b", 0.0, 10.0, 1.0, 0.5)
    x = st.slider("Choose x", 0.0, 10.0, 3.0, 0.5)
    y = a * x + b

    st.metric("Computed value of y", f"{y:.2f}")

    if show_formula:
        st.latex(fr"y = {a:.1f}x + {b:.1f}")
        st.markdown(f"When `x = {x:.1f}`, the output is **{y:.2f}**.")


if __name__ == "__main__":
    run()
