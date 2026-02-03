#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
from reportlab.lib.colors import HexColor
import re
import os
import glob

def create_pdf(md_file, pdf_file):
    doc = SimpleDocTemplate(
        pdf_file,
        pagesize=A4,
        rightMargin=2*cm,
        leftMargin=2*cm,
        topMargin=2*cm,
        bottomMargin=2*cm
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        'Title1',
        parent=styles['Heading1'],
        fontSize=18,
        spaceAfter=20,
        spaceBefore=10,
        textColor=HexColor('#003366'),
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )

    chapter_style = ParagraphStyle(
        'Chapter',
        parent=styles['Heading2'],
        fontSize=14,
        spaceAfter=15,
        spaceBefore=20,
        textColor=HexColor('#333333'),
        fontName='Helvetica-Bold'
    )

    body_style = ParagraphStyle(
        'BodyText',
        parent=styles['Normal'],
        fontSize=11,
        spaceAfter=8,
        spaceBefore=4,
        alignment=TA_JUSTIFY,
        fontName='Helvetica',
        leading=15
    )

    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()

    story = []
    lines = content.split('\n')

    for line in lines:
        line = line.strip()

        if not line:
            continue

        def escape_html(text):
            text = text.replace('&', '&amp;')
            text = text.replace('<', '&lt;')
            text = text.replace('>', '&gt;')
            text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)
            text = re.sub(r'\*(.+?)\*', r'<i>\1</i>', text)
            return text

        if line.startswith('# ') and not line.startswith('## '):
            title = escape_html(line[2:].strip())
            story.append(Paragraph(title, title_style))
            story.append(Spacer(1, 20))

        elif line.startswith('## '):
            title = escape_html(line[3:].strip())
            story.append(Paragraph(title, chapter_style))

        else:
            text = escape_html(line)
            story.append(Paragraph(text, body_style))

    doc.build(story)
    print(f"Created: {pdf_file}")

# Trouver tous les fichiers markdown de chapitres
md_files = sorted(glob.glob('/home/user/Bascar/Chapitre_*.md'))

for md_file in md_files:
    pdf_file = md_file.replace('.md', '.pdf')
    create_pdf(md_file, pdf_file)

print(f"\nTotal: {len(md_files)} PDFs created")
