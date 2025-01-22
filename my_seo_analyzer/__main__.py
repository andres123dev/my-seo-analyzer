#!/usr/bin/env python3
# -*- coding: utf-8 -*

__author__ =        "Andrés Fernández Burón"
__name__ =          "__main__"
__description__ =   "The main script of the app."
__description__ =   "Script to request a HTML document, analyze his SEO & generate a report."
__copyright__ =     "Copyright 2022-2025, Andres Fernandez Buron"
__license__ =       "Andres Fernandez Buron, All rights reserved"
__date__ =          "15-05-2022"
__status__ =        "Development"
__version__ =       "0.1"
__maintainer__ =    "Andres Fernandez Buron"
__email__ =         "https://github.com/andres123dev/my-seo-analyzer/new/choose"

#==============================================================================
# SELF SUBMODULES
#==============================================================================
from utils.text import *
from utils.user_interface import *
from utils.filesys import *

from extract.http_request import *
from extract.seo_analysis import *

from report.output import *

#==============================================================================
# VARS TO CONFIG THE APP
#==============================================================================
global output_path, user_agent
global URL, force_https, force_js

URL = ""
output_path = 'Documents/my-seo-analyzer-reports'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'

force_https = False
force_js = False

# ============================================================================= 
# ---- FUNCIONES --------------------------------------------------------------
# =============================================================================

# ------------------------------------------------------------------------------
# OBTENGO LOS PARÁMETROS RECIBIDOS POR EL SCRIPT O TERMINO
# ------------------------------------------------------------------------------
import argparse

def handle_params():
    
    # PARSEO LOS PARÁMETROS
    parser = argparse.ArgumentParser(description=__description__)

    parser.add_argument('-v', '--version', action='version', version=f"\n My SEO analyzer \n Version: {__version__}\n Author: {__author__}\n")

    parser.add_argument('-url', type=str, help='The URL of the webpage to request.')

    parser.add_argument('-https', '--force_https', action='store_true', default=False, help='Force theuse of HTTPS at request.')
    parser.add_argument('-js', '--force_js', action='store_true', default=False, help='Force the JS interpretation at HTTP request.')

    # COMPRUEBO LOS PARÁMETROS RECIBIDOS
    args = parser.parse_args()

    # PARAM -URL
    if args.url is not None:
        global URL
        URL = args.url
    else:
        print_error(param_error_text)
        print(param_help_text)
        terminar()

    # PARAM -HTTPS
    if args.force_https:
        global force_https
        force_https = True

    # PARAM -JS
    if args.force_js:
        global force_js
        force_js = True

# ------------------------------------------------------------------------------
# MAIN FUNCTION
# ------------------------------------------------------------------------------

def main():

    global URL, force_https, force_js, output_path

    # LIMPIO LA CONSOLA Y MUESTRO LA CABECERA DE LA APLICACIÓN
    print_start_header()

    # OBTENGO LOS PARÁMETROS RECIBIDOS
    handle_params()

    # DOY FORMATO LA URL
    url = normalize_URL( URL, force_https )

    print(f" Force HTTPS: {force_https}")
    print(f" Force JS:    {force_js}\n")
    print(f" URL:         {URL}")
    print(f" REQUEST:     {url}\n")

    # REALIZO LA PETICIÓN HTTP
    response = make_http_request( url, user_agent )
    html_doc = handle_http_response( response )

    # ANALIZO EL SEO DEL HTML
    data_dict = analyze_document_seo( html_doc )
    
    print_header()
    print_seo_verbose( data_dict )

    output_path = get_dir_name_for_URL( output_path, url )
    file_name = get_file_name_for_URL( url )

    create_dir_if_not_exists( output_path )

    output_path = get_full_path_for_URL( output_path, file_name )
    generate_out_pdf( output_path, url, user_agent, response, data_dict )
    
    print(f"SEO report {file_name} exported to {output_path}")
    

# ============================================================================= 
# ---- EL SCRIPT --------------------------------------------------------------
# =============================================================================

# RUN THE MAIN FUNCTION
if __name__ == "__main__":
    main()
    
    print()
    #terminar()
        
