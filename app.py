import streamlit as st
import uuid
from streamlit_option_menu import option_menu
import home, analyzer, builder, dashboard, tips, job, feedback, about, history
import db

st.set_page_config(page_title="ResuTrack AI", layout="wide")
# --- PERSISTENT SESSION ID ---
# Stored in the URL as ?sid=xxxx so it survives a page refresh (as long as the
# URL is kept/bookmarked). This is what lets scan history persist per-user
# without needing a full login system, while still keeping each user's data
# separate from everyone else's in the SQLite database.
if "sid" not in st.query_params:
    new_sid = str(uuid.uuid4())[:12]
    st.query_params["sid"] = new_sid
    st.session_state.session_id = new_sid
else:
    st.session_state.session_id = st.query_params["sid"]


if 'latest_analysis' not in st.session_state:
    st.session_state.latest_analysis = None
if 'nav_to' not in st.session_state:
    st.session_state.nav_to = None
    #db.init_db()

# --- GLOBAL NEON CSS ---
st.markdown("""
    <style>
    .stApp { background-color: #05070a !important; color: white; font-family: 'Inter', sans-serif; }

    [data-testid="stSidebar"] { 
        background-color: #05070a !important;border-right: 2px solid #00d4ff; box-shadow: 5px 0 15px rgba(0, 212, 255, 0.2);
    }
    .nav-link {
        color: white !important;font-family: 'Rajdhani', sans-serif; text-transform: uppercase; letter-spacing: 1px; transition: 0.3s !important;
    }
    .nav-link:hover {
        color: #00d4ff !important; text-shadow: 0 0 10px #00d4ff;
    }
    .nav-link-selected {
        background-color: rgba(0, 212, 255, 0.1) !important; border-left: 4px solid #00d4ff !important;
        color: #00d4ff !important; text-shadow: 0 0 15px #00d4ff;
    }
    .sidebar-title {
        text-align: center; font-family: 'Orbitron', sans-serif; font-size: 1.8rem; margin-bottom: 20px;
          background: linear-gradient(90deg, #00d4ff, #ffffff, #00d4ff);background-size: 200% auto;
        -webkit-background-clip: text; -webkit-text-fill-color: transparent; animation: shimmerTitle 3s linear infinite;
    }
    @keyframes shimmerTitle {
        0% { background-position: 0% center; }
        100% { background-position: 200% center; }
    }
div.stButton>button
{
background:linear-gradient(135deg,#00d4ff 0%,#0080ff 50%, #00d4ff 100%) !important;
        background-size: 200% auto !important;  color: white !important;  border-radius: 12px !important;
        padding: 10px 20px !important;  font-weight: bold !important;
        font-size: 0.9rem !important;  border: none !important;  box-shadow: 0 4px 20px rgba(0, 212, 255, 0.4) !important;
        transition: all 0.35s cubic-bezier(0.25, 0.8, 0.25, 1) !important;
    }
    div.stButton > button:hover {
        background-position: right center !important; transform: scale(1.06) translateY(-3px) !important; box-shadow: 0 8px 30px rgba(0, 212, 255, 0.7) !important;
    }
    div.stButton > button:active {
        transform: scale(0.98) !important;
    }
    </style>
""", unsafe_allow_html=True)

PAGE_LIST = ["Home", "Resume Analyzer", "Resume Generator", "Analytics Dashboard",  "Career Roadmap", "Job Radar","Resume History","About"]

# --- NAV_TO FIX ---
if st.session_state.nav_to is not None:
    if st.session_state.nav_to in PAGE_LIST:
        st.session_state['menu_key'] = st.session_state.nav_to
    st.session_state.nav_to = None

# sidebar nav
with st.sidebar:
    st.markdown("<h2 class='sidebar-title'> AI Resume Hub</h2>", unsafe_allow_html=True)

    selected = option_menu(
        None, 
        PAGE_LIST,
        icons=['house', 'cpu', 'file-earmark-plus', 'speedometer2', 'clock-history', 'lightbulb', 'search','info-circle'],
        menu_icon="cast", 
        key='menu_key',
        styles={
            "container": {"padding": "0!important", "background-color": "transparent"},
            "icon": {"color": "#00d4ff", "font-size": "1.2rem"},
            "nav-link": {
                "font-size": "1rem",  "text-align": "left", "margin": "5px", "--hover-color": "rgba(0, 212, 255, 0.15)"
            },
            "nav-link-selected": {"background-color": "rgba(0, 212, 255, 0.2)"},
        })

# --- ROUTING ---
if selected == "Home":
    home.show_home()
elif selected == "Resume Analyzer":
    analyzer.show_analyzer()
elif selected == "Resume Generator":
    builder.show_builder()
elif selected == "Analytics Dashboard":
    dashboard.show_dashboard()
elif selected == "Career Roadmap":
    tips.show_tips()
elif selected == "Job Radar":
    job.show_jobs()
elif selected == "Resume History":
    history.show_history()
elif selected == "About":
    about.show_about()