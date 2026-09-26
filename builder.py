import streamlit as st
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch

def local_css():
    st.markdown("""
        <style>
        .stApp { background-color: #010409; color: #ffffff; font-family: 'Rajdhani', sans-serif; }
        .neon-title { font-family: 'Orbitron'; color: #00d4ff !important; text-shadow: 0 0 15px #00d4ff; text-align: center; }
        .resume-paper { background-color: white !important; color: black !important; padding: 40px !important; box-shadow: 0 0 25px rgba(0, 212, 255, 0.3); line-height: 1.4; }
        .paper-header { border-bottom: 2px solid #333; font-weight: bold; text-transform: uppercase; margin-top: 15px; margin-bottom: 5px; color: black !important; }
        .skill-tag { display: inline-block; background-color: #f1f1f1; border: 1px solid #ddd; border-radius: 4px; padding: 2px 8px; margin: 2px; font-size: 10pt; color: black !important; }
        .stButton>button { border: 1px solid #00d4ff; background: rgba(0,212,255,0.1); color: #00d4ff; font-weight: bold; width: 100%; }
        .stButton>button:hover { background: linear-gradient(135deg, #00d4ff, #0080ff); color: black; box-shadow: 0 0 10px #00d4ff; }

        /* --- Template picker cards --- */
        .tpl-card {
            border-radius: 12px; padding: 10px; height: 150px; position: relative;
            border: 2px solid rgba(0,212,255,0.15); transition: 0.25s ease; overflow: hidden;
        }
        .contact-icon {
            width: 13px;  height: 13px; vertical-align: -1px; margin-right: 3px; filter: invert(20%);
        }
        .contact-icon-white {
            width: 13px; height: 13px; vertical-align: -1px; margin-right: 3px; filter: invert(100%);
        }
        .contact-item {
            display: inline-flex; align-items: center; margin: 0 5px; text-decoration: none; color: inherit; 
        }
        div.stButton > button[kind="secondary"] {
    background: #161b22 !important; border: 1px solid rgba(0,212,255,0.4) !important; color: #00d4ff !important; 
    border-radius: 10px !important; font-weight: 600 !important;
}
div.stButton > button[kind="secondary"]:hover {
    border-color: #00d4ff !important; color: #ffffff !important; background:rgba(0,212,255,0.4) !important;
}
        .tpl-card.selected { border-color: #00d4ff; box-shadow: 0 0 18px rgba(0,212,255,0.5); }
        .tpl-mini { background: white; border-radius: 6px; height: 100%; padding: 8px; }
        .tpl-mini .bar { height: 6px; border-radius: 3px; margin-bottom: 5px; }
        .tpl-mini .line { height: 3px; background: #ddd; border-radius: 2px; margin-bottom: 4px; }
        .tpl-name { text-align:center; color:#00d4ff; font-weight:bold; margin-top:6px; font-size:0.85rem; }
        .tpl-desc { text-align:center; color:#888; font-size:0.7rem; margin-bottom:6px; }
        .item-row-title { color: #00d4ff; font-weight: bold; margin-bottom: 4px; }
        </style>
    """, unsafe_allow_html=True)


# 3 templates 
TEMPLATES = {
    "modern": {
        "label": "Modern / Minimal",  "desc": "Clean sans-serif, subtle accent color, lots of whitespace",
    },
    "classic": {
        "label": "Classic / ATS-Safe", "desc": "Traditional serif, black & white only, safest for ATS parsers",
    },
    "creative": {
        "label": "Creative / Colorful", "desc": "Bold colored header bar + accented sections, stands out visually",
    },
}


