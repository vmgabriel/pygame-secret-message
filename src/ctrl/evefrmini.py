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
        self.eventoEjecutado = 0
        """Evento que puede enviarse a el formulario para saber en que estado esta"""
        self.tiempo = 0
        self.opcion_escojida = ""

    def salir(self):
        """Metodo de salida del proceso"""
        sys.exit(0)

    def getTiempo(self):
        return self.tiempo

    def setTiempo(self, tiempo):
        self.tiempo = tiempo

    def getOpcionEscojida(self):
        return self.opcion_escojida

    def setOpcionEscojida(self, opcion):
        self.opcion_escojida = opcion

    def enviarEventoBoton(self, boton):
        """
        Metodo que recibe los botones para revisar sus eventos

        @param boton: Boton a revisar evento
        @type boton: Boton
        """
        self.botones.append(boton)

    def getEventoEjecutado(self):
        """
        Retorna el evento que ejecuto algun boton

        @return: eventoejecutado
        @rtype: int
        """
        return self.eventoEjecutado

    def setEventoEjecutado(self,ee):
        self.eventoEjecutado=ee

    def desactivarBotonesMenuPrincipal(self):
        """
        Desactiva los botones del menu principal
        """
        #Los botones van de 0 a 3
        a = 0
        for x in self.botones:
            if a < 4:
                x.modificarActivo(False)
                a = a + 1

    def activarBotonesMenuPrincipal(self):
        """
        Activa los botones del menu principal
        """
        #Los botones van de 0 a 3
        a = 0
        for x in self.botones:
            if a < 4:
                x.modificarActivo(True)
                a = a + 1

    def desactivarBotonesMenuSalida(self):
        """
        Desactiva los botones del menu de Salida
        """
        #Los Botones son 4 y 5
        self.botones[4].modificarActivo(False)
        self.botones[5].modificarActivo(False)

    def activarBotonesMenuSalida(self):
        """
        Activa los botones del menu de Salida
        """
        #Los Botones son 4 y 5
        self.botones[4].modificarActivo(True)
        self.botones[5].modificarActivo(True)

    def desactivarBotonesPuntuacion(self):
        """
        Desactiva los botones de la puntuacion
        """
        self.botones[6].modificarActivo(False)

    def activarBotonesPuntuacion(self):
        """
        Activa los botones de la puntuacion
        """
        self.botones[6].modificarActivo(True)

    def activarBotonesTutorial(self):
        """Activa el conjunto de botones"""
        self.botones[7].modificarActivo(True)
        self.botones[8].modificarActivo(True)
        self.botones[9].modificarActivo(True)
        self.botones[10].modificarActivo(True)
        self.botones[11].modificarActivo(True)
        self.botones[12].modificarActivo(True)

    def desactivarBotonesTutorial(self):
        """Desactiva el conjunto de botones"""
        self.botones[7].modificarActivo(False)
        self.botones[8].modificarActivo(False)
        self.botones[9].modificarActivo(False)
        self.botones[10].modificarActivo(False)
        self.botones[11].modificarActivo(False)
        self.botones[12].modificarActivo(False)

    def activarBotonesJuego(self):
        """Activa el conjunto de botones del juego"""
        self.botones[13].modificarActivo(True)
        self.botones[14].modificarActivo(True)
        self.botones[15].modificarActivo(True)
        self.botones[16].modificarActivo(True)
        self.botones[17].modificarActivo(True)

    def desactivarBotonesJuego(self):
        """Desactiva el conjunto de botones del juego"""
        self.botones[13].modificarActivo(False)
        self.botones[14].modificarActivo(False)
        self.botones[15].modificarActivo(False)
        self.botones[16].modificarActivo(False)
        self.botones[17].modificarActivo(False)

    def evePrincipal(self,evento,TIEMPO):
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
                        self.eventoEjecutado = 2
                    if (x.geteventoActivo() == 2):
                        self.eventoEjecutado = 3
                    if (x.geteventoActivo() == 3):
                        self.eventoEjecutado = 4
                    if (x.geteventoActivo() == 4):
                        self.eventoEjecutado = 5
                    if (x.geteventoActivo() == 5):
                        self.salir()
                    if (x.geteventoActivo() == 6):
                        self.eventoEjecutado = 1
                    if (x.geteventoActivo() == 7):
                        if (self.eventoEjecutado < 8):
                            self.eventoEjecutado = 8
                        elif (self.eventoEjecutado >= 8):
                            self.eventoEjecutado += 1
                        if (self.eventoEjecutado == 16):
                            self.eventoEjecutado = 1
                    if (x.geteventoActivo() == 8 or x.geteventoActivo() == 9 or x.geteventoActivo() == 10 or x.geteventoActivo() == 11):
                        self.opcion_escojida = x.getString()
        if evento.type == pygame.MOUSEBUTTONUP:
            for x in self.botones:
                if (x.estaEncima(evento.pos[0], evento.pos[1])):
                    x.modificarEstadoBoton(2)
            if (self.eventoEjecutado == 1):
                self.activarBotonesMenuPrincipal()
                self.desactivarBotonesMenuSalida()
                self.desactivarBotonesPuntuacion()
                self.desactivarBotonesTutorial()
                self.desactivarBotonesJuego()
        if evento.type == pygame.MOUSEMOTION:
            for x in self.botones:
                if (x.estaEncima(evento.pos[0], evento.pos[1])):
                    x.modificarEstadoBoton(2)
                else:
                    x.modificarEstadoBoton(1)
        if evento.type == TIEMPO:
            self.tiempo-=1
