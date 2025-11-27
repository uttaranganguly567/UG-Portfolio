from pathlib import Path

from dotenv import load_dotenv
import streamlit as st
from portfolio_pages import home, projects, skills, contact

# Load environment variables from .env located alongside this script (if present)
_env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=_env_path, override=False)

# Page configuration
st.set_page_config(
    page_title="Uttaran Ganguly | Portfolio",
    page_icon="👨‍💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for dark theme and modern styling
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Jost:wght@300;400;500;600;700&family=Oswald:wght@300;400;500;600&family=Poppins:wght@400;500;600;700&family=Science+Gothic:wdth,wght@75..125,300..700&family=Source+Sans+3:wght@300;400;500;600;700&display=swap');

        :root {
            --primary-color: #1f1f1f;
            --secondary-color: #2d2d2d;
            --accent-color: #00d4ff;
            --text-color: #e0e0e0;
            --heading-font: 'Poppins', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            --body-font: 'Jost', 'Source Sans 3', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            --display-font: 'Science Gothic', 'Poppins', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            --accent-font: 'Oswald', 'Poppins', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        @keyframes pulseGlow {
            0%, 100% {
                box-shadow: 0 0 8px rgba(0, 212, 255, 0.35);
                opacity: 1;
            }
            50% {
                box-shadow: 0 0 18px rgba(0, 212, 255, 0.6);
                opacity: 0.75;
            }
        }

        @keyframes subtleFloat {
            0%, 100% {
                transform: translateY(0px);
            }
            50% {
                transform: translateY(-6px);
            }
        }

        @keyframes sheen {
            0% {
                background-position: 200% 0;
            }
            100% {
                background-position: -200% 0;
            }
        }

        body {
            background-color: #1a1a1a;
            color: var(--text-color);
            font-family: var(--body-font);
            font-weight: 400;
            letter-spacing: 0.02em;
            -webkit-font-smoothing: antialiased;
            text-rendering: optimizeLegibility;
        }

        .main {
            background-color: #1a1a1a;
        }

        [data-testid="stSidebar"] {
            background-color: #1f1f1f;
            font-family: var(--body-font);
            padding: 0;
            min-height: 100vh;
        }

        [data-testid="stSidebar"] > div:first-child {
            background-color: #1f1f1f;
            height: 100%;
            display: flex;
            flex-direction: column;
        }

        [data-testid="stSidebar"] section[data-testid="stSidebarContent"] {
            flex: 1;
            display: flex;
            justify-content: center;
            align-items: stretch;
            padding: 0;
        }

        [data-testid="stSidebar"] section[data-testid="stSidebarContent"] > div {
            width: 100%;
            height: 100%;
            display: flex;
            flex-direction: column;
            justify-content: stretch;
            align-items: stretch;
            padding: 1.6rem 1.1rem 1.6rem 1.1rem;
            box-sizing: border-box;
        }

        [data-testid="stSidebar"] h1,
        [data-testid="stSidebar"] h2,
        [data-testid="stSidebar"] h3 {
            font-family: var(--accent-font);
            letter-spacing: 0.08em;
        }

        [data-testid="stSidebar"] div[data-testid="stRadio"] {
            width: 100%;
            height: 100%;
            display: flex;
            justify-content: center;
        }

        [data-testid="stSidebar"] div[data-testid="stRadio"] > div {
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            width: 100%;
            max-width: 230px;
            align-items: stretch;
            height: 100%;
            gap: 1.2rem;
            padding: 0.3rem 0;
        }

        [data-testid="stSidebar"] div[data-testid="stRadio"] > div > label {
            display: flex;
            align-items: center;
            gap: 0.75rem;
            width: 100% !important;
            flex: 1;
            box-sizing: border-box;
            padding: 1rem 1.45rem 1rem 2.4rem;
            margin: 0;
            border-radius: 14px;
            border: 1px solid rgba(0,212,255,0.25);
            background: linear-gradient(135deg, rgba(0,212,255,0.18), rgba(0,212,255,0.02));
            font-family: 'Science Gothic', var(--display-font);
            font-variation-settings: "wdth" 92, "wght" 520;
            letter-spacing: 0.1em;
            text-transform: uppercase;
            color: var(--text-color);
            cursor: pointer;
            transition: transform 0.25s ease, box-shadow 0.25s ease, border-color 0.25s ease;
            position: relative;
        }

        [data-testid="stSidebar"] div[data-testid="stRadio"] > div > label::before {
            content: "";
            width: 10px;
            height: 10px;
            border-radius: 50%;
            background: rgba(0,212,255,0.6);
            box-shadow: 0 0 8px rgba(0,212,255,0.4);
            transition: transform 0.3s ease, opacity 0.3s ease;
            position: absolute;
            left: 1.35rem;
        }

        [data-testid="stSidebar"] div[data-testid="stRadio"] > div > label:hover {
            transform: translateX(6px);
            box-shadow: 0 12px 24px rgba(0, 212, 255, 0.2);
            border-color: rgba(0,212,255,0.5);
        }

        [data-testid="stSidebar"] div[data-testid="stRadio"] > div > label:has(input:checked) {
            background: linear-gradient(135deg, rgba(0,212,255,0.35), rgba(0,120,200,0.35));
            border-color: rgba(0,212,255,0.7);
            box-shadow: 0 15px 28px rgba(0, 212, 255, 0.25);
        }

        [data-testid="stSidebar"] div[data-testid="stRadio"] > div > label:has(input:checked)::before {
            transform: scale(1.3);
        }

        [data-testid="stSidebar"] div[data-testid="stRadio"] > div > label > div:first-child {
            display: none;
        }

        [data-testid="stSidebar"] div[data-testid="stRadio"] > div > label > div:last-child {
            width: 100%;
            font-family: 'Science Gothic', var(--display-font);
            letter-spacing: 0.1em;
            white-space: nowrap;
        }

        h1, h2 {
            color: var(--accent-color);
            font-family: var(--heading-font);
            font-weight: 600;
            letter-spacing: 0.05em;
            margin-bottom: 0.75rem;
        }

        h3, h4, h5, h6 {
            color: var(--accent-color);
            font-family: var(--accent-font);
            font-weight: 500;
            letter-spacing: 0.06em;
            margin-bottom: 0.65rem;
            text-transform: uppercase;
        }

        h1.hero-title {
            font-size: 3.8rem;
            font-family: var(--display-font);
            background: linear-gradient(120deg, rgba(0,212,255,0.95), rgba(0,120,255,0.75));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: sheen 14s linear infinite;
            font-variation-settings: "wdth" 95, "wght" 520;
            letter-spacing: 0.08em;
        }

        .hero-subtitle {
            font-size: 1.4rem;
            color: rgba(224, 224, 224, 0.9);
            letter-spacing: 0.08em;
            animation: subtleFloat 8s ease-in-out infinite;
        }

        p, li {
            color: var(--text-color);
            font-family: var(--body-font);
            font-size: 1.05rem;
            line-height: 1.75;
            letter-spacing: 0.01em;
        }

        a {
            color: var(--accent-color);
            text-decoration: none;
            font-weight: 500;
        }

        a:hover {
            text-decoration: underline;
        }

        .section-title {
            font-size: 2.5rem;
            font-family: var(--display-font);
            font-weight: 600;
            margin-bottom: 1.5rem;
            text-align: center;
            color: var(--accent-color);
            letter-spacing: 0.1em;
            font-variation-settings: "wdth" 90, "wght" 520;
            text-transform: uppercase;
        }

        .section-title::after {
            content: "";
            display: block;
            height: 3px;
            width: 90px;
            margin: 0.75rem auto 0;
            border-radius: 999px;
            background: linear-gradient(90deg, rgba(0,212,255,0), rgba(0,212,255,0.95), rgba(0,212,255,0));
            animation: pulseGlow 4.5s ease-in-out infinite;
        }

        .skill-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            gap: 1rem;
            margin: 2rem 0;
        }

        .skill-card {
            background: linear-gradient(120deg, rgba(0,212,255,0.12), rgba(0,212,255,0.02));
            padding: 1.5rem;
            border-radius: 12px;
            text-align: center;
            border: 1px solid var(--accent-color);
            transition: all 0.3s ease;
            font-family: var(--heading-font);
            font-weight: 500;
            letter-spacing: 0.04em;
            background-size: 220% 220%;
            animation: sheen 12s linear infinite;
            margin: 0.75rem 0;
        }

        .skill-card h4 {
            font-family: var(--display-font);
            font-variation-settings: "wdth" 80, "wght" 480;
            letter-spacing: 0.05em;
            text-transform: none;
        }

        .skill-card:hover {
            background-color: #3a3a3a;
            transform: translateY(-5px);
            box-shadow: 0 5px 15px rgba(0, 212, 255, 0.3);
        }

        .project-card {
            background-color: var(--secondary-color);
            padding: 2rem;
            border-radius: 16px;
            margin: 1.5rem 0;
            border-left: 3px solid var(--accent-color);
            transition: all 0.3s ease;
            font-family: var(--body-font);
            letter-spacing: 0.01em;
            position: relative;
            overflow: hidden;
        }

        .project-card::before {
            content: "";
            position: absolute;
            inset: 0;
            border-radius: inherit;
            background: radial-gradient(circle at top right, rgba(0, 212, 255, 0.18), transparent 55%);
            opacity: 0;
            transition: opacity 0.4s ease;
        }

        .project-card:hover::before {
            opacity: 1;
        }

        .project-card h3 {
            font-family: var(--display-font);
            font-weight: 600;
            letter-spacing: 0.06em;
            font-variation-settings: "wdth" 88, "wght" 510;
            margin-bottom: 0.75rem;
            text-transform: none;
        }

        .project-card:hover {
            background-color: #3a3a3a;
            box-shadow: 0 5px 20px rgba(0, 212, 255, 0.2);
            animation: subtleFloat 6s ease-in-out infinite;
        }

        .home-highlight {
            background: linear-gradient(140deg, rgba(0,212,255,0.18), rgba(0,212,255,0.08));
            border: 1px solid rgba(0,212,255,0.35);
            animation: sheen 18s linear infinite;
        }

        .home-highlight h4 {
            font-family: var(--display-font);
            font-variation-settings: "wdth" 85, "wght" 500;
            letter-spacing: 0.06em;
            text-transform: none;
        }

        .project-link {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 0.65rem;
            padding: 0.75rem 1.65rem;
            border-radius: 999px;
            background: linear-gradient(135deg, rgba(0,212,255,0.5), rgba(0,120,255,0.65));
            color: #04151f !important;
            font-family: 'Jost', var(--body-font);
            font-weight: 600;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            text-decoration: none;
            box-shadow: 0 14px 30px rgba(0,212,255,0.28);
            position: relative;
            overflow: hidden;
            transition: transform 0.25s ease, box-shadow 0.25s ease, background 0.35s ease;
        }

        .project-link::before {
            content: "";
            position: absolute;
            inset: 0;
            background: radial-gradient(circle at top left, rgba(255,255,255,0.55), transparent 55%);
            opacity: 0;
            pointer-events: none;
            transition: opacity 0.35s ease;
        }

        .project-link::after {
            content: "↗";
            font-size: 1.1rem;
            transition: transform 0.25s ease;
        }

        .project-link:hover {
            transform: translateY(-4px);
            box-shadow: 0 20px 40px rgba(0,212,255,0.35);
            background: linear-gradient(135deg, rgba(0,212,255,0.68), rgba(0,120,255,0.85));
        }

        .project-link:hover::before {
            opacity: 1;
        }

        .project-link:hover::after {
            transform: translateX(6px);
        }

        .contact-info {
            background: linear-gradient(135deg, rgba(0,212,255,0.1), rgba(0,212,255,0));
            padding: 1.5rem;
            border-radius: 12px;
            margin: 1rem 0;
            border: 1px solid var(--accent-color);
            font-family: var(--body-font);
            background-size: 200% 200%;
            animation: sheen 16s linear infinite;
        }

        .contact-info h3 {
            font-family: var(--display-font);
            font-variation-settings: "wdth" 85, "wght" 500;
            letter-spacing: 0.05em;
            text-transform: none;
        }

        .intro-text {
            font-size: 1.1rem;
            color: #bfc4cc;
            line-height: 1.85;
            margin: 2rem 0;
            font-family: var(--body-font);
        }

        .stButton button {
            font-family: var(--heading-font);
            letter-spacing: 0.05em;
            background: linear-gradient(135deg, rgba(0,212,255,0.85), rgba(0,140,200,0.85));
            border: none;
            border-radius: 999px;
            transition: transform 0.25s ease, box-shadow 0.25s ease;
        }

        .stButton button:hover {
            transform: translateY(-3px);
            box-shadow: 0 12px 24px rgba(0, 212, 255, 0.25);
        }

        .home-pill {
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            padding: 0.6rem 1.25rem;
            border-radius: 999px;
            background: linear-gradient(135deg, rgba(0,212,255,0.18), rgba(0,212,255,0.05));
            border: 1px solid rgba(0,212,255,0.35);
            font-family: var(--body-font);
            letter-spacing: 0.05em;
            animation: pulseGlow 8s ease-in-out infinite;
        }

        /* Hide Streamlit share toolbar but keep sidebar toggle */
        [data-testid="stToolbarActions"] {
            display: none !important;
        }
    </style>
""", unsafe_allow_html=True)
# Sidebar navigation with modern styling
if "current_page" not in st.session_state:
    st.session_state.current_page = "Home"

nav_options = ["Home", "Projects", "Skills", "Contact"]
default_index = nav_options.index(st.session_state.current_page) if st.session_state.current_page in nav_options else 0

nav_selection = st.sidebar.radio(
    "Go to page",
    nav_options,
    index=default_index,
    label_visibility="collapsed",
    key="navigation_radio"
)

st.session_state.current_page = nav_selection
page = st.session_state.current_page

# Route to the selected page
if page == "Home":
    home.show()
elif page == "Projects":
    projects.show()
elif page == "Skills":
    skills.show()
elif page == "Contact":
    contact.show()

# Footer
st.markdown("---")
# st.markdown(
#     """
#     <div style='text-align: center; color: #707070; font-size: 0.85rem; margin-top: 3rem;'>
#         <p>© 2025 Uttaran Ganguly | Built with Streamlit</p>
#     </div>
#     """,
#     unsafe_allow_html=True
# )
