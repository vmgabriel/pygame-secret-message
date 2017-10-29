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
        self.estadoBoton = 1 #Estado actual del Boton
        self.color1 = (200, 176, 148) #Color sin pasar por el
        self.color2 = (145, 118, 86) #Color pasando por el
        self.color3 = (0, 0, 0) #Color cuando es seleccionado
        self.colorletra1 = (0, 0, 0) #Color de la letra 1
        self.colorletra2 = (255, 255, 255) # Color de la letra 2
        self.colorletra3 = (190, 190, 190) #Color de la letra 3
        self.rectt = (100, 100, 200, 50) #Tamaño del boton
        self.width = 0 #Tamaño de los bordes
        self.string = datoInterno #nombre que va a tener que es visible
        self.postextoX = self.rectt[2] + 100
        self.postextoY = self.rectt[3] + 25
        self.texto = Titulo(self.string, self.postextoX, self.postextoY, 15, 2,
            self.colorletra1)
        self.eventoActivo = 1

    def pintar(self,tamVentana):
        """
        Pinta el Cuadro

        @param tamVentana: Tamano de la ventana
        @type tamVentana: Surface
        """
        self.actualizarBoton()
        if (self.estadoBoton == 1):
            pygame.draw.rect(tamVentana, self.color1, self.rectt, self.width)
        elif (self.estadoBoton == 2):
            pygame.draw.rect(tamVentana, self.color2, self.rectt, self.width)
        elif (self.estadoBoton == 3):
            pygame.draw.rect(tamVentana, self.color3, self.rectt, self.width)
        self.texto.pintar(tamVentana)

    def actualizarBoton(self):
        """Actualiza el boton con alguno de los componentes cambiados"""
        if (self.estadoBoton == 1):
            self.texto = Titulo(self.string, self.postextoX, self.postextoY, 15, 2,
                self.colorletra1)
        elif (self.estadoBoton == 2):
            self.texto = Titulo(self.string, self.postextoX, self.postextoY, 15, 2,
                self.colorletra2)
        elif (self.estadoBoton == 3):
            self.texto = Titulo(self.string, self.postextoX, self.postextoY, 15, 2,
                self.colorletra3)

    def estaEncima(self, posX, posY):
        """
        Revisa si las coordenadas que se dan estan dentro del boton

        @param posX: Posicion X que se va a revisar
        @type posX: int
        @param posY: Posicion Y que se va a revisar
        @type posY: int

        @return: Valor True o False diciendo si esta encima
        @rtype: bool
        """
        return ((self.rectt[0] <= posX and self.rectt[1] <= posY) and
            ((self.rectt[0] + self.rectt[2]) >= posX) and
            ((self.rectt[1] + self.rectt[3]) >= posY))

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
        self.actualizarBoton()

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
        self.actualizarBoton()

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
        self.actualizarBoton()

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
        self.actualizarBoton()

    def modificarColor3(self, R, G, B):
        """
        Modifica los colores del boton estando el cursor encima

        @param R: Seleccion del color para RGB
        @param G: Seleccion del color para RGB
        @param B: Seleccion del color para RGB
        @type R: int
        @type G: int
        @type B: int
        """
        self.color3 = (R, G, B)
        self.actualizarBoton()

    def modificarColorLetra1(self, R, G, B):
        """
        Modifica los colores de la letra del boton sin estar el cursor encima

        @param R: Seleccion del color para RGB
        @param G: Seleccion del color para RGB
        @param B: Seleccion del color para RGB
        @type R: int
        @type G: int
        @type B: int
        """
        self.colorletra1 = (R, G, B)
        self.actualizarBoton()

    def modificarColorLetra2(self, R, G, B):
        """
        Modifica los colores de la letra del boton estando el cursor encima

        @param R: Seleccion del color para RGB
        @param G: Seleccion del color para RGB
        @param B: Seleccion del color para RGB
        @type R: int
        @type G: int
        @type B: int
        """
        self.colorletra2 = (R, G, B)
        self.actualizarBoton()

    def modificarColorLetra3(self, R, G, B):
        """
        Modifica los colores de la letra del boton estando el cursor encima

        @param R: Seleccion del color para RGB
        @param G: Seleccion del color para RGB
        @param B: Seleccion del color para RGB
        @type R: int
        @type G: int
        @type B: int
        """
        self.colorletra3 = (R, G, B)
        self.actualizarBoton()

    def modificarGrosor(self,width):
        """
        Modifica el grueso del boton

        @param width: Ancho del borde del boton
        @type width: int
        """
        self.width = width
        self.actualizarBoton()

    def modificarEstadoBoton(self,estado):
        """
        Modifica el actual estado del boton

        @param estado: Estado del boton a cambiar
        @type estado: int
        """
        self.estadoBoton = estado

    def modificarEvento(self, evento):
        """
        Evento que se va a enlazar cuando se activa con el cursor oprimido

        @param evento: Numero de enlace para los eventos
        @type evento: int
        """
        self.eventoActivo = evento

    def getColor1(self):
        """
        Retorna el valor del color (R, G, B)

        @return: Color actual del boton
        @rtype: (R, G, B)
        """
        return self.color1

    def getColor2(self):
        """
        Retorna el valor del color2 (R, G, B)

        @return: Color 2 actual del boton
        @rtype: (R, G, B)
        """
        return self.color2

    def getColor3(self):
        """
        Retorna el valor del color3 (R, G, B)

        @return: Color 3 actual del boton
        @rtype: (R, G, B)
        """
        return self.color3

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

    def getEstadoBoton(self):
        """
        Retorna el estado del boton sea:
            1. Color1, Letra1 para el boton inactivo
            2. Color2, Letra2 para el boton con el cursor encima
            3. Color3, Letra3 para el boton oprimido

        @return: Entero que da el actual estado del boton
        @rtype: int
        """
        return self.estadoBoton

    def geteventoActivo(self):
        """
        Retorna el Evento del Boton

        @return: Numero del evento del boton
        @rtype: int
        """
        return self.eventoActivo
