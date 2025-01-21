#!/usr/bin/env python3
# -*- coding: utf-8 -*

__author__ =        "Andrés Fernández Burón"
__name__ =          "seo_analysis"
__description__ =   "Functions to analyze the SEO of the HTML document."
__copyright__ =     "Copyright 2022-2025, Andres Fernandez Buron"
__license__ =       "Andres Fernandez Buron, All rights reserved"
__date__ =          "15-05-2022"
__status__ =        "Development"
__version__ =       "0.1"
__maintainer__ =    "Andres Fernandez Buron"
__email__ =         "https://github.com/andres123dev/my-seo-analyzer/new/choose"

# ============================================================================= 
# ---- FUNCIONES --------------------------------------------------------------
# =============================================================================

# ------------------------------------------------------------------------------
# DEVUELVO EL STR DE UN TAG DE BS4 SIN ESPACIOS BLANCOS GRANDES
# ------------------------------------------------------------------------------
def strip_whitespaces( tag ):
    tag = str( tag )
    tag = tag.strip()
    tag = tag.replace('  ', '')
    tag = tag.replace('\n', '')
    tag = tag.replace('\t', '')
    return tag

# ------------------------------------------------------------------------------
# ANALIZO EL SEO DEL HTML Y DEVUELVO UN DICT (k/v)
# ------------------------------------------------------------------------------
from bs4 import BeautifulSoup

def analyze_document_seo( response_text ):
        
    # MAPEO A MEMORIA EL DOM DEL HTML
    soup = BeautifulSoup(response_text, features='html.parser')
    #soup = BeautifulSoup(response_text, features='lxml')
    #soup = BeautifulSoup(response_text, features='html5lib')
    #print(soup.prettify())

    data_dict = {}
    
    data_dict['title'] = soup.title.string if soup.title!=None else ''

    data_dict['description'] = soup.find('meta', attrs={'name':'description'})

    data_dict['keywords'] = soup.find('meta', attrs={'name':'keywords'})
    
    data_dict['css_links'] = soup.find_all('link', attrs={'rel':'stylesheet','type':'text/css'})
    data_dict['onpage_css'] = soup.find_all('style')

    data_dict['script_links'] = soup.find_all('script', src=True)
    data_dict['onpage_scripts'] = soup.find_all('script', src=False)
    
    for i in range(1, 7):
        data_dict[f"h{i}_titles"] = soup.find_all(f"h{i}")
    
    data_dict['paragraphs'] = text = soup.find_all('p')

    data_dict['anchors'] = soup.find_all('a', href=True)
    
    data_dict['images'] = soup.find_all('img', src=True)
    
    data_dict['forms'] = soup.find_all('form')
    
    data_dict['headers'] = soup.find_all('header')
    data_dict['navs'] = soup.find_all('nav')
    data_dict['asides'] = soup.find_all('aside')
    data_dict['mains'] = soup.find_all('main')
    data_dict['articles'] = soup.find_all('article')
    data_dict['sections'] = soup.find_all('section')
    data_dict['footers'] = soup.find_all('footer')
    
    text = strip_whitespaces(soup.body.get_text())
    data_dict['text'] = text

    return data_dict

# ------------------------------------------------------------------------------
# IMPRIMO EL RESUMEN DEL ANÁLISIS SEO
# ------------------------------------------------------------------------------
def print_seo_verbose( data_dict ):
    
    print(f" ========================================")
    print(f" ==== META TAGS =========================")
    print(f" ========================================")
    print(f" TITLE:       {data_dict['title']}\n")
    print(f" DESCRIPTION: {data_dict['description']}\n")
    print(f" KEYWORDS:    {data_dict['keywords']}\n")
    
    print(f" ========================================")
    print(f" ==== DOCUMENT STATS ====================")
    print(f" ========================================\n")
    print(f" PALABRAS:    {len(data_dict['text'].strip().split(' '))}")
    print(f" LETRAS:      {len(data_dict['text'].strip())}")
    print()

    print(f" ========================================")
    print(f" ==== DOCUMENT TITLES ===================")
    print(f" ========================================")
    for i in range(1, 7):
        print(f""" H{i}:          {len(data_dict[f"h{i}_titles"])}""")

    print(f" ========================================")
    print(f" ==== DOCUMENT ELEMENTS =================")
    print(f" ========================================")

    print(f" PARAGRAPHS:  {len(data_dict['paragraphs'])}")
    print(f" ANCHORS:     {len(data_dict['anchors'])}")
    print(f" IMAGES:      {len(data_dict['images'])}")
    print(f" FORMULARIES: {len(data_dict['forms'])}")
    print()

    #print(f" ========================================")
    #print(f" ==== DOCUMENT ANCHORS ==================")
    #print(f" ========================================")
    #print(f" ANCHORS:     {len(data_dict['anchors'])}")
    #print(f" LINKS:       {len(data_dict['links'])}")
    
    print(f" ========================================")
    print(f" ==== REFERENCED FILES ==================")
    print(f" ========================================")
    print(f" EXTERN STYLES:      {len(data_dict['css_links'])}")
    print(f" ON PAGESTYLES:      {len(data_dict['onpage_css'])}")
    print()
    print(f" EXTERN SCRIPTS:     {len(data_dict['script_links'])}")
    print(f" ON PAGESCRIPTS:     {len(data_dict['onpage_scripts'])}")
    print()


"""
class MySeoData():
    def __init__( self, data ):
        
        self.title = data['title']
        self.description = data['description']
        self.keywords = data['keywords']
    
        self.h1_titles = data['h1_titles']
        self.h2_titles = data['h2_titles']
        self.h3_titles = data['h3_titles']
        self.h4_titles = data['h4_titles']
        self.h5_titles = data['h5_titles']
        self.h6_titles = data['h6_titles']

        self.text = data['text']
        
        self.onpage_css = data['onpage_css']
        self.css_links = data['css_links']
        self.scripts = data['script']
        
        self.anchors = data['a']
        self.images = data['img']
        self.forms = data['form']
"""
