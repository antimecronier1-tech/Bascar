#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Génération du PDF complet - Hypnomachie
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib import colors
import os

# Dimensions
PAGE_WIDTH, PAGE_HEIGHT = A4

def lire_fichier_md(chemin):
    """Lit un fichier markdown et retourne son contenu."""
    with open(chemin, 'r', encoding='utf-8') as f:
        return f.read()

def nettoyer_texte(texte):
    """Nettoie le texte pour éviter les problèmes XML."""
    texte = texte.replace('&', '&amp;')
    texte = texte.replace('<', '&lt;')
    texte = texte.replace('>', '&gt;')
    return texte

def parser_markdown(contenu):
    """Parse un fichier markdown simple et retourne une structure."""
    lignes = contenu.split('\n')
    structure = {'titre': '', 'sections': []}
    section_courante = None
    paragraphe_courant = []

    for ligne in lignes:
        ligne_strip = ligne.strip()

        if ligne_strip.startswith('# '):
            structure['titre'] = ligne_strip[2:]
        elif ligne_strip.startswith('## '):
            if section_courante and paragraphe_courant:
                section_courante['paragraphes'].append(' '.join(paragraphe_courant))
                paragraphe_courant = []
            if section_courante:
                structure['sections'].append(section_courante)
            section_courante = {'sous_titre': ligne_strip[3:], 'paragraphes': []}
        elif ligne_strip == '':
            if paragraphe_courant and section_courante:
                section_courante['paragraphes'].append(' '.join(paragraphe_courant))
                paragraphe_courant = []
        else:
            if section_courante:
                paragraphe_courant.append(ligne_strip)

    if paragraphe_courant and section_courante:
        section_courante['paragraphes'].append(' '.join(paragraphe_courant))
    if section_courante:
        structure['sections'].append(section_courante)

    return structure

