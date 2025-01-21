#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ =        "Andrés Fernández Burón"
__name__ =          "http_request"
__description__ =   "Functions to handle HTTP requests and responses."
__copyright__ =     "Copyright 2022-2025, Andres Fernandez Buron"
__license__ =       "Andres Fernandez Buron, All rights reserved"
__date__ =          "15-05-2022"
__status__ =        "Development"
__version__ =       "0.1"
__maintainer__ =    "Andres Fernandez Buron"
__email__ =         "https://github.com/andres123dev/my-seo-analyzer/new/choose"

#==============================================================================
#---- FUNCIONES CON PETICIONES HTTP -------------------------------------------
#==============================================================================

# ------------------------------------------------------------------------------
# DEVUELVO LA URL NORMALIZADA
# ------------------------------------------------------------------------------
def normalize_URL( URL, force_https ):
    URL.strip(' ')
    if not URL.startswith('http'):
        if force_https:
            URL = f"https://{URL}"
        else:
            URL = f"http://{URL}"
    if not URL.endswith('/'):
        URL = f"{URL}/"
    return URL

# ------------------------------------------------------------------------------
# HAGO UNA PETICIÓN A LA URL Y DEVUELVO LA RESPUESTA O TERMINO
# ------------------------------------------------------------------------------
from utils.text import request_error_text
from utils.user_interface import print_error, terminar

import requests

def make_http_request( URL, user_agent ):

    # REALIZO LA PETICIÓN HTTP
    response = None
    try:
        response = requests.get(URL, params={}, headers={'User-Agent': user_agent}, verify=False)
    except Exception as e:
        print_error(request_error_text, e)
        terminar()

    return response

# ------------------------------------------------------------------------------
# HANDLE THE RESPONSE OF THE REQUEST
# ------------------------------------------------------------------------------

from utils.text import not_html_error_text

def handle_http_response( response ):

    # SI LA RESPUESTA ES 200 (OK)    
    if( response.ok ):

        # SI NO ES UN HTML TERMINO EL SCRIPT
        if( not 'html' in response.headers['Content-type'] ):
            print_error(not_html_error_text)
            terminar()

    return response.text
    