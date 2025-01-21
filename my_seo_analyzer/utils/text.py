#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ =        "Andrés Fernández Burón"
__name__ =          "text"
__description__ =   "The text of my-SEO-analyzer application"
__copyright__ =     "Copyright 2022-2025, Andres Fernandez Buron"
__license__ =       "Andres Fernandez Buron, All rights reserved"
__date__ =          "15-05-2022"
__status__ =        "Development"
__version__ =       "0.1"
    
#==============================================================================
#---- FUNCIONES DEL PROGRAMA --------------------------------------------------
#==============================================================================


# ------------------------------------------------------------------------------
# BANNER DE LA APLICACIÓN
# ------------------------------------------------------------------------------
banner = """          _____________________________________
         / ================================== /|
        / ========= MY SEO analyzer ======== /||
       / ================================== /|||
      /                                    /||||
     /  Request to an URL for a HTML,     /|||||
    /  analyze the SEO of the document   /||||||
   /  and generate a report in PDF      /|||||||
  /____________________________________////////
 |                                     |//////
 | Andres Fernandez Buron              |/////
 |                                     |////
 | Copyright (C) 2022                  |///
 | All rights reserved                 |//
 |_____________________________________|/
"""




# ------------------------------------------------------------------------------
# CABECERA DE LA APLICACIÓN
# ------------------------------------------------------------------------------
info = """ ================================================
 My SEO analyzer              Copyright (C) 2022
 Andres Fernandez Buron      All rights reserved
 ================================================
"""

# ------------------------------------------------------------------------------
# MENSAJE DE ERROR AL LLAMARAL SCRIPT SIN PARÁMETROS
# ------------------------------------------------------------------------------
param_error_text = """ No se ha recibido ningún parámetro.

 El script espera recibir al menos, 1 parámetro."""

# ------------------------------------------------------------------------------
# MENSAJE DE ERROR AL HACER LA PETICIÓN HTTP
# ------------------------------------------------------------------------------
request_error_text = """ Ha habido un error al hacer la petición HTTP.

 Comprueba tu conexión a internet."""

# ------------------------------------------------------------------------------
# MENSAJE DE ERROR SI LA RESPUESTA NO ES UN HTML
# ------------------------------------------------------------------------------
not_html_error_text = " La respuesta a la petición NO ES un documento HTML."

# ------------------------------------------------------------------------------
# TEXTO EXPLICATIVO DE LOS PARÁMETROS
# ------------------------------------------------------------------------------
param_help_text = """ Primer Argumento: URL
 El primer parámetro es obligatorio.
 Consiste en la URL del documento que se va a analizar.

 Ejemplos:

 HTTP REQUESTS:

    py my-seo-analyzer -url paginaweb.com
    py my-seo-analyzer -url http://paginaweb.com

 HTTPS REQUEST:

    py my-seo-analyzer -url paginaweb.com -https
    py my-seo-analyzer -url paginaweb.com --force-https
    py my-seo-analyzer -url https://paginaweb.com

"""

