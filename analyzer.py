import streamlit as st
import PyPDF2
import json
from groq import Groq
from datetime import datetime
import db
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from io import BytesIO

client = Groq(api_key=st.secrets["GROQ_API_KEY"])
MODEL_NAME = "openai/gpt-oss-120b"

AVAILABLE_ROLES = [
    "SDE", "Full Stack Developer", "Backend Developer", "Frontend Developer", "Software Engineer", "Mobile App Developer", "Game Developer", "Data Scientist", 
    "DevOps Engineer", "Cloud Architect", "ML Engineer", "Data Engineer", "Network Engineer", "AI Engineer", "Cybersecurity Analyst", "Java Developer", 
    "Python Developer", "UI/UX Designer", "QA Engineer", "Database Administrator", "Ethical Hacker", "Computer Vision Engineer", "NLP Engineer", "Digital Forensics Engineer",
    "IoT Engineer", "Blockchain Developer", "QA Automation Engineer", "Product Manager", "Security Engineer", "Data Analyst", 
    "Android Developer", "iOS Developer", "SDET (Software Development Engineer in Test)", 
    "Embedded Systems Engineer", "Systems Engineer", "Solutions Architect",  "IT Support Engineer", "Site Reliability Engineer (SRE)", "Data Architect", 
    "Frontend Architect", "CRM Developer", "ERP Consultant", "BI Engineer (Business Intelligence)",  "Systems Administrator", "Technical Writer", "Solutions Engineer", "Scrum Master", 
    "Technical Product Manager (TPM)", "Release Engineer", "Cloud Security Engineer"
]

ROLE_TO_TIPS_MAP = {
    "SDE": "Software Development Engineer (SDE)", "Software Engineer": "Software Development Engineer (SDE)",
    "Full Stack Developer": "Full Stack Developer", "Backend Developer": "Backend Developer",
    "Frontend Developer": "Frontend Developer", "Data Scientist": "Data Scientist",
    "DevOps Engineer": "DevOps Engineer", "Cloud Architect": "Cloud Architect",
    "ML Engineer": "ML Engineer", "Data Engineer": "Data Engineer",
    "Network Engineer": "Network Engineer", "Cybersecurity Analyst": "Cybersecurity Analyst",
    "Java Developer": "Java Developer", "Python Developer": "Python Developer",
    "UI/UX Designer": "UI/UX Designer", "Database Administrator": "Database Administrator (DBA)",
    "Computer Vision Engineer": "Computer Vision Engineer", "NLP Engineer": "NLP Engineer (Natural Language Processing)",
    "Blockchain Developer": "Blockchain Developer", "QA Automation Engineer": "QA Automation Engineer",
    "Product Manager": "Product Manager", "Security Engineer": "Security Engineer",
    "Data Analyst": "Data Analyst", "Android Developer": "Android Developer",
    "Solutions Architect": "Solutions Architect", "IT Support Engineer": "IT Support Engineer",
    "Site Reliability Engineer (SRE)": "Site Reliability Engineer (SRE)", "Data Architect": "Data Architect",
    "Frontend Architect": "Frontend Architect", "CRM Developer": "CRM Developer",
    "ERP Consultant": "ERP Consultant", "BI Engineer (Business Intelligence)": "BI Engineer (Business Intelligence)",
    "Systems Administrator": "Systems Administrator", "Technical Writer": "Technical Writer",
    "Solutions Engineer": "Solutions Engineer", "Scrum Master": "Scrum Master",
    "Technical Product Manager (TPM)": "Technical Product Manager (TPM)", "Release Engineer": "Release Engineer",
    "Cloud Security Engineer": "Cloud Security Engineer",
}

LUCIDE_ICONS = {
    "target": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#00d4ff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/></svg>',
    "check": '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#10b981" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>',
    "alert": '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#ef4444" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>',
    "sparkles": '<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#00d4ff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m12 3-1.9 5.8a2 2 0 0 1-1.28 1.28L3 12l5.8 1.9a2 2 0 0 1 1.28 1.28L12 21l1.9-5.8a2 2 0 0 1 1.28-1.28L21 12l-5.8-1.9a2 2 0 0 1-1.28-1.28Z"/></svg>',
}