def render_template_picker():
    """Draws 3 clickable mini-preview cards and returns the currently selected template id."""
    if "resume_template" not in st.session_state:
        st.session_state.resume_template = "modern"

    st.markdown(" :material/palette: Choose a Template")
    cols = st.columns(3)

    mini_previews = {
        "modern": '<div class="tpl-mini"><div class="bar" style="background:#7c7c7c; width:60%; margin:0 auto 8px;"></div><div class="line" style="width:90%; margin:0 auto 4px;"></div><div class="line" style="width:70%; margin:0 auto 4px;"></div><div class="line" style="width:85%; margin:0 auto 4px;"></div><div class="line" style="width:50%; margin:8px auto 4px;"></div><div class="line" style="width:80%; margin:0 auto 4px;"></div></div>',
        "classic": '<div class="tpl-mini" style="border:1px solid #999;"><div class="bar" style="background:#000; width:50%; margin:0 auto 8px; height:5px;"></div><div class="line" style="width:95%; margin:0 auto 4px; background:#333;"></div><div class="line" style="width:95%; margin:0 auto 10px; background:#333;"></div><div class="bar" style="background:#000; width:35%; height:3px; margin-bottom:4px;"></div><div class="line" style="width:100%; margin-bottom:4px;"></div><div class="line" style="width:80%;"></div></div>',
        "creative": '<div class="tpl-mini" style="padding:0;"><div style="background:linear-gradient(135deg,#7C3AED,#EC4899); height:35%; border-radius:6px 6px 0 0;"></div><div style="padding:8px;"><div class="line" style="width:60%; background:#7C3AED; height:4px;"></div><div class="line" style="width:90%; margin-top:6px;"></div><div class="line" style="width:70%;"></div></div></div>',
    }

    for col, tpl_id in zip(cols, TEMPLATES.keys()):
        meta = TEMPLATES[tpl_id]
        is_selected = st.session_state.resume_template == tpl_id
        with col:
            card_class = "tpl-card selected" if is_selected else "tpl-card"
            st.markdown(f'<div class="{card_class}">{mini_previews[tpl_id]}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="tpl-name">{meta["label"]}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="tpl-desc">{meta["desc"]}</div>', unsafe_allow_html=True)
            btn_label = "Selected" if is_selected else "Select"
            if st.button(btn_label, key=f"pick_{tpl_id}", use_container_width=True):
                st.session_state.resume_template = tpl_id
                st.rerun()

    return st.session_state.resume_template


def flatten_skills(skill_list):
    """Splits each entry on commas so 'javascript, python, dsa' typed in one box
    still becomes 3 separate bullet items."""
    result = []
    for entry in skill_list:
        if entry:
            result.extend([s.strip() for s in entry.split(",") if s.strip()])
    return result


