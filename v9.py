"""Version 9: use tabs and caching."""

import pandas as pd
import streamlit as st


@st.cache_data
def build_demo_schedule(multiplier: int) -> pd.DataFrame:
    df = pd.DataFrame(
        {
            "day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
            "hours": [1, 2, 1, 3, 2, 4, 2],
        }
    )
    df["hours"] = df["hours"] * multiplier
    return df


def run() -> None:
    st.set_page_config(page_title="AI Study Buddy v9", layout="wide")
    st.title("AI Study Buddy")
    st.write("This version uses cached data and tabs.")

    multiplier = st.sidebar.slider("Scale study hours", 1, 4, 1)
    df = build_demo_schedule(multiplier)

    dashboard_tab, notes_tab = st.tabs(["Dashboard", "Notes"])

    with dashboard_tab:
        st.dataframe(df, use_container_width=True, hide_index=True)
        st.line_chart(df.set_index("day"))
        st.metric("Total hours", int(df["hours"].sum()))

    with notes_tab:
        note = st.text_area("What did you learn from this app?")
        if note.strip():
            st.success("Nice. You now have multiple sections in one app.")


if __name__ == "__main__":
    run()
