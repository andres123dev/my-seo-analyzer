#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ =        "Andrés Fernández Burón"
__name__ =          "output_doc"
__description__ =   "Class to generate the SEO report document."
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

from reportlab.platypus import Paragraph, Spacer, PageBreak

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm

from .styles import *
from .template import *


# ============================================================================= 
# ---- FUNCIONES --------------------------------------------------------------
# =============================================================================


# ============================================================================= 
# ---- CLASES -----------------------------------------------------------------
# =============================================================================

# SEO ANALYSIS DOC TEMPLATE
class MySeoAnalysisTemplate( MyDocTemplate ):

    def __init__(self, *args, **kwargs):
        MyDocTemplate.__init__(self, *args, **kwargs)

    # FRONT PAGE
    def add_front_page( self, url, hua, response ):

        self.add_paragraph("My SEO analyzer's report", title_style)
        self.elements.append(Spacer(1, cm))
        
        #IMAGEN...

        colWidths = [4*cm, 14*cm]

        # Añadir tablas con información de MySEOanalyzer
        self.add_paragraph("SEO analysis & report generator", bold_style )
        data = [
            ['Application', 'My SEO analyzer'],
            ['Version', __version__],
        ]
        self.add_table( data, colWidths )

        data = [
            ['Author', 'Andres Fernandez Buron'],
            ['Copyright (C)', '2022 All rights reserved'],
        ]
        self.add_table( data, colWidths )

        self.elements.append(Spacer(1, cm))

        # Añadir tabla con resumen de la petición HTTP
        self.add_paragraph('The HTTP request', bold_style)
        data = [
            ['Requested URL', url],
            ['HTTP User Agent', Paragraph(hua, table_text_style)],
            ['Force HTTPS', False],
            ['Run Javascript', False],
        ]
        self.add_table( data, colWidths )

        # Añadir tabla con resumen de la respuesta HTTP
        self.add_paragraph('The HTTP response', bold_style)
        data = [
            ['Response', f"{response.status_code} {response.reason}"],
            ['Encoding', response.encoding],
        ]
        self.add_table( data, colWidths )

        # Añadir tabla con información del reporte SEO
        from datetime import datetime
        current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        self.elements.append( Spacer(1, cm) )

        self.add_paragraph("My SEO analyzer's report", bold_style)
        data = [
            ['Report file', Paragraph(self.filename, table_text_style)],
            ['Date & time', current_datetime],
        ]
        self.add_table( data, colWidths )

        self.elements.append(Spacer(1, 2*cm))
        self.elements.append( PageBreak() )

    # INDEX PAGE 
    def add_index_page( self ):
        self.add_paragraph("0. Index of My SEO analyzer's report", heading1_style)
        #self.elements.append( Spacer(1, cm) )
        self.elements.append( self.toc )
        self.elements.append( Spacer(1, cm) )
        self.elements.append( PageBreak() )

    # SECTION 2 - META TAGS
    def add_metatags_section( self, title, description, keywords ):

        title_min_len = 50
        description_min_len = 150

        self.add_heading('2. Meta tags', heading1_style, level=0)
        #self.elements.append( Spacer(1, cm) )
    
        self.add_heading('2.1. Title', heading2_style, level=1)
        self.add_paragraph(title, black_style)
        self.add_paragraph(f"Length: {len(title)}")
        if len(title) < title_min_len:
            self.add_paragraph("The title must be larger.", error_style)
        else:
            self.add_paragraph("The title has a good length.", ok_style)
        self.elements.append( Spacer(1, cm) )

        self.add_heading('2.2. Description', heading2_style, level=1)
        if description != None:
            description = description['content']
            self.add_paragraph(description, black_style)
            self.add_paragraph(f"Length: {len(description)}")
            if len(title) < description_min_len:
                self.add_paragraph("The description must be larger.", error_style)
            else:
                self.add_paragraph("The title has a good length.", ok_style)
        else:
            self.add_paragraph("The document has not description.", error_style)
        self.elements.append( Spacer(1, cm) )

        self.add_heading('2.3. Keywords', heading2_style, level=1)
        if keywords != None:
            keywords = keywords['content']
            self.add_paragraph(keywords, black_style)
            self.add_paragraph(f"<b>Count:</b> {len(keywords)}")
        else:
            self.add_paragraph("The document has not keywords.", error_style)
        #self.elements.append( Spacer(1, cm) )
        
        self.elements.append( Spacer(1, 2*cm) )
        self.elements.append( PageBreak() )
    
    # SECTION 3 - HTML TITLES
    def add_titles_section( self, data_dict ):

        htitles_min_len = 50
        htitles_max_len = 80

        self.add_heading('3. HTML titles', heading1_style, level=0)
        #self.elements.append( Spacer(1, cm) )

        for i in range(1, 7):
            self.add_heading(f"3.{i}. H{i} titles", heading2_style, level=1)
            if len(data_dict[f"h{i}_titles"]) == 0:
                self.add_paragraph(f"The document has not a H{i} title.", error_style)
                self.elements.append( Spacer(1, cm) )
            else:
                self.add_paragraph(f"""The document has {len(data_dict[f"h{i}_titles"])} titles H{i}.""")

                if i == 1:
                    if len(data_dict[f"h{i}_titles"]) == 1:
                        self.add_paragraph(f"This document has an unique title of type H1.", ok_style)
                    else:
                        self.add_paragraph(f"This document must have an unique H1 title.", error_style)
                
                self.elements.append( Spacer(1, cm) )

                for title in data_dict[f"h{i}_titles"]:
                    title = title.text

                    self.add_paragraph(f"{title}", black_style)
                    self.add_paragraph(f"The title H{i} has a length of {len(title)}.")

                    if len(title) < htitles_min_len:
                        self.add_paragraph('The length is too short.', error_style)
                    elif len(title) > htitles_max_len:
                        self.add_paragraph('The length is too long.', error_style)
                    else:
                        self.add_paragraph('The length has a good length.', ok_style)
                    self.elements.append( Spacer(1, cm) )

        #self.elements.append(Spacer(1, 2*cm))
        self.elements.append( PageBreak() )
    
    # SECTION 4 - DOCUMENT CONTENT
    def add_content_section( self, text, paragraphs, anchors, images, forms ):
        self.add_heading('4. Document content', heading1_style, level=0)
        self.elements.append( Spacer(1, cm) )

        self.add_heading('4.1. HTML elements', heading2_style, level=1)
        self.add_paragraph(f"The document has <b> {len(paragraphs)} paragraphs</b>.")
        self.add_paragraph(f"The document has <b> {len(anchors)} anchors</b>.", normal_style)
        self.add_paragraph(f"The document has <b> {len(images)} images</b>.", normal_style)
        self.add_paragraph(f"The document has <b> {len(forms)} forms</b>.", normal_style)
        self.elements.append( Spacer(1, cm) )
    
        self.add_heading('4.1. Text content', heading2_style, level=1)
        self.add_paragraph(f"The document has <b> {len(text.strip().split(' '))} words</b>.")
        self.add_paragraph(f"The document has <b> {len(text.strip())} characters</b>.")
        self.elements.append( Spacer(1, cm) )

        #self.elements.append( Spacer(1, 2*cm) )
        self.elements.append( PageBreak() )

    # SECTION 5 - HTML DOCUMENT
    def add_document_section( self, html_headers, navs, asides, mains, articles, sections, footers ):
        self.add_heading('5. HTML document', heading1_style, level=0)
        self.elements.append( Spacer(1, cm) )
        
        #self.add_heading('5.1. Doctype', heading2_style, level=1)
        #self.add_paragraph( doctype )
        
        self.add_heading('5.1. HTML 5 entities', heading2_style, level=1)
        self.elements.append( Spacer(1, cm) )
        self.add_paragraph(f"The document has <b> {len(html_headers)} headers</b>.", normal_style)
        self.add_paragraph(f"The document has <b> {len(navs)} navs</b>.", normal_style)
        self.add_paragraph(f"The document has <b> {len(asides)} asides</b>.", normal_style)
        self.add_paragraph(f"The document has <b> {len(mains)} mains</b>.", normal_style)
        self.add_paragraph(f"The document has <b> {len(articles)} articles</b>.", normal_style)
        self.add_paragraph(f"The document has <b> {len(sections)} sections</b>.", normal_style)
        self.add_paragraph(f"The document has <b> {len(footers)} footers</b>.", normal_style)
        self.elements.append( Spacer(1, cm) )

        if len(html_headers)==0 and len(navs)==0 and len(asides)==0 and len(mains)==0 and len(articles)==0 and len(sections)==0 and len(footers)==0:
            self.add_paragraph(f"The document has not any HTML 5 semantical tags.", error_style)
            self.elements.append( Spacer(1, cm) )

        #self.elements.append( Spacer(1, 2*cm) )
        self.elements.append( PageBreak() )

    # SECTION 6 - REFERENCED FILES
    def add_referenced_section( self, css_links, onpage_css, script_links, onpage_scripts ):

        max_files = 10

        self.add_heading('6. Referenced files', heading1_style, level=0)
        self.elements.append( Spacer(1, cm) )

        self.add_heading('6.1. CSS styles', heading2_style, level=1)
        self.elements.append( Spacer(1, cm) )

        self.elements.append( Paragraph(f"<b>Extern CSS files:</b> {len(css_links)}", normal_style) )
        if len(css_links) > max_files:
            self.add_paragraph(f"The document references a lot of CSS files.", error_style)
        else:
            self.add_paragraph(f"The document references less than {max_files} CSS files.", ok_style)
        self.elements.append( Spacer(1, cm) )

        self.elements.append( Paragraph(f"<b>On page CSS styles:</b> {len(onpage_css)}", normal_style) )
        if len(onpage_css) == 0:
            self.add_paragraph(f"The document has not on page CSS code using <b>STYLE</b> tag.", ok_style)
        elif len(onpage_css) > 0:
            self.add_paragraph(f"The document has on page CSS code using <b>STYLE</b> tag.", error_style)
        self.elements.append( Spacer(1, cm) )

        self.add_heading('6.2. JS scripts', heading2_style, level=1)
        self.elements.append( Spacer(1, cm) )

        self.elements.append( Paragraph(f"<b>Extern Javascript files:</b> {len(script_links)}", normal_style) )
        if len(script_links) > max_files:
            self.add_paragraph(f"The document references a lot of Javascript files.", error_style)
        else:
            self.add_paragraph(f"The document references less than {max_files} Javascript files.", ok_style)
        self.elements.append( Spacer(1, cm) )
        
        self.elements.append( Paragraph(f"<b>On page Javascript scripts:</b> {len(onpage_scripts)}", normal_style) )
        if len(onpage_scripts) == 0:
            self.add_paragraph(f"The document has not on page Javascript code in <b>SCRIPT</b> tag.", ok_style)
        elif len(onpage_scripts) > 0:
            self.add_paragraph(f"The document has on page Javascript code using <b>SCRIPT</b> tag.", error_style)
        self.elements.append( Spacer(1, cm) )

        #self.elements.append(Spacer(1, 2*cm))
        self.elements.append( PageBreak() )
    
    # SECTION 7 - LINKS
    def add_links_section( self, url, anchors ):
        self.add_heading('7. Document links', heading1_style, level=0)
        self.elements.append( Spacer(1, cm) )

        links = [a for a in anchors if a.text.replace(' ', '')!='' and a.get('href')!='#' and a.get('href')!='javascript:void(0)']

        dominio = url.replace('https://', '').replace('http://', '').split('/')[0]
        internal_links = [a for a in links if a.get('href').startswith(url[:round(len(url))]) or a.get('href').startswith(dominio) or a.get('href').startswith('/') ]
        external_links = [a for a in links if not a.get('href').startswith(url[:round(len(url))]) and not a.get('href').startswith(dominio) and not a.get('href').startswith('/') ]
    
        self.add_paragraph(f"The document has <b>{len(anchors)}</b> <b>anchors</b>.")
        self.add_paragraph(f"From these anchors, <b>{len(links)}</b> are <b>links</b>.")
        self.elements.append( Spacer(1, cm) )
        self.add_paragraph(f"Of them, {len(internal_links)} are <b>internal links</b>.")
        self.add_paragraph(f"And {len(external_links)} are <b>external links</b>.")
        self.elements.append( Spacer(1, cm) )
        
        """
        # Internal links
        self.add_heading('7.1. Internal Links', heading2_style, level=1)
        for a in internal_links:
            self.add_paragraph(f"{a.text}")
            self.add_paragraph(f"{a.get('href')}", anchor_style)

        # External links
        self.add_heading('7.2. External Links', heading2_style, level=1)
        for a in external_links:
            self.add_paragraph(f"{a.text}")
            self.add_paragraph(f"{a.get('href')}", anchor_style)

        self.elements.append( Spacer(1, 2*cm) )
        self.elements.append( PageBreak() )
        """

    """
    def add_resume_section( self, data_dict ):

        #self.add_paragraph("HTML document:", bold_style)

        #self.add_paragraph("Referenced files:", bold_style)
        
        self.add_paragraph("HTML 5 tags:", bold_style)
        data = [
            ['header', len(data_dict['headers']) ],
            ['nav', len(data_dict['navs']) ],
            ['aside', len(data_dict['asides']) ],
            ['main', len(data_dict['mains']) ],
            ['article', len(data_dict['articles']) ],
            ['section', len(data_dict['sections']) ],
            ['footer', len(data_dict['footers']) ],
        ]
        self.add_table( data )
        
        self.add_paragraph("HTML tags:", bold_style)
        data = [
            ['paragraphs', len(data_dict['paragraphs']) ],
            ['anchors', len(data_dict['anchors']) ],
            ['images', len(data_dict['images']) ],
            ['forms', len(data_dict['forms']) ],
        ]
        self.add_table( data )

        self.elements.append( Spacer(1, 2*cm) )
        self.elements.append( PageBreak() )
    """

    # SECTION 1 - HTTP HEADERS
    def add_headers_section( self, response ):

        colWidths = [6*cm, 13*cm]

        self.add_heading('1. HTTP response headers', heading1_style, level=0)
        self.elements.append( Spacer(1, cm) )

        # ---- Headers related to the content ------
        self.add_heading('1.1. Content headers', heading2_style, level=1)
        data = []
        searched = [
            'content-type', 'content-language', 'content-encoding', 'content-length'
            'date', 'last-modified', 'age',
            'referrer-policy', 
        ]
        for current in searched:
            key = ''
            value = ''
            for each in response.headers.keys():
                if each.lower() == current:
                    key = each
                    value = response.headers[each]
                    break
            if key == '':
                key = current
            data.append( [key, Paragraph(value, table_text_style)] )
        if len(data) > 0:
            self.add_table( data, colWidths )
        else:
            self.add_paragraph(f"There are not HTTP headers related to 'Content'.", error_style)
            self.elements.append(Spacer(1, cm))

        # Headers related to cache
        self.add_heading('1.2. Cache headers', heading2_style, level=1)
        #searched = ['cache-control', 'expires', 'pragma']
        data = []
        for key in response.headers.keys():
            if 'cache' in key.lower() or 'pragma' in key.lower() or 'expires' in key.lower():
                if not key.lower().startswith('x-'):
                    data.append( [key, Paragraph(response.headers[key], table_text_style)] )
        if len(data) > 0:
            self.add_table( data, colWidths )
        else:
            self.add_paragraph(f"There are not HTTP headers related to 'Cache'.", error_style)
            self.elements.append(Spacer(1, cm))

        # ---- Headers related to the connection & the server ----
        self.add_heading('1.3. Connection headers', heading2_style, level=1)
        data = []
        searched = ['server', 'connection', 'keep-alive', 'status']
        for key in response.headers.keys():
            if key.lower() in searched:
                data.append( [key, Paragraph(response.headers[key], table_text_style)] )
            elif 'server' in key.lower() or 'accept' in key.lower() or 'transfer' in key.lower():
                data.append( [key, Paragraph(response.headers[key], table_text_style)] )
        if len(data) > 0:
            self.add_table( data, colWidths )
        else:
            self.add_paragraph(f"There are not HTTP headers related to 'Connection'.", error_style)
            self.elements.append(Spacer(1, cm))
    
        #self.elements.append(Spacer(1, 2*cm))
        self.elements.append( PageBreak() )

        # Headers related to cookies
        self.add_heading('1.4. Cookie headers', heading2_style, level=1)
        data = []
        searched = ['set-cookie']
        for key in response.headers.keys():
            if 'cookie' in key.lower():
                data.append( [key, Paragraph(response.headers[key], table_text_style)] )
        if len(data) > 0:
            self.add_table( data, colWidths )
        else:
            self.add_paragraph(f"There are not HTTP headers related to 'Cookies'.", normal_style)
            self.elements.append(Spacer(1, cm))

        # Headers related to session
        self.add_heading('1.5. Session headers', heading2_style, level=1)
        data = []
        for key in response.headers.keys():
            if 'session' in key.lower():
                data.append( [key, Paragraph(response.headers[key], table_text_style)] )
        if len(data) > 0:
            self.add_table( data, colWidths )
        else:
            self.add_paragraph(f"There are not HTTP headers related to 'Sessions'.", normal_style)
            self.elements.append(Spacer(1, cm))
    
        #self.elements.append(Spacer(1, 2*cm))
        self.elements.append( PageBreak() )

        # Headers related to security
        self.add_heading('1.6. Security headers', heading2_style, level=1)

        data = []
        for key in response.headers.keys():
            if 'security' in key.lower() or 'secure' in key.lower() or 'policy' in key.lower() or 'privacy' in key.lower():
                data.append( [key, Paragraph(response.headers[key], table_text_style)] )
        if len(data) > 0:
            self.add_table( data, colWidths )
        else:
            self.add_paragraph(f"There are not HTTP headers related to 'Security, secure, policy or privacy'.", error_style)
            self.elements.append(Spacer(1, cm))
                
        # Headers starting with 'X-'
        data = []
        for key in response.headers.keys():
            if key.lower().startswith('x-') and key.lower() not in searched:
                data.append( [key, Paragraph(response.headers[key], table_text_style)] )
        if len(data) > 0:
            self.add_table( data, colWidths )
        else:
            self.add_paragraph(f"There are not HTTP headers related to 'X- Security'.", error_style)
            self.elements.append(Spacer(1, cm))

        # Other headers
        self.add_heading('1.7. Other headers', heading2_style, level=1)
        data = []
        for key in response.headers.keys():
            if key.lower() in ['content-type', 'content-length', 'content-language', 'content-encoding', 'date', 'last-modified', 'referrer-policy', 'age']:
                continue
            elif key.lower() in ['connection', 'server']:
                continue
            elif 'accept' in key.lower() or 'transfer' in key.lower():
                continue
            elif 'cache' in key.lower() or 'pragma' in key.lower() or 'expires' in key.lower():
                continue
            elif 'security' in key.lower() or 'secure' in key.lower() or 'policy' in key.lower() or 'privacy' in key.lower():
                continue
            elif key.lower().startswith('x-'):
                continue
            elif 'cookie' in key.lower() or 'session' in key.lower():
                continue

            data.append( [key, Paragraph(response.headers[key], table_text_style)] )
            
        if len(data) > 0:
            self.add_table( data, colWidths )
        else:
            self.add_paragraph(f"There are not more HTTP headers.", normal_style)
            self.elements.append(Spacer(1, cm))
    
        #self.elements.append(Spacer(1, 2*cm))
        self.elements.append( PageBreak() )
    