def build_resume_html(d, font_size, bullet_type, theme_color, template):
    """Builds the live HTML preview with real SVG icons."""
    LUCIDE = "https://cdn.jsdelivr.net/npm/lucide-static@latest/icons"
    icon_cls = "contact-icon-white" if template == "creative" else "contact-icon"

    contact_parts = []
    if d.get("email"):
        contact_parts.append(f'<span class="contact-item"><img src="{LUCIDE}/mail.svg" class="{icon_cls}">{d["email"]}</span>')
    if d.get("phone"): 
        contact_parts.append(f'<span class="contact-item"><img src="{LUCIDE}/phone.svg" class="{icon_cls}">{d["phone"]}</span>')
    if d.get("loc"):
        contact_parts.append(f'<span class="contact-item"><img src="{LUCIDE}/map-pin.svg" class="{icon_cls}">{d["loc"]}</span>')

    social_map = {
        "linkedin": ("linkedin.svg", "LinkedIn"), 
        "github": ("github.svg", "GitHub"), 
        "portfolio": ("globe.svg", "Portfolio"),
    }

    links_list = []
    for k, (icon_name, label) in social_map.items():
        if d.get(k):
            links_list.append(
                f'<a href="{d[k]}" target="_blank" class="contact-item" style="color:inherit;">'
                f'<img src="{LUCIDE}/{icon_name}" class="{icon_cls}"> {label}</a>'
            )

    social_html = " | ".join(links_list)

    if template == "classic":
        font_family = "Georgia, 'Times New Roman', serif"
        accent = "#000000"
        header_style = f"color:{accent}; border-bottom: 1.5px solid {accent}; text-transform:uppercase; letter-spacing:1px; font-size: {font_size}pt;"
        name_style = f"text-align:center; margin:0; color:{accent}; text-transform:uppercase; letter-spacing:2px;"
        wrapper_style = f"font-size:{font_size}pt; font-family:{font_family};"

    elif template == "creative":
        font_family = "Arial, sans-serif"
        accent = theme_color if theme_color != "#000000" else "#7C3AED"
        wrapper_style = f"font-size:{font_size}pt; font-family:{font_family}; padding:0 !important;"
        name_style = "text-align:center; margin:0; color:white;"
        header_style = f"color:white; background:{accent}; padding:4px 10px; border-radius:4px; display:inline-block; font-size:{font_size}pt;"

    else:  
        font_family = "'Segoe UI', Arial, sans-serif"
        accent = theme_color if theme_color != "#000000" else "#4B5563"
        header_style = f"color:{accent}; border-bottom: 2px solid {accent}; font-size:{font_size}pt;"
        name_style = f"text-align:center; margin:0; color:{accent}; font-weight:300; letter-spacing:1px;"
        wrapper_style = f"font-size:{font_size}pt; font-family:{font_family};"

    resume_html = f'<div class="resume-paper" style="{wrapper_style}">'

    if template == "creative":
        resume_html += f'''
            <div style="background:{accent}; margin:-40px -40px 20px -40px; padding:30px 40px; border-radius:8px 8px 0 0;">
                <h1 style="{name_style}">{d["name"].upper() or "YOUR NAME"}</h1>
                <p style="text-align:center; margin:8px 0 0; color:white; opacity:0.9;">{" ".join(contact_parts)}<br>{social_html}</p>
            </div>
        '''
    else:
        resume_html += f'<h1 style="{name_style}">{d["name"].upper() or "YOUR NAME"}</h1>'
        resume_html += f'<p style="text-align:center; margin:5px 0;">{" " .join(contact_parts)}<br>{social_html}</p>'
        resume_html += '<hr style="border: 1px solid #333;">'

    def section_header(title):
        if template == "creative":
            return f'<div style="margin-top:15px; margin-bottom:5px;"><span style="{header_style}">{title}</span></div>'
        return f'<div class="paper-header" style="{header_style}">{title}</div>'

    def title_date_row(title_html, date_str):
        """Title/company on the left, dates right-aligned on the right — standard resume layout."""
        return (
            f'<div style="display:flex; justify-content:space-between; align-items:baseline;">'
            f'<span>{title_html}</span>'
            f'<span style="white-space:nowrap; margin-left:10px; color:#555;">{date_str}</span>'
            f'</div>'
        )

    if d['summary']:
        resume_html += section_header("Summary") + f'<p>{d["summary"]}</p>'

    if any(d['tech_skills']) or any(d['soft_skills']):
        resume_html += section_header("Skills")
        if any(d['tech_skills']):
            resume_html += "<p><b>Technical:</b></p>"
            resume_html += "".join([f"<p style='margin:2px 0;'>{bullet_type} {s}</p>" for s in flatten_skills(d['tech_skills'])])
        if any(d['soft_skills']):
            resume_html += "<p><b>Soft Skills:</b></p>"
            resume_html += "".join([f"<p style='margin:2px 0;'>{bullet_type} {s}</p>" for s in flatten_skills(d['soft_skills'])])

    if d['projects']:
        resume_html += section_header("Projects")
        for p in d['projects']:
            if p.get('t'):
                date_str = f"{p.get('start_date', '')} - {p.get('end_date', '')}" if p.get('start_date') or p.get('end_date') else ""
                proj_title_html = f"<b>{p['t']}</b>"
                resume_html += f"<p>{title_date_row(proj_title_html, date_str)}</p>"
                if p.get('tech'):
                    resume_html += f"<p style='margin-top:-6px; color:#555;'><i>Technologies: {p['tech']}</i></p>"
                if p.get('d'):
                    resume_html += f"<p style='margin-top:-6px;'>{p.get('d', '')}</p>"

    if d['exp']:
        resume_html += section_header("Experience")
        for ex in d['exp']:
            if ex.get('role'):
                exp_dates = f"{ex.get('start_date', '')} - {ex.get('end_date', '')}" if ex.get('start_date') or ex.get('end_date') else ""
                exp_title = f"<b>{ex['role']}</b> | {ex.get('comp', '')}"
                resume_html += f"<p>{title_date_row(exp_title, exp_dates)}</p>"
                if ex.get('desc'):
                    resume_html += f"<p style='margin-top:-8px; margin-left:5px;'>{ex['desc']}</p>"

    if d['edu']['ug'].get('n') or d['edu']['ug'].get('d'):
        resume_html += section_header("Education")
        if d['edu']['ug'].get('d'): 
            ug_dates = f"{d['edu']['ug'].get('start', '')} - {d['edu']['ug'].get('end', '')}" if d['edu']['ug'].get('start') or d['edu']['ug'].get('end') else ""
            ug_titles = f"{bullet_type} <b>{d['edu']['ug']['d']}</b> ({d ['edu']['ug']['n']}) -CGPA: {d['edu']['ug']['c']}"
            resume_html += f"<p>{title_date_row(ug_titles, ug_dates)}</p>"
        if d['edu']['twelve'].get('n'): 
            resume_html += f"<p>{bullet_type} 12th: {d['edu']['twelve']['n']} ({d['edu']['twelve']['p']}%)</p>"
        if d['edu']['ten'].get('n'): 
            resume_html += f"<p>{bullet_type} 10th: {d['edu']['ten']['n']} ({d['edu']['ten']['p']}%)</p>"

    if any(d['awards']):
        resume_html += section_header("Achievements")
        for aw in d['awards']: 
            if aw: resume_html += f"<p>{bullet_type} {aw}</p>"

    if any(d['certs']):
        resume_html += section_header("Certifications")
        for c in d['certs']: 
            if c: resume_html += f"<p>{bullet_type} {c}</p>"

    resume_html += "</div>"
    return resume_html


