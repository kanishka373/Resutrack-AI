import streamlit as st
def show_about():
    LUCIDE = "https://cdn.jsdelivr.net/npm/lucide-static@latest/icons"
    st.markdown("""
        <style>
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }to { opacity: 1; transform: translateY(0); }
        }
        .about-card {
            background: rgba(0, 212, 255, 0.15) !important; border: 2px solid #00d4ff !important; backdrop-filter: blur(10px);
            border-radius: 15px; padding: 25px; margin-bottom: 20px; transition: all 0.4s ease; animation: fadeIn 0.8s ease-out;   box-shadow: 0 0 15px rgba(0, 212, 255, 0.2);
        }
        .about-card:hover {
            background: rgba(0, 212, 255, 0.25) !important; border-color: #ffffff; box-shadow: 0 0 30px rgba(0, 212, 255, 0.6);  transform: translateY(-8px);
        }
        .section-title {
            color: #00d4ff;  font-size: 1.5rem; font-weight: bold; margin-bottom: 15px; display: flex; align-items: center;gap: 10px;
        }
        .skill-tag {
            background: rgba(0, 212, 255, 0.2); color: #00d4ff;border: 1px solid #00d4ff;padding: 5px 12px;border-radius: 20px;
            font-size: 0.85rem; display: inline-block; margin: 5px;
        }
        .highlight { color: #00d4ff; font-weight: bold; }
.concept-icon {
    width: 22px; height: 22px; filter: invert(68%) sepia(95%) saturate(1352%) hue-rotate(163deg) brightness(101%) contrast(101%);
}
        </style>
    """, unsafe_allow_html=True)

    # Header
    st.markdown(f"<h1 style='text-align:center; color:#00d4ff;'> <img src='{LUCIDE}/sparkles.svg' class='concept-icon'> About ResuTrack</h1>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    # 1. Project overview — what ResuTrack is
    st.markdown(f'''
        <div class="about-card" style="text-align:center;">
            <p style="color:#eee; font-size:1.05rem; line-height:1.8; max-width:750px; margin:0 auto;">
                <b style="color:#00d4ff;">ResuTrack</b> was built to solve a real problem — generic resume advice online never 
                tells you what's <i>actually</i> missing for the specific role you're targeting. It combines 
                AI-powered ATS analysis, progress tracking, and career guidance into one tool, so the entire 
                job-hunt loop (analyze → improve → learn → apply) lives in one place.
            </p>
        </div>
    ''', unsafe_allow_html=True)

    # 2. What it does
    st.markdown(f'''
        <div class="about-card">
            <div class="section-title"><img src='{LUCIDE}/rocket.svg' class='concept-icon'>  What It Does</div>
            <ul style="color:#eee; line-height:1.9;">
                <li><b style="color:#00d4ff";>Resume Analyzer</b> — real LLM scoring (Groq / Llama-3.3), weighted across skills, format, keywords, and impact.</li>
                <li><b style="color:#00d4ff";>Resume Generator</b> — live preview synced to an actual PDF generator, not a mockup.</li>
                <li><b style="color:#00d4ff";>Analytics Dashboard</b> — every analysis gets tracked and charted (score trend, skill match breakdown, most frequently missing skills).</li>
                <li><b style="color:#00d4ff";>Resume History</b> — every scan logged with detected/missing skills, viewable and deletable.</li>
                <li><b style="color:#00d4ff";>Job Radar</b> — pulls live listings from a real jobs API, not static links.</li>
                <li><b style="color:#00d4ff";>Career Roadmaps</b> — 45+ role-specific roadmaps researched and structured by hand, not AI-generated.</li>
                <li><b style="color:#00d4ff";>Interview Prep</b> — generates tailored interview questions and gives AI feedback on your typed-in answers.</li>
                <li><b style="color:#00d4ff";>Supabase Database</b> — runs on a hosted PostgreSQL (Supabase) database, so scan history and dashboard data persist reliably across redeploys.</li>
            </ul>
        </div>
    ''', unsafe_allow_html=True)

    # 3. Tech Stack
        # 3. Tech Stack
    tech_stack = ["Python", "Streamlit", "Groq (Llama-3.3)", "Supabase (PostgreSQL)", "PyPDF2", "ReportLab", "Plotly", "Adzuna API"]
    tags_html = "".join([f'<div class="skill-tag">{tech}</div>' for tech in tech_stack])
    st.markdown(f'''
        <div class="about-card">
            <div class="section-title"><img src="{LUCIDE}/cpu.svg" class="concept-icon"> Tech Stack</div>
            {tags_html}
        </div>
    ''', unsafe_allow_html=True)

        # 4. About the creator — at the very end
       # 4. About the creator — at the very end
    st.markdown(f'''
        <div class="about-card">
            <div class="section-title"><img src='{LUCIDE}/user.svg' class='concept-icon'> Who Built This</div>
            <p style="color:#eee; font-size:1.05rem; line-height:1.7;">
                Hi, I'm <span class="highlight">Kanishka</span>, a Computer Science student with a genuine 
                interest in full-stack development. I enjoy building things end-to-end — from the database 
                up to the interface — and figuring out how real systems actually work, rather than just 
                following tutorials.
            </p>
            <p style="color:#eee; font-size:1.05rem; line-height:1.7; margin-top:12px;">
                I built ResuTrack because I was curious what a resume tool would look like if it actually 
                read your resume properly instead of just keyword-matching. Along the way, it taught me more 
                about ATS systems, LLM prompting, and database design than any tutorial could have. If it 
                helps you too, that's a bonus.
            </p>
        </div>
    ''', unsafe_allow_html=True)

    # 5. Footer section
    st.markdown("""
    <div style="text-align:center; margin-top:40px; padding-top:24px; border-top:1px solid rgba(0,212,255,0.15);">
        <p style="font-size:1rem; color:#8b949e; letter-spacing:1px;">
            Made with <span style="color:#00d4ff;">♦</span> by 
            <span style="color:#00d4ff; font-weight:700;">Kanishka</span>
        </p>
        <p style="font-size:0.9rem; color:gray; margin-top:4px;">&copy; 2026 ResuTrack</p>
    </div>
""", unsafe_allow_html=True)

if __name__ == "__main__":
    show_about()