import streamlit as st
import requests
from collections import Counter
import textwrap

def show_jobs():
    LUCIDE = "https://cdn.jsdelivr.net/npm/lucide-static@latest/icons"

    if 'scan_active' not in st.session_state:
        st.session_state.scan_active = False
    st.markdown("""
        <style>
        .stApp { background-color: #030508; color: white; font-family: 'Inter', sans-serif; }
            @keyframes float {
            0% { transform: translateY(0px); box-shadow: 0 0 15px rgba(0,212,255,0.2); }
             50% { transform: translateY(-8px); box-shadow: 0 0 25px rgba(0,212,255,0.4); }
            100% { transform: translateY(0px); box-shadow: 0 0 15px rgba(0,212,255,0.2); }
        }

        .result-box {
            background: rgba(0, 212, 255, 0.08); border: 1px solid rgba(0, 212, 255, 0.25); border-radius: 12px;
            padding: 14px; margin-bottom: 20px; animation: float 4s ease-in-out infinite; transition: 0.3s;
            backdrop-filter: blur(10px);
        }
        .result-box:hover {
            background: rgba(0, 212, 255, 0.15);border-color: #00d4ff;animation-play-state: paused;
        }

        .company-logo {
            width: 38px;  height: 38px;  object-fit: contain;  background: rgba(255, 255, 255, 0.9);  border-radius: 10px;
            padding: 8px;  margin-right: 15px;  box-shadow: 0 0 10px rgba(0,212,255,0.3);
        }
        .concept-icon {
            width: 24px; height: 24px; margin-bottom: 0; vertical-align: -4px; margin-right: 8px;
            filter: invert(68%) sepia(95%) saturate(1352%) hue-rotate(163deg) brightness(101%) contrast(101%);
        }

        .skill-tag {
            background: rgba(0, 212, 255, 0.1); color: #00d4ff; border: 1px solid rgba(0, 212, 255, 0.3);
            padding: 4px 12px; border-radius: 20px; font-size: 0.8rem; margin-right: 5px; display: inline-block; margin-top: 5px;
        }
        div.stButton > button[kind="secondary"] {
    background: #161b22 !important; border: 1px solid rgba(0,212,255,0.4) !important; color: #00d4ff !important; 
    border-radius: 10px !important; font-weight: 600 !important;
}
div.stButton > button[kind="secondary"]:hover {
    border-color: #00d4ff !important; color: #ffffff !important; background:rgba(0,212,255,0.4) !important;
}

        .view-btn {
            background: linear-gradient(135deg, #00d4ff, #0080ff); color: #000 !important; border: none; padding: 10px 20px;
            border-radius: 8px; text-decoration: none !important; font-weight: bold;
            display: inline-block; margin-top: 15px; width: 100%; text-align: center;
        }
        .view-btn:hover { background: linear-gradient(135deg, #0080ff, #00d4ff); color: white !important; }
        .section-header { color: #00d4ff; font-size: 1.5rem; font-weight: bold; margin: 25px 0; border-left: 5px solid #00d4ff; padding-left: 15px;display:flex;align-items:center; }
        .apply-btn-inline {
            background: linear-gradient(135deg, #00d4ff, #0080ff); color: #000 !important; border: none; padding: 8px 20px;
            border-radius: 8px; text-decoration: none !important; font-weight: bold; text-align: center; min-width: 100px;
        }
        </style>
    """, unsafe_allow_html=True)
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
<img src="https://cdn.jsdelivr.net/npm/lucide-static@latest/icons/radar.svg" style="width:26px;height:26px;
filter: invert(68%) sepia(95%) saturate(1352%) hue-rotate(163deg) brightness(101%) contrast(101%);">
</div>
<div style="flex:1;">
<h1 style="font-family:'Orbitron',sans-serif; font-size:1.55rem; font-weight:800; color:#ffffff; margin:0 0 6px; letter-spacing:1px;">Job Radar</h1>
<div style="width:42px; height:2px; background:#00d4ff; margin-bottom:10px; position:relative; overflow:hidden;">
<div style="position:absolute; top:0; left:0; width:100%; height:100%; background:#ffffff; animation:underlineSlide 2.5s ease-in-out infinite;"></div>
</div>
<p style="color:#c9d1d9; font-size:0.85rem; margin:0; line-height:1.6; max-width:420px;">
Search <span style="color:#00d4ff; font-weight:700;">live job listings</span> and see
<span style="color:#00d4ff; font-weight:700;">trending skills</span> in real time.</p>
</div>
</div>
</div>
''', unsafe_allow_html=True)

    st.markdown("<h4 style='text-align:left; color:#00d4ff;'> <img src='" + LUCIDE + "/trending-up.svg' class='concept-icon'> Live Job Board</h4>", unsafe_allow_html=True)
    KNOWN_SKILLS = {
        "python", "javascript", "typescript", "java", "c++", "c#", "go", "rust", "php", "ruby",
        "swift", "kotlin", "react", "react.js", "angular", "vue", "vue.js", "node.js", "nodejs",
        "django", "flask", "spring", "spring boot", ".net", "aws", "azure", "gcp", "docker",
        "kubernetes", "devops", "ci/cd", "git", "linux", "sql", "mysql", "postgresql", "mongodb",
        "redis", "graphql", "rest api", "machine learning", "deep learning", "data science",
        "artificial intelligence", "ai", "nlp", "computer vision", "tensorflow", "pytorch",
        "html", "css", "html5", "css3", "tailwind", "bootstrap", "cloud", "microservices",
        "agile", "scrum", "cybersecurity", "blockchain", "figma", "ui/ux",
    }

    @st.cache_data(ttl=1800, show_spinner=False)
    def compute_trending_skills():
        """Pulls live listings from the same job-board API used by the search below,
        then counts how often each KNOWN tech skill appears across them — real numbers,
        not hardcoded ones, filtered down to only meaningful tech keywords."""
        try:
            resp = requests.get("https://www.arbeitnow.com/api/job-board-api", timeout=8)
            resp.raise_for_status()
            jobs = resp.json().get("data", [])
        except requests.exceptions.RequestException:
            return [], 0, "Couldn't reach the job board right now."

        tag_counter = Counter()
        for j in jobs:
            for t in (j.get("tags") or []):
                if t and t.strip().lower() in KNOWN_SKILLS:
                    tag_counter[t.strip()] += 1

        top_tags = tag_counter.most_common(10)
        return top_tags, len(jobs), None

    with st.spinner("Analyzing live job listings..."):
        top_tags, total_jobs_scanned, fetch_err = compute_trending_skills()

    if fetch_err:
        st.info(fetch_err + " Try the search below instead.")
    elif not top_tags:
        st.info("No recognizable tech-skill tags found in the current live listings — try again later, the board refreshes often.")
    else:
        st.caption(f"Computed live just now from {total_jobs_scanned} current listings on the job board — these are the most-requested tech skills right now, not a fixed list.")

        for i in range(0, len(top_tags), 5):
            cols = st.columns(5)
            for j in range(5):
                if i + j < len(top_tags):
                    tag, count = top_tags[i + j]
                    pct = round((count / total_jobs_scanned) * 100) if total_jobs_scanned else 0
                    cols[j].markdown(textwrap.dedent(f'''
                        <div class="result-box" style="text-align:center; padding:15px; border-radius:10px;">
                            <h6 style="margin:5px 0; color:white; font-size:0.9rem;">{tag}</h6>
                            <p style="color:#00ff88; font-weight:bold; margin:0;">{count} listings ({pct}%)</p>
                        </div>
                    ''').strip(), unsafe_allow_html=True)

    st.markdown(f'<div class="section-header"><img src="{LUCIDE}/search.svg" class="concept-icon"> Custom Search Filters</div>', unsafe_allow_html=True)
    f1, f2 = st.columns(2)
    role_in = f1.text_input("Target Role", value="", placeholder="ex: SDE Intern / Java Developer")
    loc_in = f2.text_input("Location", value="", placeholder="ex: Remote / Bangalore / Delhi")

    c1, c2 = st.columns(2)
    job_type = c1.selectbox("Job Type", ["All Types", "Full Time", "Part Time", "Contract"])
    experience = c2.selectbox("Experience Level", ["Any", "Fresher / Intern", "Junior (0-2 yrs)", "Mid-level (2-5 yrs)", "Senior (5+ yrs)"])
    st.caption("Experience level is detected from job titles (keyword-based), since job APIs don't provide it as clean structured data.")

    SALARY_RANGES = {
        "Any": (0, 0),
        "0-3 LPA": (0, 300000), "3-6 LPA": (300000, 600000), "6-10 LPA": (600000, 1000000), "10-15 LPA": (1000000, 1500000),
        "15-25 LPA": (1500000, 2500000), "25+ LPA": (2500000, 0),
    }
    salary_col,_ = st.columns([1,2])
    with salary_col:
     salary_choice = st.selectbox("Salary Range", list(SALARY_RANGES.keys()))
    salary_min, salary_max = SALARY_RANGES[salary_choice]
    _, scan_btn_col, _ = st.columns([1, 1, 1])
    with scan_btn_col:
        if st.button(" :material/rocket_launch: ACTIVATE SCANNER ", use_container_width=True):
            if not role_in.strip() and not loc_in.strip():
                st.warning("Please enter a role or location to search.")
            else:
                st.session_state.scan_active = True

    if st.session_state.scan_active:
        if role_in and loc_in:
            search_title = f"{role_in} Jobs in {loc_in}"
        elif role_in:
            search_title = f"{role_in} Jobs Across India"
        elif loc_in:
            search_title = f"Top Jobs in {loc_in}"
        else:
            search_title = "Top Jobs Across India"
        st.markdown(f'<div class="section-header"><img src="{LUCIDE}/rocket.svg" class="concept-icon">Search Results: {search_title}</div>', unsafe_allow_html=True)

        EXPERIENCE_KEYWORDS = {
            "Fresher / Intern": ["fresher", "intern", "trainee", "entry level", "entry-level", "graduate"],
            "Junior (0-2 yrs)": ["junior", "associate"],"Mid-level (2-5 yrs)": ["mid-level", "mid level"],
            "Senior (5+ yrs)": ["senior", "lead", "principal", "staff"],
        }

        @st.cache_data(ttl=600,show_spinner=False)
        def fetch_adzuna_jobs(what, where, job_type_param, sal_min, sal_max):
            """Fetches live jobs from Adzuna's India job search API — supports real
            location search and salary range filtering, unlike the previous free API."""
            app_id = st.secrets.get("ADZUNA_APP_ID", "")
            app_key = st.secrets.get("ADZUNA_APP_KEY", "")
            if not app_id or not app_key:
                return [], "Adzuna API credentials aren't set up yet — add ADZUNA_APP_ID and ADZUNA_APP_KEY to secrets.toml."

            url = "https://api.adzuna.com/v1/api/jobs/in/search/1"
            params = {
                "app_id": app_id,
                "app_key": app_key,
                "results_per_page":50,
                "content-type": "application/json",
            }
            if what:
                params["what"] = what
            if where:
                params["where"] = where
            if sal_min > 0:
                params["salary_min"] = sal_min
            if sal_max > 0:
                params["salary_max"] = sal_max
            if job_type_param == "Full Time":
                params["full_time"] = 1
            elif job_type_param == "Part Time":
                params["part_time"] = 1
            elif job_type_param == "Contract":
                params["contract"] = 1

            try:
                resp = requests.get(url, params=params, timeout=8)
                resp.raise_for_status()
                return resp.json().get("results", []), None
            except requests.exceptions.Timeout:
                return [], "Adzuna took too long to respond. Please try again."
            except requests.exceptions.RequestException:
                return [], "Couldn't reach Adzuna right now. Try again in a bit."

        with st.spinner(" Searching live job listings..."):
            raw_jobs, fetch_error = fetch_adzuna_jobs(role_in,loc_in.strip() or "India",job_type,salary_min,salary_max)

        if fetch_error:
            st.warning(fetch_error)
        else:

            jobs = []
            for r in raw_jobs:
                jobs.append({
                    "title": r.get("title") or "Untitled Role",
                    "company_name": (r.get("company") or {}).get("display_name") or "Not specified",
                    "location": (r.get("location") or {}).get("display_name") or "Not specified",
                    "url": r.get("redirect_url"),
                    "salary_min": r.get("salary_min"),
                    "salary_max": r.get("salary_max"),
                    "category": (r.get("category") or {}).get("label", ""),
                })

            if experience != "Any":
                keywords = EXPERIENCE_KEYWORDS[experience]
                jobs = [j for j in jobs if any(kw in j["title"].lower() for kw in keywords)]

            jobs = jobs[:10]

            if not jobs:
                st.info("No jobs found with these filters. Try: a broader role name, removing the Salary Range, or removing the Experience Level filter — not every Adzuna listing has that data.")
            else:
                st.caption(f"Showing {len(jobs)} live listings from Adzuna, fetched just now.")
                jobs_col=st.columns(2)
                for idx,job in enumerate(jobs):
                    title = job["title"]
                    company = job["company_name"]
                    location = job["location"]
                    url = job["url"]
                    def to_lpa(amount):
                        return  round (amount /100000,1)
                    if job["salary_min"] and job["salary_max"]:
                        salary_line = f"₹{to_lpa(job['salary_min'])}L – ₹{to_lpa(job['salary_max'])}L /yr"
                    else:
                        salary_line = "Salary not listed"
                    apply_html = (
                        f'<a href="{url}" target="_blank" class="view-btn">Apply Now →</a>'
                        if url else
                        '<p style="color:#888; text-align:center; margin-top:15px;">Application link unavailable</p>'
                    )
                    with jobs_col[idx % 2]:
                        st.markdown(textwrap.dedent(f'''
                            <div class="result-box">
                            <h3 style="margin:0; color:#00d4ff;">{title}</h3>
                            <p style="color:#a0aec0; margin:6px 0;">{company} · {location}</p>
                            <p style="color:#00ff88; font-weight:bold; margin:0 0 8px;">{salary_line}</p>
                            {apply_html}
                        </div>
                    ''').strip(), unsafe_allow_html=True)


        st.markdown(f'<div class="section-header"><img src="{LUCIDE}/link-2.svg" class="concept-icon"> More Places to Search</div>', unsafe_allow_html=True)
        LOGO = "https://www.google.com/s2/favicons"
        results_cols = st.columns(3)
        platforms = [
            ("LinkedIn", f"{LOGO}?domain=linkedin.com&sz=128", "https://linkedin.com/jobs"),
            ("Google Careers", f"{LOGO}?domain=google.com&sz=128", "https://careers.google.com"),
            ("Indeed", f"{LOGO}?domain=indeed.com&sz=128", "https://indeed.com"),
            ("Naukri.com", f"{LOGO}?domain=naukri.com&sz=128", "https://naukri.com"),
            ("Glassdoor", f"{LOGO}?domain=glassdoor.com&sz=128", "https://glassdoor.com"),
            ("Wellfound", f"{LOGO}?domain=wellfound.com&sz=128", "https://wellfound.com")
        ]

        for i, (name, icon, url) in enumerate(platforms):
            dynamic_desc = f"{role_in} jobs in {loc_in}" if role_in and loc_in else "Hiring now"
            with results_cols[i % 3]:
                st.markdown(textwrap.dedent(f'''
                    <div class="result-box">
                        <div style="display:flex; align-items:center;">
                            <img src="{icon}" class="company-logo" style="width:35px; height:35px;">
                            <h3 style="margin:0; color:#00d4ff;">{name}</h3>
                        </div>
                        <p style="color:#a0aec0; margin-top:10px;">{dynamic_desc}</p>
                        <a href="{url}" target="_blank" class="view-btn">View Jobs on {name} →</a>
                    </div>
                ''').strip(), unsafe_allow_html=True)

        st.markdown(f'<div class="section-header"><img src="{LUCIDE}/building-2.svg" class="concept-icon"> Featured Tech Companies</div>', unsafe_allow_html=True)
        st.caption("Well-known tech employers — not live vacancy listings from our API.")
        companies = [
            ("Apple", f"{LOGO}?domain=apple.com&sz=128", ["Hardware", "iOS", "Design"], "https://apple.com/careers"),
            ("Meta", f"{LOGO}?domain=meta.com&sz=128", ["AR/VR", "AI", "Mobile"], "https://metacareers.com"),
            ("Amazon", f"{LOGO}?domain=amazon.com&sz=128", ["E-commerce", "AWS", "Ops"], "https://amazon.jobs"),
            ("Microsoft", f"{LOGO}?domain=microsoft.com&sz=128", ["Cloud", "Enterprise", "Gaming"], "https://careers.microsoft.com"),
            ("Google", f"{LOGO}?domain=google.com&sz=128", ["Cloud", "AI", "Mobile"], "https://careers.google.com"),
            ("Netflix", f"{LOGO}?domain=netflix.com&sz=128", ["Streaming", "Java", "Scale"], "https://jobs.netflix.com"),
            ("Atlassian", f"{LOGO}?domain=atlassian.com&sz=128", ["DevTools", "Agile", "SaaS"], "https://www.atlassian.com/company/careers"),
            ("Adobe", f"{LOGO}?domain=adobe.com&sz=128", ["Creative Cloud", "Design", "Cloud"], "https://careers.adobe.com"),
            ("Salesforce", f"{LOGO}?domain=salesforce.com&sz=128", ["CRM", "Cloud", "Enterprise"], "https://careers.salesforce.com"),
            ("IBM", f"{LOGO}?domain=ibm.com&sz=128", ["AI", "Cloud", "Consulting"], "https://www.ibm.com/careers"),
            ("Flipkart", f"{LOGO}?domain=flipkart.com&sz=128", ["E-commerce", "Java", "Scale"], "https://www.flipkartcareers.com"),
            ("Swiggy", f"{LOGO}?domain=swiggy.com&sz=128", ["Logistics", "Backend", "Scale"], "https://careers.swiggy.com")
        ]

        company_cols = st.columns(4)
        for i, (name, logo_url, tags, url) in enumerate(companies):
            tags_html = "".join([f'<span class="skill-tag">{tag}</span>' for tag in tags])
            with company_cols[i % 4]:
                st.markdown(textwrap.dedent(f'''
                    <div class="result-box" style="text-align:center;">
                        <img src="{logo_url}" class="company-logo" style="margin:0 auto 10px auto; display:block;">
                        <h3 style="margin:0; font-size:1.1rem; color:white;">{name}</h3>
                        <div style="margin-top:8px;">{tags_html}</div>
                        <a href="{url}" target="_blank" class="apply-btn-inline" style="display:block; margin-top:12px;">APPLY</a>
                    </div>
                ''').strip(), unsafe_allow_html=True)

if __name__ == "__main__":
    show_jobs()