def build_pdf(d, font_size, bullet, theme_hex, template):
    """Real PDF Generator logic."""
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter, rightMargin=40, leftMargin=40, topMargin=40, bottomMargin=40)
    story = []

    if template == "classic":
        font_main, font_bold = "Times-Roman", "Times-Bold"
        h_color = colors.black
        line_color = colors.black
        name_align = 1  
        header_underline = True
    elif template == "creative":
        font_main, font_bold = "Helvetica", "Helvetica-Bold"
        h_color = colors.HexColor(theme_hex) if theme_hex != "#000000" else colors.HexColor("#7C3AED")
        line_color = h_color
        name_align = 1
        header_underline = False
    else:  # modern
        font_main, font_bold = "Helvetica", "Helvetica-Bold"
        h_color = colors.HexColor(theme_hex) if theme_hex != "#000000" else colors.HexColor("#4B5563")
        line_color = h_color
        name_align = 1
        header_underline = False

    title_s = ParagraphStyle('T', fontName=font_bold, fontSize=font_size+6, textColor=h_color, alignment=name_align, spaceAfter=4)
    sub_s = ParagraphStyle('S', fontName=font_main, fontSize=font_size-1, textColor=colors.HexColor('#444444'), alignment=name_align, spaceAfter=8)
    head_s = ParagraphStyle('H', fontName=font_bold, fontSize=font_size+2, textColor=h_color, spaceBefore=10, spaceAfter=2, keepWithNext=True)
    body_s = ParagraphStyle('B', fontName=font_main, fontSize=font_size, textColor=colors.black, leading=font_size+4, spaceAfter=3)
    italic_s = ParagraphStyle('I', fontName=font_main, fontSize=font_size-1, textColor=colors.HexColor('#555555'), leading=font_size+3, spaceAfter=3)
    date_s = ParagraphStyle('D', fontName=font_main, fontSize=font_size, textColor=colors.HexColor('#444444'), alignment=2, leading=font_size+4, spaceAfter=3)

    if template == "creative":
        name_para = Paragraph(d['name'].upper() or 'YOUR NAME', ParagraphStyle('TC', fontName=font_bold, fontSize=font_size+6, textColor=colors.white, alignment=1))
        links = [d[k] for k in ['email', 'phone', 'loc'] if d[k]]
        socials = [k.capitalize() for k in ['linkedin', 'github', 'portfolio'] if d[k]]
        contact_text = " | ".join(links) + ("<br/>" + " | ".join(socials) if socials else "")
        contact_para = Paragraph(contact_text, ParagraphStyle('SC', fontName=font_main, fontSize=font_size-1, textColor=colors.white, alignment=1))
        banner = Table([[name_para], [contact_para]], colWidths=[7.2*inch])
        banner.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), h_color),
            ('TOPPADDING', (0, 0), (-1, -1), 8),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ]))
        story.append(banner)
        story.append(Spacer(1, 10))
    else:
        story.append(Paragraph(d['name'].upper() or 'YOUR NAME', title_s))
        links = [d[k] for k in ['email', 'phone', 'loc'] if d[k]]
        socials = [k.capitalize() for k in ['linkedin', 'github', 'portfolio'] if d[k]]
        contact_text = " | ".join(links) + ("<br/>" + " | ".join(socials) if socials else "")
        story.append(Paragraph(contact_text, sub_s))
        story.append(HRFlowable(width="100%", thickness=1.5, color=line_color, spaceAfter=6))

    def add_section(title, content_list):
        if content_list:
            story.append(Paragraph(title, head_s))
            if header_underline or template != "creative":
                story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor('#cccccc'), spaceAfter=4))
            for item in content_list:
                story.append(Paragraph(item, body_s))

    def add_title_date_row(title_html, date_str):
        """Two-column row: title/company on the left, dates right-aligned on the right."""
        row = Table(
            [[Paragraph(title_html, body_s), Paragraph(date_str, date_s)]],
            colWidths=[5.4*inch, 1.8*inch],
        )
        row.setStyle(TableStyle([
            ('LEFTPADDING', (0, 0), (-1, -1), 0),
            ('RIGHTPADDING', (0, 0), (-1, -1), 0),
            ('TOPPADDING', (0, 0), (-1, -1), 0),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ]))
        story.append(row)

    if d['summary']:
        add_section("SUMMARY", [d['summary']])

    skills = []
    if any(d['tech_skills']):
        skills.append("<b>Technical:</b>")
        skills.extend([f"{bullet} {s}" for s in flatten_skills(d['tech_skills'])])
    if any(d['soft_skills']):
        skills.append("<b>Soft Skills:</b>")
        skills.extend([f"{bullet} {s}" for s in flatten_skills(d['soft_skills'])])
    add_section("SKILLS", skills)

    if any(p.get('t') for p in d['projects']):
        story.append(Paragraph("PROJECTS", head_s))
        if header_underline or template != "creative":
            story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor('#cccccc'), spaceAfter=4))
        for p in d['projects']:
            if p.get('t'):
                dates = f"{p.get('start_date', '')} - {p.get('end_date', '')}" if p.get('start_date') or p.get('end_date') else ""
                add_title_date_row(f"<b>{p['t']}</b>", dates)
                if p.get('tech'):
                    story.append(Paragraph(f"<i>Technologies: {p['tech']}</i>", italic_s))
                if p.get('d'):
                    story.append(Paragraph(p['d'], body_s))

    if any(ex.get('role') for ex in d['exp']):
        story.append(Paragraph("EXPERIENCE", head_s))
        if header_underline or template != "creative":
            story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor('#cccccc'), spaceAfter=4))
        for ex in d['exp']:
            if ex.get('role'):
                dates = f"{ex.get('start_date', '')} - {ex.get('end_date', '')}" if ex.get('start_date') or ex.get('end_date') else ""
                add_title_date_row(f"<b>{ex['role']}</b> | {ex.get('comp', '')}", dates)
                if ex.get('desc'):
                    story.append(Paragraph(ex['desc'], body_s))

    edu_list = []
    if d['edu']['ug'].get('d') or d['edu']['ug'].get('n'):
       ug_dates = f" | {d['edu']['ug'].get('start', '')} - {d['edu']['ug'].get('end', '')}" if d['edu']['ug'].get('start') or d['edu']['ug'].get('end') else ""
       edu_list.append(f"{bullet} <b>{d['edu']['ug']['d']}</b><br/>&nbsp;&nbsp;&nbsp;&nbsp;{d['edu']['ug']['n']} (CGPA: {d['edu']['ug']['c']}){ug_dates}")
    if d['edu']['twelve'].get('n'): 
        edu_list.append(f"{bullet} 12th: {d['edu']['twelve']['n']} ({d['edu']['twelve']['p']}%)")
    if d['edu']['ten'].get('n'): 
        edu_list.append(f"{bullet} 10th: {d['edu']['ten']['n']} ({d['edu']['ten']['p']}%)")
    add_section("EDUCATION", edu_list)
    add_section("ACHIEVEMENTS", [f"{bullet} {aw}" for aw in d['awards'] if aw])
    add_section("CERTIFICATIONS", [f"{bullet} {c}" for c in d['certs'] if c])
    doc.build(story)
    buffer.seek(0)
    return buffer
