import streamlit as st

def show():
    """Skills page of the portfolio"""
    
    st.markdown("<h1 class='section-title'>🛠️ Skills</h1>", unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Define skills
    skills_data = {
        "Programming Languages": ["Java", "Python", "C"],
        "Databases": ["SQL"],
        "Data Science & ML": ["Numpy", "Pandas", "Scikit Learn"]
    }
    
    # Display skills by category (centered headings for mobile)
    for category, skills_list in skills_data.items():
        st.markdown(
            f"""
            <div style='text-align: center; margin: 0.5rem 0 0.65rem;'>
                <h3 style='margin: 0; letter-spacing: 0.06em; text-transform: uppercase; font-size: 1.2rem;'>
                    {category}
                </h3>
            </div>
            """,
            unsafe_allow_html=True,
        )
        
        # Create grid layout for skills
        cols = st.columns(len(skills_list) if len(skills_list) <= 3 else 3)
        
        for idx, skill in enumerate(skills_list):
            col_index = idx % len(cols)
            with cols[col_index]:
                st.markdown(f"""
                    <div class='skill-card'>
                        <h4>{skill}</h4>
                    </div>
                """, unsafe_allow_html=True)
        
        st.markdown("")  # Add spacing between categories
    
    st.markdown("---")

    st.markdown(
        """
        <h3 style='text-align: center; margin: 0.25rem 0 1rem; font-size: 1.2rem; letter-spacing: 0.04em;'>
            📚 Learning & Development
        </h3>
        """,
        unsafe_allow_html=True,
    )
    
    # Create 3 equal columns for proper alignment
    learning_cols = st.columns(3)
    
    with learning_cols[0]:
        st.markdown("""
            <div class='skill-card'>
                <h4>🔄 Continuous Learning</h4>
                <p style='font-size: 0.9rem;'>Always exploring new technologies.</p>
            </div>
        """, unsafe_allow_html=True)
    
    with learning_cols[1]:
        st.markdown("""
            <div class='skill-card'>
                <h4>🤝 Collaboration</h4>
                <p style='font-size: 0.9rem;'>Working effectively in team environments</p>
            </div>
        """, unsafe_allow_html=True)
    
    with learning_cols[2]:
        st.markdown("""
            <div class='skill-card'>
                <h4>⚡ Problem Solving</h4>
                <p style='font-size: 0.9rem;'>Tackling complex challenges</p>
            </div>
        """, unsafe_allow_html=True)
