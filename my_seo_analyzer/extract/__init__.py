#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ =        "Andrés Fernández Burón"
__name__ =          "extract"
__description__ =   "Module to get a HTML webpage & analize his SEO"
__copyright__ =     "Copyright 2022-2025, Andrés Fernández Burón"
__license__ =       "All rights reserved"
__date__ =          "15-05-2022"
__status__ =        "Development"
__version__ =       "0.1"
__maintainer__ =    "Andrés Fernández Burón"
__email__ =         "https://github.com/andres123dev/my-seo-analyzer/new/choose"

__all__ = [
    'http_request',
    'seo_analysis'
]

from .http_request import *
from .seo_analysis import *
