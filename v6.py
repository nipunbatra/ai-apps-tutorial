"""Version 6: upload a CSV file and show fallback sample data."""

from io import StringIO

import pandas as pd
import streamlit as st


def sample_dataframe() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "day": ["Mon", "Tue", "Wed", "Thu", "Fri"],
            "hours": [1, 2, 2, 3, 2],
        }
    )


def run() -> None:
    st.set_page_config(page_title="AI Study Buddy v6", layout="wide")
    st.title("AI Study Buddy")
    st.write("This version adds file upload.")

    sample_df = sample_dataframe()
    sample_csv = sample_df.to_csv(index=False)

    st.download_button(
        "Download sample CSV",
        data=sample_csv,
        file_name="study_log.csv",
        mime="text/csv",
    )

    uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.success("Using uploaded file.")
    else:
        df = pd.read_csv(StringIO(sample_csv))
        st.info("No file uploaded. Showing sample data instead.")

    required_columns = {"day", "hours"}
    if not required_columns.issubset(df.columns):
        st.error("CSV must contain the columns: day, hours")
        return

    st.dataframe(df, use_container_width=True, hide_index=True)
    st.bar_chart(df.set_index("day"))


if __name__ == "__main__":
    run()