def create_pdf():
    """Génère le PDF complet."""

    output_path = "/home/user/Bascar/Hypnomachie_Reformulation_Complete.pdf"

    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        rightMargin=2.2*cm,
        leftMargin=2.2*cm,
        topMargin=2*cm,
        bottomMargin=2*cm
    )

    # Styles
    style_titre_principal = ParagraphStyle(
        'TitrePrincipal',
        fontSize=32,
        spaceAfter=15,
        spaceBefore=80,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#1a1a2e'),
        fontName='Helvetica-Bold',
        leading=38
    )

    style_sous_titre = ParagraphStyle(
        'SousTitre',
        fontSize=18,
        spaceAfter=25,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#16213e'),
        fontName='Helvetica-Oblique',
        leading=22
    )

    style_auteur = ParagraphStyle(
        'Auteur',
        fontSize=11,
        spaceAfter=8,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#4a4a4a'),
        fontName='Helvetica',
        leading=14
    )

    style_chapitre = ParagraphStyle(
        'Chapitre',
        fontSize=16,
        spaceAfter=25,
        spaceBefore=15,
        textColor=colors.HexColor('#1a1a2e'),
        fontName='Helvetica-Bold',
        alignment=TA_LEFT,
        leading=20
    )

    style_section = ParagraphStyle(
        'Section',
        fontSize=13,
        spaceAfter=12,
        spaceBefore=20,
        textColor=colors.HexColor('#16213e'),
        fontName='Helvetica-Bold',
        alignment=TA_LEFT,
        leading=16
    )

    style_corps = ParagraphStyle(
        'Corps',
        fontSize=11,
        spaceAfter=10,
        alignment=TA_JUSTIFY,
        leading=16,
        fontName='Helvetica',
        firstLineIndent=20
    )

    style_preambule = ParagraphStyle(
        'Preambule',
        fontSize=11,
        spaceAfter=12,
        alignment=TA_JUSTIFY,
        leading=16,
        fontName='Helvetica-Oblique',
        leftIndent=15,
        rightIndent=15
    )

    style_toc_titre = ParagraphStyle(
        'TOCTitre',
        fontSize=18,
        spaceAfter=30,
        spaceBefore=20,
        textColor=colors.HexColor('#1a1a2e'),
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )

    style_toc_item = ParagraphStyle(
        'TOCItem',
        fontSize=11,
        spaceAfter=8,
        leftIndent=25,
        fontName='Helvetica',
        leading=15
    )

    style_ref_titre = ParagraphStyle(
        'RefTitre',
        fontSize=12,
        spaceAfter=10,
        spaceBefore=18,
        fontName='Helvetica-Bold',
        textColor=colors.HexColor('#1a1a2e')
    )

    style_ref = ParagraphStyle(
        'Ref',
        fontSize=10,
        spaceAfter=4,
        leftIndent=15,
        fontName='Helvetica',
        leading=13
    )

    # Construction du document
    story = []

    # ========== PAGE DE TITRE ==========
    story.append(Spacer(1, 3*cm))
    story.append(Paragraph("HYPNOMACHIE", style_titre_principal))
    story.append(Paragraph("Le Combat contre l'Hypnose Sociale", style_sous_titre))
    story.append(Spacer(1, 1.5*cm))
    story.append(Paragraph("Reformulation de l'entretien", style_auteur))
    story.append(Paragraph("Frédéric Bascunana / Bascar", style_auteur))
    story.append(Spacer(1, 0.8*cm))
    story.append(Paragraph("Partie 2 : Le ruissellement de la perversion", style_auteur))
    story.append(Spacer(1, 3*cm))

    # Ligne décorative
    ligne_style = ParagraphStyle('Ligne', alignment=TA_CENTER, textColor=colors.HexColor('#1a1a2e'))
    story.append(Paragraph("" + chr(8212)*40 + "", ligne_style))

    story.append(PageBreak())

    # ========== TABLE DES MATIÈRES ==========
    story.append(Paragraph("TABLE DES MATIÈRES", style_toc_titre))
    story.append(Spacer(1, 0.5*cm))

    chapitres_toc = [
        "Préambule",
        "Chapitre 1 : L'hypnomachie et la nature de l'hypnose sociale",
        "Chapitre 2 : La néoténie humaine et le trauma comme norme",
        "Chapitre 3 : Dissociation et identification",
        "Chapitre 4 : Le Covid comme laboratoire d'hypnose sociale",
        "Chapitre 5 : La destruction de la mémoire et le présentisme",
        "Chapitre 6 : La pulsion régressive et l'utérus artificiel",
        "Chapitre 7 : Macron et la perversion au pouvoir",
        "Chapitre 8 : Les collectifs liquides et la sortie de l'hypnose",
        "Conclusion",
        "Références citées"
    ]

    for i, titre in enumerate(chapitres_toc):
        story.append(Paragraph(f"{i+1}. {titre}", style_toc_item))

    story.append(PageBreak())

    # ========== PRÉAMBULE ==========
    story.append(Paragraph("PRÉAMBULE", style_chapitre))
    story.append(Spacer(1, 0.3*cm))

    preambule_texte = """Ce document est une reformulation directe, sans langue de bois ni filtre idéologique, d'un entretien de trois heures trente entre Frédéric Bascunana (chaîne Parisiste/Paris Intelligence Collective) et Bascar (chaîne Hypnomachie), avec les interventions d'Alain Gonzalez. L'objectif est de restituer fidèlement la substance des propos tenus, sans édulcoration.

Il ne s'agit pas d'un résumé mais d'une reformulation qui conserve l'intégralité des idées exprimées tout en les organisant de manière plus structurée. Certaines répétitions ont été supprimées, certaines digressions ont été réordonnées, mais rien n'a été censuré ni atténué.

Le lecteur est prévenu : les propos qui suivent sont directs, parfois brutaux, et remettent en question de nombreuses certitudes. Ils ne représentent pas nécessairement l'opinion des personnes ayant participé à la reformulation, mais constituent un matériau de réflexion pour quiconque souhaite comprendre les mécanismes de l'hypnose sociale contemporaine."""

    for para in preambule_texte.split('\n\n'):
        if para.strip():
            story.append(Paragraph(nettoyer_texte(para.strip()), style_preambule))

    story.append(Spacer(1, 0.5*cm))
    story.append(Paragraph("" + chr(8212)*40 + "", ligne_style))
    story.append(PageBreak())

    # ========== CHAPITRES ==========
    fichiers_chapitres = [
        "/home/user/Bascar/Chapitre_01_Hypnomachie.md",
        "/home/user/Bascar/Chapitre_02_Neotenie_Trauma.md",
        "/home/user/Bascar/Chapitre_03_Dissociation_Identification.md",
        "/home/user/Bascar/Chapitre_04_Covid_Laboratoire.md",
        "/home/user/Bascar/Chapitre_05_Destruction_Memoire.md",
        "/home/user/Bascar/Chapitre_06_Pulsion_Regressive.md",
        "/home/user/Bascar/Chapitre_07_Macron_Perversion.md",
        "/home/user/Bascar/Chapitre_08_Collectifs_Liquides.md"
    ]

    for fichier in fichiers_chapitres:
        contenu = lire_fichier_md(fichier)
        structure = parser_markdown(contenu)

        # Titre du chapitre
        story.append(Paragraph(nettoyer_texte(structure['titre']), style_chapitre))

        # Sections
        for section in structure['sections']:
            story.append(Paragraph(nettoyer_texte(section['sous_titre']), style_section))

            for paragraphe in section['paragraphes']:
                if paragraphe.strip():
                    story.append(Paragraph(nettoyer_texte(paragraphe.strip()), style_corps))

        story.append(Spacer(1, 0.3*cm))
        story.append(Paragraph("" + chr(8212)*40 + "", ligne_style))
        story.append(PageBreak())

    # ========== CONCLUSION ==========
    story.append(Paragraph("CONCLUSION", style_chapitre))
    story.append(Paragraph("Vers l'éveil individuel et collectif", style_section))

    conclusion_texte = """Ce parcours à travers les mécanismes de l'hypnose sociale nous amène à une conclusion à la fois sobre et porteuse d'espoir. Sobre, parce que les forces qui maintiennent l'humanité en transe sont puissantes, enracinées, et ne seront pas vaincues par quelques prises de conscience isolées. Porteuse d'espoir, parce que chaque individu qui s'éveille, même partiellement, même temporairement, affaiblit l'emprise du système.

Les points essentiels à retenir sont les suivants. Premièrement, nous sommes presque tous en transe la plupart du temps, que cette transe soit dissociative ou identificatoire. Deuxièmement, cette vulnérabilité est exploitée par les politiciens, les publicitaires et les ingénieurs sociaux de toute obédience. Troisièmement, les mécanismes sont multiples et se renforcent mutuellement : destruction de la mémoire, exploitation de la pulsion régressive, création d'illusions groupales, inversion de la normalité.

Le système se perpétue par substitution permanente : une crise chasse l'autre avant qu'on ait pu analyser la précédente. Il se perpétue aussi par la logique même de l'institution, qui finit toujours par servir sa propre perpétuation plutôt que ses objectifs initiaux. Et il se perpétue par l'inversion de la normalité, où celui qui refuse l'hallucination collective est traité comme un fou.

La sortie passe par le travail individuel, car il ne peut y avoir de changement extérieur sans transformation intérieure. Elle passe par la redescente du mental vers le cœur, par la reconnexion avec l'intelligence du corps et des affects. Elle passe éventuellement par des collectifs liquides, ces formes d'organisation souples qui résistent à la capture par le pouvoir.

Krishna Murti disait : « Ce n'est pas un signe de bonne santé que d'être bien adapté à une société profondément malade. » Cette phrase résonne particulièrement aujourd'hui. Les individus les plus adaptés à notre société sont souvent les plus malades au sens profond, les plus coupés d'eux-mêmes, les plus aliénés.

L'hypnomachie est un combat de longue haleine qui ne connaîtra probablement jamais de victoire finale. Mais ce combat n'est pas vain. Chaque instant d'éveil, aussi bref soit-il, a une valeur inestimable. Ces moments où le voile se déchire, où l'on voit les choses telles qu'elles sont, changent quelque chose en profondeur. Ils laissent une trace qui ne s'efface pas entièrement.

C'est pourquoi il faut continuer le combat, sans espoir excessif mais sans désespoir non plus. Continuer à chercher l'éveil pour soi-même. Continuer à aider ceux qui le cherchent. Continuer à créer des espaces où la transe a moins de prise. C'est tout ce que nous pouvons faire. C'est déjà beaucoup."""

    for para in conclusion_texte.split('\n\n'):
        if para.strip():
            story.append(Paragraph(nettoyer_texte(para.strip()), style_corps))

    story.append(PageBreak())

    # ========== RÉFÉRENCES ==========
    story.append(Paragraph("RÉFÉRENCES CITÉES", style_chapitre))
    story.append(Spacer(1, 0.3*cm))

    story.append(Paragraph("Ouvrages", style_ref_titre))
    refs_livres = [
        "Howard Bloom, Le Principe de Lucifer (tomes 1 et 2)",
        "Pierre Janet, L'automatisme psychologique (1889)",
        "Ernest Hilgard, Divided Consciousness (1977)",
        "Erich Fromm, La peur de la liberté (1941)",
        "Hannah Arendt, Les origines du totalitarisme",
        "Noam Chomsky, La fabrique du consentement",
        "Arthur Koestler, Le zéro et l'infini",
        "Alexandre Zinoviev, Les hauteurs béantes",
        "Norbert Elias, La civilisation des mœurs",
        "François Hartog, Régimes d'historicité",
        "Milan Kundera, Le livre du rire et de l'oubli (1979)",
        "Jean Baudrillard, Simulacres et simulation",
        "Paul Watzlawick, La réalité de la réalité",
        "Didier Anzieu, Le groupe et l'inconscient (1975)",
        "Léon Festinger, L'échec d'une prophétie",
        "Christopher Clark, Les somnambules",
        "Mattias Desmet, Psychologie du totalitarisme"
    ]
    for ref in refs_livres:
        story.append(Paragraph(f"• {nettoyer_texte(ref)}", style_ref))

    story.append(Paragraph("Films", style_ref_titre))
    refs_films = [
        "Inception (Christopher Nolan)",
        "Le complot (sur Popieluszko)",
        "Munich (Steven Spielberg)",
        "L'homme irrationnel (Woody Allen)"
    ]
    for ref in refs_films:
        story.append(Paragraph(f"• {nettoyer_texte(ref)}", style_ref))

    story.append(Paragraph("Concepts clés", style_ref_titre))
    refs_concepts = [
        "Mimésis (René Girard)",
        "Discours du capitaliste (Jacques Lacan)",
        "Violence symbolique (Pierre Bourdieu)",
        "Formation de masse (Mattias Desmet)",
        "Agents de mise en conformité (Howard Bloom)",
        "Régimes d'historicité / Présentisme (François Hartog)",
        "Solve et coagula (tradition alchimique)"
    ]
    for ref in refs_concepts:
        story.append(Paragraph(f"• {nettoyer_texte(ref)}", style_ref))

    # ========== PIED DE PAGE FINAL ==========
    story.append(Spacer(1, 2*cm))
    story.append(Paragraph("" + chr(8212)*40 + "", ligne_style))
    story.append(Spacer(1, 0.5*cm))

    style_footer = ParagraphStyle(
        'Footer',
        fontSize=9,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#666666'),
        fontName='Helvetica-Oblique',
        leading=12
    )
    story.append(Paragraph("Document généré à partir du transcript de l'entretien Parisiste × Hypnomachie", style_footer))
    story.append(Paragraph("Partie 2 : Le ruissellement de la perversion", style_footer))

    # Génération
    doc.build(story)
    print(f"PDF généré : {output_path}")
    return output_path

if __name__ == "__main__":
    create_pdf()