def local_css():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
        .stApp { background-color: #0d1117; color:white; font-family: 'Plus Jakarta Sans', sans-serif; }
        
        /* Clean Header */
        .brand-header {
            display: flex;  align-items: center;  gap: 14px; padding: 10px 0 20px 0;
        }
        .brand-logo-lucide {
            width: 48px; height: 48px;  background: rgba(0, 212, 255, 0.08);  border: 1px solid rgba(0, 212, 255, 0.3);
            border-radius: 12px;  display: flex; align-items: center; justify-content: center;  box-shadow: 0 0 20px rgba(0, 212, 255, 0.15);
            transition: all 0.3s ease;
        }
        .brand-logo-lucide:hover {
            transform: scale(1.05);  border-color: #00d4ff; box-shadow: 0 0 25px rgba(0, 212, 255, 0.3);
        }
        /* Glass Cards */
        .glass-card {
            background: rgba(22, 27, 34, 0.75);border: 1px solid #30363d;border-radius:16px; padding: 22px; margin-bottom: 20px; transition: all 0.3s ease;
        }
        .glass-card:hover {
            border-color: rgba(0, 212, 255, 0.4);
            transform: scale(1.02)translateY(-2px); box-shadow: 0 0 20px rgba(0, 212, 255, 0.2); pointer-events: auto;
              cursor: pointer;
        }

        /* Metric Cards */
        .metric-card {
            background: #161b22;  border: 1px solid #30363d; border-radius: 16px; padding: 22px;text-align: center; height: 100%; display: flex; flex-direction: column; justify-content: center; transition: all 0.3s ease;
        }
        .metric-card:hover {
            border-color: #00d4ff; box-shadow: 0 0 20px rgba(0, 212, 255, 0.2); transform: translateY(-2px);
        }

        /* Dynamic Lucide Radial ATS Meter Container */
        .ats-gauge-container {
            background: #161b22;border: 1px solid #30363d;  border-radius: 16px;  padding: 22px 16px;
            text-align: center;transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);cursor: pointer;
        }
        .ats-gauge-container:hover {
            border-color: #00d4ff;  box-shadow: 0 0 25px rgba(0, 212, 255, 0.3);  transform: scale(1.03);
        }

        /* Lucide Pill Badges */
        .badge-present {
            background: rgba(16, 185, 129, 0.12); color:#10b981; border: 1px solid rgba(16, 185, 129, 0.25);
            font-weight: 600; font-size: 0.85rem; padding: 6px 14px; border-radius: 30px;  display: inline-flex; align-items: center;
         gap: 6px; margin: 4px; transition: transform 0.2s ease;
        }
        .badge-present:hover { transform: translateY(-1px); border-color: #10b981; }
        .badge-missing {
            background: rgba(239, 68, 68, 0.12); color: #ef4444; border: 1px solid rgba(239, 68, 68, 0.25);
            font-weight: 600; font-size: 0.85rem; padding: 6px 14px; border-radius: 30px;  display: inline-flex;
          align-items: center; gap: 6px; margin: 4px;transition: transform 0.2s ease;
        }
        .badge-missing:hover { transform: translateY(-1px); border-color: #ef4444; }

        /* Buttons Styling */
        div.stButton > button[kind="primary"] {
            background: linear-gradient(135deg, #00d4ff 0%, #0080ff 100%) !important; color: #0d1117 !important; font-weight: 700 !important; 
            border: none !important; border-radius: 10px !important; padding: 10px 20px !important; transition: all 0.2s ease !important; 
            box-shadow: 0 4px 15px rgba(0, 212, 255, 0.25) !important;
        }
        div.stButton > button[kind="primary"]:hover {
            transform: translateY(-2px) !important; box-shadow: 0 6px 20px rgba(0, 212, 255, 0.45) !important;
        }
        div.stButton > button[kind="secondary"] {
            background: #161b22 !important; border: 1px solid rgba(0,212,255,0.4) !important; color: #00d4ff !important;  border-radius: 10px !important; font-weight: 600 !important;
        }
        div.stButton > button[kind="secondary"]:hover {
            border-color: #00d4ff !important; color: #ffffff !important;background:rgba(0,212,255,0.4) !important;;
        }

        /* PDF Download Button */
        div[data-testid="stDownloadButton"] > button {
            background: linear-gradient(135deg, #10b981 0%, #059669 100%) !important; color: #ffffff !important;
            font-weight: 700 !important; border-radius: 10px !important; border: none !important; padding: 12px 22px !important;
            box-shadow: 0 4px 15px rgba(16, 185, 129, 0.25) !important; transition: all 0.2s ease !important;
        }
        div[data-testid="stDownloadButton"] > button:hover {
            transform: translateY(-2px) !important; box-shadow: 0 6px 20px rgba(16, 185, 129, 0.45) !important;
        }
        .score-row {
            background: #161b22; border: 1px solid #30363d; border-radius: 12px; padding: 14px 18px;  margin-bottom: 12px; transition: all 0.2s ease;
        }
        .score-row:hover {
            border-color: rgba(0, 212, 255, 0.3); transform: translateX(4px);
        }
        </style>
    """, unsafe_allow_html=True)

def styled_heading(text):
    st.markdown(f'''
        <div style="display:flex; align-items:center; gap:10px; border-left:4px solid #00d4ff;
            padding:10px 16px; background:rgba(0,212,255,0.06); border-radius:0 8px 8px 0; margin:20px 0 14px 0;">
            <span style="color:#00d4ff; font-size:1.1rem; font-weight:700; letter-spacing:0.5px;">{text}</span>
        </div>
    ''', unsafe_allow_html=True)

def build_full_report_pdf(data):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter, rightMargin=40, leftMargin=40, topMargin=40, bottomMargin=40)
    styles = getSampleStyleSheet()
    
    title_s = ParagraphStyle('T', fontName='Helvetica-Bold', fontSize=20, textColor=colors.HexColor('#00d4ff'), spaceAfter=8)
    sub_s = ParagraphStyle('Sub', fontName='Helvetica-Bold', fontSize=11, textColor=colors.HexColor('#8b949e'), spaceAfter=12)
    head_s = ParagraphStyle('H', fontName='Helvetica-Bold', fontSize=12, textColor=colors.HexColor('#111827'), spaceBefore=12, spaceAfter=6)
    body_s = ParagraphStyle('B', fontName='Helvetica', fontSize=10, textColor=colors.HexColor('#374151'), leading=14, spaceAfter=6)
    
    story = []
    story.append(Paragraph(" RESUME REPORT", title_s))
    story.append(Paragraph(f"Target Role: {data['role']} | ATS Score: {data['total']}%", sub_s))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#e5e7eb'), spaceAfter=12))
    story.append(Paragraph("<b>Verified Skills:</b>", head_s))
    story.append(Paragraph(", ".join(data['detected']) if data['detected'] else "None detected", body_s))  
    story.append(Paragraph("<b>Critical Keyword Gaps:</b>", head_s))
    story.append(Paragraph(", ".join(data['missing']) if data['missing'] else "None missing", body_s)) 
    story.append(Paragraph("<b>Strategic Feedback:</b>", head_s))
    story.append(Paragraph(data['feedback'].encode('ascii', 'ignore').decode(), body_s))
    
    if data.get('rewrite'):
        story.append(Paragraph("<b>Bullet Optimization:</b>", head_s))
        story.append(Paragraph(f"<b>Original:</b> {data['rewrite'].get('old', 'N/A')}", body_s))
        story.append(Paragraph(f"<b>Optimized:</b> {data['rewrite'].get('new', 'N/A')}", body_s))
    
    if st.session_state.get('interview_questions'):
        story.append(Spacer(1, 10))
        story.append(Paragraph("<b>Tailored Interview Questions:</b>", head_s))
        for i, q in enumerate(st.session_state.interview_questions, 1):
            story.append(Paragraph(f"{i}. {q.encode('ascii', 'ignore').decode()}", body_s))
            
    doc.build(story)
    buffer.seek(0)
    return buffer

def show_analyzer():
    local_css()
    st.markdown('''
<style>
@keyframes underlineSlide { 0% { transform: translateX(-100%); } 50% { transform: translateX(100%); } 100% { transform: translateX(100%); } }
@keyframes iconGlow { 0%,100% { box-shadow:0 0 12px rgba(0,212,255,0.3); } 50% { box-shadow:0 0 20px rgba(0,212,255,0.6); } }
</style>
<div style="text-align:left; padding:22px 28px; margin-bottom:20px;background: rgba(0, 212, 255, 0.15); border:2px solid #00d4ff; border-radius:16px; position:relative; overflow:hidden; box-shadow: 0 0 20px rgba(0, 212, 255, 0.25);">
<div style="display:flex; align-items:flex-start; gap:18px;">
<div style="width:56px; height:56px; border-radius:50%; background:radial-gradient(circle, rgba(0,212,255,0.18), rgba(0,212,255,0.02));
border:1.5px solid rgba(0,212,255,0.4); display:flex; align-items:center; justify-content:center; flex-shrink:0;
animation:iconGlow 2.5s ease-in-out infinite;">
<img src="https://cdn.jsdelivr.net/npm/lucide-static@latest/icons/scan-search.svg" style="width:26px;height:26px;
filter: invert(68%) sepia(95%) saturate(1352%) hue-rotate(163deg) brightness(101%) contrast(101%);">
</div>
<div style="flex:1;">
<h1 style="font-family:'Orbitron',sans-serif; font-size:1.55rem; font-weight:800; color:#ffffff; margin:0 0 6px; letter-spacing:1px;">RESUME ANALYZER</h1>
<div style="width:42px; height:2px; background:#00d4ff; margin-bottom:10px; position:relative; overflow:hidden;">
<div style="position:absolute; top:0; left:0; width:100%; height:100%; background:#ffffff; animation:underlineSlide 2.5s ease-in-out infinite;"></div>
</div>
<p style="color:#c9d1d9; font-size:0.85rem; margin:0; line-height:1.6; max-width:420px;">
Get an <span style="color:#00d4ff; font-weight:700;">ATS match score</span> and
<span style="color:#00d4ff; font-weight:700;">AI feedback</span> on your resume.</p>
</div>
</div>
</div>
''', unsafe_allow_html=True)

    with st.sidebar:
        st.markdown('<h3 style="color:#f3f4f6; font-size:1rem; font-weight:700; letter-spacing:0.5px;">CONFIGURATIONS</h3>', unsafe_allow_html=True)
        role = st.selectbox("Target Role", AVAILABLE_ROLES)
        uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
        analyze_now = st.button(" :material/rocket_launch: Deep Scan", type="primary", use_container_width=True)

    if uploaded_file and analyze_now:
        with st.status("Analyzing Resume...", expanded=True) as status:
            st.write("Extracting text from PDF... This may take a few seconds...")
            reader = PyPDF2.PdfReader(uploaded_file)
            resume_text = " ".join([p.extract_text() or "" for p in reader.pages])

            if len(resume_text.strip()) < 50:
                status.update(label="Couldn't parse PDF", state="error", expanded=True)
                st.error("Please ensure you are uploading a text-based PDF file.")
                st.stop()
            st.write("Sending resume text to AI model for analysis...")
            prompt = f"""
            Analyze resume for {role}. Strictly return JSON:
            {{
              "scores": {{"skills": 0-100, "format": 0-100, "keywords": 0-100, "impact": 0-100}},
              "detected": ["core skills ACTUALLY present in resume for {role}"],
              "missing": ["3-6 critical skills missing for {role}"],
              "audit": [{{ "item": "string", "pass": bool, "msg": "string" }}],
              "feedback": "string",
              "rewrite": {{ "old": "ONE single weak bullet from resume", "new": "an optimized, impact-driven version of that line" }}
            }}
            """
            
            try:
                response = client.chat.completions.create(
                    messages=[{"role": "user", "content": prompt + "\n" + resume_text}],
                    model=MODEL_NAME, response_format={"type": "json_object"}
                )
                res = json.loads(response.choices[0].message.content)
                st.write("Calculating your Ats Score..")

                raw = res.get('scores', {})
                s_score = round((raw.get('skills', 0) / 100) * 60, 1)
                f_score = round((raw.get('format', 0) / 100) * 20, 1)
                k_score = round((raw.get('keywords', 0) / 100) * 10, 1)
                i_score = round((raw.get('impact', 0) / 100) * 10, 1)
                total = round(s_score + f_score + k_score + i_score, 1)
                st.write("Saving your results..")

                entry = {
                    "date": datetime.now().strftime("%Y-%m-%d"),
                    "timestamp": datetime.now().strftime("%I:%M %p"), "role": role,
                    "filename": uploaded_file.name, "ats_score": total,
                    "detected": res.get('detected', []),"missing": res.get('missing', []),
                    "insight": res.get('feedback', '')
                }
                db.add_scan(st.session_state.session_id, entry)

                st.session_state.last_analysis = {
                    "role": role, "total": total,
                    "s_score": s_score, "f_score": f_score, "k_score": k_score, "i_score": i_score,
                    "detected": res.get('detected', []), "missing": res.get('missing', []),
                    "audit": res.get('audit', []), "feedback": res.get('feedback', ''), "rewrite": res.get('rewrite', {}),
                    "date": entry["date"], "resume_text": resume_text
                }
                st.session_state.pop('interview_questions', None)

                status.update(label="Complete!", state="complete", expanded=False)
                st.rerun()
            except Exception as e:
                status.update(label="Analysis failed", state="error", expanded=True)
                st.error(f"Error: {e}")

    if st.session_state.get('last_analysis'):
        data = st.session_state.last_analysis
        role = data['role']
        total = data['total']
        s_score, f_score, k_score, i_score = data['s_score'], data['f_score'], data['k_score'], data['i_score']

        TAB_LABELS = ["OVERVIEW", "SKILL MATCH", "AUDIT & FEEDBACK", "ROADMAP", "INTERVIEW PREP"]
        if "analyzer_active_tab_idx" not in st.session_state:
            st.session_state.analyzer_active_tab_idx = 0

        tab_cols = st.columns(5)
        for i, label in enumerate(TAB_LABELS):
            with tab_cols[i]:
                btn_type = "primary" if st.session_state.analyzer_active_tab_idx == i else "secondary"
                if st.button(label, key=f"analyzer_tab_btn_{i}", use_container_width=True, type=btn_type):
                    st.session_state.analyzer_active_tab_idx = i
                    st.rerun()

        active_idx = st.session_state.analyzer_active_tab_idx

        # TAB 0: OVERVIEW
        if active_idx == 0:
            st.markdown("<br>", unsafe_allow_html=True)
            
            # Lucide Minimal SVG Gauge Ring
            dash_offset = 283 - (283 * total / 100)
            meter_color = "#00d4ff" if total >= 70 else ("#f59e0b" if total >= 50 else "#ef4444")
            glow_color = "rgba(0, 212, 255, 0.4)" if total >= 70 else ("rgba(245, 158, 11, 0.4)" if total >= 50 else "rgba(239, 68, 68, 0.4)")
            
            m1, m2, m3 = st.columns(3)
            with m1:
                st.markdown(f'''
                    <div class="ats-gauge-container">
                        <div style="color:#8b949e; font-size:0.8rem; font-weight:700; margin-bottom:12px; letter-spacing:0.8px;">ATS SCORE METER</div>
                        <div style="position:relative; width:130px; height:130px; margin:0 auto;">
                            <svg width="130" height="130" viewBox="0 0 100 100" style="transform: rotate(-90deg);">
                                <defs>
                                    <linearGradient id="atsGradient" x1="0%" y1="0%" x2="100%" y2="100%">
                                        <stop offset="0%" stop-color="{meter_color}" />
                                        <stop offset="100%" stop-color="#0080ff" />
                                    </linearGradient>
                                    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
                                        <feDropShadow dx="0" dy="0" stdDeviation="3" flood-color="{glow_color}"/>
                                    </filter>
                                </defs>
                                <circle cx="50" cy="50" r="45" stroke="#21262d" stroke-width="7" fill="none" />
                                <circle cx="50" cy="50" r="45" stroke="url(#atsGradient)" stroke-width="7" fill="none"
                                    stroke-dasharray="283" stroke-dashoffset="{dash_offset}" stroke-linecap="round" filter="url(#glow)"
                                    style="transition: stroke-dashoffset 1.2s ease-in-out;" />
                            </svg>
                            <div style="position:absolute; top:50%; left:50%; transform:translate(-50%, -50%); text-align:center;">
                                <span style="font-size:2.1rem; font-weight:800; color:{meter_color}; line-height:1; display:block;">{total}%</span>
                                <span style="font-size:0.65rem; color:#8b949e; font-weight:700; text-transform:uppercase;">Score</span>
                            </div>
                        </div>
                    </div>
                ''', unsafe_allow_html=True)
            with m2:
                st.markdown(f'''
                    <div class="metric-card">
                        <div style="color:#8b949e; font-size:0.8rem; font-weight:700; letter-spacing:0.8px;">SKILL RELEVANCE</div>
                        <div style="font-size:2.4rem; font-weight:800; color:#10b981; margin-top:8px;">{s_score}<span style="font-size:1rem; color:#6b7280;">/60</span></div>
                    </div>
                ''', unsafe_allow_html=True)
            with m3:
                st.markdown(f'''
                    <div class="metric-card">
                        <div style="color:#8b949e; font-size:0.8rem; font-weight:700; letter-spacing:0.8px;">FORMATTING & IMPACT</div>
                        <div style="font-size:2.4rem; font-weight:800; color:#00d4ff; margin-top:8px;">{f_score + i_score}<span style="font-size:1rem; color:#6b7280;">/30</span></div>
                    </div>
                ''', unsafe_allow_html=True)

            st.markdown("<br>", unsafe_allow_html=True)
            styled_heading("Score Breakdown")
            metrics = [("ATS Formatting", f_score, 20, "#00d4ff"), ("Keyword Optimization", k_score, 10, "#3b82f6"),
                       ("Action Impact", i_score, 10, "#a85547")]
            for name, val, m_max, clr in metrics:
                perc = (val/m_max) * 100
                st.markdown(f"""
                    <div class="score-row">
                        <div style="display:flex; justify-content:space-between; margin-bottom:6px; font-size:0.88rem; font-weight:600;">
                            <span>{name}</span><span style="color:{clr}; font-weight:700;">{val} / {m_max}</span>
                        </div>
                        <div style="background:#21262d; height:7px; border-radius:4px; overflow:hidden;">
                            <div style="background:{clr}; width:{perc}%; height:100%; border-radius:4px; box-shadow: 0 0 8px {clr}; transition: width 1s ease;"></div>
                        </div>
                    </div>
                """, unsafe_allow_html=True)

            st.markdown("<br>", unsafe_allow_html=True)
            pdf_report = build_full_report_pdf(data)
            _, pdf_btn_col, _ = st.columns([1,1,1])
            with pdf_btn_col:
             st.download_button(
                label="Download Report (PDF)",data=pdf_report,file_name=f"ATS_Report_{role.replace(' ', '_')}.pdf",mime="application/pdf",
                key="section_pdf_download", use_container_width=True
            )

        # TAB 1: SKILL MATCH
        elif active_idx == 1:
            st.markdown("<br>", unsafe_allow_html=True)
            c1, c2 = st.columns(2)
            with c1:
                styled_heading("Detected Skills")
                badges_html = "".join([f'<span class="badge-present">{LUCIDE_ICONS["check"]} {s}</span>' for s in data['detected']])
                st.markdown(badges_html if badges_html else "<p style='color:#6b7280;'>No skills detected</p>", unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)
            with c2:
                styled_heading("Missing Skills")
                badges_html = "".join([f'<span class="badge-missing">{LUCIDE_ICONS["alert"]} {s}</span>' for s in data['missing']])
                st.markdown(badges_html if badges_html else "<p style='color:#10b981;'>No major skills missing!</p>", unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)

        # TAB 2: AUDIT & FEEDBACK
        elif active_idx == 2:
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown('<div/>', unsafe_allow_html=True)
            styled_heading("ATS Compliance Audit")
            for a in data['audit']:
                icon_svg = LUCIDE_ICONS["check"] if a["pass"] else LUCIDE_ICONS["alert"]
                st.markdown(f'''
                    <div style="display:flex; align-items:flex-start; gap:10px; margin-bottom:12px; font-size:0.92rem;">
                        <span style="margin-top:2px;">{icon_svg}</span>
                        <div><b>{a["item"]}</b>: <span style="color:#8b949e;">{a["msg"]}</span></div>
                    </div>
                ''', unsafe_allow_html=True)
            
            st.markdown("<hr style='border-color:#30363d;'>", unsafe_allow_html=True)
            styled_heading("Executive Assessment")
            st.write(data['feedback'])
            st.markdown('</div>', unsafe_allow_html=True)

            styled_heading("Bullet Optimization Suggestion")
            old_line = data["rewrite"].get("old", "N/A")
            new_line = data["rewrite"].get("new", "N/A")
            
            st.markdown("**Original Bullet:**")
            st.error(old_line)
            st.markdown("**Optimized Replacement:**")
            st.success(new_line)
            st.markdown('</div>', unsafe_allow_html=True)

        # TAB 3: ROADMAP of choosen role
        elif active_idx == 3:
            st.markdown("<br>", unsafe_allow_html=True)
            styled_heading("Upskilling Action Plan")
            for m in data['missing'][:4]:
                st.markdown(f'''
                    <div class="glass-card" style="margin-bottom:12px; padding:18px;">
                        <div style="font-weight:700; font-size:0.95rem; color:#f3f4f6;">LEARN {m.upper()}</div>
                        <a href="https://www.youtube.com/results?search_query={m}+tutorial" target="_blank" style="color:#00d4ff; text-decoration:none; font-size:0.85rem; font-weight:600; display:inline-flex; align-items:center; gap:6px; margin-top:6px;">
                            {LUCIDE_ICONS["sparkles"]} Recommended Tutorials
                        </a>
                    </div>
                ''', unsafe_allow_html=True)

            tips_role = ROLE_TO_TIPS_MAP.get(role)
            if tips_role:
                _, col_center, _ = st.columns([1, 2, 1])
                with col_center:
                    if st.button(
                        f" :material/menu_book: View Career Guide for {role}", 
                        use_container_width=True, 
                        key="goto_career_tips"
                    ):
                        st.session_state.selected_tip_role = tips_role
                        st.session_state.nav_to = "Career Roadmap"
                        st.rerun()

        # TAB 4: INTERVIEW PREP and question/answer feedback
        elif active_idx == 4:
            st.markdown("<br>", unsafe_allow_html=True)
            styled_heading("Prepared Interview Questions")

            if st.session_state.get('interview_questions'):
                if 'interview_feedback' not in st.session_state:
                    st.session_state.interview_feedback = {}

                for idx, q in enumerate(st.session_state.interview_questions, 1):
                    st.markdown(f'''
                        <div class="glass-card" style="margin-bottom:10px; padding:14px 18px; border-left:3px solid #00d4ff;">
                            <span style="color:#00d4ff; font-weight:700; margin-right:8px;">Q{idx:02d}.</span>{q}
                        </div>
                    ''', unsafe_allow_html=True)

                    user_answer = st.text_area(
                        "Your answer",
                        key=f"answer_input_{idx}",
                        placeholder="Type your answer here...",label_visibility="collapsed", height=90
                    )

                    if st.button("Get AI Feedback", key=f"feedback_btn_{idx}", type="secondary"):
                        if not user_answer.strip():
                            st.warning("Please write an answer first.")
                        else:
                            with st.spinner("Evaluating your answer..."):
                                try:
                                    fb_prompt = f"""
                                    You are an interview coach. The candidate was asked this interview question:
                                    "{q}"

                                    Their answer was:
                                    "{user_answer}"

                                    Give short, direct feedback (3-5 sentences) on how good this answer is,
                                    what's missing, and one concrete way to improve it. Be honest, not overly nice.
                                    """
                                    fb_response = client.chat.completions.create(
                                        messages=[{"role": "user", "content": fb_prompt}],
                                        model=MODEL_NAME
                                    )
                                    st.session_state.interview_feedback[idx] = fb_response.choices[0].message.content
                                except Exception as e:
                                    st.error(f"Feedback error: {e}")

                    if idx in st.session_state.interview_feedback:
                        st.markdown(f'''
                            <div class="glass-card" style="margin-bottom:16px; padding:14px 18px; border-left:3px solid #10b981; background:rgba(16,185,129,0.06);">
                                <b style="color:#10b981;">AI Feedback:</b><br>
                                <span style="color:#c9d1d9;">{st.session_state.interview_feedback[idx]}</span>
                            </div>
                        ''', unsafe_allow_html=True)
                
                _, col_btn, _ = st.columns([1, 1.5, 1])
                with col_btn:
                    if st.button(" :material/refresh: Regenerate Questions", key="regen_btn", type="secondary", use_container_width=True):
                        st.session_state.pop('interview_questions', None)
                        st.rerun()
            else:
                _, col_btn, _ = st.columns([1, 1.5, 1])
                with col_btn:
                    if st.button(" :material/auto_awesome: Generate Interview Questions", key="gen_btn", type="secondary", use_container_width=True):
                        with st.spinner("Generating tailored interview questions..."):
                            try:
                                iq_prompt = f"""
                                Based on this resume and target role "{role}", generate 10 technical and behavioral interview questions.
                                Return strictly JSON: {{"questions": ["q1", "q2", ...]}}
                                RESUME TEXT: {data.get('resume_text', '')}
                                """
                                iq_response = client.chat.completions.create(
                                    messages=[{"role": "user", "content": iq_prompt}],
                                    model=MODEL_NAME,
                                    response_format={"type": "json_object"}
                                )
                                iq_res = json.loads(iq_response.choices[0].message.content)
                                st.session_state.interview_questions = iq_res.get("questions", [])
                                st.rerun()
                            except Exception as e:
                                st.error(f"Generation error: {e}")

if __name__ == "__main__":
    show_analyzer()