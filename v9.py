"""Version 9: train and use a simple sklearn classifier."""

import pandas as pd
import streamlit as st
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression


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
    st.set_page_config(page_title="AI Study Buddy v9", layout="wide")
    st.title("AI Study Buddy")
    st.write("This version trains a small sklearn model and uses it for prediction.")

    model, df, species_names = load_model()

    st.markdown("### Dataset preview")
    st.dataframe(df.head(), use_container_width=True, hide_index=True)

    st.markdown("### Predict flower type")
    sepal_length = st.slider("Sepal length (cm)", 4.0, 8.0, 5.8, 0.1)
    sepal_width = st.slider("Sepal width (cm)", 2.0, 4.5, 3.0, 0.1)
    petal_length = st.slider("Petal length (cm)", 1.0, 7.0, 4.3, 0.1)
    petal_width = st.slider("Petal width (cm)", 0.1, 2.5, 1.3, 0.1)

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
    st.success(f"Predicted class: **{species_names[prediction]}**")

    if st.checkbox("Show class probabilities"):
        proba_df = pd.DataFrame(
            {
                "species": species_names,
                "probability": model.predict_proba(input_df)[0],
            }
        )
        st.dataframe(proba_df, use_container_width=True, hide_index=True)


if __name__ == "__main__":
    run()
