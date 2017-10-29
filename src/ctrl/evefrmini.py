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
    botones = []
    """Lista de todos los botones que an sido instanciados y asociados a un evento"""

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

    def enviarEventoBoton(self, boton):
        self.botones.append(boton)

    def evePrincipal(self,evento):
        """
        Metodo que gestionara todos los procesos del juego

        @param evento: Eventos que suceden en el momento
        @type evento: Event
        """
        self.is_running=True
        if evento.type == QUIT:
            self.salir()
        if evento.type == pygame.MOUSEBUTTONDOWN:
            for x in self.botones:
                if (x.estaEncima(evento.pos[0], evento.pos[1])):
                    if (x.geteventoActivo() == 1):
                        print("Evento Activo 1")
                    if (x.geteventoActivo() == 2):
                        print("Evento Activo 2")
                    if (x.geteventoActivo() == 3):
                        print("Evento Activo 3")
                    if (x.geteventoActivo() == 4):
                        print("Evento Activo 4")
        if evento.type == pygame.MOUSEBUTTONUP:
            for x in self.botones:
                if (x.estaEncima(evento.pos[0], evento.pos[1])):
                    x.modificarEstadoBoton(2)
        if evento.type == pygame.MOUSEMOTION:
            for x in self.botones:
                if (x.estaEncima(evento.pos[0], evento.pos[1])):
                    x.modificarEstadoBoton(2)
                else:
                    x.modificarEstadoBoton(1)
