#!/urs/bin/env python
# -*- coding: utf-8 -*-

"""
Utilidades de la vista

@author: Dalia Muñoz - Gabriel Vargas
@version: 0.1
@license: GPL
@contact: vmgabriel96@gmail.com
"""

import sys
import pygame
from pygame.locals import *

class Utils:
    """Clase enfocada en la construccion de algunas utilidades del sistema"""
    def __init__(self):
        pass
    
    def load_image(self, filename, transparent=False):
        """
        Metodo que cargara toda imagen que sele de, esta tiene que tener un formato...

        @param filename: Ruta del Archivo
        @type filename: str
        @param transparent: Parametro no necesario, le da transparencia a la imagen, por defecto esta en falso
        @type transparent: bool

        @return: Imagen Cargada y lista para usar
        @rtype: Image
        """
        try: image = pygame.image.load(filename)
        except pygame.error, message:
            raise SystemExit, message
        image = image.convert()
        if transparent:
            color = image.get_at((0,0))
            image.set_colorkey(color, RLEACCEL)
        return image

    def texto(self, texto, posx, posy, color=(255, 255, 255)):
        """
        Metodo cuyo uso se enfoca en construir el texto para el juego

        @param texto: Texto que se va a construir con la tipografia
        @type texto: str
        @param posx: Posicion en la coordenada X donde se va a poner
        @type posx: int
        @param posy: Posicion en la coordenada Y donde se va a poner
        @type posy: int
        @param color: Color que se le va a dar al texto
        @type color: Color RSA

        @return: tupla con el sprite y su correspondiente rect
        @rtype: pygame.font.render, pygame.font.render.get_rect
        """
        fuente = pygame.font.Font("view/tipografias/Bethanie-Snake.ttf", 40)
        salida = pygame.font.Font.render(fuente, texto, 1, color)
        salida_rect = salida.get_rect()
        salida_rect.centerx = posx
        salida_rect.centery = posy
        return salida, salida_rect
