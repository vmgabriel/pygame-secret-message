#!/urs/bin/env python
# -*- coding: utf-8 -*-

import sys
import pygame
from pygame.locals import *

"""
Archivo de la clase Imagenes, se centra en cargar los datos de los archivos

@author: Dalia Muñoz - Gabriel Vargas
@version: 0.1
@license: GPL
@contact: vmgabriel96@gmail.com
"""

class Imagen(object):
    """Clase enfocada en la construccion de las imagenes"""
    direccion = ""
    """Variable enfocada en la ruta del archivos"""
    posicion = (0, 0)
    """Guardara la posicion de la imagen donde va a aparecer en la pantalla"""

    def __init__(self, direccion = "", posicion = (0,0), transparencia = False):
        """
        Enfocado en guardar las propiedades iniciales de la imagen

        @param direccion: Ruta de la imagen
        @type direccion: str
        @param posicion: Posicion de la imagen que va aparecer en pantalla
        @type posicion: (int, int)
        """
        self.direccion = direccion
        self.posicion = posicion

        #Cargara de forma global para la clase la imagen
        self.imagen_cargada = self.load_image(self.direccion, transparencia)

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

    def ponerImagen(self, screen):
        """
        Es el encargado de mostrar la imagen en el screen

        @param screen: Es la pantalla generada por PYGAME para su posterior uso
        @type screen: Surface
        """
        screen.blit(self.imagen_cargada, self.posicion)
