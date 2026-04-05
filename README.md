# AI Apps Tutorial

Minimal Streamlit apps for the course "Software Tools and Techniques for AI".

Each file adds one new idea, so students can run the versions in order:

```bash
pip install -r requirements.txt
streamlit run v1.py
streamlit run v2.py
...
streamlit run v10.py
```

The final deployable app is `app.py`, which imports `v10.py`.

## What each version teaches

| File | New idea |
|---|---|
| `v1.py` | title, text, basic app structure |
| `v2.py` | text input and button |
| `v3.py` | slider, selectbox, radio, simple logic |
| `v4.py` | sidebar, columns, metrics, progress |
| `v5.py` | dataframe and charts |
| `v6.py` | file upload and sample CSV download |
| `v7.py` | text area and simple text analysis |
| `v8.py` | checkbox, markdown, and LaTeX |
| `v9.py` | a simple sklearn classifier with cached loading |
| `v10.py` | a final sklearn app with charts, tabs, upload, markdown, and export |

## Suggested lab flow

1. Run `v1.py` to show how quickly a web app appears.
2. Move to `v2.py` to explain reruns and buttons.
3. Use `v3.py` and `v4.py` to cover widgets and layout.
4. Use `v5.py` and `v6.py` for data display and CSV upload.
5. Use `v7.py` and `v8.py` for text display, markdown, and math.
6. Use `v9.py` to show how sklearn fits into a Streamlit app.
7. End with `v10.py`, then deploy `app.py`.

## Local setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

Run Streamlit from the repository root so local paths behave the same way as deployment.

## Deployment

- Streamlit Community Cloud: see `deploy/streamlit-community-cloud.md`
- Hugging Face Spaces: use the separate `hf-spaces-deploy-tutorial` repo

## Notes for teaching

- The apps stay self-contained so students can open one file and understand it.
- The examples are student-friendly and now include a minimal sklearn model.
- Markdown, LaTeX, checkbox widgets, charts, and CSV upload are all covered before deployment.
