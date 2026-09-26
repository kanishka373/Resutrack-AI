import streamlit as st
import pandas as pd
import plotly.express as px
from collections import Counter
import db

def local_css():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
        
        .stApp { 
            background-color: #0b0f19; color: #f1f5f9; font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif; 
        }
        
        .dash-title { 
            color: #00d4ff !important; font-family: 'Rajdhani', sans-serif; text-align: center; font-size: 2.2rem; 
            font-weight: 700; text-transform: uppercase; letter-spacing: 2px; text-shadow: 0 0 12px rgba(0, 212, 255, 0.65);
            margin-bottom: 24px; 
        }
        
        .section-heading {
            color: #38bdf8; font-size: 1.1rem; font-weight: 600; margin-top: 24px; margin-bottom: 12px; letter-spacing: 0;
            display: flex; align-items: center; gap: 8px;
        }
        .concept-icon {
            width: 20px; height: 20px; filter: invert(68%) sepia(95%) saturate(1352%) hue-rotate(163deg) brightness(101%) contrast(101%);
        }
        @keyframes cardFadeIn {
            0% { opacity: 0; transform: translateY(8px); } 100% { opacity: 1; transform: translateY(0); }
        }

        .stat-card {
            position: relative; background: linear-gradient(145deg, #151c2c 0%, #10151f 100%); border: 1px solid #26334d; border-radius: 14px;
            padding: 18px 16px; text-align: center; margin-bottom: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.25); animation: cardFadeIn 0.5s ease-out;
            overflow: hidden;
        }
        .stat-card:hover {
           border-color: #00d4ff; box-shadow: 0 0 25px rgba(0,212,255,.35);}

        .stat-card::before {
            content: ""; position: absolute; top: 0; left: 0; right: 0; height: 3px; background: var(--accent-color, #38bdf8);
            box-shadow: 0 0 10px var(--accent-color, #38bdf8);
        }

        .stat-icon {
            width: 22px; height: 22px; margin-bottom: 8px; opacity: 0.9;
        }

        .stat-val { 
            font-size: 1.6rem; font-weight: 700; margin-top: 2px;
        }
        .stat-label { 
            color: #94a3b8; font-size: 0.75rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.6px; 
        }
        
        .chart-box {
            background: #151c2c; border-radius: 10px; padding: 16px; border: 1px solid #26334d;
        }
        
        .insight-line {
            display: flex; align-items: center; gap: 8px; background: #1e293b; border-left: 4px solid #38bdf8; 
            border-radius: 8px; padding: 10px 16px; margin-bottom: 20px; color: #e2e8f0; font-size: 0.9rem;
        }

        .skill-tag {
            display: inline-block; padding: 5px 12px; border-radius: 6px; font-size: 0.85rem; font-weight: 500; margin: 4px;
        }
        .tag-fixed { background: rgba(16, 185, 129, 0.15); color: #34d399; border: 1px solid rgba(16, 185, 129, 0.3); }
        .tag-missing { background: rgba(239, 68, 68, 0.15); color: #f87171; border: 1px solid rgba(239, 68, 68, 0.3); }
        .tag-gap { background: rgba(245, 158, 11, 0.15); color: #fbbf24; border: 1px solid rgba(245, 158, 11, 0.3); }

        div[data-baseweb="select"] > div { 
            background-color: #1e293b !important; border-color: #334155 !important; color: #f8fafc !important;
            border-radius: 8px !important;
        }

        .vs-card {
            background: #151c2c; border: 1px solid #26334d; border-radius: 12px;
            padding: 24px 16px; text-align: center; height: 100%;
        }
        .vs-card-new { border-color: #10b981; box-shadow: 0 0 15px rgba(16, 185, 129, 0.15); }
        .vs-score { font-size: 2.4rem; font-weight: 800; color: #f8fafc; }
        .vs-label { color: #64748b; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 8px; }
        .vs-sub { color: #94a3b8; font-size: 0.85rem; margin-top: 10px; }
        .vs-divider { display: flex; align-items: center; justify-content: center; font-weight: 800; color: #475569; font-size: 1.4rem; height: 100%; }
        .vs-delta { font-size: 0.95rem; font-weight: 700; margin-top: 6px; }

        div.stButton > button[kind="primary"] {
            background: linear-gradient(135deg, #00d4ff 0%, #0080ff 100%) !important;
            color: #0d1117 !important; font-weight: 700 !important; 
            border: none !important; border-radius: 10px !important; padding: 10px 20px !important;
            transition: all 0.2s ease !important; 
            box-shadow: 0 4px 15px rgba(0, 212, 255, 0.25) !important;
        }
        div.stButton > button[kind="primary"]:hover {
            transform: translateY(-2px) !important; box-shadow: 0 6px 20px rgba(0, 212, 255, 0.45) !important;
        }
        div.stButton > button[kind="secondary"] {
            background: #161b22 !important; border: 1px solid rgba(0,212,255,0.4) !important; color: #00d4ff !important; 
            border-radius: 10px !important; font-weight: 600 !important;
        }
        div.stButton > button[kind="secondary"]:hover {
            border-color: #00d4ff !important; color: #ffffff !important; background:rgba(0,212,255,0.4) !important;
        }
        </style>
    """, unsafe_allow_html=True)

def show_dashboard():
    local_css()
    LUCIDE = "https://cdn.jsdelivr.net/npm/lucide-static@latest/icons"
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
<img src="https://cdn.jsdelivr.net/npm/lucide-static@latest/icons/layout-dashboard.svg" style="width:26px;height:26px;
filter: invert(68%) sepia(95%) saturate(1352%) hue-rotate(163deg) brightness(101%) contrast(101%);">
</div>
<div style="flex:1;">
<h1 style="font-family:'Orbitron',sans-serif; font-size:1.55rem; font-weight:800; color:#ffffff; margin:0 0 6px; letter-spacing:1px;">DASHBOARD</h1>
<div style="width:42px; height:2px; background:#00d4ff; margin-bottom:10px; position:relative; overflow:hidden;">
<div style="position:absolute; top:0; left:0; width:100%; height:100%; background:#ffffff; animation:underlineSlide 2.5s ease-in-out infinite;"></div>
</div>
<p style="color:#c9d1d9; font-size:0.85rem; margin:0; line-height:1.6; max-width:420px;">
Track your <span style="color:#00d4ff; font-weight:700;">ATS score progress</span> and
<span style="color:#00d4ff; font-weight:700;">skill gaps</span> over time.</p>
</div>
</div>
</div>
''', unsafe_allow_html=True)
    
    session_id = st.session_state.get('session_id', 'default_user')
    data = db.get_history(session_id)
    
    if not data:
        st.warning(" No analysis history found. Run a Resume Scan first!")
        return

    latest = data[-1]
    scores = [d.get('ats_score', 0) for d in data]
    roles_list = [d.get('role', 'N/A') for d in data]
    most_common_role = Counter(roles_list).most_common(1)[0][0] if roles_list else "N/A"

    # KPI Stat Cards
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(f'''
            <div class="stat-card" style="--accent-color:#38bdf8;">
                <img src="{LUCIDE}/target.svg" class="stat-icon" style="filter: invert(68%) sepia(95%) saturate(1352%) hue-rotate(163deg) brightness(101%) contrast(101%);">
                <div class="stat-label">Current Score</div>
                <div class="stat-val" style="color:#38bdf8;">{latest.get("ats_score", 0)}%</div>
            </div>
        ''', unsafe_allow_html=True)
    with col2:
        diff = round(scores[-1] - scores[-2], 1) if len(scores) > 1 else 0
        p_color = "#10b981" if diff >= 0 else "#ef4444"
        st.markdown(f'''
            <div class="stat-card" style="--accent-color:{p_color};">
                <img src="{LUCIDE}/trending-up.svg" class="stat-icon" style="filter: invert(68%) sepia(85%) saturate(1000%) hue-rotate({"110deg" if diff>=0 else "320deg"}) brightness(101%) contrast(101%);">
                <div class="stat-label">Improvement</div>
                <div class="stat-val" style="color:{p_color};">{"+" if diff >= 0 else ""}{diff}%</div>
            </div>
        ''', unsafe_allow_html=True)
    with col3:
        st.markdown(f'''
            <div class="stat-card" style="--accent-color:#a78bfa;">
                <img src="{LUCIDE}/briefcase.svg" class="stat-icon" style="filter: invert(68%) sepia(45%) saturate(2000%) hue-rotate(220deg) brightness(105%) contrast(101%);">
                <div class="stat-label">Top Target Role</div>
                <div class="stat-val" style="color:#a78bfa; font-size:1.1rem; word-break:break-word;">{most_common_role}</div>
            </div>
        ''', unsafe_allow_html=True)
    with col4:
        st.markdown(f'''
            <div class="stat-card" style="--accent-color:#f59e0b;">
                <img src="{LUCIDE}/scan-line.svg" class="stat-icon" style="filter: invert(68%) sepia(85%) saturate(1200%) hue-rotate(0deg) brightness(105%) contrast(101%);">
                <div class="stat-label">Scans Logged</div>
                <div class="stat-val" style="color:#f59e0b;">{len(data)}</div>
            </div>
        ''', unsafe_allow_html=True)

    latest_score = latest.get("ats_score", 0)
    top_missing = latest.get("missing", [])[:2]
    if latest_score >= 80:
        insight_icon, insight_txt = "target", "Great job — you're hitting the ATS benchmark. Focus on quantifying project impact next."
    elif latest_score >= 60:
        insight_icon, insight_txt = "zap", f"Decent score — add mentions of {', '.join(top_missing) if top_missing else 'key skills'} to push higher."
    else:
        insight_icon, insight_txt = "alert-triangle", f"Low match — prioritize adding {', '.join(top_missing) if top_missing else 'core skills'} to your resume."
    st.markdown(f'<div class="insight-line"><img src="{LUCIDE}/{insight_icon}.svg" style="width:16px;height:16px;filter: invert(68%) sepia(95%) saturate(1352%) hue-rotate(163deg) brightness(101%) contrast(101%);">{insight_txt}</div>', unsafe_allow_html=True)

    # Progress Chart — hero section
    st.markdown(f'<div class="section-heading"><img src="{LUCIDE}/activity.svg" class="concept-icon"> Preparation Progress</div>', unsafe_allow_html=True)
    df = pd.DataFrame(data)
    df['Scan_Index'] = range(1, len(df) + 1)
        
    fig = px.area(df, x='Scan_Index', y='ats_score', markers=True, labels={'Scan_Index': 'Scan Number', 'ats_score': 'ATS Score %'})
    fig.update_traces(line_color='#38bdf8', fillcolor='rgba(56, 189, 248, 0.08)', marker=dict(size=7, color="#10b981"))
    
    fig.add_hline(
        y=90, 
        line_dash="dash", line_color="#f59e0b", annotation_text="90% Target Benchmark", annotation_position="bottom right",
        annotation_font_color="#f59e0b"
    )
    
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color="#94a3b8", margin=dict(l=5, r=10, t=15, b=5), xaxis=dict(showgrid=False), yaxis=dict(showgrid=True, gridcolor='#1e293b', range=[0, 105]), height=320)
        
    with st.container(border=True):
        st.plotly_chart(fig, use_container_width=True)

    # Comparison Section
    st.markdown(f'<div class="section-heading"><img src="{LUCIDE}/git-compare.svg" class="concept-icon"> Scan Comparison</div>', unsafe_allow_html=True)

    if len(data) < 2:
        st.info(" Run at least 2 scans to unlock side-by-side comparison.")
    else:
        scan_labels = [f"Scan {i+1} · {d.get('role', 'N/A')} ({d.get('ats_score', 0)}%)" for i, d in enumerate(data)]

        cmp_col1, cmp_col2 = st.columns(2)
        old_idx = cmp_col1.selectbox("Base Scan (Older)", range(len(data)), format_func=lambda i: scan_labels[i], index=0, key="cmp_old")
        new_idx = cmp_col2.selectbox("Comparison Scan (Newer)", range(len(data)), format_func=lambda i: scan_labels[i], index=len(data) - 1, key="cmp_new")

        old_scan, new_scan = data[old_idx], data[new_idx]
        old_score, new_score = old_scan.get('ats_score', 0), new_scan.get('ats_score', 0)
        old_det, new_det = len(old_scan.get('detected', [])), len(new_scan.get('detected', []))
        old_mis, new_mis = len(old_scan.get('missing', [])), len(new_scan.get('missing', []))

        score_diff = round(new_score - old_score, 1)
        diff_color = "#10b981" if score_diff >= 0 else "#ef4444"
        diff_arrow = "↑" if score_diff > 0 else ("↓" if score_diff < 0 else "→")
        diff_sign = "+" if score_diff > 0 else ""

        vc1, vc2, vc3 = st.columns([2, 0.6, 2])
        with vc1:
            st.markdown(f'''
                <div class="vs-card">
                    <div class="vs-label">Older Scan</div>
                    <div class="vs-score">{old_score}%</div>
                    <div class="vs-sub">{old_det} detected · {old_mis} missing</div>
                </div>
            ''', unsafe_allow_html=True)
        with vc2:
            st.markdown('<div class="vs-divider">VS</div>', unsafe_allow_html=True)
        with vc3:
            st.markdown(f'''
                <div class="vs-card vs-card-new">
                    <div class="vs-label">Newer Scan</div>
                    <div class="vs-score">{new_score}%</div>
                    <div class="vs-delta" style="color:{diff_color};">{diff_arrow} {diff_sign}{score_diff}%</div>
                    <div class="vs-sub">{new_det} detected · {new_mis} missing</div>
                </div>
            ''', unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        old_missing, new_detected, new_missing = set(old_scan.get('missing', [])), set(new_scan.get('detected', [])), set(new_scan.get('missing', []))
        fixed_skills = old_missing & new_detected
        still_missing = old_missing & new_missing
        newly_missing = new_missing - old_missing

        skill_col1, skill_col2 = st.columns(2)
        with skill_col1:
            st.markdown('<p style="color:#10b981; font-weight:600; font-size:0.9rem;">Resolved Skills</p>', unsafe_allow_html=True)
            if fixed_skills:
                tags = "".join([f'<span class="skill-tag tag-fixed">{s}</span>' for s in fixed_skills])
                st.markdown(f'<div class="chart-box">{tags}</div>', unsafe_allow_html=True)
            else:
                st.caption("No missing skills were resolved between selected scans.")

        with skill_col2:
            st.markdown('<p style="color:#f59e0b; font-weight:600; font-size:0.9rem;">Unresolved & New Gaps</p>', unsafe_allow_html=True)
            if still_missing or newly_missing:
                tags = "".join([f'<span class="skill-tag tag-missing">{s} (Still Missing)</span>' for s in still_missing])
                tags += "".join([f'<span class="skill-tag tag-gap">{s} (New Gap)</span>' for s in newly_missing])
                st.markdown(f'<div class="chart-box">{tags}</div>', unsafe_allow_html=True)
            else:
                st.caption("No missing skill gaps detected!")

if __name__ == "__main__":
    show_dashboard()