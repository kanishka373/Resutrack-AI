import streamlit as st
def show_home():

    st.markdown("""
        <style>
        .stApp { background-color: #030508; color: white; }
        
        @keyframes fadeInUp {
            from { opacity: 0; transform: translateY(30px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .hero-section {
            text-align: center; padding: 40px 20px; animation: fadeInUp 0.8s ease-out;
        }
        .main-title {
         font-size: 3.5rem; font-weight: 800; color: #00d4ff !important; text-shadow: 0 0 25px rgba(0, 212, 255, 0.6);
            margin-bottom: 10px; font-family: 'Orbitron', sans-serif;
        }
        .hero-desc {
            font-size: 1.2rem; color: #aaa; max-width: 800px; margin: 0 auto 20px;
        }

        /* BRIGHT NEON BLUE BOXES */
        .info-box {
            background: rgba(0, 212, 255, 0.15) !important;   border: 2px solid #00d4ff !important;   backdrop-filter: blur(10px);
            border-radius: 15px;  padding: 25px;  margin-bottom: 20px;  transition: all 0.4s ease;  animation: fadeInUp 1s ease-out;
            height: 100%;  box-shadow: 0 0 15px rgba(0, 212, 255, 0.2);
        }
        .info-box:hover {
            background: rgba(0, 212, 255, 0.25) !important;  border-color: #ffffff;  box-shadow: 0 0 30px rgba(0, 212, 255, 0.6);  transform: translateY(-8px);
        }
        
        .section-heading {
            color: #00d4ff; font-size: 1.8rem; font-weight: bold; margin: 40px 0 25px; text-align: center;text-transform: uppercase;
        }

        .feature-title {
            color: #ffffff;font-weight: bold;font-size: 1.2rem;margin-bottom: 10px;
        }
        div.stButton > button[kind="secondary"] {
    background: #161b22 !important; border: 1px solid rgba(0,212,255,0.4) !important; color: #00d4ff !important;  border-radius: 10px !important; font-weight: 600 !important;
}
div.stButton > button[kind="secondary"]:hover {
    border-color: #00d4ff !important; color: #ffffff !important; background:rgba(0,212,255,0.4) !important;
}
        .feat-icon {
    width: 28px; height: 28px; margin-bottom: 8px;
    filter: invert(68%) sepia(95%) saturate(1352%) hue-rotate(163deg) brightness(101%) contrast(101%); display: block;
}
.step-icon {
    width: 22px;height: 22px;vertical-align: -5px;margin-right: 8px; filter: invert(68%) sepia(95%) saturate(1352%) hue-rotate(163deg) brightness(101%) contrast(101%);
}
        div.stButton > button {
            background: linear-gradient(45deg, #00d4ff, #0080ff) !important;  color: white !important;  border-radius: 12px !important;
            padding: 12px 25px !important;  font-weight: bold !important;  border: none !important; transition: 0.3s !important;
        }
        </style>
    """, unsafe_allow_html=True)
    LUCIDE = "https://cdn.jsdelivr.net/npm/lucide-static@latest/icons"
    #  HERO SECTION
    st.markdown('<div class="hero-section">', unsafe_allow_html=True)
    st.markdown('<h1 class="main-title">Career Clarity, Powered by AI</h1>', unsafe_allow_html=True)
    st.markdown('<p class="hero-desc">Optimize your career path with deep-learning based resume audits and real-time skill matching.</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    btn_col1, btn_col2, btn_col3 = st.columns(3)
    with btn_col1:
         if st.button(":material/search_insights: Analyze Now", use_container_width=True):
            st.session_state.nav_to = "Resume Analyzer" # "menu_key" ki jagah "nav_to" use kiya
            st.rerun()
    with btn_col2:
        if st.button(":material/create: Build Profile", use_container_width=True):
            st.session_state.nav_to = "Resume Builder"
            st.rerun()
    with btn_col3:
        if st.button(":material/search: Find Jobs", use_container_width=True):
            st.session_state.nav_to = "Job Radar"
            st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="section-heading"> Core Features</div>', unsafe_allow_html=True)
    f_col1, f_col2 = st.columns(2)
    with f_col1:
        st.markdown(f'<div class="info-box"><img src="{LUCIDE}/brain-circuit.svg" class="feat-icon"><div class="feature-title">Advanced Analyzer</div><p>Our Hybrid ATS Engine uses Llama-3 to score your resume based on industry standards.</p></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="info-box"><img src="{LUCIDE}/file-text.svg" class="feat-icon"><div class="feature-title">ATS Resume Builder</div><p>Generate resumes that pass through automated filters with clean formatting.</p></div>', unsafe_allow_html=True)
       
    with f_col2:
        st.markdown(f'<div class="info-box"><img src="{LUCIDE}/target.svg" class="feat-icon"><div class="feature-title">Skill Gap Analysis</div><p>Instantly identify what\'s missing between your profile and the JD.</p></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="info-box"><img src="{LUCIDE}/briefcase.svg" class="feat-icon"><div class="feature-title">Smart Match Jobs</div><p>Get recommended roles where your current skills give you an edge.</p></div>', unsafe_allow_html=True)
    #  WORKFLOW
    st.markdown('<div class="section-heading"><Settings />How It Works</div>', unsafe_allow_html=True)
    steps_col1, steps_col2 = st.columns(2)
    with steps_col1:
        st.markdown(f'<div class="info-box"><img src="{LUCIDE}/upload.svg" class="step-icon"><b>Step 1:</b> Upload Resume & JD</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="info-box"><img src="{LUCIDE}/target.svg" class="step-icon"><b>Step 3:</b> Get Real ATS Score</div>', unsafe_allow_html=True)   
    with steps_col2:
        st.markdown(f'<div class="info-box"><img src="{LUCIDE}/cpu.svg" class="step-icon"><b>Step 2:</b> AI Extracts Competencies</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="info-box"><img src="{LUCIDE}/trending-up.svg" class="step-icon"><b>Step 4:</b> Follow the Skill Roadmap</div>', unsafe_allow_html=True)
    
       