# ------------------------------------------------------------------------------
# GENERATE A PDF WITH THE SEO ANALYSIS
# ------------------------------------------------------------------------------
def generate_out_pdf( filename, url, hua, response, data_dict ):

    # PDF Document
    doc = MySeoAnalysisTemplate( filename, pagesize=A4 )
    
    # Document content
    doc.add_front_page( url, hua, response )        # Front page
    doc.add_index_page()                            # Index page
    
    #doc.add_resume_section( data_dict )            # Report resume
    
    doc.add_headers_section( response )             # 1 - HTTP headers

    # 2 - META tags
    doc.add_metatags_section( data_dict['title'], data_dict['description'], data_dict['keywords'] )

    doc.add_titles_section( data_dict )             # 3 - HTML titles

    # 4 - Document content
    doc.add_content_section( 
        data_dict['text'], data_dict['paragraphs'],
        data_dict['anchors'], data_dict['images'], data_dict['forms']
    )

    # 5 - HTML document
    doc.add_document_section(data_dict['headers'], data_dict['navs'], data_dict['asides'], data_dict['mains'], data_dict['articles'], data_dict['sections'], data_dict['footers'] )
    
    # 6 - Referenced files
    doc.add_referenced_section( data_dict['css_links'], data_dict['onpage_css'], data_dict['script_links'], data_dict['onpage_scripts'] )

    doc.add_links_section( url, data_dict['anchors'] )   # 7 - Links

    
    # Build PDF document
    doc.multiBuild( doc.elements, onFirstPage=doc.draw_header_footer, onLaterPages=doc.draw_header_footer )

