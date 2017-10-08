#!/urs/bin/env python
# -*- coding: utf-8 -*-

import sys
import pygame
from pygame.locals import *

"""
Archivo enfocado en controlar los eventos del sistema

@author: Dalia Muñoz - Gabriel Vargas
@version: 0.1
@license: GPL
@contact: vmgabriel96@gmail.com
"""

class eveFrmIni:
    """Clase enfocada en la inspeccion de los eventos del sistema del formulario, juego"""
    def __init__(self):
        """Constructor la clase manejadora de los eventos"""
        self.inicializador=0
        """Variable cargadora de algunos procesos"""

    def salir(self):
        """Metodo de salida del proceso"""
        sys.exit(0)

    def evePrincipal(self,evento):
        """
        Metodo que gestionara todos los procesos del juego

        @param evento: Eventos que suceden en el momento
        @type evento: Event
        """
        if evento.type == QUIT:
            self.salir()
