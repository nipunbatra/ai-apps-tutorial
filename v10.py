"""Version 10: a small final app that combines the main ideas."""

from io import StringIO

import pandas as pd
import streamlit as st
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression


@st.cache_data
def get_demo_csv() -> str:
    df = pd.DataFrame(
        [
            {
                "sepal length (cm)": 5.1,
                "sepal width (cm)": 3.5,
                "petal length (cm)": 1.4,
                "petal width (cm)": 0.2,
            },
            {
                "sepal length (cm)": 6.4,
                "sepal width (cm)": 3.2,
                "petal length (cm)": 4.5,
                "petal width (cm)": 1.5,
            },
            {
                "sepal length (cm)": 6.9,
                "sepal width (cm)": 3.1,
                "petal length (cm)": 5.4,
                "petal width (cm)": 2.1,
            },
        ]
    )
    return df.to_csv(index=False)


@st.cache_resource
def load_model() -> tuple[LogisticRegression, pd.DataFrame, list[str]]:
    iris = load_iris(as_frame=True)
    X = iris.data
    y = iris.target

    model = LogisticRegression(max_iter=300)
    model.fit(X, y)

    df = X.copy()
    df["species"] = [iris.target_names[index] for index in y]
    return model, df, list(iris.target_names)


def run() -> None:
    st.set_page_config(page_title="Iris Classifier App", layout="wide")

    st.sidebar.header("App controls")
    student_name = st.sidebar.text_input("Student name", placeholder="Enter your name")
    show_probabilities = st.sidebar.checkbox("Show prediction probabilities", value=True)
    show_formula = st.sidebar.checkbox("Show a simple model formula", value=False)

    model, iris_df, species_names = load_model()
    sample_csv = get_demo_csv()

    st.title("Iris Classifier App")
    st.write(
        "A small final app that combines widgets, charts, markdown, LaTeX, "
        "file upload, and a simple sklearn model."
    )

    if student_name.strip():
        st.success(f"Hello, {student_name}. Try a few flower measurements below.")

    explore_tab, predict_tab, upload_tab = st.tabs(
        ["Explore the data", "Single prediction", "Batch prediction"]
    )

    with explore_tab:
        st.markdown("### Iris dataset")
        st.dataframe(iris_df.head(10), use_container_width=True, hide_index=True)

        chart_df = (
            iris_df.groupby("species")[["petal length (cm)", "petal width (cm)"]]
            .mean()
            .reset_index()
        )
        st.bar_chart(chart_df.set_index("species"))

        st.markdown(
            """
            ### Why this app is useful
            - it uses a real sklearn model
            - it stays small enough to deploy easily
            - it shows how Python becomes a useful web interface
            """
        )

    with predict_tab:
        st.markdown("### Enter flower measurements")
        col1, col2 = st.columns(2)
        sepal_length = col1.slider("Sepal length (cm)", 4.0, 8.0, 5.8, 0.1)
        sepal_width = col2.slider("Sepal width (cm)", 2.0, 4.5, 3.0, 0.1)
        petal_length = col1.slider("Petal length (cm)", 1.0, 7.0, 4.3, 0.1)
        petal_width = col2.slider("Petal width (cm)", 0.1, 2.5, 1.3, 0.1)

        input_df = pd.DataFrame(
            [
                {
                    "sepal length (cm)": sepal_length,
                    "sepal width (cm)": sepal_width,
                    "petal length (cm)": petal_length,
                    "petal width (cm)": petal_width,
                }
            ]
        )

        prediction = int(model.predict(input_df)[0])
        st.success(f"Predicted flower: **{species_names[prediction]}**")

        if show_probabilities:
            proba_df = pd.DataFrame(
                {
                    "species": species_names,
                    "probability": model.predict_proba(input_df)[0],
                }
            )
            st.dataframe(proba_df, use_container_width=True, hide_index=True)

        if show_formula:
            st.markdown("### A simple linear model view")
            st.latex(r"z = w_1x_1 + w_2x_2 + w_3x_3 + w_4x_4 + b")
            st.markdown("The classifier uses the four measurements to compute class scores.")

    with upload_tab:
        st.markdown("### Predict from a CSV file")
        st.download_button(
            "Download sample CSV",
            data=sample_csv,
            file_name="iris_samples.csv",
            mime="text/csv",
        )

        uploaded_file = st.file_uploader("Upload your own CSV", type="csv")

        if uploaded_file is not None:
            df = pd.read_csv(uploaded_file)
            st.success("Using uploaded CSV.")
        else:
            df = pd.read_csv(StringIO(sample_csv))
            st.info("No file uploaded. Showing sample CSV instead.")

        required_columns = [
            "sepal length (cm)",
            "sepal width (cm)",
            "petal length (cm)",
            "petal width (cm)",
        ]
        if not set(required_columns).issubset(df.columns):
            st.error("CSV must contain the four iris measurement columns.")
            return

        df = df[required_columns].copy()
        predictions = model.predict(df)
        df["predicted_species"] = [species_names[index] for index in predictions]
        st.dataframe(df, use_container_width=True, hide_index=True)

        st.markdown("### Export a short summary")
        summary_lines = [f"Rows predicted: {len(df)}"]
        if student_name.strip():
            summary_lines.append(f"Run by: {student_name}")
        summary_lines.append(f"Classes used: {', '.join(species_names)}")
        summary_text = "\n".join(summary_lines)

        st.code(summary_text)
        st.download_button(
            "Download summary",
            data=summary_text,
            file_name="prediction_summary.txt",
            mime="text/plain",
        )


if __name__ == "__main__":
    run()
