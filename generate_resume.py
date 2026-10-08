import os
import re
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
)

def build_pdf(filename="resume.pdf"):
    # Target exact 1-page A4 (595.27 x 841.89 points)
    # Margins: 32 pt (0.44 in) left/right, 20 pt top/bottom
    # Printable width: 595.27 - 64 = 531.27 pt
    # Printable height: 841.89 - 40 = 801.89 pt
    # pageCompression=0 ensures maximum ATS plain-text parsing across all engines
    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        leftMargin=32,
        rightMargin=32,
        topMargin=20,
        bottomMargin=20,
        pageCompression=0
    )

    styles = getSampleStyleSheet()

    # 2026 Modern Tech Executive Color Palette
    PRIMARY = colors.HexColor("#0B2545")       # Deep Midnight Navy
    SECONDARY = colors.HexColor("#134074")     # Slate Indigo
    ACCENT_LINK = colors.HexColor("#0284C7")   # Sky 600 / Tech Cyan
    TEXT_DARK = colors.HexColor("#0F172A")     # Slate 900 (High contrast)
    TEXT_MUTED = colors.HexColor("#475569")    # Slate 600
    LINE_COLOR = colors.HexColor("#CBD5E1")    # Slate 300 for crisp hairline dividers

    # Custom Typography Styles - calibrated for exact 1-page A4 density
    name_style = ParagraphStyle(
        'DocName',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=18.0,
        leading=21.0,
        textColor=PRIMARY,
        alignment=1 # Center
    )

    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.8,
        leading=11.5,
        textColor=SECONDARY,
        alignment=1
    )

    contact_style = ParagraphStyle(
        'ContactBar',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.7,
        leading=10.5,
        textColor=TEXT_MUTED,
        alignment=1
    )

    section_header_style = ParagraphStyle(
        'SectionHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.2,
        leading=11.5,
        textColor=PRIMARY,
        spaceBefore=0,
        spaceAfter=0
    )

    entry_title_style = ParagraphStyle(
        'EntryTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.4,
        leading=11.0,
        textColor=TEXT_DARK
    )

    entry_subtitle_style = ParagraphStyle(
        'EntrySubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.8,
        leading=10.5,
        textColor=TEXT_MUTED
    )

    skill_label_style = ParagraphStyle(
        'SkillLabel',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.0,
        leading=10.8,
        textColor=TEXT_DARK
    )

    skill_value_style = ParagraphStyle(
        'SkillValue',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.0,
        leading=10.8,
        textColor=TEXT_DARK
    )

    bullet_style = ParagraphStyle(
        'BulletText',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.85,
        leading=10.5,
        textColor=TEXT_DARK,
        leftIndent=10,
        firstLineIndent=-6
    )

    story = []

    # ==========================
    # HEADER (2026 Trend: Live Portfolio + GitHub + LinkedIn + Contact)
    # ==========================
    story.append(Paragraph("AHM ZAFIR HASAN", name_style))
    story.append(Spacer(1, 1.5))
    story.append(Paragraph("FULL-STACK DEVELOPER &bull; .NET &amp; WEB SYSTEMS", title_style))
    story.append(Spacer(1, 2.0))
    
    contact_line_1 = [
        "Dhaka, Bangladesh",
        "+880 1747 544 273",
        '<a href="mailto:ahmzafirhasan@gmail.com"><font color="#0284C7">ahmzafirhasan@gmail.com</font></a>'
    ]
    story.append(Paragraph(" &nbsp;&bull;&nbsp; ".join(contact_line_1), contact_style))
    story.append(Spacer(1, 1.0))

    contact_line_2 = [
        '<a href="https://zafff-e.github.io"><font color="#0284C7"><b>Portfolio:</b> zafff-e.github.io</font></a>',
        '<a href="https://github.com/Zafff-e"><font color="#0284C7"><b>GitHub:</b> github.com/Zafff-e</font></a>',
        '<a href="https://linkedin.com/in/zafir-hasan-developer"><font color="#0284C7"><b>LinkedIn:</b> in/zafir-hasan-developer</font></a>'
    ]
    story.append(Paragraph(" &nbsp;&bull;&nbsp; ".join(contact_line_2), contact_style))
    story.append(Spacer(1, 3.0))
    story.append(HRFlowable(width="100%", thickness=1.2, color=PRIMARY, spaceBefore=0, spaceAfter=3.5))

    # Helper for Section Title with line
    def add_section_header(title):
        p = Paragraph(f"<b>{title.upper()}</b>", section_header_style)
        story.append(p)
        story.append(HRFlowable(width="100%", thickness=0.6, color=LINE_COLOR, spaceBefore=1.0, spaceAfter=2.8))

    # ==========================
    # 1. TECHNICAL SKILLS (2026 Categorized ATS Keywords)
    # ==========================
    add_section_header("Technical Skills")
    
    skills = [
        ("Languages", "C#, JavaScript (ES6+), TypeScript, SQL, HTML5, CSS3"),
        ("Backend & Web APIs", "ASP.NET Core (.NET 9), ASP.NET MVC 5, Node.js, Express.js, RESTful Web APIs, WebSockets"),
        ("Databases & ORM", "Microsoft SQL Server (T-SQL), MongoDB, Entity Framework Core, Mongoose, 3NF Normalization"),
        ("Frontend Development", "React 19, Angular, Component Architecture, Single Page Applications (SPA), Tailwind CSS"),
        ("Architecture & Security", "Master-Detail Systems, Repository Pattern, DTOs, JWT Bearer Auth, bcrypt Hashing, CORS"),
        ("Tools & Cloud", "Git, GitHub (Branching, PRs, Code Reviews), Postman (API Testing), Microsoft Azure, VS Code, CI/CD")
    ]
    
    skill_rows = []
    for category, items in skills:
        col1 = Paragraph(f"&bull; <b>{category}:</b>", skill_label_style)
        col2 = Paragraph(items, skill_value_style)
        skill_rows.append([col1, col2])

    skill_table = Table(skill_rows, colWidths=[135, 396])
    skill_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 0.25),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0.25),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(skill_table)
    story.append(Spacer(1, 2.5))

    # ==========================
    # 2. SOFTWARE ENGINEERING PROJECTS (PAR / Quantified Impact + Clickable Repos)
    # ==========================
    add_section_header("Software Engineering Projects")

    # Project 1: TechNova E-Commerce (Node.js, Express, MongoDB)
    p1_header = [
        Paragraph("<b>TechNova E-Commerce Platform</b> | <font color='#475569'><i>Node.js, Express.js, MongoDB, WebSockets, bcrypt</i></font>", entry_title_style),
        Paragraph('<a href="https://github.com/Zafff-e"><font color="#0284C7"><b>GitHub ↗</b></font></a>', ParagraphStyle('R1', parent=entry_subtitle_style, alignment=2))
    ]
    t1 = Table([p1_header], colWidths=[455, 76])
    t1.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('PADDING', (0,0), (-1,-1), 0)]))
    story.append(t1)
    story.append(Spacer(1, 0.6))
    story.append(Paragraph("&bull; Architected a modular backend using <b>Node.js &amp; Express.js</b>, deploying 12+ RESTful endpoints for user auth, product catalogs, shopping cart sessions, and cash-on-delivery order processing.", bullet_style))
    story.append(Paragraph("&bull; Modeled normalized document schemas and references using <b>MongoDB &amp; Mongoose</b>; integrated <b>WebSockets</b> for real-time inventory level updates without client polling.", bullet_style))
    story.append(Paragraph("&bull; Enforced secure password protection via <b>bcrypt</b> hashing and session tokens; automated transactional order validation and dynamic invoice tracking.", bullet_style))
    story.append(Spacer(1, 2.4))

    # Project 2: ProductCatalogSPA Master-Detail Platform (.NET 9 & React/Angular)
    p2_header = [
        Paragraph("<b>Product Catalog &amp; Master-Detail System</b> | <font color='#475569'><i>C#, ASP.NET Core (.NET 9), EF Core, SQL Server, React 19</i></font>", entry_title_style),
        Paragraph('<a href="https://github.com/Zafff-e/AspNetCore-ProductCatalog-MVC"><font color="#0284C7"><b>GitHub ↗</b></font></a>', ParagraphStyle('R2', parent=entry_subtitle_style, alignment=2))
    ]
    t2 = Table([p2_header], colWidths=[455, 76])
    t2.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('PADDING', (0,0), (-1,-1), 0)]))
    story.append(t2)
    story.append(Spacer(1, 0.6))
    story.append(Paragraph("&bull; Engineered high-throughput RESTful Web APIs handling normalized Category-Product-Brand master-detail CRUD hierarchies, utilizing EF Core Code-First migrations and DTO contracts.", bullet_style))
    story.append(Paragraph("&bull; Developed dual frontend clients: Angular client with dynamic child brand insertions, and React 19 client featuring instant search filtering and dual Grid/Table view modes.", bullet_style))
    story.append(Paragraph("&bull; Implemented memory-safe multipart image streaming with GUID file naming to prevent server collisions, coupled with zero-latency client-side thumbnail previews.", bullet_style))
    story.append(Spacer(1, 2.4))

    # Project 3: Capstone Booking Marketplace
    p3_header = [
        Paragraph("<b>Skill-Commerce Booking Marketplace</b> | <font color='#475569'><i>C#, ASP.NET Core, Angular, SQL Server, REST API Architecture</i></font>", entry_title_style),
        Paragraph('<a href="https://github.com/Zafff-e"><font color="#0284C7"><b>GitHub ↗</b></font></a>', ParagraphStyle('R3', parent=entry_subtitle_style, alignment=2))
    ]
    t3 = Table([p3_header], colWidths=[455, 76])
    t3.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('PADDING', (0,0), (-1,-1), 0)]))
    story.append(t3)
    story.append(Spacer(1, 0.6))
    story.append(Paragraph("&bull; Serving as backend and database lead on team capstone designing <b>RESTful API services</b> for customer bookings, provider scheduling, and profile management.", bullet_style))
    story.append(Paragraph("&bull; Established API contracts, led daily standups, and managed the team repository on <b>Git/GitHub</b> with active branch protection and peer code reviews.", bullet_style))
    story.append(Spacer(1, 2.4))

    # Project 4: Monthly Power Plant Generation Relational Database
    p4_header = [
        Paragraph("<b>Power Plant Operations Database Architecture</b> | <font color='#475569'><i>Microsoft SQL Server, Relational Design (3NF), T-SQL</i></font>", entry_title_style),
        Paragraph('<a href="https://github.com/Zafff-e/-Power-Plant-Operations-Reporting-Database."><font color="#0284C7"><b>GitHub ↗</b></font></a>', ParagraphStyle('R4', parent=entry_subtitle_style, alignment=2))
    ]
    t4 = Table([p4_header], colWidths=[455, 76])
    t4.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('PADDING', (0,0), (-1,-1), 0)]))
    story.append(t4)
    story.append(Spacer(1, 0.6))
    story.append(Paragraph("&bull; Designed a normalized 3NF relational database schema across 12+ tables modeling monthly power generation metrics, plant operations, and fuel types from industrial records.", bullet_style))
    story.append(Paragraph("&bull; Transformed raw operational spreadsheets into structured SQL tables, enforcing primary/foreign keys, referential integrity, and indexed queries for high-speed reporting.", bullet_style))
    story.append(Spacer(1, 2.5))

    # ==========================
    # 3. EXPERIENCE & TECHNICAL TRAINING
    # ==========================
    add_section_header("Experience &amp; Technical Training")

    # Training: IsDB
    tr_header = [
        Paragraph("<b>IsDB-BISEW IT Scholarship Programme</b> | <font color='#475569'>Star Computer Systems Limited (SCSL)</font>", entry_title_style),
        Paragraph("<font color='#475569'>Jan 2026 &ndash; Present</font>", ParagraphStyle('R5', parent=entry_subtitle_style, alignment=2))
    ]
    t_tr = Table([tr_header], colWidths=[400, 131])
    t_tr.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('PADDING', (0,0), (-1,-1), 0)]))
    story.append(t_tr)
    story.append(Paragraph("<i>Enterprise Software Engineering Trainee (Intensive 9-Month Full-Time Diploma, Round 70)</i>", entry_subtitle_style))
    story.append(Spacer(1, 0.5))
    story.append(Paragraph("&bull; Selected for prestigious, fully-funded enterprise software engineering scholarship; completed 1,000+ hours of rigorous backend and full-stack software development.", bullet_style))
    story.append(Paragraph("&bull; Built and deployed 8+ enterprise applications spanning <b>Database Design &amp; Implementation (MS SQL Server)</b>, <b>C# / ASP.NET Core Web APIs (.NET 9)</b>, <b>Entity Framework Core</b>, and <b>Cloud Services (Azure)</b>.", bullet_style))
    story.append(Spacer(1, 2.0))

    # Headless Technology
    s_header = [
        Paragraph("<b>Headless Technology</b> | <font color='#475569'>Web Development &amp; IT Associate</font>", entry_title_style),
        Paragraph("<font color='#475569'>Jan 2019 &ndash; Dec 2020</font>", ParagraphStyle('R6', parent=entry_subtitle_style, alignment=2))
    ]
    ts = Table([s_header], colWidths=[400, 131])
    ts.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('PADDING', (0,0), (-1,-1), 0)]))
    story.append(ts)
    story.append(Spacer(1, 0.5))
    story.append(Paragraph("&bull; Developed and maintained web applications and supported IT infrastructure; managed database updates and implemented technical solutions for client workflows.", bullet_style))
    story.append(Spacer(1, 2.0))

    # Marico Bangladesh Limited
    m_header = [
        Paragraph("<b>Marico Bangladesh Limited</b> | <font color='#475569'>Management Trainee Officer</font>", entry_title_style),
        Paragraph("<font color='#475569'>Jan 2021 &ndash; Feb 2022</font>", ParagraphStyle('R7', parent=entry_subtitle_style, alignment=2))
    ]
    tm = Table([m_header], colWidths=[400, 131])
    tm.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('PADDING', (0,0), (-1,-1), 0)]))
    story.append(tm)
    story.append(Spacer(1, 0.5))
    story.append(Paragraph("&bull; Collaborated with commercial teams to analyze market performance data, evaluate distribution metrics, and prepare quantitative executive reports.", bullet_style))
    story.append(Spacer(1, 2.5))

    # ==========================
    # 4. EDUCATION & QUALIFICATIONS
    # ==========================
    add_section_header("Education &amp; Qualifications")

    edu_isdb = [
        Paragraph("<b>IsDB-BISEW IT Scholarship</b> &mdash; Professional Diploma in Enterprise Systems Development (C# .NET)", entry_title_style),
        Paragraph("<font color='#475569'>2026</font>", ParagraphStyle('R8', parent=entry_subtitle_style, alignment=2))
    ]
    t_edu1 = Table([edu_isdb], colWidths=[430, 101])
    t_edu1.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('PADDING', (0,0), (-1,-1), 0)]))
    story.append(t_edu1)
    story.append(Spacer(1, 1.2))

    edu_du = [
        Paragraph("<b>University of Dhaka</b> &mdash; Bachelor of Social Sciences (B.S.S. Hons) in Economics", entry_title_style),
        Paragraph("<font color='#475569'>2014 &ndash; 2019</font>", ParagraphStyle('R9', parent=entry_subtitle_style, alignment=2))
    ]
    t_edu2 = Table([edu_du], colWidths=[430, 101])
    t_edu2.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('PADDING', (0,0), (-1,-1), 0)]))
    story.append(t_edu2)
    story.append(Paragraph("&bull; Quantitative foundation in Econometrics, Mathematical Statistics, and Analytical Data Modeling.", bullet_style))
    story.append(Spacer(1, 1.5))

    # Credentials row (IELTS Band 7.5 + College)
    cred_row = [
        Paragraph("<b>Certifications &amp; Languages:</b> <b>IELTS Band 7.5</b> (CEFR C1 &mdash; Proficient) &bull; Bengali (Native) &bull; HSC (CPSCR)", entry_subtitle_style),
        Paragraph("<font color='#475569'>Proficient User</font>", ParagraphStyle('R10', parent=entry_subtitle_style, alignment=2))
    ]
    t_cred = Table([cred_row], colWidths=[430, 101])
    t_cred.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('PADDING', (0,0), (-1,-1), 0)]))
    story.append(t_cred)

    doc.build(story)

    # Check page count
    with open(filename, "rb") as f:
        data = f.read()
        page_matches = re.findall(rb'/Type\s*/Page\b', data)
        print(f"Generated {filename} with {len(page_matches)} page(s).")
        if len(page_matches) != 1:
            print("WARNING: Page count is not 1!")

if __name__ == "__main__":
    build_pdf("resume.pdf")
