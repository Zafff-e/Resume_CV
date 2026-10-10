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
    # Margins: 28 pt left/right, 16 pt top/bottom
    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        leftMargin=28,
        rightMargin=28,
        topMargin=16,
        bottomMargin=16,
        pageCompression=0
    )

    styles = getSampleStyleSheet()

    PRIMARY = colors.HexColor("#0B2545")       # Deep Midnight Navy
    SECONDARY = colors.HexColor("#134074")     # Slate Indigo
    ACCENT_LINK = colors.HexColor("#0284C7")   # Sky 600 / Tech Cyan
    TEXT_DARK = colors.HexColor("#0F172A")     # Slate 900
    TEXT_MUTED = colors.HexColor("#475569")    # Slate 600
    LINE_COLOR = colors.HexColor("#CBD5E1")    # Slate 300

    name_style = ParagraphStyle(
        'DocName',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=17.0,
        leading=20.0,
        textColor=PRIMARY,
        alignment=1
    )

    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.4,
        leading=10.8,
        textColor=SECONDARY,
        alignment=1
    )

    contact_style = ParagraphStyle(
        'ContactBar',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.4,
        leading=9.8,
        textColor=TEXT_MUTED,
        alignment=1
    )

    section_header_style = ParagraphStyle(
        'SectionHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.6,
        leading=10.8,
        textColor=PRIMARY,
        spaceBefore=0,
        spaceAfter=0
    )

    summary_style = ParagraphStyle(
        'DocSummary',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.5,
        leading=10.0,
        textColor=TEXT_DARK,
        alignment=4
    )

    entry_title_style = ParagraphStyle(
        'EntryTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.1,
        leading=10.3,
        textColor=TEXT_DARK
    )

    entry_subtitle_style = ParagraphStyle(
        'EntrySubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.5,
        leading=9.8,
        textColor=TEXT_MUTED
    )

    skill_label_style = ParagraphStyle(
        'SkillLabel',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=7.6,
        leading=10.0,
        textColor=TEXT_DARK
    )

    skill_value_style = ParagraphStyle(
        'SkillValue',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.6,
        leading=10.0,
        textColor=TEXT_DARK
    )

    bullet_style = ParagraphStyle(
        'BulletText',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.5,
        leading=9.8,
        textColor=TEXT_DARK,
        leftIndent=9,
        firstLineIndent=-5
    )

    story = []

    # ==========================
    # HEADER
    # ==========================
    story.append(Paragraph("AHM ZAFIR HASAN", name_style))
    story.append(Spacer(1, 1.0))
    story.append(Paragraph("JUNIOR SOFTWARE ENGINEER &bull; FULL-STACK .NET &amp; WEB SYSTEMS", title_style))
    story.append(Spacer(1, 1.2))
    
    contact_line_1 = [
        "Dhaka, Bangladesh",
        "+880 1747 544 273",
        '<a href="mailto:ahmzafirhasan@gmail.com"><font color="#0284C7">ahmzafirhasan@gmail.com</font></a>'
    ]
    story.append(Paragraph(" &nbsp;&bull;&nbsp; ".join(contact_line_1), contact_style))
    story.append(Spacer(1, 0.6))

    contact_line_2 = [
        '<a href="https://zafff-e.github.io"><font color="#0284C7"><b>Portfolio:</b> zafff-e.github.io</font></a>',
        '<a href="https://github.com/Zafff-e"><font color="#0284C7"><b>GitHub:</b> github.com/Zafff-e</font></a>',
        '<a href="https://linkedin.com/in/zafir-hasan-developer"><font color="#0284C7"><b>LinkedIn:</b> in/zafir-hasan-developer</font></a>'
    ]
    story.append(Paragraph(" &nbsp;&bull;&nbsp; ".join(contact_line_2), contact_style))
    story.append(Spacer(1, 2.0))
    story.append(HRFlowable(width="100%", thickness=1.0, color=PRIMARY, spaceBefore=0, spaceAfter=2.0))

    def add_section_header(title):
        p = Paragraph(f"<b>{title.upper()}</b>", section_header_style)
        story.append(p)
        story.append(HRFlowable(width="100%", thickness=0.5, color=LINE_COLOR, spaceBefore=0.6, spaceAfter=1.8))

    # ==========================
    # 1. PROFESSIONAL SUMMARY
    # ==========================
    add_section_header("Professional Summary")
    story.append(Paragraph(
        "Passionate and analytical aspiring Software Developer focused on building reliable, scalable, and user-centric software solutions. Developing expertise in full-stack .NET development, RESTful APIs, database engineering, and modern frontend technologies through the IsDB-BISEW IT Scholarship Programme. Driven by continuous learning, emerging technologies, and solving real-world problems through software engineering, with a strong commitment to professional growth and meaningful contributions to technology-driven teams.",
        summary_style
    ))
    story.append(Spacer(1, 1.8))

    # ==========================
    # 2. TECHNICAL SKILLS
    # ==========================
    add_section_header("Technical Skills")
    
    skills = [
        ("Backend Development", "C# (.NET 9/8, .NET Framework 4.8), ASP.NET Core Web API, Minimal APIs, ASP.NET MVC 5, Web API 2, Node.js, Express.js"),
        ("Databases & ORM", "Microsoft SQL Server (T-SQL, Stored Procs, TVPs, Transactions, Schemabound Views, UDFs, Indexing), EF Core, EF6, ADO.NET, MongoDB"),
        ("Frontend & Mobile", "React 19 / 18, TypeScript, JavaScript (ES6+), Angular (Standalone), Flutter/Dart, HTML5, CSS3, Bootstrap 5, Vite, Axios, EJS"),
        ("Architecture & Security", "3-Tier Architecture, Master-Detail Systems, Repository Pattern, Factory Pattern, DTOs, JWT Bearer, OWIN OAuth 2.0, bcrypt, CORS"),
        ("Hardware & Systems", "Desktop & Laptop Hardware Diagnostics & Component Repair, Custom PC Rigs, Thermal Management, BIOS/UEFI Recovery"),
        ("Tools & Platforms", "Visual Studio 2022, VS Code, SSMS, Git, GitHub (Branching, PRs), Postman, Google Play Console, Swagger/OpenAPI, Azure")
    ]
    
    skill_rows = []
    for category, items in skills:
        col1 = Paragraph(f"&bull; <b>{category}:</b>", skill_label_style)
        col2 = Paragraph(items, skill_value_style)
        skill_rows.append([col1, col2])

    skill_table = Table(skill_rows, colWidths=[120, 419])
    skill_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 0.1),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0.1),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(skill_table)
    story.append(Spacer(1, 1.8))

    # ==========================
    # 3. FEATURED SOFTWARE & MOBILE PROJECTS
    # ==========================
    add_section_header("Featured Software &amp; Mobile Projects")

    # Project 1: Candela (Google Play Store 10K+ App)
    candela_header = [
        Paragraph("<b>Candela &mdash; HSC Physics &amp; Math Mobile App</b> | <font color='#475569'><i>Flutter, Dart, Mobile Architecture &bull; <b>10K+ Installs &bull; 4.6★</b></i></font>", entry_title_style),
        Paragraph('<a href="https://play.google.com/store/apps/details?id=com.polin.kawser.candela&amp;hl=en"><font color="#0284C7"><b>Google Play ↗</b></font></a>', ParagraphStyle('R_Candela', parent=entry_subtitle_style, alignment=2))
    ]
    t_candela = Table([candela_header], colWidths=[455, 84])
    t_candela.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('PADDING', (0,0), (-1,-1), 0)]))
    story.append(t_candela)
    story.append(Spacer(1, 0.3))
    story.append(Paragraph("&bull; Contributed as co-developer to production Android educational app live on <b>Google Play Store with 10,000+ active installs</b> and a <b>4.6★ user rating across 570+ reviews</b>.", bullet_style))
    story.append(Paragraph("&bull; Structured core formula indexation, offline mathematical study modules, responsive mobile UI views, and optimized client navigation workflows.", bullet_style))
    story.append(Spacer(1, 1.6))

    # Project 2: ProductCatalogSPA
    p1_header = [
        Paragraph("<b>ProductCatalogSPA &amp; Product Management System</b> | <font color='#475569'><i>C#, ASP.NET Core (.NET 9), EF Core, SQL Server, React 19, Angular</i></font>", entry_title_style),
        Paragraph('<a href="https://github.com/Zafff-e/AspNetCore-ProductCatalog-MVC"><font color="#0284C7"><b>GitHub ↗</b></font></a>', ParagraphStyle('R1', parent=entry_subtitle_style, alignment=2))
    ]
    t1 = Table([p1_header], colWidths=[460, 79])
    t1.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('PADDING', (0,0), (-1,-1), 0)]))
    story.append(t1)
    story.append(Spacer(1, 0.3))
    story.append(Paragraph("&bull; Architected high-throughput RESTful Web API with single-controller CRUD routing, normalized Category-Product-Brand relations, and automated database seeding (`EnsureCreated()`).", bullet_style))
    story.append(Paragraph("&bull; Built dual clients: Angular client with dynamic brand row insertions and cascading deletes; React 19 client with Table and Card/Grid views and instant search filtering.", bullet_style))
    story.append(Spacer(1, 1.6))

    # Project 3: TechNova E-Commerce
    p2_header = [
        Paragraph("<b>TechNova &mdash; Real-Time Tech Hardware E-Commerce</b> | <font color='#475569'><i>Node.js, Express.js, MongoDB (Mongoose), WebSockets, bcrypt</i></font>", entry_title_style),
        Paragraph('<a href="https://github.com/Zafff-e"><font color="#0284C7"><b>GitHub ↗</b></font></a>', ParagraphStyle('R2', parent=entry_subtitle_style, alignment=2))
    ]
    t2 = Table([p2_header], colWidths=[460, 79])
    t2.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('PADDING', (0,0), (-1,-1), 0)]))
    story.append(t2)
    story.append(Spacer(1, 0.3))
    story.append(Paragraph("&bull; Developed full-stack e-commerce hardware store with product catalogs, shopping cart sessions, cash-on-delivery checkout, and MongoDB normalized document models.", bullet_style))
    story.append(Paragraph("&bull; Integrated bi-directional <b>WebSockets (`ws`)</b> to push live inventory levels without polling; automated invoice QR Code generation and transactional emails via Nodemailer.", bullet_style))
    story.append(Spacer(1, 1.6))

    # Project 4: Employee Master-Details
    p3_header = [
        Paragraph("<b>Employee Master-Details Enterprise Management</b> | <font color='#475569'><i>ASP.NET Core Web API, EF Core, SQL Server, React 18, TypeScript</i></font>", entry_title_style),
        Paragraph('<a href="https://github.com/Zafff-e"><font color="#0284C7"><b>GitHub ↗</b></font></a>', ParagraphStyle('R3', parent=entry_subtitle_style, alignment=2))
    ]
    t3 = Table([p3_header], colWidths=[460, 79])
    t3.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('PADDING', (0,0), (-1,-1), 0)]))
    story.append(t3)
    story.append(Spacer(1, 0.3))
    story.append(Paragraph("&bull; Engineered master-detail persistence resolving multipart payload constraints by combining binary image streams with client-serialized JSON strings (`EXperiencesString`).", bullet_style))
    story.append(Paragraph("&bull; Designed transactional <b>Wipe &amp; Re-insert</b> pattern in HTTP PUT endpoint to synchronize child collections without orphaned records; applied `AsNoTracking()` query optimization.", bullet_style))
    story.append(Spacer(1, 1.8))

    # ==========================
    # 4. PROFESSIONAL EXPERIENCE & IT TRAINING
    # ==========================
    add_section_header("Professional Experience &amp; IT Training")

    # IsDB Training
    tr_header = [
        Paragraph("<b>Enterprise Systems Analysis &amp; Design with C# .NET</b> &mdash; <i>IsDB-BISEW IT Scholarship Programme (SCSL)</i>", entry_title_style),
        Paragraph("<font color='#475569'>Jan 2026 &ndash; Oct 2026</font>", ParagraphStyle('R5', parent=entry_subtitle_style, alignment=2))
    ]
    t_tr = Table([tr_header], colWidths=[424, 115])
    t_tr.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('PADDING', (0,0), (-1,-1), 0)]))
    story.append(t_tr)
    story.append(Spacer(1, 0.3))
    story.append(Paragraph("&bull; Completed intensive 9-month professional software engineering curriculum (Trainee ID: <b>1294926</b>, Round 70), dedicating 1,000+ hours to enterprise software development.", bullet_style))
    story.append(Paragraph("&bull; Built and deployed 8+ full-stack applications; served as backend and database lead on capstone <b>Skill-Commerce</b> hyperlocal marketplace.", bullet_style))
    story.append(Spacer(1, 1.5))

    # Marico Bangladesh Limited
    m_header = [
        Paragraph("<b>Management Trainee Officer</b> &mdash; <i>Marico Bangladesh Limited, Dhaka</i>", entry_title_style),
        Paragraph("<font color='#475569'>2021 &ndash; 2022</font>", ParagraphStyle('R6', parent=entry_subtitle_style, alignment=2))
    ]
    tm = Table([m_header], colWidths=[424, 115])
    tm.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('PADDING', (0,0), (-1,-1), 0)]))
    story.append(tm)
    story.append(Spacer(1, 0.3))
    story.append(Paragraph("&bull; Analyzed commercial KPIs, regional market trends, and distribution performance metrics; collaborated with cross-functional commercial teams to deliver quantitative executive presentations.", bullet_style))
    story.append(Spacer(1, 1.5))

    # HSC ICT Instructor & Hardware Specialist
    inst_header = [
        Paragraph("<b>HSC ICT Instructor &amp; Hardware Systems Specialist</b> &mdash; <i>Academic Mentorship &amp; Tech Services, Dhaka</i>", entry_title_style),
        Paragraph("<font color='#475569'>Academic &amp; Hardware Track</font>", ParagraphStyle('R7', parent=entry_subtitle_style, alignment=2))
    ]
    t_inst = Table([inst_header], colWidths=[395, 144])
    t_inst.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('PADDING', (0,0), (-1,-1), 0)]))
    story.append(t_inst)
    story.append(Spacer(1, 0.3))
    story.append(Paragraph("&bull; Taught national NCTB HSC ICT syllabus to college students: C programming syntax, relational SQL databases, Boolean logic gates, and web design fundamentals.", bullet_style))
    story.append(Paragraph("&bull; Lifelong hardware mastery: component-level troubleshooting, repair, custom PC builds, thermal repasting, and BIOS/firmware restorations for laptops and desktops.", bullet_style))
    story.append(Spacer(1, 1.8))

    # ==========================
    # 5. EDUCATION & CERTIFICATIONS
    # ==========================
    add_section_header("Education &amp; Qualifications")

    edu_rows = [
        [
            Paragraph("<b>Diploma in Enterprise Systems Development (C# .NET)</b> &mdash; IsDB-BISEW IT Scholarship Programme (SCSL)", entry_title_style),
            Paragraph("<font color='#475569'>2026</font>", ParagraphStyle('R8', parent=entry_subtitle_style, alignment=2))
        ],
        [
            Paragraph("<b>Bachelor of Social Sciences (B.S.S. Hons) in Economics</b> &mdash; University of Dhaka (DU)", entry_title_style),
            Paragraph("<font color='#475569'>2014 &ndash; 2019</font>", ParagraphStyle('R9', parent=entry_subtitle_style, alignment=2))
        ],
        [
            Paragraph("<b>Certifications &amp; Languages:</b> <b>IELTS Band 7.5</b> (CEFR C1 &mdash; Proficient) &bull; Bengali (Native) &bull; HSC (CPSCR)", entry_subtitle_style),
            Paragraph("<font color='#475569'>CEFR C1 Proficient</font>", ParagraphStyle('R10', parent=entry_subtitle_style, alignment=2))
        ]
    ]
    t_edu = Table(edu_rows, colWidths=[429, 110])
    t_edu.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 0.25),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0.25),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(t_edu)

    doc.build(story)

    with open(filename, "rb") as f:
        data = f.read()
        page_matches = re.findall(rb'/Type\s*/Page\b', data)
        print(f"Generated {filename} with {len(page_matches)} page(s).")
        if len(page_matches) != 1:
            print("WARNING: Page count is not 1!")

if __name__ == "__main__":
    build_pdf("resume.pdf")
