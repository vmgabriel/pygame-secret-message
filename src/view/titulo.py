#!/urs/bin/env python
# -*- coding: utf-8 -*-

import sys
import pygame
from pygame.locals import *

"""
Archivo de la clase Titulo, se centra en crear los titulos en general

@author: Dalia Muñoz - Gabriel Vargas
@version: 0.1
@license: GPL
@contact: vmgabriel96@gmail.com
"""

class Titulo(object):
    """Clase enfocada en la construccion de titulos"""
    tipografia1 = "view/tipografias/gunplay-3d.ttf"
    """Tipografia1 que se va a usar"""
    tipografia2 = "view/tipografias/gunplay-rg.ttf"
    """tipografia2 que se va a usar"""
    tipografia3 = "view/tipografias/neuropol.ttf"

    def __init__(self, texto, posx, posy, tam = 40, tipografia = 1,
        color=(255, 255, 255)):
        """
        Constructor del texto

        @param texto: Texto que se va a construir con la tipografia
        @type texto: str
        @param posx: Posicion en la coordenada X donde se va a poner
        @type posx: int
        @param posy: Posicion en la coordenada Y donde se va a poner
        @type posy: int
        @param tam: tamaño de la letra
        @type tam: int
        @param tipografia: Tipo de Tipografia a usar
        @type tipografia: int
        @param color: Color que se le va a dar al texto
        @type color: Color RSA
        """
        if (tipografia == 1):
            self.fuente = pygame.font.Font(self.tipografia1, tam)
        elif (tipografia == 2):
            self.fuente = pygame.font.Font(self.tipografia2, tam)
        else:
            self.fuente = pygame.font.Font(self.tipografia3, tam)
        self.salida = pygame.font.Font.render(self.fuente, texto, 1, color)
        self.salida_rect = self.salida.get_rect()
        self.salida_rect.centerx = posx
        self.salida_rect.centery = posy

    def pintar(self, screen):
        """
        Pinta El Texto en la Pantalla

        @param screen: Pantalla en la que se va a imprimir el texto
        @type screen: Surface
        """
        screen.blit(self.salida, self.salida_rect)
