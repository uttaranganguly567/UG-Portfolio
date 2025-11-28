from pathlib import Path

from dotenv import load_dotenv
import streamlit as st

# Load environment variables from .env located alongside this script (if present)
_env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=_env_path, override=False)

from portfolio_pages import home, projects, skills, contact

# Page configuration
st.set_page_config(
    page_title="Uttaran Ganguly | Portfolio",
    page_icon="👨‍💻",
    layout="wide",
    initial_sidebar_state="collapsed"
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
            display: none;
        }

        [data-testid="collapsedControl"] {
            display: none !important;
        }

        .nav-container-wrapper {
            position: sticky;
            top: 0;
            z-index: 60;
            padding: 0 0 2.4rem;
            background: transparent;
            backdrop-filter: none;
            border-bottom: none;
        }

        .nav-container {
            width: min(900px, 90%);
            margin: 0 auto;
            padding: 1.2rem 1.6rem;
            border-radius: 999px;
            background: linear-gradient(135deg, rgba(0,212,255,0.16), rgba(0,120,200,0.12));
            box-shadow: 0 22px 42px rgba(0, 0, 0, 0.4);
            border: 1px solid rgba(0,212,255,0.25);
            backdrop-filter: blur(24px);
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .nav-menu {
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 1.1rem;
            flex-wrap: wrap;
            margin: 0;
        }

        .nav-button {
            display: inline-flex;
            align-items: center;
            gap: 0.75rem;
            padding: 0.95rem 1.85rem;
            border-radius: 14px;
            border: 1px solid rgba(0,212,255,0.25);
            background: linear-gradient(135deg, rgba(0,212,255,0.18), rgba(0,212,255,0.05));
            font-family: 'Science Gothic', var(--display-font);
            font-variation-settings: "wdth" 92, "wght" 520;
            letter-spacing: 0.11em;
            text-transform: uppercase;
            color: var(--text-color);
            cursor: pointer;
            position: relative;
            overflow: hidden;
            transition: transform 0.25s ease, box-shadow 0.25s ease, border-color 0.25s ease;
            text-decoration: none;
            box-shadow: 0 6px 18px rgba(0,212,255,0.18);
            white-space: nowrap;
        }

        .nav-button::before {
            content: "";
            display: inline-block;
            width: 10px;
            height: 10px;
            border-radius: 50%;
            background: rgba(0,212,255,0.6);
            box-shadow: 0 0 8px rgba(0,212,255,0.4);
            transition: transform 0.3s ease;
        }

        .nav-button:hover {
            transform: translateY(-4px);
            box-shadow: 0 14px 28px rgba(0, 212, 255, 0.24);
            border-color: rgba(0,212,255,0.45);
        }

        .nav-button.active {
            background: linear-gradient(135deg, rgba(0,212,255,0.38), rgba(0,120,200,0.35));
            border-color: rgba(0,212,255,0.7);
            box-shadow: 0 18px 34px rgba(0, 212, 255, 0.28);
            color: #04151f;
        }

        .nav-button.active::before {
            transform: scale(1.35);
        }

        @media (max-width: 768px) {
            .nav-container-wrapper {
                padding: 0 0 2rem;
            }

            .nav-container {
                width: 92%;
                padding: 0.9rem 1.1rem;
            }

            .nav-menu {
                gap: 0.75rem;
            }

            .nav-button {
                width: 100%;
                justify-content: center;
            }
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
            font-variation-settings: "wdth" 95, "wght" 520;
            letter-spacing: 0.08em;
            color: #ffffff;
        }

        .hero-title .hero-gradient {
            background: linear-gradient(
                120deg,
                #ffffff 0%,
                #eef5ff 15%,
                #b7dbff 30%,
                #66b0ff 45%,
                #1f66c5 55%,
                #66b0ff 70%,
                #b7dbff 85%,
                #ffffff 100%
            );
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            color: #ffffff;
            background-size: 200% 100%;
            animation: sheen 20s linear infinite;
            display: inline-block;
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
# Top navigation bar
nav_options = ["Home", "Projects", "Skills", "Contact"]

if hasattr(st, "query_params"):
    params = dict(st.query_params)

    def _set_query_params(**kwargs) -> None:
        for key, value in kwargs.items():
            st.query_params[key] = value
else:
    params = st.experimental_get_query_params()

    def _set_query_params(**kwargs) -> None:
        st.experimental_set_query_params(**kwargs)

if "current_page" not in st.session_state:
    st.session_state.current_page = "Home"

requested_page = params.get("page", st.session_state.current_page)
if isinstance(requested_page, list):
    requested_page = requested_page[0] if requested_page else st.session_state.current_page

if requested_page not in nav_options:
    requested_page = "Home"

if st.session_state.current_page != requested_page:
    st.session_state.current_page = requested_page

current_param_page = params.get("page")
if isinstance(current_param_page, list):
    current_param_page = current_param_page[0] if current_param_page else None

if current_param_page != st.session_state.current_page:
    _set_query_params(page=st.session_state.current_page)

nav_html = "<div class='nav-container-wrapper'><div class='nav-container'><div class='nav-menu'>"
for option in nav_options:
    active_class = " active" if st.session_state.current_page == option else ""
    nav_html += (
        f"<a class='nav-button{active_class}' href='?page={option}' target='_self' "
        f"rel='noopener noreferrer'>{option}</a>"
    )
nav_html += "</div></div></div>"

st.markdown(nav_html, unsafe_allow_html=True)

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
