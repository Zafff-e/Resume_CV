import os
import pymupdf
from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Table, TableStyle, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

def build_modern_resume(pdf_path="AhmZafirHasan_Resume_Modern.pdf"):
    PAGE_W, PAGE_H = A4
    HEADER_H = 104.0
    BODY_H = PAGE_H - HEADER_H

    # Define full-page canvas with zero outer margins
    frame = Frame(0, 0, PAGE_W, PAGE_H, leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0, id='F1')
    template = PageTemplate(id='T1', frames=[frame])
    doc = BaseDocTemplate(pdf_path, pagesize=A4, pageTemplates=[template], pageCompression=0)

    # Palette
    NAVY = colors.HexColor('#0B2545')
    SKY = colors.HexColor('#38BDF8')
    TEXT_DARK = colors.HexColor('#1E293B')
    TEXT_MUTED = colors.HexColor('#475569')
    LINE_MUTED = colors.HexColor('#CBD5E1')
    SIDEBAR_BG = colors.HexColor('#F1F5F9')
    GOLD = colors.HexColor('#F59E0B')

    styles = getSampleStyleSheet()

    # --- Header Styles ---
    name_style = ParagraphStyle(
        'HName',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=20.0,
        leading=23.0,
        textColor=colors.white
    )

    tagline_style = ParagraphStyle(
        'HTagline',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.6,
        leading=11.2,
        textColor=SKY
    )

    contact_style = ParagraphStyle(
        'HContact',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.8,
        leading=10.0,
        textColor=colors.HexColor('#E2E8F0')
    )

    badge_style = ParagraphStyle(
        'HBadge',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=7.4,
        leading=9.0,
        textColor=NAVY,
        alignment=1
    )

    linkedin_style = ParagraphStyle(
        'HLinkedIn',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.6,
        leading=9.5,
        textColor=colors.HexColor('#BAE6FD')
    )

    # --- Content Styles ---
    sec_heading_style = ParagraphStyle(
        'SecHead',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10.2,
        leading=12.8,
        textColor=NAVY,
        spaceBefore=0,
        spaceAfter=0
    )

    summary_style = ParagraphStyle(
        'Summary',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11.6,
        textColor=TEXT_DARK,
        alignment=4
    )

    item_title_style = ParagraphStyle(
        'ItemTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.3,
        leading=11.8,
        textColor=colors.HexColor('#0F172A')
    )

    item_sub_style = ParagraphStyle(
        'ItemSub',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=8.0,
        leading=10.4,
        textColor=TEXT_MUTED
    )

    project_link_style = ParagraphStyle(
        'ProjLink',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.0,
        leading=11.8,
        textColor=colors.HexColor('#0284C7'),
        alignment=2
    )

    def project_header_table(title_markup, url, link_label):
        row = [
            Paragraph(f"<b>{title_markup}</b>", item_title_style),
            Paragraph(f'<a href="{url}"><font color="#0284C7"><b>{link_label}</b></font></a>', project_link_style)
        ]
        t = Table([row], colWidths=[275, 80])
        t.setStyle(TableStyle([
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('PADDING', (0,0), (-1,-1), 0),
            ('TOPPADDING', (0,0), (-1,-1), 0),
            ('BOTTOMPADDING', (0,0), (-1,-1), 0),
        ]))
        return t

    bullet_style = ParagraphStyle(
        'Bullet',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.3,
        leading=11.0,
        textColor=TEXT_DARK,
        leftIndent=9,
        firstLineIndent=-6
    )

    sidebar_cat_style = ParagraphStyle(
        'SidebarCat',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.9,
        leading=11.2,
        textColor=NAVY
    )

    sidebar_val_style = ParagraphStyle(
        'SidebarVal',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.0,
        leading=10.5,
        textColor=TEXT_DARK
    )

    sidebar_edu_deg = ParagraphStyle(
        'EduDeg',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.6,
        leading=11.0,
        textColor=colors.HexColor('#0F172A')
    )

    sidebar_edu_sub = ParagraphStyle(
        'EduSub',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=7.8,
        leading=10.0,
        textColor=TEXT_MUTED
    )

    sidebar_edu_note = ParagraphStyle(
        'EduNote',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.6,
        leading=9.8,
        textColor=TEXT_DARK
    )

    def section_header(title):
        return [
            Paragraph(f"<b>{title.upper()}</b>", sec_heading_style),
            HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceBefore=2.0, spaceAfter=4.5)
        ]

    # ==========================
    # HEADER CONSTRUCTION
    # ==========================
    badge_portfolio = Table(
        [[Paragraph('<a href="https://zafff-e.github.io"><font color="#0B2545"><b>&bull; Portfolio:</b> zafff-e.github.io</font></a>', badge_style)]],
        colWidths=[122], rowHeights=[15.0]
    )
    badge_portfolio.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), GOLD),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
    ]))

    badge_github = Table(
        [[Paragraph('<a href="https://github.com/Zafff-e"><font color="#0B2545"><b>&bull; GitHub:</b> github.com/Zafff-e</font></a>', badge_style)]],
        colWidths=[122], rowHeights=[15.0]
    )
    badge_github.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), GOLD),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
    ]))

    badge_linkedin_style = ParagraphStyle(
        'HBadgeLI',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=7.4,
        leading=9.0,
        textColor=colors.HexColor('#0B2545'),
        alignment=1
    )

    badge_linkedin = Table(
        [[Paragraph('<a href="https://linkedin.com/in/zafir-hasan-developer"><font color="#0B2545"><b>&bull; LinkedIn:</b> in/zafir-hasan-developer</font></a>', badge_linkedin_style)]],
        colWidths=[148], rowHeights=[15.0]
    )
    badge_linkedin.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#38BDF8')),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
    ]))

    badges_bar = Table(
        [[badge_portfolio, badge_github, badge_linkedin]],
        colWidths=[126, 126, 154]
    )
    badges_bar.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('PADDING', (0,0), (-1,-1), 0),
    ]))

    header_elements = [
        Paragraph("AHM ZAFIR HASAN", name_style),
        Spacer(1, 2.0),
        Paragraph("JUNIOR SOFTWARE DEVELOPER &bull; FULL-STACK .NET &amp; WEB SYSTEMS", tagline_style),
        Spacer(1, 3.2),
        Paragraph("Dhaka, Bangladesh &nbsp;&bull;&nbsp; +880 1747 544 273 &nbsp;&bull;&nbsp; <a href=\"mailto:ahmzafirhasan@gmail.com\"><font color=\"#BAE6FD\">ahmzafirhasan@gmail.com</font></a>", contact_style),
        Spacer(1, 4.8),
        badges_bar
    ]

    header_cell = Table([[header_elements]], colWidths=[PAGE_W])
    header_cell.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), NAVY),
        ('LEFTPADDING', (0,0), (-1,-1), 22),
        ('RIGHTPADDING', (0,0), (-1,-1), 22),
        ('TOPPADDING', (0,0), (-1,-1), 12),
        ('BOTTOMPADDING', (0,0), (-1,-1), 10),
    ]))

    # ==========================
    # LEFT COLUMN (MAIN BODY)
    # ==========================
    left = []

    # 1. Summary
    left.extend(section_header("Professional Summary"))
    left.append(Paragraph(
        "Passionate and analytical aspiring Software Developer focused on building reliable, scalable, and user-centric software solutions. Developing expertise in full-stack .NET development, RESTful APIs, database engineering, and modern frontend technologies through the IsDB-BISEW IT Scholarship Programme. Driven by continuous learning, emerging technologies, and solving real-world problems through software engineering, with a strong commitment to professional growth and meaningful contributions to technology-driven teams.",
        summary_style
    ))
    left.append(Spacer(1, 7.5))

    # 2. Featured Projects
    left.extend(section_header("Featured Projects"))

    # Candela
    left.append(project_header_table(
        "Candela &mdash; HSC Physics &amp; Math Mobile App",
        "https://play.google.com/store/apps/details?id=com.polin.kawser.candela&amp;hl=en",
        "Google Play ↗"
    ))
    left.append(Paragraph("Flutter, Dart, Mobile Architecture &bull; <font color='#0B2545'><b>10K+ Installs &bull; 4.6★</b></font>", item_sub_style))
    left.append(Spacer(1, 1.2))
    left.append(Paragraph("&bull; Contributed as co-developer to a production Android educational app live on Google Play Store with <b>10,000+ active installs</b> and a <b>4.6★ user rating across 570+ reviews</b>.", bullet_style))
    left.append(Paragraph("&bull; Structured core formula indexation, offline mathematical study modules, responsive mobile UI views, and optimized client navigation workflows.", bullet_style))
    left.append(Spacer(1, 6.5))

    # ProductCatalogSPA
    left.append(project_header_table(
        "ProductCatalogSPA &amp; Product Management System",
        "https://github.com/Zafff-e/AspNetCore-ProductCatalog-MVC",
        "GitHub ↗"
    ))
    left.append(Paragraph("C#, ASP.NET Core (.NET 9), EF Core, SQL Server, React 19, Angular", item_sub_style))
    left.append(Spacer(1, 1.2))
    left.append(Paragraph("&bull; Architected a high-throughput RESTful Web API with single-controller CRUD routing, normalized Category-Product-Brand relations, and automated database seeding (<font face='Courier' color='#0B2545'><b>EnsureCreated()</b></font>).", bullet_style))
    left.append(Paragraph("&bull; Built dual clients: an Angular client with dynamic brand row insertions and cascading deletes, and a React 19 client with Table and Card/Grid views and instant search filtering.", bullet_style))
    left.append(Spacer(1, 6.5))

    # TechNova
    left.append(project_header_table(
        "TechNova &mdash; Real-Time Tech Hardware E-Commerce",
        "https://github.com/Zafff-e",
        "GitHub ↗"
    ))
    left.append(Paragraph("Node.js, Express.js, MongoDB (Mongoose), WebSockets, bcrypt", item_sub_style))
    left.append(Spacer(1, 1.2))
    left.append(Paragraph("&bull; Developed a full-stack e-commerce hardware store with product catalogs, shopping cart sessions, cash-on-delivery checkout, and normalized MongoDB document models.", bullet_style))
    left.append(Paragraph("&bull; Integrated bi-directional <b>WebSockets (<font face='Courier' color='#0B2545'>ws</font>)</b> to push live inventory levels without polling; automated invoice QR Code generation and transactional emails via Nodemailer.", bullet_style))
    left.append(Spacer(1, 6.5))

    # Employee Master-Details
    left.append(project_header_table(
        "Employee Master-Details Enterprise Management",
        "https://github.com/Zafff-e",
        "GitHub ↗"
    ))
    left.append(Paragraph("ASP.NET Core Web API, EF Core, SQL Server, React 18, TypeScript", item_sub_style))
    left.append(Spacer(1, 1.2))
    left.append(Paragraph("&bull; Developed master-detail persistence resolving multipart payload constraints by combining binary image streams with client-serialized JSON strings (<font face='Courier' color='#0B2545'>EXperiencesString</font>).", bullet_style))
    left.append(Paragraph("&bull; Designed a transactional <b>Wipe &amp; Re-insert</b> pattern in HTTP PUT endpoint to synchronize child collections without orphaned records; applied <font face='Courier' color='#0B2545'><b>AsNoTracking()</b></font> query optimization.", bullet_style))
    left.append(Spacer(1, 7.5))

    # 3. Professional Experience & IT Training
    left.extend(section_header("Professional Experience &amp; IT Training"))

    # IsDB
    left.append(Paragraph("<b>Enterprise Systems Analysis &amp; Design with C# .NET</b>", item_title_style))
    left.append(Paragraph("IsDB-BISEW IT Scholarship Programme (SCSL) &bull; Jan 2026 &ndash; Oct 2026", item_sub_style))
    left.append(Spacer(1, 1.2))
    left.append(Paragraph("&bull; Completed an intensive 9-month professional software development curriculum (Trainee ID: <b>1294926</b>, Round 70), dedicating 1,000+ hours to enterprise software development.", bullet_style))
    left.append(Paragraph("&bull; Built and deployed 8+ full-stack applications; served as backend and database lead on the capstone <b>Skill-Commerce</b> hyperlocal marketplace.", bullet_style))
    left.append(Spacer(1, 6.0))

    # Marico
    left.append(Paragraph("<b>Management Trainee Officer</b>", item_title_style))
    left.append(Paragraph("Marico Bangladesh Limited, Dhaka &bull; 2021 &ndash; 2022", item_sub_style))
    left.append(Spacer(1, 1.2))
    left.append(Paragraph("&bull; Analyzed commercial KPIs, regional market trends, and distribution performance metrics; collaborated with cross-functional commercial teams to deliver quantitative executive presentations.", bullet_style))
    left.append(Spacer(1, 6.0))

    # HSC ICT Instructor & Hardware Specialist
    left.append(Paragraph("<b>HSC ICT Instructor &amp; Hardware Systems Specialist</b>", item_title_style))
    left.append(Paragraph("Academic Mentorship &amp; Tech Services, Dhaka &bull; Academic &amp; Hardware Track", item_sub_style))
    left.append(Spacer(1, 1.2))
    left.append(Paragraph("&bull; Taught national NCTB HSC ICT syllabus to college students: C programming syntax, relational SQL databases, Boolean logic gates, and web design fundamentals.", bullet_style))
    left.append(Paragraph("&bull; Hardware mastery: component-level troubleshooting, repair, custom PC builds, thermal repasting, and BIOS/firmware restorations for laptops and desktops.", bullet_style))

    # ==========================
    # RIGHT COLUMN (SIDEBAR)
    # ==========================
    right = []

    # 1. Technical Skills
    right.extend(section_header("Technical Skills"))

    skills_data = [
        ("Backend Development", "C# (.NET 9/8, .NET Framework 4.8), ASP.NET Core Web API, Minimal APIs, ASP.NET MVC 5, Web API 2, Node.js, Express.js"),
        ("Databases & ORM", "Microsoft SQL Server (T-SQL, Stored Procs, TVPs, Transactions, Schemabound Views, UDFs, Indexing), EF Core, EF6, ADO.NET, MongoDB"),
        ("Frontend & Mobile", "React 19 / 18, TypeScript, JavaScript (ES6+), Angular (Standalone), Flutter/Dart, HTML5, CSS3, Bootstrap 5, Vite, Axios, EJS"),
        ("Architecture & Security", "3-Tier Architecture, Master-Detail Systems, Repository Pattern, Factory Pattern, DTOs, JWT Bearer, OWIN OAuth 2.0, bcrypt, CORS"),
        ("Hardware & Systems", "Desktop & Laptop Hardware Diagnostics & Component Repair, Custom PC Rigs, Thermal Management, BIOS/UEFI Recovery"),
        ("Tools & Platforms", "Visual Studio 2022, VS Code, SSMS, Git, GitHub (Branching, PRs), Postman, Google Play Console, Swagger/OpenAPI, Azure")
    ]

    for cat, items in skills_data:
        right.append(Paragraph(f"<b>{cat}</b>", sidebar_cat_style))
        right.append(Spacer(1, 1.2))
        right.append(Paragraph(items, sidebar_val_style))
        right.append(Spacer(1, 5.5))

    right.append(Spacer(1, 4.0))

    # 2. Education
    right.extend(section_header("Education"))

    edu_data = [
        ("Diploma in Enterprise Systems Development (C# .NET)",
         "IsDB-BISEW IT Scholarship Programme (SCSL), 2026",
         "Enterprise C# OOP, SQL Server, ASP.NET Core Web API, EF Core, React, Angular."),
        ("Bachelor of Social Sciences (B.S.S. Hons) in Economics",
         "University of Dhaka (DU), 2014 – 2019",
         "Quantitative Analysis, Econometrics & Data Modeling."),
        ("Higher Secondary Certificate (HSC)",
         "Cantonment Public School & College, Rangpur (CPSCR), 2011 – 2013",
         "Science (Mathematics, Physics, Chemistry).")
    ]

    for deg, inst, note in edu_data:
        right.append(Paragraph(f"<b>{deg}</b>", sidebar_edu_deg))
        right.append(Spacer(1, 1.0))
        right.append(Paragraph(inst, sidebar_edu_sub))
        right.append(Spacer(1, 1.0))
        right.append(Paragraph(note, sidebar_edu_note))
        right.append(Spacer(1, 5.5))

    right.append(Spacer(1, 3.0))

    # 3. Certifications & Languages
    right.extend(section_header("Certifications & Languages"))

    right.append(Paragraph("<b>IELTS Band 7.5</b> (CEFR Level C1 &mdash; Proficient User)", sidebar_val_style))
    right.append(Spacer(1, 1.0))
    right.append(Paragraph("<font color='#475569'><i>Listening: 8.5 &bull; Reading: 8.0 &bull; Speaking: 7.0 &bull; Writing: 6.5</i></font>", sidebar_edu_note))
    right.append(Spacer(1, 3.5))
    right.append(Paragraph("<b>Bengali:</b> Native &nbsp;&bull;&nbsp; <b>English:</b> Professional Working Fluency", sidebar_val_style))
    right.append(Spacer(1, 3.5))

    # 4. Professional Reference
    right.extend(section_header("Professional Reference"))

    right.append(Paragraph("<b>Nishat Sharmeen</b>", sidebar_edu_deg))
    right.append(Spacer(1, 0.8))
    right.append(Paragraph("Senior Faculty &bull; IsDB-BISEW IT Scholarship Project", sidebar_edu_sub))
    right.append(Spacer(1, 0.8))
    right.append(Paragraph("Cross Platform Apps using ASP.NET, Angular &amp; React", sidebar_edu_note))
    right.append(Spacer(1, 1.2))
    right.append(Paragraph("<a href=\"mailto:nishatsharmeen@gmail.com\"><font color=\"#0284C7\">nishatsharmeen@gmail.com</font></a>", sidebar_edu_note))
    right.append(Spacer(1, 0.8))
    right.append(Paragraph("<a href=\"https://www.linkedin.com/in/nishat-sharmeen-71996132/\"><font color=\"#0284C7\">LinkedIn: in/nishat-sharmeen-71996132</font></a>", sidebar_edu_note))

    # ==========================
    # MASTER 2-COLUMN TABLE
    # ==========================
    col_w_left = PAGE_W * 0.655
    col_w_right = PAGE_W - col_w_left

    master_table_data = [
        [header_cell, ''],
        [left, right]
    ]

    master_table = Table(
        master_table_data,
        colWidths=[col_w_left, col_w_right],
        rowHeights=[HEADER_H, BODY_H]
    )

    master_table.setStyle(TableStyle([
        ('SPAN', (0,0), (1,0)),
        ('PADDING', (0,0), (-1,-1), 0),

        # Left Column Body Styling
        ('BACKGROUND', (0,1), (0,1), colors.white),
        ('VALIGN', (0,1), (0,1), 'TOP'),
        ('LEFTPADDING', (0,1), (0,1), 20),
        ('RIGHTPADDING', (0,1), (0,1), 14),
        ('TOPPADDING', (0,1), (0,1), 10),
        ('BOTTOMPADDING', (0,1), (0,1), 10),

        # Right Column Sidebar Styling
        ('BACKGROUND', (1,1), (1,1), SIDEBAR_BG),
        ('VALIGN', (1,1), (1,1), 'TOP'),
        ('LEFTPADDING', (1,1), (1,1), 14),
        ('RIGHTPADDING', (1,1), (1,1), 18),
        ('TOPPADDING', (1,1), (1,1), 10),
        ('BOTTOMPADDING', (1,1), (1,1), 10),
        ('LINEBEFORE', (1,1), (1,1), 0.75, LINE_MUTED),
    ]))

    doc.build([master_table])
    print(f"Built {pdf_path} successfully.")

if __name__ == '__main__':
    build_modern_resume("AhmZafirHasan_Resume_Modern.pdf")
