"""Version 5: show a dataframe and a chart."""

import pandas as pd
import streamlit as st


def run() -> None:
    st.set_page_config(page_title="AI Study Buddy v5", layout="wide")
    st.title("AI Study Buddy")
    st.write("This version introduces tabular data and charts.")

    multiplier = st.slider("Scale the study hours", 1, 3, 1)

    df = pd.DataFrame(
        {
            "day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
            "hours": [1, 2, 1, 3, 2, 4, 2],
        }
    )
    df["hours"] = df["hours"] * multiplier

    st.dataframe(df, use_container_width=True, hide_index=True)
    st.line_chart(df.set_index("day"))

    total_hours = int(df["hours"].sum())
    st.metric("Total planned hours", total_hours)


if __name__ == "__main__":
    run()
