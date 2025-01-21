#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ =        "Andrés Fernández Burón"
__name__ =          "filesys"
__description__ =   "Functions to generate handle file paths."
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

from .user_interface import terminar

#============================================================================== 
# ---- FUNCIONES CON RUTAS ----------------------------------------------------
#==============================================================================

# ------------------------------------------------------------------------------
# DEVUELVO LA RUTA NORMALIZADA, EN FUNCIÓN DEL EL SEPARADOR DE RUTAS DEL SISTEMA
# ------------------------------------------------------------------------------
def normalize_path( dir_path ):
    dir_path = dir_path.strip(' ')
    if(os.name=='nt' or os.name=='ce' or os.name=='dos'):
        if( dir_path.find('/') != -1 ):
            dir_path = dir_path.replace('/', os.path.sep)
    elif (os.name=='posix' or os.name=='mac' or os.name=='java'):
        if( dir_path.find('\\') != -1 ):
            dir_path = dir_path.replace('\\', os.path.sep)
    return dir_path

# ------------------------------------------------------------------------------
# RUTA RELATIVA A LA CARPETA DEL USUARIO
# ------------------------------------------------------------------------------

def get_dir_name_for_URL( base_path, URL ):
    dir_name = URL.replace('://', '_')
    dir_name = dir_name.replace('/?', '/GET/')
    dir_name = dir_name[:len(dir_name)-1]
    #return f"{os.path.expanduser('~')}{os.sep}{base_path}{os.sep}{dir_name}"
    return f"{os.path.expanduser('~')}{os.sep}{base_path}"

def get_file_name_for_URL( URL ):
    file_name = URL.replace('http://', '')
    file_name = file_name.replace('https://', '')
    file_name = file_name.replace('/?', '')
    file_name = file_name[:len(file_name)-1]
    file_name = f"{file_name}.pdf"
    return file_name

def get_full_path_for_URL( file_path, file_name ):
    full_file_path = f"{file_path}{os.sep}{file_name}"
    return normalize_path( full_file_path )

#============================================================================== 
# ---- FUNCIONES CON DIRECTORIO -----------------------------------------------
#==============================================================================

# ------------------------------------------------------------------------------
# CREO EL DIRECTORIO, SI NO EXISTE
# ------------------------------------------------------------------------------
import os

def create_dir_if_not_exists( dir_path ):
    if( not os.path.isdir( dir_path ) ):
        try:
            #os.mkdir(dir_path)
            os.makedirs(dir_path, exist_ok=True)
        except Exception as e:
            print(f"\n Error al crear el directorio !!\n {dir_path}\n\n {e}\n")
            terminar()
