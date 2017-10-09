#!/urs/bin/env python
# -*- coding: utf-8 -*-

import sys
import pygame
from pygame.locals import *
from utils import Utils

"""
Archivo de la clase Boton, se centra en crear botones para el menu

@author: Dalia Muñoz - Gabriel Vargas
@version: 0.1
@license: GPL
@contact: vmgabriel96@gmail.com
"""

class Boton:
    """Crea Botones con algunas caracteristicas generales para el menu"""
    def __init__(self,datoInterno):
        self.color1 = (200, 176, 148)
        self.color2 = (145, 118, 86)
        self.rectt = (100, 100, 200, 50)
        self.width = 0
        self.string = datoInterno
        self.utilidades = Utils()

    def pintar(self,tamVentana):
        pygame.draw.rect(tamVentana, self.color1, self.rectt, self.width)

    def modificarString(self, string):
        self.string = string

    def modificarTamano(self, posX, poxY):
        self.rectt = (self.rectt[0], self.rectt[1], posX, posY)

    def modificarPosicion(self, tamX, tamY):
        self.rectt = (tamX, tamY, self.rectt[2], self.rectt[3])

    def modificarColor1(self, R, G, B):
        self.color1 = (R, G, B)

    def modificarColor2(self, R, G, B):
        self.color2 = (R, G, B)

    def modificarGrosor(self,width):
        self.width = width

    def getColor(self):
        return self.color

    def getRect(self):
        return self.rectt

    def getWidth(self):
        return self.width

    def getString(self):
        return self.string