def show_builder():
    local_css()
    if 'res_data' not in st.session_state:
        st.session_state.res_data = {
            "name": "", "email": "", "phone": "", "loc": "", "linkedin": "", "github": "", "portfolio": "",
            "summary": "", "tech_skills": [""], "soft_skills": [""], "exp": [], "projects": [], 
            "edu": {"ug": {"n":"", "d":"", "c":""}, "twelve": {"n":"", "p":""}, "ten": {"n":"", "p":""}},
            "awards": [""], "certs": [""]
        }
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
<img src="https://cdn.jsdelivr.net/npm/lucide-static@latest/icons/file-cog.svg" style="width:26px;height:26px;
filter: invert(68%) sepia(95%) saturate(1352%) hue-rotate(163deg) brightness(101%) contrast(101%);">
</div>
<div style="flex:1;">
<h1 style="font-family:'Orbitron',sans-serif; font-size:1.55rem; font-weight:800; color:#ffffff; margin:0 0 6px; letter-spacing:1px;">RESUME GENERATOR</h1>
<div style="width:42px; height:2px; background:#00d4ff; margin-bottom:10px; position:relative; overflow:hidden;">
<div style="position:absolute; top:0; left:0; width:100%; height:100%; background:#ffffff; animation:underlineSlide 2.5s ease-in-out infinite;"></div>
</div>
<p style="color:#c9d1d9; font-size:0.85rem; margin:0; line-height:1.6; max-width:420px;">
Turn your details into a <span style="color:#00d4ff; font-weight:700;">recruiter-ready</span> resume with
<span style="color:#00d4ff; font-weight:700;">live preview</span> and instant PDF export.</p>
</div>
</div>
</div>
''', unsafe_allow_html=True)
    col1, col2 = st.columns([1, 1.2], gap="medium")
    d = st.session_state.res_data

    with col1:
        st.markdown(" :material/edit_document:  RESUME EDITOR")
        with st.expander(" :material/person:  1.PERSONAL & SOCIAL LINKS", expanded=True):
            d['name'] = st.text_input("Full Name", d['name'])
            c1, c2 = st.columns(2)
            d['email'] = c1.text_input("Email", d['email'])
            d['phone'] = c2.text_input("Phone Number", d['phone'])
            d['loc'] = st.text_input("Location", d['loc'])
            d['linkedin'] = st.text_input("LinkedIn URL", d['linkedin'])
            d['github'] = st.text_input("GitHub URL", d['github'])
            d['portfolio'] = st.text_input("Portfolio Link", d['portfolio'])

        with st.expander(" :material/description: 2.PROFESSIONAL SUMMARY"):
            d['summary'] = st.text_area("Summary", d['summary'], height=80)

        with st.expander(" :material/psychology: 3.SKILLS (TECH & SOFT)"):
            st.caption("Technical Skills")
            for i, s in enumerate(d['tech_skills']):
                sc1, sc2 = st.columns([5, 1])
                d['tech_skills'][i] = sc1.text_input(f"Tech Skill {i+1}", s, key=f"ts_{i}", label_visibility="collapsed")
                if sc2.button(":material/delete:", key=f"ts_del_{i}", use_container_width=True):
                    d['tech_skills'].pop(i)
                    st.rerun()
            if st.button(" :material/add:  Add Tech Skill"): 
                d['tech_skills'].append("")
                st.rerun()

            st.caption("Soft Skills")
            for i, s in enumerate(d['soft_skills']):
                sc1, sc2 = st.columns([5, 1])
                d['soft_skills'][i] = sc1.text_input(f"Soft Skill {i+1}", s, key=f"ss_{i}", label_visibility="collapsed")
                if sc2.button(":material/delete:", key=f"ss_del_{i}", use_container_width=True):
                    d['soft_skills'].pop(i)
                    st.rerun()
            if st.button(" :material/add: Add Soft Skill"): 
                d['soft_skills'].append("")
                st.rerun()

        with st.expander(" :material/work: 4.WORK EXPERIENCE"):
            for i, ex in enumerate(d['exp']):
                with st.container(border=True):
                    hc1, hc2 = st.columns([5, 1])
                    hc1.markdown(f"**Experience {i+1}**")
                    if hc2.button(":material/delete:", key=f"exp_del_{i}", use_container_width=True):
                        d['exp'].pop(i)
                        st.rerun()
                    ex['role'] = st.text_input(f"Job Role {i+1}", value=ex.get('role',''), key=f"r_{i}")
                    ex['comp'] = st.text_input(f"Company {i+1}", value=ex.get('comp',''), key=f"c_{i}")
                    date_col1, date_col2 = st.columns(2)
                    ex['start_date'] = date_col1.text_input(f"Start Date {i+1}", value=ex.get('start_date',''), key=f"sd_{i}", placeholder="e.g. Jan 2024")
                    ex['end_date'] = date_col2.text_input(f"End Date {i+1}", value=ex.get('end_date',''), key=f"end_{i}", placeholder="e.g. Present")
                    ex['desc'] = st.text_area(f"What did you do {i+1}", value=ex.get('desc',''), key=f"ed_{i}")
            if st.button(" :material/add: Add Experience"): 
                d['exp'].append({"role":"", "comp":"", "desc":"", "start_date":"", "end_date":""})
                st.rerun()

        with st.expander(" :material/assignment: 5. PROJECTS"):
            for i, p in enumerate(d['projects']):
                with st.container(border=True):
                    hc1, hc2 = st.columns([5, 1])
                    hc1.markdown(f"**Project {i+1}**")
                    if hc2.button(":material/delete:", key=f"proj_del_{i}", use_container_width=True):
                        d['projects'].pop(i)
                        st.rerun()
                    p['t'] = st.text_input(f"Project Title {i+1}", value=p.get('t',''), key=f"pt_{i}")
                    p['tech'] = st.text_input(f"Technologies Used {i+1}", value=p.get('tech',''), key=f"ptech_{i}", placeholder="e.g. React, Node.js, MongoDB")
                    p_col1, p_col2 = st.columns(2)
                    p['start_date'] = p_col1.text_input(f"Project Start Date {i+1}", value=p.get('start_date',''), key=f"psd_{i}", placeholder="e.g. Jan 2024")
                    p['end_date'] = p_col2.text_input(f"Project End Date {i+1}", value=p.get('end_date',''), key=f"ped_{i}", placeholder="e.g. Present / Mar 2024")
                    p['d'] = st.text_area(f"Project Description {i+1}", value=p.get('d',''), key=f"pd_{i}")
            if st.button(" :material/add: Add Project"): 
                d['projects'].append({"t":"", "tech":"", "start_date":"", "end_date":"", "d":""})
                st.rerun()

        with st.expander(" :material/school: 6.EDUCATION"):
            d['edu']['ug']['d'] = st.text_input("Degree", d['edu']['ug'].get('d',''))
            d['edu']['ug']['n'] = st.text_input("College Name", d['edu']['ug'].get('n',''))
            d['edu']['ug']['c'] = st.text_input("CGPA", d['edu']['ug'].get('c',''))
            edu_date_col1, edu_date_col2 = st.columns(2)
            d['edu']['ug']['start'] = edu_date_col1.text_input("Start Year", d['edu']['ug'].get('start',''))
            d['edu']['ug']['end'] = edu_date_col2.text_input("End Year (or Expected)", d['edu']['ug'].get('end',''))
            
            d['edu']['twelve']['n'] = st.text_input("12th School", d['edu']['twelve'].get('n',''))
            d['edu']['twelve']['p'] = st.text_input("12th %", d['edu']['twelve'].get('p',''))
            d['edu']['ten']['n'] = st.text_input("10th School", d['edu']['ten'].get('n',''))
            d['edu']['ten']['p'] = st.text_input("10th %", d['edu']['ten'].get('p',''))

        with st.expander(" :material/emoji_events: 7.ACHIEVEMENTS & CERTS"):
            st.caption("Achievements")
            for i, aw in enumerate(d['awards']):
                ac1, ac2 = st.columns([5, 1])
                d['awards'][i] = ac1.text_input(f"Award {i+1}", aw, key=f"aw_{i}", label_visibility="collapsed")
                if ac2.button(":material/delete:", key=f"aw_del_{i}", use_container_width=True):
                    d['awards'].pop(i)
                    st.rerun()
            if st.button(" :material/add:  Add Award"): 
                d['awards'].append("")
                st.rerun()

            st.caption("Certifications")
            for i, c in enumerate(d['certs']):
                cc1, cc2 = st.columns([5, 1])
                d['certs'][i] = cc1.text_input(f"Cert {i+1}", c, key=f"ce_{i}", label_visibility="collapsed")
                if cc2.button(":material/delete:", key=f"ce_del_{i}", use_container_width=True):
                    d['certs'].pop(i)
                    st.rerun()
            if st.button(" :material/add:  Add Cert"): 
                d['certs'].append("")
                st.rerun()

    with col2:
        #st.markdown(" :material/visibility:  LIVE PREVIEW & FORMATTING")
        st.markdown("""
         <div style="
            text-align: center;color: #00d4ff; font-size: 1.15rem; font-weight: 700; letter-spacing: 0.5px; margin-bottom: 15px;
        ">  👁 LIVE PREVIEW & FORMATTING
        </div>
    """, unsafe_allow_html=True)
        selected_template = render_template_picker()
        st.markdown("---")
        f1, f2, f3 = st.columns(3)
        font_size = f1.slider("Font Size", 10, 14, 11)
        bullet_type = f2.selectbox("Bullet Style", ["•", "➤", "▪", "–"])
        theme_color = f3.color_picker(
            "Accent Color",
            "#000000",
            disabled=(selected_template == "classic"),
            help="Accent color is disabled for the Classic/ATS-Safe template — it's intentionally black & white for ATS parsers." if selected_template == "classic" else None
        )

        resume_html = build_resume_html(d, font_size, bullet_type, theme_color, selected_template)
        st.markdown(resume_html, unsafe_allow_html=True)
        st.divider()

        pdf_file = build_pdf(d, font_size, bullet_type, theme_color, selected_template)
        st.download_button(
            label="DOWNLOAD RESUME PDF",
            data=pdf_file,
            file_name=f"{d['name'].replace(' ', '_') or 'Resume_Pro'}_{selected_template}.pdf",
            mime="application/pdf"
        )

if __name__ == "__main__":
    show_builder()