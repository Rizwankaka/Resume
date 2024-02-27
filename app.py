import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
st.write('''
# Rizwan Rizwan, MSc.
##### *Resume* 
''')

image = Image.open('dp.jpg')
st.image(image, width=150)

st.markdown('## Professional Summary', unsafe_allow_html=True)
st.info('''
- An accomplished Mechanical and Sustainable Energy Engineer with extensive experience in energy systems, mechanical engineering, and data analysis. 
- Proven expertise in project design, execution, and management with a strong background in research and development. 
- Skilled in utilizing advanced software and programming languages for data analysis, machine learning, and AI applications. 
- Demonstrates a strong commitment to sustainability, innovation, and client satisfaction.
''')
#####################
st.markdown('## Personal Information', unsafe_allow_html=True)
st.markdown("""
- **Marital Status:** Married
- **Gender:** Male
- **Date of Birth:** December 24, 1985
""", unsafe_allow_html=True)
#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="#" target="_blank">Rizwan Rizwan</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#projects">Projects</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#skills">Skills</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#contact">Contact</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

#####################
st.markdown('## Education', unsafe_allow_html=True)
st.write('**M.Sc. Sustainable Energy Systems**')
st.write('_Aachen University of Applied Science, Juelich Campus, Germany_ (2010-2014)')
st.write('**B.Eng. Mechanical Engineering**')
st.write('_NED University of Engineering & Technology, Karachi, Pakistan_ (2004-2007)')


#####################
st.markdown('## Professional Experience', unsafe_allow_html=True)

st.write('**Freelance Data Analyst**, `EssayShark` (2022-Present)')
st.markdown("""
- Engaged in Python & R programming, statistical analysis, exploratory data analysis, machine learning, and deep learning projects.
- Expertise in computer vision, OpenCV, generative AI, artificial intelligence, Streamlit web app development, chatbot development, AI image generation, and API integration.
- Proficient in MATLAB, Excel, PowerPoint, and Word for data analysis and presentation.
""")

st.write('**EV Bike Designer & Entrepreneur**, Karachi, Pakistan (2021-2022)')
st.markdown("""
- Designed and marketed eclectic bikes for the Pakistani market, emphasizing sustainable transportation.
""")

st.write('**Founder**,`my Innovative Energy Solutions`, Karachi, Pakistan (2015-2021)')
st.markdown("""
- Specialized in the design and execution of Photovoltaic Systems for various applications, focusing on innovative energy solutions.
""")

st.write('**Project Engineer**, `Diefenbacher GmbH` (2014-2015)')
st.markdown("""
- Led project planning and coordination, focusing on digitalization, advanced plant engineering, operational excellence, and sustainability solutions.
- Ensured compliance with industry standards and QA/QC policies, representing client interests.
""")

st.write('**Research Assistant**, `German Aerospace & Research Center`, Germany (2011-2013)')
st.markdown("""
- Performed modeling and simulation of thermal energy storages using Matlab® for solar thermal power plants and high temperature process heat applications.
""")

st.write('**Project Engineer**, `FND Consulting Engineers`, Karachi, Pakistan (2008-2010)')
st.markdown("""
- Designed and executed HVACR systems, including technical documentation, client interaction, and project management.
""")


#####################
st.markdown('## Projects', unsafe_allow_html=True)

st.markdown("""
<div style="text-align: left;">
    <h3>Highlighted Projects</h3>
    <ul>
        <li>
            <b>Machine Learning Model for Predictive Maintenance:</b> Developed a predictive maintenance model using Python and scikit-learn. The model accurately predicts when industrial equipment will require maintenance.
            <br><a href="https://github.com/Rizwankaka/Predictive-Maintenance-Model" target="_blank"><img src="https://img.shields.io/badge/GitHub-View%20Project-blue?style=for-the-badge&logo=github" alt="GitHub"/></a>
        </li>
        <li>
            <b>Energy Consumption Forecasting:</b> Utilized time series analysis and machine learning to forecast energy consumption for commercial buildings, improving energy planning and cost savings.
            <br><a href="https://kaggle.com/rizwankaka/energy-consumption-forecasting" target="_blank"><img src="https://img.shields.io/badge/Kaggle-View%20Project-20BEFF?style=for-the-badge&logo=kaggle" alt="Kaggle"/></a>
        </li>
    </ul>
</div>
""", unsafe_allow_html=True)



#####################
st.markdown('## Skills', unsafe_allow_html=True)

st.markdown("""
- **Engineering Software:** Auto-CAD, Pro-E/Creo, Solid Edge ST7, Solid Works 2015, CATIA V5, ANSYS 14, Siemens NX 7.5
- **Data Science Simulation & Programming:** Python, R, SQL, Matlab/Simulink, Power BI, Tableue
- **Project Management & Design:** MS-Office, MS-Visio, MS-Project, Asana, Smart Draw, Primavera
- **Digital Literacy:** SEO, Digital Marketing, WordPress, E-commerce, Graphic Design
- **Other Tools:** Mendeley, Xpert, Origin, Photoshop, CorelDraw, Adobe Premiere, Camtasia Studio
""", unsafe_allow_html=True)
#####################
# st.markdown('''
# ## Certifications
# '''
# I have many certifications in the field of DataScience, Machine Learning, AI, and Python. will provide on demand
# ''')

#####################
st.markdown('''
## Languages
''')

txt4('Urdu-Punjabi-Hindi', 'Native', 'Professional working proficiency')
txt4('English', 'Expert', 'Professional working proficiency')
txt4('German', 'Intermediate', 'Limited working proficiency')

#####################
st.markdown('## Interests')
st.markdown("""
- Passionate about sustainable technical projects <br>
- Travelling, hiking, cycling & photography <br>
- Reading, documentaries <br>
- Sports <br>
- Enjoys cooking and social work
""", unsafe_allow_html=True)

#####################
st.markdown('## Contact', unsafe_allow_html=True)

st.markdown("""
<div style="text-align: left;">
    <p><b>Author:</b> Rizwan</p>
    <p>
        <a href="https://github.com/Rizwankaka" target="_blank"><img src="https://img.shields.io/badge/GitHub-Profile-blue?style=for-the-badge&logo=github" alt="GitHub"/></a>
    </p>
    <p>
        <a href="https://www.linkedin.com/in/rizwan-rizwan-1351a650/" target="_blank"><img src="https://img.shields.io/badge/LinkedIn-Profile-blue?style=for-the-badge&logo=linkedin" alt="LinkedIn"/></a>
    </p>
    <p>
        <a href="https://twitter.com/RizwanRizwan_" target="_blank"><img src="https://img.shields.io/badge/Twitter-Profile-blue?style=for-the-badge&logo=twitter" alt="Twitter"/></a>
    </p>
    <p>
        <a href="https://www.facebook.com/RIZWANNAZEEER" target="_blank"><img src="https://img.shields.io/badge/Facebook-Profile-blue?style=for-the-badge&logo=facebook" alt="Facebook"/></a>
    </p>
    <p>
        <a href="mailto:riwan.rewala@gmail.com" target="_blank"><img src="https://img.shields.io/badge/Gmail-Contact%20Me-red?style=for-the-badge&logo=gmail" alt="Gmail"/></a>
    </p>
</div>
""", unsafe_allow_html=True)





