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
    # Margins: 30 pt left/right, 18 pt top/bottom
    # pageCompression=0 ensures maximum ATS plain-text parsing across all engines
    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        leftMargin=30,
        rightMargin=30,
        topMargin=18,
        bottomMargin=18,
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
        fontSize=17.5,
        leading=20.5,
        textColor=PRIMARY,
        alignment=1 # Center
    )

    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11.0,
        textColor=SECONDARY,
        alignment=1
    )

    contact_style = ParagraphStyle(
        'ContactBar',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.5,
        leading=10.0,
        textColor=TEXT_MUTED,
        alignment=1
    )

    section_header_style = ParagraphStyle(
        'SectionHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.8,
        leading=11.0,
        textColor=PRIMARY,
        spaceBefore=0,
        spaceAfter=0
    )

    summary_style = ParagraphStyle(
        'DocSummary',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.6,
        leading=10.2,
        textColor=TEXT_DARK,
        alignment=4 # Justify
    )

    entry_title_style = ParagraphStyle(
        'EntryTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.2,
        leading=10.5,
        textColor=TEXT_DARK
    )

    entry_subtitle_style = ParagraphStyle(
        'EntrySubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.6,
        leading=10.0,
        textColor=TEXT_MUTED
    )

    skill_label_style = ParagraphStyle(
        'SkillLabel',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=7.7,
        leading=10.2,
        textColor=TEXT_DARK
    )

    skill_value_style = ParagraphStyle(
        'SkillValue',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.7,
        leading=10.2,
        textColor=TEXT_DARK
    )

    bullet_style = ParagraphStyle(
        'BulletText',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.6,
        leading=10.0,
        textColor=TEXT_DARK,
        leftIndent=9,
        firstLineIndent=-5
    )

    story = []

    # ==========================
    # HEADER (Live Portfolio + GitHub + LinkedIn + Contact)
    # ==========================
    story.append(Paragraph("AHM ZAFIR HASAN", name_style))
    story.append(Spacer(1, 1.0))
    story.append(Paragraph("JUNIOR SOFTWARE ENGINEER &bull; FULL-STACK .NET &amp; WEB SYSTEMS", title_style))
    story.append(Spacer(1, 1.5))
    
    contact_line_1 = [
        "Dhaka, Bangladesh",
        "+880 1747 544 273",
        '<a href="mailto:ahmzafirhasan@gmail.com"><font color="#0284C7">ahmzafirhasan@gmail.com</font></a>'
    ]
    story.append(Paragraph(" &nbsp;&bull;&nbsp; ".join(contact_line_1), contact_style))
    story.append(Spacer(1, 0.8))

    contact_line_2 = [
        '<a href="https://zafff-e.github.io"><font color="#0284C7"><b>Portfolio:</b> zafff-e.github.io</font></a>',
        '<a href="https://github.com/Zafff-e"><font color="#0284C7"><b>GitHub:</b> github.com/Zafff-e</font></a>',
        '<a href="https://linkedin.com/in/zafir-hasan-developer"><font color="#0284C7"><b>LinkedIn:</b> in/zafir-hasan-developer</font></a>'
    ]
    story.append(Paragraph(" &nbsp;&bull;&nbsp; ".join(contact_line_2), contact_style))
    story.append(Spacer(1, 2.5))
    story.append(HRFlowable(width="100%", thickness=1.0, color=PRIMARY, spaceBefore=0, spaceAfter=2.5))

    # Helper for Section Title with line
    def add_section_header(title):
        p = Paragraph(f"<b>{title.upper()}</b>", section_header_style)
        story.append(p)
        story.append(HRFlowable(width="100%", thickness=0.5, color=LINE_COLOR, spaceBefore=0.8, spaceAfter=2.0))

    # ==========================
    # 1. PROFESSIONAL SUMMARY
    # ==========================
    add_section_header("Professional Summary")
    story.append(Paragraph(
        "Results-driven <b>Junior Software Engineer / Full-Stack .NET Developer</b> with hands-on enterprise application development training via the prestigious <b>IsDB-BISEW IT Scholarship Programme</b> (Round 70, Trainee ID: 1294926). Proficient in building high-performance RESTful Web APIs, scalable relational databases, and dynamic SPAs using <b>C#, ASP.NET Core (.NET 9/8), EF Core, SQL Server (T-SQL), React 19, and Angular</b>. Strong expertise in software engineering patterns (Repository, Factory, DTOs), multi-tier architecture, and real-time WebSockets. Grounded in quantitative analysis with an Economics degree from the <b>University of Dhaka</b> and an <b>IELTS Band 7.5</b>.",
        summary_style
    ))
    story.append(Spacer(1, 2.0))

    # ==========================
    # 2. TECHNICAL SKILLS
    # ==========================
    add_section_header("Technical Skills")
    
    skills = [
        ("Backend Development", "C# (.NET 9/8, .NET Framework 4.8), ASP.NET Core Web API, Minimal APIs, ASP.NET MVC 5, Web API 2, Node.js, Express.js"),
        ("Databases & ORM", "Microsoft SQL Server (T-SQL, Stored Procs, TVPs, Transactions, Schemabound Views, UDFs, Indexing), EF Core, EF6, ADO.NET, MongoDB"),
        ("Frontend Development", "React 19 / 18, TypeScript, JavaScript (ES6+), Angular (Standalone Components), HTML5, CSS3, Bootstrap 5, Vite, Axios, EJS"),
        ("Architecture & Security", "3-Tier Architecture, Master-Detail Relational Architecture, Repository Pattern, Factory Pattern, DTOs, JWT Bearer, OWIN OAuth, bcrypt"),
        ("Tools & Platforms", "Visual Studio 2022, VS Code, SQL Server Management Studio (SSMS), Git, GitHub (Branching, PRs), Postman, Swagger/OpenAPI")
    ]
    
    skill_rows = []
    for category, items in skills:
        col1 = Paragraph(f"&bull; <b>{category}:</b>", skill_label_style)
        col2 = Paragraph(items, skill_value_style)
        skill_rows.append([col1, col2])

    skill_table = Table(skill_rows, colWidths=[125, 410])
    skill_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 0.15),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0.15),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(skill_table)
    story.append(Spacer(1, 2.0))

    # ==========================
    # 3. FEATURED SOFTWARE PROJECTS
    # ==========================
    add_section_header("Featured Software Projects")

    # Project 1: ProductCatalogSPA
    p1_header = [
        Paragraph("<b>ProductCatalogSPA &amp; Product Management System</b> | <font color='#475569'><i>C#, ASP.NET Core (.NET 9), EF Core, SQL Server, React 19, Angular</i></font>", entry_title_style),
        Paragraph('<a href="https://github.com/Zafff-e/AspNetCore-ProductCatalog-MVC"><font color="#0284C7"><b>GitHub ↗</b></font></a>', ParagraphStyle('R1', parent=entry_subtitle_style, alignment=2))
    ]
    t1 = Table([p1_header], colWidths=[460, 75])
    t1.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('PADDING', (0,0), (-1,-1), 0)]))
    story.append(t1)
    story.append(Spacer(1, 0.4))
    story.append(Paragraph("&bull; Architected high-throughput RESTful Web API with single-controller CRUD routing, normalized Category-Product-Brand relations, and automated database seeding (`EnsureCreated()`).", bullet_style))
    story.append(Paragraph("&bull; Built dual clients: Angular client with dynamic brand row insertions and cascading deletes; React 19 client with Table and Card/Grid views and instant search filtering.", bullet_style))
    story.append(Paragraph("&bull; Implemented secure `multipart/form-data` image streaming with GUID file naming to prevent collisions, zero-latency previews, and JWT authentication.", bullet_style))
    story.append(Spacer(1, 1.8))

    # Project 2: TechNova E-Commerce
    p2_header = [
        Paragraph("<b>TechNova &mdash; Real-Time Tech Hardware E-Commerce</b> | <font color='#475569'><i>Node.js, Express.js, MongoDB (Mongoose), WebSockets, bcrypt</i></font>", entry_title_style),
        Paragraph('<a href="https://github.com/Zafff-e"><font color="#0284C7"><b>GitHub ↗</b></font></a>', ParagraphStyle('R2', parent=entry_subtitle_style, alignment=2))
    ]
    t2 = Table([p2_header], colWidths=[460, 75])
    t2.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('PADDING', (0,0), (-1,-1), 0)]))
    story.append(t2)
    story.append(Spacer(1, 0.4))
    story.append(Paragraph("&bull; Developed full-stack e-commerce hardware store with product catalogs, shopping cart sessions, cash-on-delivery checkout, and MongoDB normalized document models.", bullet_style))
    story.append(Paragraph("&bull; Integrated bi-directional <b>WebSockets (`ws`)</b> to push live inventory levels and order status updates without polling; enforced bcrypt password hashing.", bullet_style))
    story.append(Paragraph("&bull; Automated transactional order confirmations via Nodemailer and generated dynamic QR Codes for invoice retrieval and package delivery tracking.", bullet_style))
    story.append(Spacer(1, 1.8))

    # Project 3: Employee Master-Details
    p3_header = [
        Paragraph("<b>Employee Master-Details Enterprise Management</b> | <font color='#475569'><i>ASP.NET Core Web API, EF Core, SQL Server, React 18, TypeScript</i></font>", entry_title_style),
        Paragraph('<a href="https://github.com/Zafff-e"><font color="#0284C7"><b>GitHub ↗</b></font></a>', ParagraphStyle('R3', parent=entry_subtitle_style, alignment=2))
    ]
    t3 = Table([p3_header], colWidths=[460, 75])
    t3.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('PADDING', (0,0), (-1,-1), 0)]))
    story.append(t3)
    story.append(Spacer(1, 0.4))
    story.append(Paragraph("&bull; Engineered master-detail persistence resolving multipart payload constraints by combining binary image streams with client-serialized JSON strings (`EXperiencesString`).", bullet_style))
    story.append(Paragraph("&bull; Designed transactional <b>Wipe &amp; Re-insert</b> pattern in HTTP PUT endpoint to synchronize child collections without orphaned records; applied `AsNoTracking()` read optimization.", bullet_style))
    story.append(Paragraph("&bull; Built memory-safe UI state using `crypto.randomUUID()` for Virtual DOM stability and `URL.revokeObjectURL()` to eliminate client memory leaks during uploads.", bullet_style))
    story.append(Spacer(1, 1.8))

    # Project 4: Skill-Commerce Capstone / ShortAPI
    p4_header = [
        Paragraph("<b>Skill-Commerce Marketplace &amp; Supply Chain Web API (ShortAPI)</b> | <font color='#475569'><i>C#, ASP.NET Core, OWIN OAuth 2.0, SQL Server, Postman</i></font>", entry_title_style),
        Paragraph('<a href="https://github.com/Zafff-e"><font color="#0284C7"><b>GitHub ↗</b></font></a>', ParagraphStyle('R4', parent=entry_subtitle_style, alignment=2))
    ]
    t4 = Table([p4_header], colWidths=[460, 75])
    t4.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('PADDING', (0,0), (-1,-1), 0)]))
    story.append(t4)
    story.append(Spacer(1, 0.4))
    story.append(Paragraph("&bull; Backend &amp; database lead on capstone booking platform: architected relational schema, appointment booking states, and 15+ normalized REST API endpoints.", bullet_style))
    story.append(Paragraph("&bull; Built enterprise REST API secured by OWIN OAuth 2.0 tokens, custom `MultipartFormatter` for combined JSON and raw byte arrays, and verified via Postman test suites.", bullet_style))
    story.append(Spacer(1, 2.0))

    # ==========================
    # 4. PROFESSIONAL EXPERIENCE & IT TRAINING
    # ==========================
    add_section_header("Professional Experience &amp; IT Training")

    # IsDB Training
    tr_header = [
        Paragraph("<b>Enterprise Systems Analysis &amp; Design with C# .NET</b> &mdash; <i>IsDB-BISEW IT Scholarship Programme (SCSL)</i>", entry_title_style),
        Paragraph("<font color='#475569'>Jan 2026 &ndash; Oct 2026</font>", ParagraphStyle('R5', parent=entry_subtitle_style, alignment=2))
    ]
    t_tr = Table([tr_header], colWidths=[420, 115])
    t_tr.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('PADDING', (0,0), (-1,-1), 0)]))
    story.append(t_tr)
    story.append(Spacer(1, 0.3))
    story.append(Paragraph("&bull; Completed intensive 9-month professional software engineering curriculum (Trainee ID: <b>1294926</b>, Round 70), dedicating 1,000+ hours to enterprise software development.", bullet_style))
    story.append(Paragraph("&bull; Built and deployed 8+ full-stack and multi-tier applications across desktop, web, and cloud; served as backend and database lead on capstone <b>Skill-Commerce</b> marketplace.", bullet_style))
    story.append(Spacer(1, 1.6))

    # Marico Bangladesh Limited
    m_header = [
        Paragraph("<b>Management Trainee Officer</b> &mdash; <i>Marico Bangladesh Limited, Dhaka</i>", entry_title_style),
        Paragraph("<font color='#475569'>2021 &ndash; 2022</font>", ParagraphStyle('R6', parent=entry_subtitle_style, alignment=2))
    ]
    tm = Table([m_header], colWidths=[420, 115])
    tm.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('PADDING', (0,0), (-1,-1), 0)]))
    story.append(tm)
    story.append(Spacer(1, 0.3))
    story.append(Paragraph("&bull; Analyzed business KPIs, regional market trends, and distribution performance metrics; collaborated with cross-functional commercial teams to deliver quantitative executive presentations.", bullet_style))
    story.append(Spacer(1, 1.6))

    # IT Instructor / Coordinator
    inst_header = [
        Paragraph("<b>IT Workshop Coordinator / ICT Instructor</b> &mdash; <i>Freelance / Community Initiatives, Dhaka</i>", entry_title_style),
        Paragraph("<font color='#475569'>Prior Experience</font>", ParagraphStyle('R7', parent=entry_subtitle_style, alignment=2))
    ]
    t_inst = Table([inst_header], colWidths=[420, 115])
    t_inst.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('PADDING', (0,0), (-1,-1), 0)]))
    story.append(t_inst)
    story.append(Spacer(1, 0.3))
    story.append(Paragraph("&bull; Instructed students and trainees in computer fundamentals, relational database logic, and productivity workflows.", bullet_style))
    story.append(Spacer(1, 2.0))

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
    t_edu = Table(edu_rows, colWidths=[425, 110])
    t_edu.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 0.3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0.3),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(t_edu)

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
