# Yoji Macadangdang — Streamlit Portfolio

## Run locally

```powershell
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

## Images and content

- Profile photo: replace `profile.png` beside `app.py`. The path is defined in `app.py` as `PROFILE_IMAGE`.
- Photobooth screenshot: create `assets/photobooth.png`. It automatically replaces the labeled screenshot placeholder. No code edit needed.
- Skill ratings: `SKILLS` in `app.py` contains illustrative draft values. Replace them with your real self-assessment and then remove the draft warning and update the rating labels. Editing ratings in the live app does not change the source file.
- The LinkedIn URL supplied was a personal feed URL, not a public profile, so it is not presented as a contact link. Add a public `/in/...` profile URL when available.
- The autobiography uses the supplied facts; expand it with your own background and education details before submission if desired.
- Feedback is a session-only demonstration. It does not deliver messages to Yoji and is not persistent.

## Deploy to Streamlit Community Cloud

1. Sign in to GitHub and create a public repository (for example `yoji-portfolio`).
2. Upload `app.py`, `requirements.txt`, `profile.png`, and the `.streamlit/config.toml` file, preserving the `.streamlit` folder. Include `assets/photobooth.png` when ready. Do not upload a virtual environment or secrets.
3. Visit https://share.streamlit.io and create an account. Connect GitHub when prompted.
4. Click **Create app**, choose your repository and branch, and enter `app.py` as the main file path. Select Python 3.11 in advanced settings if offered.
5. Deploy, then open the public `.streamlit.app` URL and test every page. Submit that URL with **Yoji Macadangdang — F3**.

Official guide: https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/deploy

## Components used

Titles, headers, Markdown, image, sidebar, columns, radio navigation, metrics, tabs, containers, expanders, text inputs, text area, selectboxes, multiselect, checkbox, slider, editable table, bar chart, buttons, form validation, session state, download buttons, and custom theme.
