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
        self.is_running = False
        """Variable cargadora de algunos procesos"""

    def salir(self):
        """Metodo de salida del proceso"""
        sys.exit(0)

    # def getEventosPersonalizados(self,ev1,ev2):
    #     """
    #     Recibira los eventos personalizados para poder ser personalizados
    #
    #     @type ev1: Evento personalizado 1 entrada de imagen inicializada en la vista
    #     @type ev2: Evento personalizado 2 salida de imagen inicializada en la vista
    #     """
    #     self.ev1=ev1
    #     self.ev2=ev2

    def evePrincipal(self,evento):
        """
        Metodo que gestionara todos los procesos del juego

        @param evento: Eventos que suceden en el momento
        @type evento: Event
        """
        self.is_running=True
        if evento.type == QUIT:
            self.salir()
