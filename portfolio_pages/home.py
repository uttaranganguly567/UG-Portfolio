import streamlit as st

def show():
    """Home page of the portfolio"""
    
    st.markdown("""
        <div style='text-align: center; padding: 2.5rem 0;'>
            <span class='home-pill'>✨ Information Technology · B.Tech (4th Year)</span>
            <h1 class='hero-title' style='margin: 1.5rem 0 0;'><span class='hero-gradient'>Uttaran Ganguly</span></h1>
            <p class='hero-subtitle' style='margin-top: 0.75rem;'>
                Building intuitive digital experiences with code and curiosity
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### 👋 Welcome")
        st.info(
            "Hi, I’m Uttaran Ganguly."
        )
    
    with col2:
        st.markdown("### 🎓 Education")
        st.info(
            "IT Undergrad at STCET, Kolkata (2022 - Present)."
        )
    
    st.markdown("---")
    
    st.markdown("### 🚀 What I Do")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
            <div class='project-card home-highlight' style='text-align: center;'>
                <h4>💻 Development</h4>
                <p>Build. Refine. Ship.</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div class='project-card home-highlight' style='text-align: center;'>
                <h4>📊 Data Science</h4>
                <p>Learn. Model. Predict.</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
            <div class='project-card home-highlight' style='text-align: center;'>
                <h4>🔧 Problem Solving</h4>
                <p>Think. Plan. Solve.</p>
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
