import streamlit as st
import db

def local_css():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700&family=Rajdhani:wght@500;700&display=swap');
        .stApp { background-color: #020617; color: #ffffff; font-family: 'Rajdhani', sans-serif; }

        .neon-title { color: #00d4ff !important; text-shadow: 0 0 20px #00d4ff; font-family: 'Orbitron'; text-align: center; font-size: 2.5rem; margin-bottom: 30px; }
        .history-card {
            background: rgba(15, 23, 42, 0.7); border: 1px solid rgba(0, 212, 255, 0.25); border-radius: 15px;
            padding: 18px 22px;  margin-bottom: 10px;  transition: 0.3s ease;
        }
        .history-card:hover {
            border-color: #00d4ff;  box-shadow: 0 0 20px rgba(0, 212, 255, 0.25);
        }
        div.stButton > button[kind="secondary"] {
    background: #161b22 !important; border: 1px solid rgba(0,212,255,0.4) !important; color: #00d4ff !important; 
    border-radius: 10px !important; font-weight: 600 !important;
}
div.stButton > button[kind="secondary"]:hover {
    border-color: #00d4ff !important; color: #ffffff !important; background:rgba(0,212,255,0.4) !important;
}
        .scan-role { color: #00d4ff; font-weight: bold; font-size: 1.05rem; }
        .scan-file { color: #fff; font-size: 0.85rem; margin-top: 2px; }
        .scan-date { color: #fff; font-size: 0.8rem; margin-top: 4px; }

        .badge {
            display: inline-block;  padding: 5px 14px;  border-radius: 20px;  font-weight: bold;  font-size: 1rem;
            margin-top: 6px;
        }
        .badge-excellent { background: rgba(0, 255, 127, 0.15); color: #00ff7f; border: 1px solid #00ff7f; }
        .badge-good { background: rgba(255, 200, 0, 0.15); color: #ffc800; border: 1px solid #ffc800; }
        .badge-needs-work { background: rgba(255, 49, 49, 0.15); color: #ff3131; border: 1px solid #ff3131; }
        .hist-icon { width: 16px; height: 16px; vertical-align: -3px; margin-right: 4px;
    filter: invert(68%) sepia(95%) saturate(1352%) hue-rotate(163deg) brightness(101%) contrast(101%); }
    .icon-green { width: 16px; height: 16px; vertical-align: -3px; margin-right: 4px;

    filter: invert(64%) sepia(59%) saturate(4826%) hue-rotate(101deg) brightness(100%) contrast(101%); }
.icon-red { width: 16px; height: 16px; vertical-align: -3px; margin-right: 4px;

    filter: invert(20%) sepia(94%) saturate(7492%) hue-rotate(357deg) brightness(101%) contrast(96%); }
        </style>
    """, unsafe_allow_html=True)

def get_badge(score):
    if score >= 85:
        return '<span class="badge badge-excellent">🟢 Excellent</span>'
    elif score >= 70:
        return '<span class="badge badge-good">🟡 Good</span>'
    else:
        return '<span class="badge badge-needs-work">🔴 Needs Improvement</span>'

def show_history():
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
<img src="https://cdn.jsdelivr.net/npm/lucide-static@latest/icons/history.svg" style="width:26px;height:26px;
filter: invert(68%) sepia(95%) saturate(1352%) hue-rotate(163deg) brightness(101%) contrast(101%);">
</div>
<div style="flex:1;">
<h1 style="font-family:'Segoe UI', Arial,sans-serif; font-size:1.55rem; font-weight:800; color:#ffffff; margin:0 0 6px; letter-spacing:1px;">RESUME SCAN HISTORY</h1>
<div style="width:42px; height:2px; background:#00d4ff; margin-bottom:10px; position:relative; overflow:hidden;">
<div style="position:absolute; top:0; left:0; width:100%; height:100%; background:#ffffff; animation:underlineSlide 2.5s ease-in-out infinite;"></div>
</div>
<p style="color:#c9d1d9; font-size:0.85rem; margin:0; line-height:1.6; max-width:420px;">
Every scan is <span style="color:#00d4ff; font-weight:700;">saved and tracked</span> so you can revisit
<span style="color:#00d4ff; font-weight:700;">past results</span> anytime.</p>
</div>
</div>
</div>
''', unsafe_allow_html=True)
    history = db.get_history(st.session_state.session_id)

    if not history:
        st.warning("No scans yet. Run the Resume Analyzer first!")
        return

    st.caption(f"Showing {len(history)} scan(s). This history now persists across refreshes.")

    # Show most recent first
    for position, entry in enumerate(reversed(history), 1):
        score = entry.get('ats_score', 0)
        filename = entry.get('filename', 'resume.pdf')
        detected_count = len(entry.get('detected', []))
        missing_count = len(entry.get('missing', []))
        db_id = entry['db_id']

        col1, col2 = st.columns([5, 1])
        with col1:
            st.markdown(f"""
                <div class="history-card">
                    <div class="scan-role">Scan {position} · {entry.get('role', 'N/A')}</div>
                     <div class="scan-file"><img src="{LUCIDE}/file-text.svg" class="hist-icon"> {filename} · <img src="{LUCIDE}/check-circle.svg" class="icon-green"> {detected_count} detected · <img src="{LUCIDE}/x-circle.svg" class="icon-red"> {missing_count} missing</div>
                    {get_badge(score)} <span style="color:#eee; margin-left:8px;">{score}%</span>
                    <div class="scan-date">{entry.get('date', '')} · {entry.get('timestamp', '')}</div>
                </div>
            """, unsafe_allow_html=True)

        with col2:
            if st.button(" :material/delete: Delete", key=f"delete_{db_id}", use_container_width=True):
                db.delete_scan(db_id)
                st.rerun()

        with st.expander(f"Expand Details — Scan {position}"):
            st.markdown(f'<p><img src="{LUCIDE}/check-circle.svg" class="icon-green"> <b>Detected Skills</b></p>', unsafe_allow_html=True)
            detected = entry.get('detected', [])
            st.markdown(f'<p style="color:#eee;">{", ".join(detected) if detected else "None recorded"}</p>', unsafe_allow_html=True)

            st.markdown(f'<p><style="color: #fff;"><img src="{LUCIDE}/x-circle.svg" class="icon-red"> <b>Missing Skills</b></p>', unsafe_allow_html=True)
            missing = entry.get('missing', [])
            st.write(", ".join(missing) if missing else "None recorded")

            st.markdown(f'<p><style="color: #fff;"><img src="{LUCIDE}/message-circle.svg" class="hist-icon"> <b>Feedback</b></p>', unsafe_allow_html=True)
            st.write(entry.get('insight', 'No feedback recorded'))

if __name__ == "__main__":
    show_history()