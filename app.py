from pathlib import Path
import json
import re

import pandas as pd
import streamlit as st

ROOT = Path(__file__).resolve().parent
PROFILE_IMAGE = ROOT / "profile.png"
PHOTOBOOTH_IMAGE = ROOT / "assets" / "photobooth.png"

st.set_page_config(page_title="Yoji Macadangdang | Portfolio", page_icon="✦", layout="wide")

PROJECTS = [
    dict(title="Empress Photobooth", category="Desktop applications", role="Sole developer",
         tools=["Electron", "Node.js", "React"], status="Established business",
         summary="I built the photobooth application from end to end. The project grew into an established company called Empress.",
         outcome="From a software project to an established photobooth business.",
         lesson="I handled the entire application using Electron, Node.js, and React."),
    dict(title="Production RAG & Follow-up Automation", category="AI & automation", role="Founding engineer",
         tools=["GoHighLevel", "Zapier", "Python"], status="In active use",
         summary="I worked as the founding engineer on a retrieval-augmented generation (RAG) and follow-up bot built through GoHighLevel, with Zapier and Python.",
         outcome="The contracting company continues to use the system.",
         lesson="I worked on an AI and automation system used by a real company."),
    dict(title="AI Receptionist", category="AI & automation", role="Side-project developer",
         tools=["Gemini 2.5 Flash", "Python", "React", "TypeScript"], status="Learning project",
         summary="I built an AI receptionist as a side project using Gemini 2.5 Flash, Python, React, and TypeScript.",
         outcome="A hands-on project for learning rate limits and agent orchestration.",
         lesson="I explored how to set rate limits and coordinate agents through an orchestrator."),
]
# Illustrative draft ratings, not verified proficiency claims. Replace with your self-assessment.
SKILLS = {"Python": 4, "React": 4, "TypeScript": 3, "Node.js": 4,
          "Electron": 4, "Zapier": 3, "GoHighLevel": 3, "AI orchestration": 3}

