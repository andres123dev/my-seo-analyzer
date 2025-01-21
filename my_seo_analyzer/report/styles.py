#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ =        "Andrés Fernández Burón"
__name__ =          "styles"
__description__ =   "Styles for the generated SEO report document."
__copyright__ =     "Copyright 2022-2025, Andres Fernandez Buron"
__license__ =       "Andres Fernandez Buron, All rights reserved"
__date__ =          "15-05-2022"
__status__ =        "Development"
__version__ =       "0.1"
__maintainer__ =    "Andres Fernandez Buron"
__email__ =         "https://github.com/andres123dev/my-seo-analyzer/new/choose"


from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

from reportlab.platypus import TableStyle

from reportlab.lib import colors

# Estilos personalizados
styles = getSampleStyleSheet()
    
title_style = ParagraphStyle(
    name='TitleStyle',
    parent=styles['Title'],
    fontSize=28,
    fontName='Helvetica-Bold',
    textColor=colors.royalblue,
    alignment=1,  # 1 para centrar el texto
    spaceAfter=20
)

heading1_style = ParagraphStyle(
    name='Heading1Style',
    parent=styles['Heading1'],
    fontSize=18,
    fontName='Helvetica-Bold',
    textColor=colors.darkblue,
    alignment=1,  # 1 para centrar el texto
    spaceBefore=14,
    spaceAfter=14,
)
heading2_style = ParagraphStyle(
    name='Heading2Style',
    parent=styles['Heading2'],
    fontSize=16,
    fontName='Helvetica-Bold',
    textColor=colors.navy,
    spaceBefore=14,
    spaceAfter=14,
)

toc_heading1_style = ParagraphStyle(
    name='TocHeading1Style',
    parent=styles['Heading1'],
    fontSize=14,
    fontName='Helvetica',
    textColor=colors.darkblue,
    leading=4,
    spaceBefore=4,
    spaceAfter=4,
)
toc_heading2_style = ParagraphStyle(
    name='TocHeading2Style',
    parent=styles['Heading2'],
    fontSize=14,
    fontName='Times-Roman',
    textColor=colors.navy,
    leading=4,
    spaceBefore=2,
    spaceAfter=2,
    leftIndent=30,
)

normal_style = ParagraphStyle(
    name='NormalStyle',
    parent=styles['Normal'],
    fontSize=10,
    fontName='Helvetica',
    textColor=colors.royalblue,
    spaceAfter=12
)
bold_style = ParagraphStyle(
    name='BoldStyle',
    parent=normal_style,
    fontName='Helvetica-Bold',
)
black_style = ParagraphStyle(
    name='BoldStyle',
    parent=normal_style,
    textColor=colors.black,
)
anchor_style = ParagraphStyle(
    name='AnchorStyle',
    parent=normal_style,
    textColor=colors.purple
)
ok_style = ParagraphStyle(
    name='OkStyle',
    parent=normal_style,
    textColor=colors.forestgreen
)
error_style = ParagraphStyle(
    name='ErrorStyle',
    parent=normal_style,
    textColor=colors.darkred
)
table_text_style = ParagraphStyle(
    name='ErrorStyle',
    parent=normal_style,
    fontSize=10,
    fontName='Helvetica',
    textColor=colors.navy
)
table_style = TableStyle([
    ('GRID', (0, 0), (-1, -1), 1, colors.navy),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),

    ('VALIGN', (0,0), (0, -1), 'TOP'),
    ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
    ('TEXTCOLOR', (0, 0), (0, -1), colors.whitesmoke),
    ('BACKGROUND', (0, 0), (0, -1), colors.grey),

    ('FONTNAME', (1, 0), (-1, -1), 'Helvetica'),
    ('TEXTCOLOR', (1, 0), (-1, -1), colors.navy),
    ('BACKGROUND', (1, 0), (-1, -1), colors.beige),

])
