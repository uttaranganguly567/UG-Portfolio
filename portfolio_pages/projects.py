import streamlit as st

def show():
    """Projects page of the portfolio"""
    
    st.markdown("<h1 class='section-title'>🚀 Projects</h1>", unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Project 1: Campus Core
    st.markdown("""
        <div class='project-card'>
            <h3>Campus Core</h3>
            <p>Records made easy.</p>
            <p><strong>Tech Stack:</strong> Built with React on the front, Node and Express on the back, and MongoDB Atlas for data.</p>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown("**Project Description:**\nA student information system built by our team that lets students and staff manage records, track data and handle tasks in a simple interface. React powered the frontend, Node and Express handled the backend, and MongoDB Atlas stored all data with JWT securing user access.")
    with col2:
        st.markdown("<a class='project-link' href='https://campus-core.onrender.com/login' target='_blank' rel='noopener noreferrer'>Visit Project</a>", unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Project 2: GoldFilmDB
    st.markdown("""
        <div class='project-card'>
            <h3>GoldFilmDB</h3>
            <p>Movies, clear view.</p>
            <p><strong>Tech Stack:</strong> Runs on Spring Boot with MongoDB Atlas, and a React frontend served through Docker on Render.</p>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown("""
            **Project Description:**
            
            A movie platform that lets users browse films, check trailers and share ratings. It uses a Spring Boot backend with MongoDB Atlas and a React frontend, shipped through Docker and deployed on Render.
            
            ⚠️ **Note:** This application may take time to load on first access because the backend 
            and frontend run as separate services on free hosting and may need to spin up.
        """)
    with col2:
        st.markdown("<a class='project-link' href='https://goldfilmdb-zj31.onrender.com/' target='_blank' rel='noopener noreferrer'>Visit Project</a>", unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("### 📋 More Projects Coming Soon")
    st.info("I'm constantly working on new projects. Check back soon for more updates!")
