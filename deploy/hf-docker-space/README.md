---
title: AI Apps Tutorial Docker
emoji: A
colorFrom: green
colorTo: blue
sdk: docker
app_port: 7860
---

# AI Apps Tutorial Docker Space

This is the README to use when deploying the app as a custom Docker Space on Hugging Face.

Copy this file to the root of the Space repository together with:

- `Dockerfile`
- `app.py`
- `v10.py`
- `requirements.txt`
- `.streamlit/config.toml`

The Docker container runs Streamlit on port `7860`, which matches the `app_port` value above.
