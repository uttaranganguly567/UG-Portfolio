import streamlit as st

def show():
    """Home page of the portfolio"""
    
    st.markdown("""
        <div style='text-align: center; padding: 2.5rem 0;'>
            <span class='home-pill'>✨ Information Technology · B.Tech (4th Year)</span>
            <h1 class='hero-title' style='margin: 1.5rem 0 0;'>Uttaran Ganguly</h1>
            <p class='hero-subtitle' style='margin-top: 0.75rem;'>
                Building intuitive digital experiences with code and curiosity
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### 👋 Welcome")
        st.markdown("""
            <div class='intro-text'>
                I'm a 4th year B.Tech student in Information Technology at 
                <strong>St. Thomas' College of Engineering and Technology, Kolkata</strong>.
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("### 🎓 Education")
        st.info(
            "**St. Thomas' College of Engineering and Technology, Kolkata**\n\n"
            "B.Tech in Information Technology (4th Year)\n\n"
            "Expected Graduation: 2025"
        )
    
    st.markdown("---")
    
    st.markdown("### 🚀 What I Do")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
            <div class='project-card home-highlight' style='text-align: center;'>
                <h4>💻 Development</h4>
                <p>Building full-stack web applications with modern frameworks</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div class='project-card home-highlight' style='text-align: center;'>
                <h4>📊 Data Science</h4>
                <p>Analyzing data and building predictive models</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
            <div class='project-card home-highlight' style='text-align: center;'>
                <h4>🔧 Problem Solving</h4>
                <p>Writing clean, efficient code and debugging complex issues</p>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("### 📧 Get In Touch")
        st.markdown("[💌 Email Me](mailto:uttaranganguly20@gmail.com)")
    with col2:
        st.markdown("### 🔗 Connect")
        st.markdown("[LinkedIn](https://www.linkedin.com/in/uttaran-ganguly/)")
    with col3:
        st.markdown("### 💼 Professional")
        st.markdown("[GitHub](https://github.com/uttaranganguly567)")
