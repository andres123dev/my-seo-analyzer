#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ =        "Andrés Fernández Burón"
__name__ =          "my_seo_analyzer"
__description__ =   "Console app to request an URL, analize the SEO and generate a report."
__copyright__ =     "Copyright 2022-2025, Andrés Fernández Burón"
__license__ =       "All rights reserved"
__date__ =          "15-05-2022"
__status__ =        "Development"
__version__ =       "0.1"
__maintainer__ =    "Andrés Fernández Burón"
__email__ =         "https://github.com/andres123dev/my-seo-analyzer/new/choose"

__all__ = [
    'utils',
    'extract',
    'report'
]

from .utils import *
from .extract import *
from .report import *
