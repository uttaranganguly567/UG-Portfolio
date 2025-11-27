import streamlit as st

def show():
    """Projects page of the portfolio"""
    
    st.markdown("<h1 class='section-title'>🚀 Projects</h1>", unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Project 1: Campus Core
    st.markdown("""
        <div class='project-card'>
            <h3>Campus Core</h3>
            <p>A comprehensive campus management system designed to streamline student and faculty interactions.</p>
            <p><strong>Tech Stack:</strong> Full-Stack Web Application</p>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown("**Project Description:**\nA platform for managing campus activities, events, and communications.")
    with col2:
        st.markdown("<a class='project-link' href='https://campus-core.onrender.com/login' target='_blank' rel='noopener noreferrer'>Visit Project</a>", unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Project 2: GoldFilmDB
    st.markdown("""
        <div class='project-card'>
            <h3>GoldFilmDB</h3>
            <p>A movie database application that allows users to browse, search, and explore film information.</p>
            <p><strong>Tech Stack:</strong> Full-Stack Web Application (Microservices)</p>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown("""
            **Project Description:**
            
            A distributed movie database with separate frontend and backend services. 
            The application showcases microservices architecture with independent scaling capabilities.
            
            ⚠️ **Note:** This application may take time to load on first access because the backend 
            and frontend run as separate services on free hosting and may need to spin up.
        """)
    with col2:
        st.markdown("<a class='project-link' href='https://goldfilmdb-zj31.onrender.com/' target='_blank' rel='noopener noreferrer'>Visit Project</a>", unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("### 📋 More Projects Coming Soon")
    st.info("I'm constantly working on new projects. Check back soon for more updates!")
