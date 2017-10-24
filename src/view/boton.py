#!/urs/bin/env python
# -*- coding: utf-8 -*-

import sys
import pygame
from pygame.locals import *
from titulo import Titulo

"""
Archivo de la clase Boton, se centra en crear botones para el menu

@author: Dalia Muñoz - Gabriel Vargas
@version: 0.1
@license: GPL
@contact: vmgabriel96@gmail.com
"""

class Boton(object):
    """Crea Botones con algunas caracteristicas generales para el menu"""

    def __init__(self,datoInterno):
        """Cargador principal del boton gestiona en general todas las propiedades
        del la clase

        @param datoInterno: Nombre que habra adentro del boton
        @type datoInterno: str
        """
        self.color1 = (200, 176, 148) #Color sin pasar por el
        self.color2 = (145, 118, 86) #Color pasando por el
        self.rectt = (100, 100, 200, 50) #Tamaño del boton
        self.width = 0 #Tamaño de los bordes
        self.string = datoInterno #nombre que va a tener que es visible
        self.postextoX = self.rectt[2] + 100
        self.postextoY = self.rectt[3] + 25
        self.texto = Titulo(self.string, self.postextoX, self.postextoY, 15, 2,
            (0, 0, 0))

    def pintar(self,tamVentana):
        """
        Pinta el Cuadro

        @param tamVentana: Tamano de la ventana
        @type tamVentana: Surface
        """
        pygame.draw.rect(tamVentana, self.color1, self.rectt, self.width)
        self.texto.pintar(tamVentana)

    def modificarString(self, string):
        """
        Modifica string visible

        @param string: Nombre nuevo
        @type string: str
        """
        self.string = string

    def modificarTamano(self, posX, posY):
        """
        Modifica el tamano de los botones

        @param posX: tamano por X
        @param posY: tamano por Y
        @type posX: int
        @type posY: int
        """
        self.rectt = (self.rectt[0], self.rectt[1], posX, posY)

    def modificarPosicion(self, tamX, tamY):
        """
        Modifica la posicion que va a aparecer los botones

        @param tamX: posicion por X
        @param tamY: posicion por Y
        @type tamX: int
        @type tamY: int
        """

        self.rectt = (tamX, tamY, self.rectt[2], self.rectt[3])
        self.postextoX = tamX + 100
        self.postextoY = tamY + 25
        self.texto = Titulo(self.string, self.postextoX, self.postextoY, 15, 2,
            (0, 0, 0))

    def modificarColor1(self, R, G, B):
        """
        Modifica los colores del boton sin estar el cursor encima

        @param R: Seleccion del color para RGB
        @param G: Seleccion del color para RGB
        @param B: Seleccion del color para RGB
        @type R: int
        @type G: int
        @type B: int
        """
        self.color1 = (R, G, B)

    def modificarColor2(self, R, G, B):
        """
        Modifica los colores del boton estando el cursor encima

        @param R: Seleccion del color para RGB
        @param G: Seleccion del color para RGB
        @param B: Seleccion del color para RGB
        @type R: int
        @type G: int
        @type B: int
        """
        self.color2 = (R, G, B)

    def modificarGrosor(self,width):
        """
        Modifica el grueso del boton

        @param width: Ancho del borde del boton
        @type width: int
        """
        self.width = width

    def getColor(self):
        """
        Retorna el valor del color (R, G, B)

        @return: Color actual del boton
        @rtype: (R, G, B)
        """
        return self.color

    def getRect(self):
        """
        Retorna el valor del boton, este tiene (TamX, TamY, PosX, PosY)

        @return: Datos con respecto a tamano y posicion
        @rtype: (TamX, TamY, PosX, PosY)
        """
        return self.rectt

    def getWidth(self):
        """
        Retorna el ancho del borde del boton

        @return: Ancho del borde del boton
        @rtype: int
        """
        return self.width

    def getString(self):
        """
        Retorna el valor del string interno

        @return: String interno que se muestra en el boton
        @rtype: str
        """
        return self.string
