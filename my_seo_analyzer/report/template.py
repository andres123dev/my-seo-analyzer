#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ =        "Andrés Fernández Burón"
__name__ =          "template"
__description__ =   "Base class to define the SEO report document."
__copyright__ =     "Copyright 2022-2025, Andres Fernandez Buron"
__license__ =       "Andres Fernandez Buron, All rights reserved"
__date__ =          "15-05-2022"
__status__ =        "Development"
__version__ =       "0.1"
__maintainer__ =    "Andres Fernandez Buron"
__email__ =         "https://github.com/andres123dev/my-seo-analyzer/new/choose"

#==============================================================================
#---- MODULOS ---------------------------------------------------------------
#==============================================================================

from reportlab.platypus import SimpleDocTemplate
#from reportlab.platypus import BaseDocTemplate

from reportlab.platypus import Frame, PageTemplate, Paragraph, Spacer, Table#, PageBreak#, Image#, PageBreak ####TableStyle
from reportlab.platypus.tableofcontents import TableOfContents

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm

from .styles import *


# ============================================================================= 
# ---- CLASES -----------------------------------------------------------------
# =============================================================================

# DOC TEMPLATE
class MyDocTemplate( SimpleDocTemplate ):

    # 
    def __init__(self, *args, **kwargs):
        SimpleDocTemplate.__init__(self, *args, **kwargs)
        
        #self.allowSplitting = 0

        self.elements = []
        self.page = 1
        
        self.addPageTemplates(self.get_page_templates())
        
        self.toc = TableOfContents()
        self.toc.levelStyles = [
            toc_heading1_style, 
            toc_heading2_style
        ]

    # Fin de página
    def draw_header_footer(self, canvas, doc):
        #canvas.saveState()
        #canvas.setFont('Helvetica', 10)
        #canvas.setFillColorRGB(0, 0, 60)
        self.draw_header(canvas)
        self.draw_footer(canvas, doc)
        #canvas.restoreState()

    # Dibujar la cabecera de la página
    def draw_header(self, canvas):
        canvas.saveState()
        canvas.setFont('Helvetica', 10)
        canvas.setFillColorRGB(0, 0, 60)
        canvas.drawString(cm, 29*cm, "Andres Fernandez Buron")
        canvas.drawString(cm, 28.5*cm, "my-seo-analyzer")
        canvas.drawRightString(20*cm, 29*cm, "Copyright (C) 2022")
        canvas.drawRightString(20*cm, 28.5*cm, "All rights reserved")
        canvas.restoreState()

    # Dibujar el pié de página
    def draw_footer(self, canvas, doc):
        canvas.saveState()
        canvas.setFont('Helvetica', 10)
        canvas.setFillColorRGB(0, 0, 60) 
        canvas.drawString(2*cm, 2* cm, f"Page {self.page}")
        self.page = canvas.getPageNumber()
        canvas.restoreState()
    
    # Devuelvo PageTemplate
    def get_page_templates(self):
        frame = Frame(
            cm, cm, 18* cm, 25* cm,
            leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0
        )
        template = PageTemplate(
            id='Normal',
            frames=[frame],
            onPage=self.draw_header_footer,
            onPageEnd=self.draw_footer
        )
        return [template]

    # Do after add a flowable
    def afterFlowable(self, flowable):
        if isinstance(flowable, Paragraph):
            text = flowable.getPlainText()
            style = flowable.style.name
            if style == 'Heading1Style':
                self.notify('TOCEntry', (0, text, self.page))
            elif style == 'Heading2Style':
                self.notify('TOCEntry', (1, text, self.page))

    # Add a title to the document
    def add_heading(self, text, styles, level):


        #text = f"""<a name="{name}">{text}</a>"""
        

        self.elements.append( Paragraph(text, styles) )

        if styles == 'Heading1Style':
            self.elements.append( Spacer(1, 2 * cm) )

        elif styles == 'Heading2Style':
            self.elements.append( Spacer(1, cm) )
        
        self.toc.addEntry(level, text, self.page)
        
    # Add a paragraph to the document
    def add_paragraph(self, text, styles=None):
        if styles == None:
            styles = normal_style
        self.elements.append(Paragraph( text, styles))
        #self.elements.append( Spacer(1, cm) )

    # Add a table to the document
    def add_table( self, data, colWidths=None ):
        table = None
        if colWidths !=None:
            table = Table(data, colWidths)
        else:
            table = Table(data)
        table.setStyle( table_style )
        self.elements.append(table)
        self.elements.append( Spacer(1, cm) )
