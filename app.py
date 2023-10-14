from pathlib import Path
import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Curriculum vitae Yash.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Yash Upadhyay"
PAGE_ICON = ":wave:"
NAME = "Yash Upadhyay"
DESCRIPTION = """
Aircraft Maintenance Engineer, assisting organization by supporting for technical records.
"""
EMAIL = "yash.upadhyay@protonmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://linkedin.com/in/yashsupadhyay",
    "GitHub": "https://github.com/yashsupadhyay",
    "Twitter": "https://x.com/yashsupadhyay",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ 5 Year 7 Months expereince extracting actionable insights from data
- ✔️ Strong hands on experience and knowledge in Technical Documents and Microsoft Apps
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 🛩️ Aircrfat Maintenance
- 📊 Data Visulization: PowerBi, MS Excel
- ✈️ Technical Documents
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Senior Engineer - Technical Records | FLYdocs India Pvt Ltd.**")
st.write("2021 - Present")
st.write(
    """
- ► Perform multiple tasks within company helping engineers of auditing work of Maintenance documents. Explore new projects like build & audit and help to produce good Productivity.

    """
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Engineer - Technical Records | FLYdocs India Pvt Ltd.**")
st.write("2019 - 2021")
st.write(
    """
- ► Handling of project of DEAS for VAA. Explore new areas of work within company. Had fulfil new Responsibilities as an engineer of technical records in Build & Audit of A/C and Top-ups of A/C.

    """
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Technical Records Assistant | FLYdocs India Pvt Ltd.**")
st.write("2018 - 2019")
st.write(
    """
- ► Responsibility of handling team for auditing Technical Records. Prepare monthly Report for technical records. Provide training for new joined employees and prepare Training material for training purpose. Data entry and export reports in various types Of maintenance software's.
"""
)

# --- JOB 4
st.write('\n')
st.write("🚧", "**Aircraft Technician | Saraya Aviation Pvt Ltd.**")
st.write("2015 - 2016")
st.write(
    """
- ► Responsibility of daily inspection, perform checks of Piper Seneca V, PA34-220T Ensure aircraft safety and airworthy condition of aircraft. Maintain all maintenance Records as per DGCA guidelines. Worked on continental LTSIO/TSIO360RB Engine, Landing Gear, Airframe and navigation system.
"""
)

# --- JOB 5
st.write('\n')
st.write("🚧", "**Trainee Technician | Wings Aviation Pvt Ltd.**")
st.write("2009 - 2012")
st.write(
    """
- ► Worked on Cessna 152 fitted with Lycoming 0-235 N2C and L2C Engine and perform Maintenance operation task. Worked on Cessna 172R/S fitted with Lycoming I0-360-L2A and perform Maintenance operation task. And worked on GARMIN G1000 fitted in aircraft. Worked on P68 Multi Engine fitted with Lycoming I0-360-A1B6 and perform Maintenance operation task.
"""
)
