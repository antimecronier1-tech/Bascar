#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.lib.colors import HexColor
import re

def create_pdf(md_file, pdf_file):
    # Configuration du document
    doc = SimpleDocTemplate(
        pdf_file,
        pagesize=A4,
        rightMargin=2*cm,
        leftMargin=2*cm,
        topMargin=2*cm,
        bottomMargin=2*cm
    )

    # Styles
    styles = getSampleStyleSheet()

    # Titre principal
    title_style = ParagraphStyle(
        'Title1',
        parent=styles['Heading1'],
        fontSize=20,
        spaceAfter=20,
        spaceBefore=30,
        textColor=HexColor('#003366'),
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )

    # Titre de chapitre
    chapter_style = ParagraphStyle(
        'Chapter',
        parent=styles['Heading1'],
        fontSize=16,
        spaceAfter=15,
        spaceBefore=25,
        textColor=HexColor('#003366'),
        fontName='Helvetica-Bold'
    )

    # Sous-titre
    subtitle_style = ParagraphStyle(
        'Subtitle',
        parent=styles['Heading2'],
        fontSize=13,
        spaceAfter=10,
        spaceBefore=15,
        textColor=HexColor('#333333'),
        fontName='Helvetica-Bold'
    )

    # Sous-sous-titre
    subsubtitle_style = ParagraphStyle(
        'Subsubtitle',
        parent=styles['Heading3'],
        fontSize=11,
        spaceAfter=8,
        spaceBefore=12,
        textColor=HexColor('#505050'),
        fontName='Helvetica-Bold'
    )

    # Corps de texte
    body_style = ParagraphStyle(
        'BodyText',
        parent=styles['Normal'],
        fontSize=10,
        spaceAfter=6,
        spaceBefore=3,
        alignment=TA_JUSTIFY,
        fontName='Helvetica',
        leading=14
    )

    # Texte en gras
    bold_style = ParagraphStyle(
        'BoldText',
        parent=body_style,
        fontName='Helvetica-Bold'
    )

    # Texte citation/italique
    italic_style = ParagraphStyle(
        'ItalicText',
        parent=body_style,
        fontName='Helvetica-Oblique',
        textColor=HexColor('#505080'),
        leftIndent=20
    )

    # Liste
    list_style = ParagraphStyle(
        'ListItem',
        parent=body_style,
        leftIndent=20,
        bulletIndent=10
    )

    # Lire le fichier markdown
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Construire le document
    story = []

    lines = content.split('\n')
    i = 0

    while i < len(lines):
        line = lines[i].strip()

        if not line:
            i += 1
            continue

        if line == '---':
            story.append(Spacer(1, 10))
            i += 1
            continue

        # Échapper les caractères spéciaux pour reportlab
        def escape_html(text):
            text = text.replace('&', '&amp;')
            text = text.replace('<', '&lt;')
            text = text.replace('>', '&gt;')
            # Convertir le markdown basique
            text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)
            text = re.sub(r'\*(.+?)\*', r'<i>\1</i>', text)
            return text

        # Titre niveau 1 (# )
        if line.startswith('# ') and not line.startswith('## '):
            title = escape_html(line[2:].strip())
            story.append(Paragraph(title, title_style))

        # Titre niveau 2 (## )
        elif line.startswith('## ') and not line.startswith('### '):
            title = escape_html(line[3:].strip())
            story.append(Paragraph(title, chapter_style))

        # Titre niveau 3 (### )
        elif line.startswith('### '):
            title = escape_html(line[4:].strip())
            story.append(Paragraph(title, subtitle_style))

        # Liste à puces
        elif line.startswith('- '):
            text = escape_html(line[2:])
            story.append(Paragraph(f"• {text}", list_style))

        # Liste numérotée
        elif re.match(r'^\d+\.', line):
            text = escape_html(line)
            story.append(Paragraph(text, list_style))

        # Texte normal
        else:
            text = escape_html(line)
            story.append(Paragraph(text, body_style))

        i += 1

    # Générer le PDF
    doc.build(story)
    print(f"PDF created successfully: {pdf_file}")

if __name__ == '__main__':
    create_pdf(
        '/home/user/Bascar/reformulation_hypnomachie.md',
        '/home/user/Bascar/Hypnomachie_Reformulation_Complete.pdf'
    )
