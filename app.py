import streamlit as st

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Mohammed Zaid | AI & Data Science",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

    /* Main page */
    .stApp {
        background-color: #0e1117;
    }

    .block-container {
        max-width: 1200px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    /* Name */
    .name {
        font-size: 52px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    /* Subtitle */
    .subtitle {
        font-size: 24px;
        color: #58a6ff;
        margin-bottom: 20px;
    }

    /* Summary box */
    .summary-box {
        background-color: #161b22;
        border-left: 4px solid #58a6ff;
        padding: 25px;
        border-radius: 12px;
        line-height: 1.8;
        font-size: 17px;
        margin-top: 20px;
        margin-bottom: 30px;
    }

    /* Section title */
    .section-title {
        font-size: 30px;
        font-weight: 700;
        margin-top: 35px;
        margin-bottom: 20px;
    }

    /* Project card */
    .project-card {
        background-color: #161b22;
        border: 1px solid #30363d;
        padding: 25px;
        border-radius: 15px;
        margin-bottom: 20px;
    }

    .project-card h3 {
        color: #58a6ff;
    }

    /* Skill tags */
    .skill {
        display: inline-block;
        background-color: #1f2937;
        border: 1px solid #374151;
        color: #93c5fd;
        padding: 8px 14px;
        border-radius: 20px;
        margin: 5px;
        font-size: 15px;
    }

    /* Education card */
    .education-card {
        background-color: #161b22;
        border: 1px solid #30363d;
        padding: 22px;
        border-radius: 15px;
        margin-bottom: 20px;
    }

    /* Contact */
    .contact-card {
        background-color: #161b22;
        border: 1px solid #30363d;
        padding: 25px;
        border-radius: 15px;
        text-align: center;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #6b7280;
        padding: 30px;
        margin-top: 50px;
    }

</style>
""", unsafe_allow_html=True)


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.title("💻 Mohammed Zaid")

    st.markdown("---")

    st.markdown("### Navigation")

    page = st.radio(
        "Select Section",
        [
            "🏠 Home",
            "👨‍💻 About Me",
            "🎓 Education",
            "🛠️ Skills",
            "🚀 Projects",
            "🏆 Achievements",
            "📞 Contact"
        ]
    )

    st.markdown("---")

    st.markdown("### AI & Data Science")

    st.write(
        "Python • Machine Learning • Data Analysis"
    )


# =========================================================
# HOME
# =========================================================

if page == "🏠 Home":

    # Name
    st.markdown(
        '<div class="name">Mohammed Zaid</div>',
        unsafe_allow_html=True
    )

    # Role
    st.markdown(
        '<div class="subtitle">AI & Data Science Student</div>',
        unsafe_allow_html=True
    )

    # Summary
    st.markdown(
        '<div class="summary-box">'
        '<b>About Me</b><br><br>'
        'AI and Data Science student with a strong foundation in '
        'Python and Machine Learning. Familiar with data preprocessing, '
        'exploratory data analysis, model development, and data visualization. '
        'Hands-on experience working on academic projects involving machine '
        'learning and real-world datasets. A quick learner with an interest '
        'in applying AI and data-driven techniques to solve practical problems.'
        '</div>',
        unsafe_allow_html=True
    )

    # Quick information
    st.markdown(
        '<div class="section-title">🚀 Quick Overview</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Projects", "5+")

    with col2:
        st.metric("CGPA", "6.75")

    with col3:
        st.metric("Python", "✓")

    with col4:
        st.metric("Machine Learning", "✓")

    # Featured Projects
    st.markdown(
        '<div class="section-title">🚀 Featured Projects</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:

        st.markdown(
            '<div class="project-card">'
            '<h3>🐾 VGGVision</h3>'
            '<p>'
            'Animal classification using VGG16 transfer learning '
            'with an interactive Streamlit interface.'
            '</p>'
            '</div>',
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            '<div class="project-card">'
            '<h3>🔐 Text Steganography</h3>'
            '<p>'
            'Interactive text steganography application built '
            'with Python and Streamlit.'
            '</p>'
            '</div>',
            unsafe_allow_html=True
        )

    # Resume
    st.markdown(
        '<div class="section-title">📄 Resume</div>',
        unsafe_allow_html=True
    )

    try:

        with open("resume.pdf", "rb") as file:
            resume_data = file.read()

        st.download_button(
            label="📥 Download My Resume",
            data=resume_data,
            file_name="Mohammed_Zaid_Resume.pdf",
            mime="application/pdf"
        )

    except FileNotFoundError:

        st.warning(
            "resume.pdf was not found. "
            "Place your resume.pdf in the same folder as app.py."
        )


# =========================================================
# ABOUT ME
# =========================================================

elif page == "👨‍💻 About Me":

    st.markdown(
        '<div class="section-title">👨‍💻 About Me</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="summary-box">'
        'AI and Data Science student with a strong foundation in '
        'Python and Machine Learning. Familiar with data preprocessing, '
        'exploratory data analysis, model development, and data visualization. '
        'Hands-on experience working on academic projects involving machine '
        'learning and real-world datasets. A quick learner with an interest '
        'in applying AI and data-driven techniques to solve practical problems.'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown("### 🎯 Areas of Interest")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info("🤖 Artificial Intelligence")

    with col2:
        st.info("📊 Data Science")

    with col3:
        st.info("🧠 Machine Learning")


# =========================================================
# EDUCATION
# =========================================================

elif page == "🎓 Education":

    st.markdown(
        '<div class="section-title">🎓 Education</div>',
        unsafe_allow_html=True
    )

    # B.Tech
    st.markdown(
        '<div class="education-card">'
        '<h3>🎓 Bachelor of Technology</h3>'
        '<h4>Artificial Intelligence and Data Science</h4>'
        '<p><b>Channabasaweshwara Institute of Technology, Tumkur</b></p>'
        '<p>CGPA: <b>6.75</b></p>'
        '</div>',
        unsafe_allow_html=True
    )

    # Diploma
    st.markdown(
        '<div class="education-card">'
        '<h3>🎓 Diploma</h3>'
        '<h4>Electronics and Communication Engineering</h4>'
        '<p><b>GPT Tumkur</b></p>'
        '<p>CGPA: <b>7.1</b></p>'
        '</div>',
        unsafe_allow_html=True
    )

    # SSLC
    st.markdown(
        '<div class="education-card">'
        '<h3>📚 SSLC</h3>'
        '<p>Percentage: <b>88.16%</b></p>'
        '</div>',
        unsafe_allow_html=True
    )


# =========================================================
# SKILLS
# =========================================================

elif page == "🛠️ Skills":

    st.markdown(
        '<div class="section-title">🛠️ Technical Skills</div>',
        unsafe_allow_html=True
    )

    skills = [
        "🐍 Python",
        "🤖 Machine Learning",
        "🐼 Pandas",
        "🔢 NumPy",
        "🧠 Scikit-learn",
        "📊 Exploratory Data Analysis",
        "📈 Matplotlib",
        "📉 Seaborn",
        "📊 Power BI",
        "📊 Tableau",
        "🚀 Streamlit",
        "🤖 Basic Robotics"
    ]

    for skill in skills:

        st.markdown(
            f'<span class="skill">{skill}</span>',
            unsafe_allow_html=True
        )


# =========================================================
# PROJECTS
# =========================================================

elif page == "🚀 Projects":

    st.markdown(
        '<div class="section-title">🚀 My Projects</div>',
        unsafe_allow_html=True
    )

    # -----------------------------------------------------
    # BITCOIN
    # -----------------------------------------------------

    with st.expander(
        "₿ Bitcoin Volatility Prediction Using Historical Data",
        expanded=True
    ):

        st.markdown("### 📌 Project Description")

        st.write(
            "Collected and analyzed historical Bitcoin price data, "
            "calculated volatility using historical and EWMA methods, "
            "and applied GARCH and LSTM models for volatility prediction."
        )

        st.markdown("### 🛠️ Technologies")

        st.code(
            "Python | Pandas | NumPy | ARCH/GARCH | "
            "TensorFlow/Keras | LSTM | Matplotlib | Jupyter Notebook",
            language="text"
        )

        st.markdown("### 📊 Evaluation")

        st.write("• RMSE")
        st.write("• MAPE")


    # -----------------------------------------------------
    # EDA
    # -----------------------------------------------------

    with st.expander(
        "📊 Exploratory Data Analysis on Various Datasets"
    ):

        st.markdown("### 📌 Project Description")

        st.write(
            "Performed data cleaning, preprocessing, statistical analysis, "
            "visualization, correlation analysis, outlier detection, "
            "and feature analysis on various datasets."
        )

        st.markdown("### 🛠️ Technologies")

        st.code(
            "Python | Pandas | NumPy | Matplotlib | "
            "Seaborn | Scikit-learn | Jupyter Notebook",
            language="text"
        )

        st.markdown("### 🔎 Key Areas")

        st.write("• Data Cleaning")
        st.write("• Data Preprocessing")
        st.write("• Statistical Analysis")
        st.write("• Data Visualization")
        st.write("• Correlation Analysis")
        st.write("• Outlier Detection")
        st.write("• Feature Analysis")


    # -----------------------------------------------------
    # VGGVISION
    # -----------------------------------------------------

    with st.expander(
        "🐾 VGGVision – Animal Classification Using VGG16"
    ):

        st.markdown("### 📌 Project Description")

        st.write(
            "A deep learning image classification project using "
            "VGG16 transfer learning. The model classifies animal "
            "images into multiple classes and is connected to an "
            "interactive Streamlit interface."
        )

        st.markdown("### 🛠️ Technologies")

        st.code(
            "Python | TensorFlow | Keras | VGG16 | "
            "Deep Learning | Streamlit",
            language="text"
        )

        st.markdown("### 📊 Model Performance")

        st.success(
            "Approximately 86% validation accuracy."
        )

        st.markdown("### 🌐 Application")

        st.write(
            "The project has been deployed as a Streamlit web application."
        )


    # -----------------------------------------------------
    # TEXT STEGANOGRAPHY
    # -----------------------------------------------------

    with st.expander(
        "🔐 Text Steganography"
    ):

        st.markdown("### 📌 Project Description")

        st.write(
            "An interactive text steganography application that "
            "provides a web interface for hiding and extracting "
            "secret information within text."
        )

        st.markdown("### 🛠️ Technologies")

        st.code(
            "Python | Streamlit | Text Steganography",
            language="text"
        )

        st.markdown("### 🌐 Live Demo")

        st.link_button(
            "🚀 Open Text Steganography",
            "https://text-steganography-749sjesjyvjpm2su3yyesd.streamlit.app/"
        )


    # -----------------------------------------------------
    # GENERATIVE AI CITY PLANNING
    # -----------------------------------------------------

    with st.expander(
        "🏙️ Generative AI Urban City Planning"
    ):

        st.markdown("### 📌 Final-Year Major Project")

        st.write(
            "Generative AI based urban city planning project "
            "focused on practical urban-development problems "
            "in Tumkur."
        )

        st.markdown("### 🎯 Planned Areas")

        st.write("• Waste and undeveloped land analysis")
        st.write("• Best-use recommendations")
        st.write("• Traffic-related planning")
        st.write("• Hospital connectivity")
        st.write("• Satellite image analysis")

        st.markdown("### 🛠️ Technologies")

        st.code(
            "Python | Artificial Intelligence | Machine Learning | "
            "Generative AI | Satellite Imagery",
            language="text"
        )


# =========================================================
# ACHIEVEMENTS
# =========================================================

elif page == "🏆 Achievements":

    st.markdown(
        '<div class="section-title">🏆 Achievements</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="project-card">'
        '<h3>🥈 Runner-Up – YUKTI 2K26 Robotics Event</h3>'
        '<p>'
        'Secured Runner-Up position in the YUKTI 2K26 Robotics Event, '
        'demonstrating teamwork, problem-solving, and robotics skills.'
        '</p>'
        '</div>',
        unsafe_allow_html=True
    )


# =========================================================
# CONTACT
# =========================================================

elif page == "📞 Contact":

    st.markdown(
        '<div class="section-title">📞 Contact Me</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:

        st.markdown(
            '<div class="contact-card">'
            '<h3>📱 Mobile</h3>'
            '<p>+91-8618879166</p>'
            '</div>',
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            '<div class="contact-card">'
            '<h3>📧 Email</h3>'
            '<p>Available in my resume</p>'
            '</div>',
            unsafe_allow_html=True
        )

    st.markdown("")

    st.info(
        "LinkedIn and GitHub links can be added here."
    )


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    '<div class="footer">'
    '© 2026 Mohammed Zaid | AI & Data Science'
    '</div>',
    unsafe_allow_html=True
)