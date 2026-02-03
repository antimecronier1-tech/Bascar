#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from fpdf import FPDF
import re

class PDF(FPDF):
    def __init__(self):
        super().__init__()
        self.add_font('DejaVu', '', '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', uni=True)
        self.add_font('DejaVu', 'B', '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', uni=True)
        # Pas de police italique disponible, on utilisera la normale avec une couleur différente

    def header(self):
        self.set_font('DejaVu', '', 8)
        self.set_text_color(128, 128, 128)
        self.cell(0, 10, 'Hypnomachie - Le combat contre l\'hypnose sociale', 0, 0, 'C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('DejaVu', '', 8)
        self.set_text_color(128, 128, 128)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def chapter_title(self, title, level=1):
        if level == 1:
            self.set_font('DejaVu', 'B', 18)
            self.set_text_color(0, 51, 102)
        elif level == 2:
            self.set_font('DejaVu', 'B', 14)
            self.set_text_color(51, 51, 51)
        elif level == 3:
            self.set_font('DejaVu', 'B', 12)
            self.set_text_color(80, 80, 80)

        self.ln(5)
        self.multi_cell(0, 8, title)
        self.ln(3)
        self.set_text_color(0, 0, 0)

    def body_text(self, text):
        self.set_font('DejaVu', '', 10)
        self.set_text_color(0, 0, 0)
        self.multi_cell(0, 6, text)
        self.ln(2)

    def bold_text(self, text):
        self.set_font('DejaVu', 'B', 10)
        self.set_text_color(0, 0, 0)
        self.multi_cell(0, 6, text)
        self.ln(2)

    def italic_text(self, text):
        self.set_font('DejaVu', '', 10)
        self.set_text_color(80, 80, 120)
        self.multi_cell(0, 6, text)
        self.ln(2)
        self.set_text_color(0, 0, 0)

def parse_markdown_to_pdf(md_file, pdf_file):
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()

    pdf = PDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    lines = content.split('\n')
    i = 0

    while i < len(lines):
        line = lines[i].strip()

        if not line or line == '---':
            i += 1
            continue

        # Titre niveau 1 (# )
        if line.startswith('# ') and not line.startswith('## '):
            title = line[2:].strip()
            pdf.chapter_title(title, level=1)

        # Titre niveau 2 (## )
        elif line.startswith('## ') and not line.startswith('### '):
            title = line[3:].strip()
            pdf.chapter_title(title, level=2)

        # Titre niveau 3 (### )
        elif line.startswith('### '):
            title = line[4:].strip()
            pdf.chapter_title(title, level=3)

        # Liste à puces
        elif line.startswith('- '):
            text = '  - ' + line[2:]
            pdf.body_text(text)

        # Liste numérotée
        elif re.match(r'^\d+\.', line):
            pdf.body_text('  ' + line)

        # Texte en gras (**texte**)
        elif line.startswith('**') and line.endswith('**'):
            text = line[2:-2]
            pdf.bold_text(text)

        # Citation ou référence
        elif line.startswith('Citation') or line.startswith('"') or line.startswith('*') and line.endswith('*'):
            text = line.strip('*')
            pdf.italic_text(text)

        # Texte normal
        else:
            # Nettoyer le markdown basique
            text = line
            text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)  # Bold
            text = re.sub(r'\*(.+?)\*', r'\1', text)  # Italic
            text = re.sub(r'`(.+?)`', r'\1', text)  # Code
            pdf.body_text(text)

        i += 1

    pdf.output(pdf_file)
    print(f"PDF created: {pdf_file}")

if __name__ == '__main__':
    parse_markdown_to_pdf(
        '/home/user/Bascar/reformulation_hypnomachie.md',
        '/home/user/Bascar/Hypnomachie_Reformulation_Complete.pdf'
    )
