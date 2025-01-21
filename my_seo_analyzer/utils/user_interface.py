#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ =        "Andrés Fernández Burón"
__name__ =          "user_interface"
__description__ =   "Functions to handle user interface using the console i/o."
__copyright__ =     "Copyright 2022-2025, Andres Fernandez Buron"
__license__ =       "Andres Fernandez Buron, All rights reserved"
__date__ =          "15-05-2022"
__status__ =        "Development"
__version__ =       "0.1"
__maintainer__ =    "Andres Fernandez Buron"
__email__ =         "https://github.com/andres123dev/my-seo-analyzer/new/choose"

from .text import banner, info
    
# ============================================================================= 
# ---- FUNCIONES --------------------------------------------------------------
# =============================================================================

# ------------------------------------------------------------------------------
# IMPRIMO EN CONSOLA, LA CABECERA INICIAL DE LA APP
# ------------------------------------------------------------------------------
import time

def print_start_header():
    clear_screen()
    print(banner)
    time.sleep( 2 )

# ------------------------------------------------------------------------------
# IMPRIMO EN CONSOLA, LA CABECERA DE LA APP
# ------------------------------------------------------------------------------
def print_header():
    clear_screen() 
    print(info)

# ------------------------------------------------------------------------------
# IMPRIMO EL ERROR EN LA CONSOLA
# ------------------------------------------------------------------------------
def print_error( message, e=None ):
    debug_error_text = ''
    if e :
        debug_error_text = f"\n\n {e}"
        
    print(f""" -------------------------------------------------
 ---- ERROR: -------------------------------------
 -------------------------------------------------
{message}{debug_error_text}
 -------------------------------------------------
 """)

# ------------------------------------------------------------------------------
# TERMINO LA APLICACIÓN
# ------------------------------------------------------------------------------
from sys import exit

def terminar( message='' ):
    #input("\n PULSA ENTER PARA TERMINAR")
    exit()
        
# ------------------------------------------------------------------------------
# DEVUELVO UN NÚMERO PEDIDO AL USUARIO
# ------------------------------------------------------------------------------
def ask_a_number( msg='Introduce un número', detalle='' ):
    num = None
    while( num == None ):
        num = ask_a_value(msg)
        try:
            num = int( num )
        except Exception as e:
            continue
    return num

# ------------------------------------------------------------------------------
# DEVUELVO UN VALOR PEDIDO AL USUARIO
# ------------------------------------------------------------------------------
def ask_a_value( msg='Introduce un valor', detalle='' ):
    if( detalle == '' ):
        print(f" {msg}: ", end='')
    else:
        print(f" {msg}\n {detalle} ", end='')
    value = None
    while( value==None or value=='' ):
        value = input('').lstrip().rstrip().strip()
    return value

# ------------------------------------------------------------------------------
# DEVUELVO INT CON LA OPCIÓN INTRODUCIDA POR EL USUARIO
# ------------------------------------------------------------------------------
def get_op_menu():
    print(menu_options_text)
    op = -2
    while op<-1 or op>4:
        op = ask_a_number('Selecciona una opcion')
    return op

# ------------------------------------------------------------------------------
# LIMPIO LA CONSOLA
# ------------------------------------------------------------------------------
import os

def clear_screen():
    if(os.name=='nt' or os.name=='ce' or os.name=='dos'):
        os.system('cls')
    elif (os.name=='posix' or os.name=='mac' or os.name=='java'):
        os.system('clear')
