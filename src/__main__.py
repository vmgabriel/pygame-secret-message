#!/urs/bin/env python
# -*- coding: utf-8 -*-

"""
Archivo enfocado en cargar las secciones del programa,FAVOR CARGAR TODO CON PYTHON 2.7

@author: Dalia Muñoz - Gabriel Vargas
@version: 0.1
@license: GPL
@contact: vmgabriel96@gmail.com
"""
import sys
import pygame
from ctrl import eveFrmIni
from model import principal
from view import frmIni

def main():
    """
    Metodo Principal construido en pase de python

    @note: Cargador Principal para evitar la priorizacion
    """
    controlador = eveFrmIni()
    vista = frmIni(controlador)
    vista.run()
    return 0

if __name__ == "__main__":
    """
    Metodo Principal

    @note: Cargador Principal correra Cli.run() que estará en cli/
    """
    pygame.init()
    main()