st.markdown("""<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@400;600;700;800&display=swap');
html, body, [class*="css"], [data-testid="stApp"] {font-family:'DM Sans',sans-serif;}
h1,h2,h3 {font-family:'Manrope',sans-serif !important;letter-spacing:-.04em;}
[data-testid="stMainBlockContainer"] {max-width:1200px;padding-top:3rem;padding-bottom:3rem;}
[data-testid="stSidebar"] {border-right:1px solid #273345;}
.eyebrow {color:#a3e8b8;letter-spacing:.2em;font-size:.72rem;font-weight:700;text-transform:uppercase;}
.hero-title {font-family:'Manrope',sans-serif;font-size:clamp(2.6rem,5vw,4.8rem);font-weight:800;line-height:1.08;letter-spacing:-.065em;margin:1rem 0;}
.intro {font-size:1.08rem;color:#b7c2cf;line-height:1.8;max-width:650px;}
.tag {display:inline-block;border:1px solid #344255;border-radius:999px;padding:5px 12px;margin:3px 5px 3px 0;font-size:.78rem;color:#cbd5e1;}
.number {color:#a3e8b8;font-family:monospace;font-size:.8rem;letter-spacing:.12em;}
.placeholder {background:linear-gradient(130deg,#1d3441,#233329);border:1px dashed #63816e;border-radius:12px;padding:2.5rem 1.5rem;text-align:center;color:#c8dbcf;margin-bottom:1rem;}
[data-testid="stImage"] img {border-radius:18px;}
[data-testid="stMetric"] {border:1px solid #2b3848;border-radius:12px;padding:16px;}
div[data-testid="stVerticalBlockBorderWrapper"] {border-radius:14px;}
</style>""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("## YM ✦")
    st.caption("PERSONAL PORTFOLIO")
    st.write("**Yoji Macadangdang**")
    st.caption("BS Computer Science · 3rd Year\n\nCIT-U · Section F3")
    st.divider()
    page = st.radio("Explore", ["Overview", "My story", "Projects", "Skills", "Say hello"])
    st.divider()
    st.caption("Built with Python + Streamlit")
    st.download_button("Download portfolio summary", json.dumps({"name": "Yoji Macadangdang", "education": "BS Computer Science, 3rd Year, CIT-U, F3", "projects": PROJECTS}, indent=2), "yoji-portfolio.json", "application/json", width="stretch")


def projects_view():
    st.markdown('<p class="eyebrow">Selected work</p>', unsafe_allow_html=True)
    st.header("Ideas put into practice.")
    st.write("A photobooth business, a company automation system, and an AI side project.")
    left, right = st.columns([2, 1])
    query = left.text_input("Search projects", placeholder="Try Python, Empress, or automation")
    category = right.selectbox("Project category", ["All projects", "Desktop applications", "AI & automation"])
    tools = st.multiselect("Filter by tools", sorted({tool for p in PROJECTS for tool in p["tools"]}))
    show_lessons = st.checkbox("Show what I worked on", value=True)
    matches = [p for p in PROJECTS if (category == "All projects" or p["category"] == category)
               and all(t in p["tools"] for t in tools)
               and query.casefold() in " ".join([p["title"], p["summary"], *p["tools"]]).casefold()]
    st.caption(f"{len(matches)} of {len(PROJECTS)} projects")
    if not matches:
        st.info("No projects match those filters. Try a different search or clear the tools.")
    for p in matches:
        with st.container(border=True):
            st.caption(f'{p["category"].upper()} · {p["status"]}')
            st.subheader(p["title"])
            if p["title"] == "Empress Photobooth":
                if PHOTOBOOTH_IMAGE.is_file():
                    st.image(str(PHOTOBOOTH_IMAGE), caption="Empress Photobooth")
                else:
                    st.markdown('<div class="placeholder">EMPRESS / PHOTOBOOTH<br><small>Screenshot placeholder · image coming soon</small></div>', unsafe_allow_html=True)
            st.write(p["summary"])
            st.markdown("".join(f'<span class="tag">{t}</span>' for t in p["tools"]), unsafe_allow_html=True)
            a, b = st.columns([1, 2])
            a.markdown(f'**My role**  \n{p["role"]}')
            b.markdown(f'**Outcome**  \n{p["outcome"]}')
            if show_lessons:
                with st.expander("Behind the project"):
                    st.write(p["lesson"])


if page == "Overview":
    content, portrait = st.columns([1.8, 1], gap="large")
    with content:
        st.markdown('<p class="eyebrow">Yoji Macadangdang / Portfolio</p>', unsafe_allow_html=True)
        st.markdown('<div class="hero-title">Curious mind.<br>Practical projects.</div>', unsafe_allow_html=True)
        st.markdown('<p class="intro">I’m Yoji, a third-year Computer Science student at CIT-U. I build software, enjoy reading, and am working toward financial freedom.</p>', unsafe_allow_html=True)
        st.markdown('<span class="tag">Computer Science</span><span class="tag">CIT-U · F3</span><span class="tag">3rd Year</span>', unsafe_allow_html=True)
        st.write("")
        if st.button("Explore my work →", type="primary"):
            st.session_state["show_featured"] = not st.session_state.get("show_featured", False)
    with portrait:
        if PROFILE_IMAGE.is_file():
            st.image(str(PROFILE_IMAGE), caption="Yoji Macadangdang")
        else:
            st.info("Profile photo placeholder — add profile.png to the app folder.")
    st.divider()
    a, b, c = st.columns(3)
    a.metric("Selected projects", len(PROJECTS))
    b.metric("Year of study", "3rd")
    c.metric("Project still used by client", "1")
    st.write("")
    st.subheader("A little about me")
    st.write("My work spans desktop software and AI automation. I built the Empress photobooth application myself, worked as a founding engineer on a company’s RAG and follow-up bot, and explored agent orchestration through an AI receptionist side project.")
    if st.session_state.get("show_featured", False):
        projects_view()
elif page == "My story":
    st.markdown('<p class="eyebrow">Beyond the code</p>', unsafe_allow_html=True)
    st.title("My story, so far.")
    about, experience, journey = st.tabs(["Autobiography", "Work & leadership", "Project milestones"])
    with about:
        st.subheader("Where I am now")
        st.write("I’m Yoji Macadangdang, a third-year Bachelor of Science in Computer Science student at CIT-U, section F3. Alongside my studies, I have worked on desktop applications and AI automation projects.")
        st.subheader("What I enjoy")
        st.write("I love to read. Outside of my studies and projects, reading is one of my interests.")
        st.subheader("What I’m working toward")
        st.write("One of my personal goals is to become financially free. My portfolio brings together the projects I have built and the experience I have gained so far.")
    with experience:
        st.subheader("Work experience")
        for role, organization in [("Automation Engineer", "Metawatt"), ("Part-Time Software Engineer", "Windsgate"), ("Software Engineer", "A&Z")]:
            with st.container(border=True):
                st.subheader(role)
                st.write(organization)
        st.subheader("Leadership & organization roles")
        for role, organization in [("Vice President-External", "CSS"), ("Chief Network and Externals Officer", "GDG"), ("Specialist", "Dilaab")]:
            with st.container(border=True):
                st.subheader(role)
                st.write(organization)
    with journey:
        st.caption("Project milestones · dates have not been provided; this is not a chronological timeline.")
        for i, p in enumerate(PROJECTS, 1):
            with st.container(border=True):
                st.markdown(f'<span class="number">PROJECT {i:02}</span>', unsafe_allow_html=True)
                st.subheader(p["title"])
                st.write(p["outcome"])
elif page == "Projects":
    projects_view()
elif page == "Skills":
    st.markdown('<p class="eyebrow">My toolkit</p>', unsafe_allow_html=True)
    st.title("Tools behind the work.")
    st.write("These technologies come from my three featured projects.")
    st.warning("Draft self-assessment: the ratings below are illustrative and need my review before submission.")
    minimum = st.slider("Minimum rating to display", 1, 5, 1)
    st.caption("1 = beginner · 3 = comfortable · 5 = advanced. Edit the draft ratings below to make your own assessment.")
    edited = st.data_editor(pd.DataFrame({"Skill": list(SKILLS), "Rating": list(SKILLS.values())}),
                            hide_index=True, disabled=["Skill"],
                            column_config={"Rating": st.column_config.NumberColumn("Draft rating / 5", min_value=1, max_value=5, step=1, required=True)},
                            key="skill_ratings", width="stretch")
    selected = edited[edited["Rating"] >= minimum]
    if selected.empty:
        st.info("No skills match this minimum rating.")
    else:
        st.bar_chart(selected.set_index("Skill"), color="#a3e8b8", horizontal=True)
    st.download_button("Download current skill ratings", edited.to_csv(index=False), "yoji-skills.csv", "text/csv")
elif page == "Say hello":
    st.markdown('<p class="eyebrow">Get in touch</p>', unsafe_allow_html=True)
    st.title("Let’s start a conversation.")
    st.caption("Demo feedback form: submissions are kept only in this browser session. They are not emailed or saved to a server.")
    with st.form("feedback_form", clear_on_submit=True):
        name = st.text_input("Your name *", max_chars=100)
        email = st.text_input("Email (optional)", max_chars=254)
        subject = st.selectbox("What brings you here?", ["Project feedback", "Collaboration", "Just saying hello"])
        message = st.text_area("Message *", max_chars=3000)
        consent = st.checkbox("Keep this message in my current session")
        submitted = st.form_submit_button("Submit feedback", type="primary")
    if submitted:
        if not name.strip() or not message.strip():
            st.error("Please enter your name and a message.")
        elif email.strip() and not re.fullmatch(r"[^\s@]+@[^\s@]+\.[^\s@]+", email.strip()):
            st.error("Please enter a valid email or leave it blank.")
        elif not consent:
            st.error("Please check the session storage box to submit.")
        else:
            st.session_state.setdefault("feedback", []).append(dict(name=name.strip(), email=email.strip(), subject=subject, message=message.strip()))
            st.success(f"Thanks, {name.strip()}! Your feedback was added to this session.")
    if st.session_state.get("feedback"):
        with st.expander("Your session’s submitted feedback"):
            for entry in st.session_state["feedback"]:
                st.write(f'{entry["name"]} · {entry["subject"]}')
                st.text(entry["message"])
            if st.button("Clear session feedback"):
                st.session_state.pop("feedback", None)
                st.rerun()

st.divider()
st.caption("Yoji Macadangdang · BS Computer Science · CIT-U · 3rd Year · F3")

