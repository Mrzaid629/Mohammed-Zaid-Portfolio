```python
import streamlit as st

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Mohammed Zaid | AI & Data Science",
    page_icon="🤖",
    layout="wide"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

.stApp {
    background-color: #0e1117;
    color: white;
}

.main-title {
    font-size: 55px;
    font-weight: 800;
    margin-bottom: 5px;
}

.subtitle {
    font-size: 24px;
    color: #58a6ff;
    margin-bottom: 20px;
}

.section-title {
    font-size: 36px;
    font-weight: 700;
    margin-top: 20px;
    margin-bottom: 25px;
}

.summary-box {
    background-color: #161b22;
    padding: 25px;
    border-radius: 15px;
    border: 1px solid #30363d;
    line-height: 1.7;
    margin-bottom: 25px;
}

.card {
    background-color: #161b22;
    padding: 22px;
    border-radius: 15px;
    border: 1px solid #30363d;
    margin-bottom: 20px;
}

.project-title {
    font-size: 25px;
    font-weight: 700;
    color: #58a6ff;
}

.skill {
    display: inline-block;
    background-color: #21262d;
    padding: 8px 15px;
    margin: 5px;
    border-radius: 20px;
    border: 1px solid #30363d;
}

.footer {
    text-align: center;
    color: #8b949e;
    margin-top: 50px;
    padding: 25px;
    border-top: 1px solid #30363d;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# PROJECT DATABASE
# =========================================================
#
# TO ADD A FUTURE PROJECT:
# Copy one project block and change the information.
#
# =========================================================

projects = [

    {
        "title": "Bitcoin Volatility Prediction Using Historical Data",
        "icon": "₿",
        "description": (
            "A machine learning project that analyzes historical Bitcoin "
            "price data and predicts volatility using statistical and "
            "deep learning approaches."
        ),
        "technologies": (
            "Python, Pandas, NumPy, ARCH/GARCH, "
            "TensorFlow, Keras, LSTM, Matplotlib, Jupyter Notebook"
        ),
        "details": [
            "Collected and analyzed historical Bitcoin price data.",
            "Calculated historical and EWMA volatility.",
            "Applied GARCH models for volatility analysis.",
            "Applied LSTM for volatility prediction.",
            "Evaluated prediction performance using RMSE and MAPE."
        ],
        "github": "",
        "demo": ""
    },

    {
        "title": "Exploratory Data Analysis on Various Datasets",
        "icon": "📊",
        "description": (
            "A collection of exploratory data analysis work involving "
            "data cleaning, statistical analysis, visualization and "
            "feature analysis."
        ),
        "technologies": (
            "Python, Pandas, NumPy, Matplotlib, "
            "Seaborn, Scikit-learn, Jupyter Notebook"
        ),
        "details": [
            "Data cleaning and preprocessing.",
            "Statistical analysis.",
            "Data visualization.",
            "Correlation analysis.",
            "Outlier detection.",
            "Feature analysis."
        ],
        "github": "",
        "demo": ""
    },

    {
        "title": "Used Cars Data Analysis & EDA",
        "icon": "🚗",
        "description": (
            "An exploratory data analysis and preprocessing project "
            "performed on a used-car dataset."
        ),
        "technologies": (
            "Python, Pandas, NumPy, Matplotlib, "
            "Seaborn, Jupyter Notebook"
        ),
        "details": [
            "Missing-value analysis.",
            "Duplicate-value handling.",
            "Categorical data cleaning and standardization.",
            "Used-car brand analysis.",
            "Fuel-type analysis.",
            "Univariate analysis.",
            "Bivariate analysis.",
            "Multivariate analysis.",
            "km_driven distribution analysis.",
            "Correlation analysis.",
            "Correlation heatmap.",
            "Outlier detection.",
            "Outlier removal using the IQR method.",
            "Removing unwanted columns.",
            "Datatype conversion.",
            "One-hot encoding."
        ],
        "github": (
            "https://github.com/Mrzaid629/"
            "Mohammed-Zaid-Portfolio/blob/main/used_cars_eda.ipynb"
        ),
        "demo": ""
    },

    {
        "title": "VGGVision – Animal Classification Using VGG16",
        "icon": "🐻",
        "description": (
            "A deep learning project using VGG16 transfer learning "
            "to classify animal images into five different classes."
        ),
        "technologies": (
            "Python, TensorFlow, Keras, VGG16, "
            "Deep Learning, Streamlit"
        ),
        "details": [
            "Used VGG16 transfer learning.",
            "Created an animal image classification model.",
            "Classified Bear, Bull, Camel, Cats and Cattle.",
            "Achieved approximately 86% validation accuracy.",
            "Created an interactive Streamlit application."
        ],
        "github": (
            "https://github.com/Mrzaid629/"
            "VGGVision-Animal-Classification.git"
        ),
        "demo": ""
    },

    {
        "title": "Text Steganography Using Innocuous Text Generation",
        "icon": "🔐",
        "description": (
            "An interactive text steganography application that "
            "hides information inside innocuous-looking text."
        ),
        "technologies": (
            "Python, Streamlit, Text Steganography, "
            "Data Security and Privacy"
        ),
        "details": [
            "Developed as part of Data Security and Privacy.",
            "Provides an interactive interface.",
            "Demonstrates the concept of hiding information in text.",
            "Deployed as a Streamlit web application."
        ],
        "github": "",
        "demo": (
            "https://text-steganography-749sjesjyvjpm2su3yyesd."
            "streamlit.app/"
        )
    },

    {
        "title": "Generative AI Urban City Planning",
        "icon": "🏙️",
        "description": (
            "A final-year major project focused on using Generative AI "
            "and data-driven approaches for urban planning in Tumkur."
        ),
        "technologies": (
            "Python, Artificial Intelligence, Generative AI, "
            "Machine Learning, Data Analysis, Satellite Imagery"
        ),
        "details": [
            "Waste and undeveloped land analysis.",
            "Best-use recommendations for undeveloped areas.",
            "Traffic planning.",
            "Hospital connectivity analysis.",
            "Satellite imagery analysis.",
            "Urban development analysis."
        ],
        "github": "",
        "demo": ""
    }

]


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("🤖 Mohammed Zaid")

page = st.sidebar.radio(
    "Navigation",
    [
        "Home",
        "About Me",
        "Education",
        "Skills",
        "Projects",
        "Achievements",
        "Contact"
    ]
)

st.sidebar.markdown("---")

st.sidebar.info(
    "AI & Data Science Student\n\n"
    "Python • Machine Learning • Data Analysis"
)


# =========================================================
# HOME
# =========================================================

if page == "Home":

    st.markdown(
        '<div class="main-title">Mohammed Zaid</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">AI & Data Science Student</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="summary-box">

    AI and Data Science student with a strong foundation in Python and
    Machine Learning. Familiar with data preprocessing, exploratory data
    analysis, model development, and data visualization. Hands-on experience
    working on academic projects involving machine learning and real-world
    datasets. A quick learner with an interest in applying AI and data-driven
    techniques to solve practical problems.

    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Projects", f"{len(projects)}+")

    with col2:
        st.metric("CGPA", "6.75")

    with col3:
        st.metric("Python", "✓")

    with col4:
        st.metric("Machine Learning", "✓")

    st.markdown("---")

    st.markdown(
        '<div class="section-title">Featured Projects</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    for index, project in enumerate(projects[:2]):

        column = col1 if index == 0 else col2

        with column:

            st.markdown(
                f"""
                <div class="card">

                <div class="project-title">
                {project["icon"]} {project["title"]}
                </div>

                <p>
                {project["description"]}
                </p>

                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown("---")

    # Resume download

    try:

        with open("resume.pdf", "rb") as file:

            resume_data = file.read()

        st.download_button(
            label="📄 Download My Resume",
            data=resume_data,
            file_name="Mohammed_Zaid_Resume.pdf",
            mime="application/pdf"
        )

    except FileNotFoundError:

        st.warning(
            "resume.pdf was not found. Please keep resume.pdf "
            "in the same folder as app.py."
        )


# =========================================================
# ABOUT ME
# =========================================================

elif page == "About Me":

    st.markdown(
        '<div class="section-title">About Me</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="summary-box">

    I am Mohammed Zaid, an Artificial Intelligence and Data Science student
    interested in Python, Machine Learning, Data Analysis and Artificial
    Intelligence.

    I enjoy working with real-world datasets, understanding patterns in data,
    building machine learning projects and creating practical applications.

    My goal is to continue improving my technical skills and use AI and
    data-driven techniques to solve real-world problems.

    </div>
    """, unsafe_allow_html=True)

    st.subheader("Areas of Interest")

    interests = [
        "Artificial Intelligence",
        "Machine Learning",
        "Data Science",
        "Exploratory Data Analysis",
        "Deep Learning",
        "Generative AI",
        "Data Visualization",
        "Python Development"
    ]

    for interest in interests:

        st.markdown(
            f'<span class="skill">{interest}</span>',
            unsafe_allow_html=True
        )


# =========================================================
# EDUCATION
# =========================================================

elif page == "Education":

    st.markdown(
        '<div class="section-title">Education</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="card">

    <h3>
    🎓 Bachelor of Technology – Artificial Intelligence & Data Science
    </h3>

    <p>
    <b>Channabasaweshwara Institute of Technology, Tumkur</b>
    </p>

    <p>
    CGPA: <b>6.75</b>
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">

    <h3>
    🎓 Diploma – Electronics & Communication Engineering
    </h3>

    <p>
    <b>GPT Tumkur</b>
    </p>

    <p>
    CGPA: <b>7.1</b>
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">

    <h3>📚 SSLC</h3>

    <p>
    Percentage: <b>88.16%</b>
    </p>

    </div>
    """, unsafe_allow_html=True)


# =========================================================
# SKILLS
# =========================================================

elif page == "Skills":

    st.markdown(
        '<div class="section-title">Skills</div>',
        unsafe_allow_html=True
    )

    st.subheader("Technical Skills")

    skills = [
        "Python",
        "Machine Learning",
        "Pandas",
        "NumPy",
        "Scikit-learn",
        "Exploratory Data Analysis",
        "Matplotlib",
        "Seaborn",
        "Power BI",
        "Tableau",
        "Streamlit",
        "TensorFlow",
        "Keras",
        "Basic Robotics"
    ]

    for skill in skills:

        st.markdown(
            f'<span class="skill">{skill}</span>',
            unsafe_allow_html=True
        )


# =========================================================
# PROJECTS
# =========================================================

elif page == "Projects":

    st.markdown(
        '<div class="section-title">My Projects</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Here are my academic, machine learning, "
        "data analysis and AI projects."
    )

    st.markdown("---")

    # Automatically display every project
    # from the projects list.

    for project in projects:

        with st.expander(
            f'{project["icon"]} {project["title"]}',
            expanded=False
        ):

            st.subheader(project["title"])

            st.write(project["description"])

            st.markdown("### 🛠️ Technologies")

            st.write(project["technologies"])

            st.markdown("### 📌 Project Details")

            for detail in project["details"]:

                st.markdown(f"- {detail}")

            # GitHub and Demo buttons

            if project["github"] or project["demo"]:

                st.markdown("---")

                col1, col2 = st.columns(2)

                if project["github"]:

                    with col1:

                        st.link_button(
                            "💻 View GitHub",
                            project["github"]
                        )

                if project["demo"]:

                    with col2:

                        st.link_button(
                            "🚀 Live Demo",
                            project["demo"]
                        )


# =========================================================
# ACHIEVEMENTS
# =========================================================

elif page == "Achievements":

    st.markdown(
        '<div class="section-title">Achievements</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="card">

    <h3>🏆 Runner-Up – YUKTI 2K26 Robotics Event</h3>

    <p>
    Secured Runner-Up position in the YUKTI 2K26 Robotics Event,
    demonstrating teamwork, problem-solving and robotics skills.
    </p>

    </div>
    """, unsafe_allow_html=True)


# =========================================================
# CONTACT
# =========================================================

elif page == "Contact":

    st.markdown(
        '<div class="section-title">Contact</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="card">

    <h3>📱 Mobile</h3>

    <p>
    +91-8618879166
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">

    <h3>💻 GitHub</h3>

    <p>
    My GitHub profile contains my projects and source code.
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.link_button(
        "💻 Open GitHub Profile",
        "https://github.com/Mrzaid629"
    )


# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<div class="footer">

© 2026 Mohammed Zaid | AI & Data Science

<br><br>

Built with Python & Streamlit 🤖

</div>
""", unsafe_allow_html=True)
```
