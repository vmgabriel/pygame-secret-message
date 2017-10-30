#!/urs/bin/env python
# -*- coding: utf-8 -*-

#modulos
import os
import sys
import pygame
from pygame.locals import *
from boton import Boton
from imagenes import Imagen
from titulo import Titulo
from tutorial import Tutorial

"""
Formulario que cargara, primera ventana

@author: Dalia Muñoz - Gabriel Vargas
@version: 0.1
@license: GPL
@contact: vmgabriel96@gmail.com
"""

class frmIni:
    """Clase que cargara la primera ventana"""
    def __init__(self,ctrl):
        """
        Constructor de la clase frmIni, inicializara algunas variables

        @param ctrl: Seccion controladora que se va a enfocar en el manejo de eventos en el juego
        @type ctrl: ctrl.eveFrmIni
        """
        self.WIDTH = 640
        """Variable del ancho de la ventana"""
        self.HEIGHT = 480
        """Variable del alto de la ventana"""
        self.titulo = "KACH! - Diversion Oculta!"
        """Titulo de la ventana"""
        self.screen = None
        """Enfocado en la ventana como tal"""
        self.controlador = ctrl
        """Es quien maneja los eventos"""
        self.etapa = 0
        """Es quien da la seccion en la que vamos en el programa"""
        self.color_fondo = (255, 255, 255)

    def menu(self):
        """
        Seccion del menu para el video juego
        """
        self.fondo_menu = Imagen("view/img/fondos/Egipto.jpg", (0, 0))
        self.fondo_menu.cambiarEscala(0.4)
        self.titulomenu = Titulo("KACH!", 150, 380, 70, 2, (36, 32, 163))
        #Todos los botones con sus respectivas posiciones
        self.btnTutorial = Boton("Tutorial")
        self.btnTutorial.modificarPosicion(400, 140)
        self.btnTutorial.modificarColor1(234, 234, 216)
        self.btnTutorial.modificarColorLetra1(21, 67, 96)
        self.btnTutorial.modificarColor2(209, 210, 179)
        self.btnTutorial.modificarColorLetra2(21, 67, 96)
        self.btnTutorial.modificarColor3(91, 202, 213)
        self.btnTutorial.modificarColorLetra3(21, 67, 96)
        self.btnTutorial.modificarEvento(1)
        self.btnEncriptar = Boton("Jugar")
        self.btnEncriptar.modificarPosicion(400, 220)
        self.btnEncriptar.modificarColor1(234, 234, 216)
        self.btnEncriptar.modificarColorLetra1(21, 67, 96)
        self.btnEncriptar.modificarColor2(209, 210, 179)
        self.btnEncriptar.modificarColorLetra2(21, 67, 96)
        self.btnEncriptar.modificarColor3(91, 202, 213)
        self.btnEncriptar.modificarColorLetra3(21, 67, 96)
        self.btnEncriptar.modificarEvento(2)
        self.btnPuntaje = Boton("Puntajes")
        self.btnPuntaje.modificarPosicion(400, 300)
        self.btnPuntaje.modificarColor1(234, 234, 216)
        self.btnPuntaje.modificarColorLetra1(21, 67, 96)
        self.btnPuntaje.modificarColor2(209, 210, 179)
        self.btnPuntaje.modificarColorLetra2(21, 67, 96)
        self.btnPuntaje.modificarColor3(91, 202, 213)
        self.btnPuntaje.modificarColorLetra3(21, 67, 96)
        self.btnPuntaje.modificarEvento(3)
        self.btnSalir = Boton("Salir")
        self.btnSalir.modificarPosicion(400, 380)
        self.btnSalir.modificarColor1(234, 234, 216)
        self.btnSalir.modificarColorLetra1(21, 67, 96)
        self.btnSalir.modificarColor2(209, 210, 179)
        self.btnSalir.modificarColorLetra2(21, 67, 96)
        self.btnSalir.modificarColor3(91, 202, 213)
        self.btnSalir.modificarColorLetra3(21, 67, 96)
        self.btnSalir.modificarEvento(4)

        #Enviando eventos de los botones
        self.controlador.enviarEventoBoton(self.btnEncriptar)
        self.controlador.enviarEventoBoton(self.btnTutorial)
        self.controlador.enviarEventoBoton(self.btnPuntaje)
        self.controlador.enviarEventoBoton(self.btnSalir)


    def cargaCreditosInicio(self):
        """
        Cargara algunas imagenes que se mostraran en la mitad de la pantalla para el inicio del juego
        """
        self.Logo1 = Imagen("view/img/UD-logo.gif", (220, 130))
        self.Logo2 = Imagen("view/img/python-logo.png", (210, 130), True)
        self.Logo3 = Imagen("view/img/pygame-logo.jpg", (120, 100))

        self.imagen_fondo_presentacion = Imagen("view/img/fondos/Egipto-night.jpg",
            (0, 0))
        self.imagen_fondo_presentacion.cambiarEscala(0.4)
        self.titulopresentacion = Titulo("KACH!", 320, 180, 60, 1, (255, 255, 255))
        self.subtitulopresentacion = Titulo("Diversion Oculta!", 320, 250,
            30, 4, (230, 233, 48))

    def menuSalida(self):
        """
        Cargara el menu de salida
        """
        self.fondo_menu = Imagen("view/img/fondos/Egipto.jpg", (0, 0))
        self.fondo_menu.cambiarEscala(0.4)
        self.titulomenu = Titulo("KACH!", 150, 380, 70, 2, (36, 32, 163))
        self.mensaje_salida = Titulo("Desea Salir ?", 350, 200, 40, 4, (36, 32, 163))

        self.btnSi = Boton("Si")
        self.btnSi.modificarPosicion(280, 420)
        self.btnSi.modificarTamano(160,50)
        self.btnSi.modificarPosicionTexto(30, 27)
        self.btnSi.modificarColor1(234, 234, 216)
        self.btnSi.modificarColorLetra1(21, 67, 96)
        self.btnSi.modificarColor2(209, 210, 179)
        self.btnSi.modificarColorLetra2(21, 67, 96)
        self.btnSi.modificarColor3(91, 202, 213)
        self.btnSi.modificarColorLetra3(21, 67, 96)
        self.btnSi.modificarEvento(5)
        self.btnNo = Boton("No")
        self.btnNo.modificarPosicion(460, 420)
        self.btnNo.modificarTamano(160,50)
        self.btnNo.modificarPosicionTexto(30, 27)
        self.btnNo.modificarColor1(234, 234, 216)
        self.btnNo.modificarColorLetra1(21, 67, 96)
        self.btnNo.modificarColor2(209, 210, 179)
        self.btnNo.modificarColorLetra2(21, 67, 96)
        self.btnNo.modificarColor3(91, 202, 213)
        self.btnNo.modificarColorLetra3(21, 67, 96)
        self.btnNo.modificarEvento(6)

        #Eventos de los botones
        self.controlador.enviarEventoBoton(self.btnSi)
        self.controlador.enviarEventoBoton(self.btnNo)

    def vistaPuntuacion(self):
        """
        Mostrara en general la puntuacion
        """
        self.fondo_puntuacion = Imagen("view/img/fondos/PaisesBajos.jpg", (0, 0))
        self.fondo_puntuacion.cambiarEscala(0.7)
        self.lblPuntuacion = Titulo("Puntuacion", 450, 30, 40, 2, (36, 32, 163))
        self.titulomenu = Titulo("KACH!", 120, 450, 70, 2, (36, 32, 163))

        #Construccion de la tabla, este va a ser una suma de botones
        self.tablanum = Boton("N")
        self.tablanum.modificarPosicion(30,50)
        self.tablanum.modificarTamano(40,40)
        self.tablanum.modificarPosicionTexto(20, 20)
        self.tablanum.modificarColor1(234, 234, 216)
        self.tablanum.modificarColor2(234, 234, 216)
        self.tablanum.modificarColor3(234, 234, 216)
        self.tablanum.modificarColorLetra1(21, 67, 96)
        self.tablanum.modificarColorLetra2(21, 67, 96)
        self.tablanum.modificarColorLetra3(21, 67, 96)
        self.tablanum.modificarEvento(0)
        self.tablajug = Boton("Jugador")
        self.tablajug.modificarPosicion(73,50)
        self.tablajug.modificarTamano(300,40)
        self.tablajug.modificarPosicionTexto(40, 20)
        self.tablajug.modificarColor1(234, 234, 216)
        self.tablajug.modificarColor2(234, 234, 216)
        self.tablajug.modificarColor3(234, 234, 216)
        self.tablajug.modificarColorLetra1(21, 67, 96)
        self.tablajug.modificarColorLetra2(21, 67, 96)
        self.tablajug.modificarColorLetra3(21, 67, 96)
        self.tablajug.modificarEvento(0)
        self.tablafecha = Boton("Fecha")
        self.tablafecha.modificarPosicion(375,50)
        self.tablafecha.modificarTamano(120,40)
        self.tablafecha.modificarPosicionTexto(40, 20)
        self.tablafecha.modificarColor1(234, 234, 216)
        self.tablafecha.modificarColor2(234, 234, 216)
        self.tablafecha.modificarColor3(234, 234, 216)
        self.tablafecha.modificarColorLetra1(21, 67, 96)
        self.tablafecha.modificarColorLetra2(21, 67, 96)
        self.tablafecha.modificarColorLetra3(21, 67, 96)
        self.tablafecha.modificarEvento(0)
        self.tablapuntaje = Boton("Puntaje")
        self.tablapuntaje.modificarPosicion(498,50)
        self.tablapuntaje.modificarTamano(100,40)
        self.tablapuntaje.modificarPosicionTexto(40, 20)
        self.tablapuntaje.modificarColor1(234, 234, 216)
        self.tablapuntaje.modificarColor2(234, 234, 216)
        self.tablapuntaje.modificarColor3(234, 234, 216)
        self.tablapuntaje.modificarColorLetra1(21, 67, 96)
        self.tablapuntaje.modificarColorLetra2(21, 67, 96)
        self.tablapuntaje.modificarColorLetra3(21, 67, 96)
        self.tablapuntaje.modificarEvento(0)

        #Para lo demas
        self.tablanum1 = Boton("1")
        self.tablanum1.modificarPosicion(30,92)
        self.tablanum1.modificarTamano(40,40)
        self.tablanum1.modificarPosicionTexto(20, 20)
        self.tablanum1.modificarColor1(234, 234, 216)
        self.tablanum1.modificarColor2(234, 234, 216)
        self.tablanum1.modificarColor3(234, 234, 216)
        self.tablanum1.modificarColorLetra1(21, 67, 96)
        self.tablanum1.modificarColorLetra2(21, 67, 96)
        self.tablanum1.modificarColorLetra3(21, 67, 96)
        self.tablanum1.modificarEvento(0)
        self.tablajug1 = Boton("Jugador1")
        self.tablajug1.modificarPosicion(73,92)
        self.tablajug1.modificarTamano(300,40)
        self.tablajug1.modificarPosicionTexto(40, 20)
        self.tablajug1.modificarColor1(234, 234, 216)
        self.tablajug1.modificarColor2(234, 234, 216)
        self.tablajug1.modificarColor3(234, 234, 216)
        self.tablajug1.modificarColorLetra1(21, 67, 96)
        self.tablajug1.modificarColorLetra2(21, 67, 96)
        self.tablajug1.modificarColorLetra3(21, 67, 96)
        self.tablajug1.modificarEvento(0)
        self.tablafecha1 = Boton("Fecha1")
        self.tablafecha1.modificarPosicion(375,92)
        self.tablafecha1.modificarTamano(120,40)
        self.tablafecha1.modificarPosicionTexto(40, 20)
        self.tablafecha1.modificarColor1(234, 234, 216)
        self.tablafecha1.modificarColor2(234, 234, 216)
        self.tablafecha1.modificarColor3(234, 234, 216)
        self.tablafecha1.modificarColorLetra1(21, 67, 96)
        self.tablafecha1.modificarColorLetra2(21, 67, 96)
        self.tablafecha1.modificarColorLetra3(21, 67, 96)
        self.tablafecha1.modificarEvento(0)
        self.tablapuntaje1 = Boton("Puntaje1")
        self.tablapuntaje1.modificarPosicion(498,92)
        self.tablapuntaje1.modificarTamano(100,40)
        self.tablapuntaje1.modificarPosicionTexto(40, 20)
        self.tablapuntaje1.modificarColor1(234, 234, 216)
        self.tablapuntaje1.modificarColor2(234, 234, 216)
        self.tablapuntaje1.modificarColor3(234, 234, 216)
        self.tablapuntaje1.modificarColorLetra1(21, 67, 96)
        self.tablapuntaje1.modificarColorLetra2(21, 67, 96)
        self.tablapuntaje1.modificarColorLetra3(21, 67, 96)
        self.tablapuntaje1.modificarEvento(0)
        self.tablanum2 = Boton("2")
        self.tablanum2.modificarPosicion(30,134)
        self.tablanum2.modificarTamano(40,40)
        self.tablanum2.modificarPosicionTexto(20, 20)
        self.tablanum2.modificarColor1(234, 234, 216)
        self.tablanum2.modificarColor2(234, 234, 216)
        self.tablanum2.modificarColor3(234, 234, 216)
        self.tablanum2.modificarColorLetra1(21, 67, 96)
        self.tablanum2.modificarColorLetra2(21, 67, 96)
        self.tablanum2.modificarColorLetra3(21, 67, 96)
        self.tablanum2.modificarEvento(0)
        self.tablajug2 = Boton("Jugador2")
        self.tablajug2.modificarPosicion(73,134)
        self.tablajug2.modificarTamano(300,40)
        self.tablajug2.modificarPosicionTexto(40, 20)
        self.tablajug2.modificarColor1(234, 234, 216)
        self.tablajug2.modificarColor2(234, 234, 216)
        self.tablajug2.modificarColor3(234, 234, 216)
        self.tablajug2.modificarColorLetra1(21, 67, 96)
        self.tablajug2.modificarColorLetra2(21, 67, 96)
        self.tablajug2.modificarColorLetra3(21, 67, 96)
        self.tablajug2.modificarEvento(0)
        self.tablafecha2 = Boton("Fecha2")
        self.tablafecha2.modificarPosicion(375,134)
        self.tablafecha2.modificarTamano(120,40)
        self.tablafecha2.modificarPosicionTexto(40, 20)
        self.tablafecha2.modificarColor1(234, 234, 216)
        self.tablafecha2.modificarColor2(234, 234, 216)
        self.tablafecha2.modificarColor3(234, 234, 216)
        self.tablafecha2.modificarColorLetra1(21, 67, 96)
        self.tablafecha2.modificarColorLetra2(21, 67, 96)
        self.tablafecha2.modificarColorLetra3(21, 67, 96)
        self.tablafecha2.modificarEvento(0)
        self.tablapuntaje2 = Boton("Puntaje2")
        self.tablapuntaje2.modificarPosicion(498,134)
        self.tablapuntaje2.modificarTamano(100,40)
        self.tablapuntaje2.modificarPosicionTexto(40, 20)
        self.tablapuntaje2.modificarColor1(234, 234, 216)
        self.tablapuntaje2.modificarColor2(234, 234, 216)
        self.tablapuntaje2.modificarColor3(234, 234, 216)
        self.tablapuntaje2.modificarColorLetra1(21, 67, 96)
        self.tablapuntaje2.modificarColorLetra2(21, 67, 96)
        self.tablapuntaje2.modificarColorLetra3(21, 67, 96)
        self.tablapuntaje2.modificarEvento(0)
        self.tablanum3 = Boton("3")
        self.tablanum3.modificarPosicion(30,176)
        self.tablanum3.modificarTamano(40,40)
        self.tablanum3.modificarPosicionTexto(20, 20)
        self.tablanum3.modificarColor1(234, 234, 216)
        self.tablanum3.modificarColor2(234, 234, 216)
        self.tablanum3.modificarColor3(234, 234, 216)
        self.tablanum3.modificarColorLetra1(21, 67, 96)
        self.tablanum3.modificarColorLetra2(21, 67, 96)
        self.tablanum3.modificarColorLetra3(21, 67, 96)
        self.tablanum3.modificarEvento(0)
        self.tablajug3 = Boton("Jugador3")
        self.tablajug3.modificarPosicion(73,176)
        self.tablajug3.modificarTamano(300,40)
        self.tablajug3.modificarPosicionTexto(40, 20)
        self.tablajug3.modificarColor1(234, 234, 216)
        self.tablajug3.modificarColor2(234, 234, 216)
        self.tablajug3.modificarColor3(234, 234, 216)
        self.tablajug3.modificarColorLetra1(21, 67, 96)
        self.tablajug3.modificarColorLetra2(21, 67, 96)
        self.tablajug3.modificarColorLetra3(21, 67, 96)
        self.tablajug3.modificarEvento(0)
        self.tablafecha3 = Boton("Fecha3")
        self.tablafecha3.modificarPosicion(375,176)
        self.tablafecha3.modificarTamano(120,40)
        self.tablafecha3.modificarPosicionTexto(40, 20)
        self.tablafecha3.modificarColor1(234, 234, 216)
        self.tablafecha3.modificarColor2(234, 234, 216)
        self.tablafecha3.modificarColor3(234, 234, 216)
        self.tablafecha3.modificarColorLetra1(21, 67, 96)
        self.tablafecha3.modificarColorLetra2(21, 67, 96)
        self.tablafecha3.modificarColorLetra3(21, 67, 96)
        self.tablafecha3.modificarEvento(0)
        self.tablapuntaje3 = Boton("Puntaje3")
        self.tablapuntaje3.modificarPosicion(498,176)
        self.tablapuntaje3.modificarTamano(100,40)
        self.tablapuntaje3.modificarPosicionTexto(40, 20)
        self.tablapuntaje3.modificarColor1(234, 234, 216)
        self.tablapuntaje3.modificarColor2(234, 234, 216)
        self.tablapuntaje3.modificarColor3(234, 234, 216)
        self.tablapuntaje3.modificarColorLetra1(21, 67, 96)
        self.tablapuntaje3.modificarColorLetra2(21, 67, 96)
        self.tablapuntaje3.modificarColorLetra3(21, 67, 96)
        self.tablapuntaje3.modificarEvento(0)
        self.tablanum4 = Boton("4")
        self.tablanum4.modificarPosicion(30,218)
        self.tablanum4.modificarTamano(40,40)
        self.tablanum4.modificarPosicionTexto(20, 20)
        self.tablanum4.modificarColor1(234, 234, 216)
        self.tablanum4.modificarColor2(234, 234, 216)
        self.tablanum4.modificarColor3(234, 234, 216)
        self.tablanum4.modificarColorLetra1(21, 67, 96)
        self.tablanum4.modificarColorLetra2(21, 67, 96)
        self.tablanum4.modificarColorLetra3(21, 67, 96)
        self.tablanum4.modificarEvento(0)
        self.tablajug4 = Boton("Jugador4")
        self.tablajug4.modificarPosicion(73,218)
        self.tablajug4.modificarTamano(300,40)
        self.tablajug4.modificarPosicionTexto(40, 20)
        self.tablajug4.modificarColor1(234, 234, 216)
        self.tablajug4.modificarColor2(234, 234, 216)
        self.tablajug4.modificarColor3(234, 234, 216)
        self.tablajug4.modificarColorLetra1(21, 67, 96)
        self.tablajug4.modificarColorLetra2(21, 67, 96)
        self.tablajug4.modificarColorLetra3(21, 67, 96)
        self.tablajug4.modificarEvento(0)
        self.tablafecha4 = Boton("Fecha4")
        self.tablafecha4.modificarPosicion(375,218)
        self.tablafecha4.modificarTamano(120,40)
        self.tablafecha4.modificarPosicionTexto(40, 20)
        self.tablafecha4.modificarColor1(234, 234, 216)
        self.tablafecha4.modificarColor2(234, 234, 216)
        self.tablafecha4.modificarColor3(234, 234, 216)
        self.tablafecha4.modificarColorLetra1(21, 67, 96)
        self.tablafecha4.modificarColorLetra2(21, 67, 96)
        self.tablafecha4.modificarColorLetra3(21, 67, 96)
        self.tablafecha4.modificarEvento(0)
        self.tablapuntaje4 = Boton("Puntaje4")
        self.tablapuntaje4.modificarPosicion(498,218)
        self.tablapuntaje4.modificarTamano(100,40)
        self.tablapuntaje4.modificarPosicionTexto(40, 20)
        self.tablapuntaje4.modificarColor1(234, 234, 216)
        self.tablapuntaje4.modificarColor2(234, 234, 216)
        self.tablapuntaje4.modificarColor3(234, 234, 216)
        self.tablapuntaje4.modificarColorLetra1(21, 67, 96)
        self.tablapuntaje4.modificarColorLetra2(21, 67, 96)
        self.tablapuntaje4.modificarColorLetra3(21, 67, 96)
        self.tablapuntaje4.modificarEvento(0)
        self.tablanum5 = Boton("5")
        self.tablanum5.modificarPosicion(30,260)
        self.tablanum5.modificarTamano(40,40)
        self.tablanum5.modificarPosicionTexto(20, 20)
        self.tablanum5.modificarColor1(234, 234, 216)
        self.tablanum5.modificarColor2(234, 234, 216)
        self.tablanum5.modificarColor3(234, 234, 216)
        self.tablanum5.modificarColorLetra1(21, 67, 96)
        self.tablanum5.modificarColorLetra2(21, 67, 96)
        self.tablanum5.modificarColorLetra3(21, 67, 96)
        self.tablanum5.modificarEvento(0)
        self.tablajug5 = Boton("Jugador5")
        self.tablajug5.modificarPosicion(73,260)
        self.tablajug5.modificarTamano(300,40)
        self.tablajug5.modificarPosicionTexto(40, 20)
        self.tablajug5.modificarColor1(234, 234, 216)
        self.tablajug5.modificarColor2(234, 234, 216)
        self.tablajug5.modificarColor3(234, 234, 216)
        self.tablajug5.modificarColorLetra1(21, 67, 96)
        self.tablajug5.modificarColorLetra2(21, 67, 96)
        self.tablajug5.modificarColorLetra3(21, 67, 96)
        self.tablajug5.modificarEvento(0)
        self.tablafecha5 = Boton("Fecha5")
        self.tablafecha5.modificarPosicion(375,260)
        self.tablafecha5.modificarTamano(120,40)
        self.tablafecha5.modificarPosicionTexto(40, 20)
        self.tablafecha5.modificarColor1(234, 234, 216)
        self.tablafecha5.modificarColor2(234, 234, 216)
        self.tablafecha5.modificarColor3(234, 234, 216)
        self.tablafecha5.modificarColorLetra1(21, 67, 96)
        self.tablafecha5.modificarColorLetra2(21, 67, 96)
        self.tablafecha5.modificarColorLetra3(21, 67, 96)
        self.tablafecha5.modificarEvento(0)
        self.tablapuntaje5 = Boton("Puntaje5")
        self.tablapuntaje5.modificarPosicion(498,260)
        self.tablapuntaje5.modificarTamano(100,40)
        self.tablapuntaje5.modificarPosicionTexto(40, 20)
        self.tablapuntaje5.modificarColor1(234, 234, 216)
        self.tablapuntaje5.modificarColor2(234, 234, 216)
        self.tablapuntaje5.modificarColor3(234, 234, 216)
        self.tablapuntaje5.modificarColorLetra1(21, 67, 96)
        self.tablapuntaje5.modificarColorLetra2(21, 67, 96)
        self.tablapuntaje5.modificarColorLetra3(21, 67, 96)
        self.tablapuntaje5.modificarEvento(0)
        self.tablanum6 = Boton("6")
        self.tablanum6.modificarPosicion(30,302)
        self.tablanum6.modificarTamano(40,40)
        self.tablanum6.modificarPosicionTexto(20, 20)
        self.tablanum6.modificarColor1(234, 234, 216)
        self.tablanum6.modificarColor2(234, 234, 216)
        self.tablanum6.modificarColor3(234, 234, 216)
        self.tablanum6.modificarColorLetra1(21, 67, 96)
        self.tablanum6.modificarColorLetra2(21, 67, 96)
        self.tablanum6.modificarColorLetra3(21, 67, 96)
        self.tablanum6.modificarEvento(0)
        self.tablajug6 = Boton("Jugador6")
        self.tablajug6.modificarPosicion(73,302)
        self.tablajug6.modificarTamano(300,40)
        self.tablajug6.modificarPosicionTexto(40, 20)
        self.tablajug6.modificarColor1(234, 234, 216)
        self.tablajug6.modificarColor2(234, 234, 216)
        self.tablajug6.modificarColor3(234, 234, 216)
        self.tablajug6.modificarColorLetra1(21, 67, 96)
        self.tablajug6.modificarColorLetra2(21, 67, 96)
        self.tablajug6.modificarColorLetra3(21, 67, 96)
        self.tablajug6.modificarEvento(0)
        self.tablafecha6 = Boton("Fecha6")
        self.tablafecha6.modificarPosicion(375,302)
        self.tablafecha6.modificarTamano(120,40)
        self.tablafecha6.modificarPosicionTexto(40, 20)
        self.tablafecha6.modificarColor1(234, 234, 216)
        self.tablafecha6.modificarColor2(234, 234, 216)
        self.tablafecha6.modificarColor3(234, 234, 216)
        self.tablafecha6.modificarColorLetra1(21, 67, 96)
        self.tablafecha6.modificarColorLetra2(21, 67, 96)
        self.tablafecha6.modificarColorLetra3(21, 67, 96)
        self.tablafecha6.modificarEvento(0)
        self.tablapuntaje6 = Boton("Puntaje6")
        self.tablapuntaje6.modificarPosicion(498,302)
        self.tablapuntaje6.modificarTamano(100,40)
        self.tablapuntaje6.modificarPosicionTexto(40, 20)
        self.tablapuntaje6.modificarColor1(234, 234, 216)
        self.tablapuntaje6.modificarColor2(234, 234, 216)
        self.tablapuntaje6.modificarColor3(234, 234, 216)
        self.tablapuntaje6.modificarColorLetra1(21, 67, 96)
        self.tablapuntaje6.modificarColorLetra2(21, 67, 96)
        self.tablapuntaje6.modificarColorLetra3(21, 67, 96)
        self.tablapuntaje6.modificarEvento(0)
        self.tablanum7 = Boton("7")
        self.tablanum7.modificarPosicion(30,344)
        self.tablanum7.modificarTamano(40,40)
        self.tablanum7.modificarPosicionTexto(20, 20)
        self.tablanum7.modificarColor1(234, 234, 216)
        self.tablanum7.modificarColor2(234, 234, 216)
        self.tablanum7.modificarColor3(234, 234, 216)
        self.tablanum7.modificarColorLetra1(21, 67, 96)
        self.tablanum7.modificarColorLetra2(21, 67, 96)
        self.tablanum7.modificarColorLetra3(21, 67, 96)
        self.tablanum7.modificarEvento(0)
        self.tablajug7 = Boton("Jugador7")
        self.tablajug7.modificarPosicion(73,344)
        self.tablajug7.modificarTamano(300,40)
        self.tablajug7.modificarPosicionTexto(40, 20)
        self.tablajug7.modificarColor1(234, 234, 216)
        self.tablajug7.modificarColor2(234, 234, 216)
        self.tablajug7.modificarColor3(234, 234, 216)
        self.tablajug7.modificarColorLetra1(21, 67, 96)
        self.tablajug7.modificarColorLetra2(21, 67, 96)
        self.tablajug7.modificarColorLetra3(21, 67, 96)
        self.tablajug7.modificarEvento(0)
        self.tablafecha7 = Boton("Fecha7")
        self.tablafecha7.modificarPosicion(375,344)
        self.tablafecha7.modificarTamano(120,40)
        self.tablafecha7.modificarPosicionTexto(40, 20)
        self.tablafecha7.modificarColor1(234, 234, 216)
        self.tablafecha7.modificarColor2(234, 234, 216)
        self.tablafecha7.modificarColor3(234, 234, 216)
        self.tablafecha7.modificarColorLetra1(21, 67, 96)
        self.tablafecha7.modificarColorLetra2(21, 67, 96)
        self.tablafecha7.modificarColorLetra3(21, 67, 96)
        self.tablafecha7.modificarEvento(0)
        self.tablapuntaje7 = Boton("Puntaje7")
        self.tablapuntaje7.modificarPosicion(498,344)
        self.tablapuntaje7.modificarTamano(100,40)
        self.tablapuntaje7.modificarPosicionTexto(40, 20)
        self.tablapuntaje7.modificarColor1(234, 234, 216)
        self.tablapuntaje7.modificarColor2(234, 234, 216)
        self.tablapuntaje7.modificarColor3(234, 234, 216)
        self.tablapuntaje7.modificarColorLetra1(21, 67, 96)
        self.tablapuntaje7.modificarColorLetra2(21, 67, 96)
        self.tablapuntaje7.modificarColorLetra3(21, 67, 96)
        self.tablapuntaje7.modificarEvento(0)

        self.btnMenu = Boton("Inicio")
        self.btnMenu.modificarPosicion(460, 420)
        self.btnMenu.modificarTamano(160,50)
        self.btnMenu.modificarPosicionTexto(30, 27)
        self.btnMenu.modificarColor1(234, 234, 216)
        self.btnMenu.modificarColorLetra1(21, 67, 96)
        self.btnMenu.modificarColor2(209, 210, 179)
        self.btnMenu.modificarColorLetra2(21, 67, 96)
        self.btnMenu.modificarColor3(91, 202, 213)
        self.btnMenu.modificarColorLetra3(21, 67, 96)
        self.btnMenu.modificarEvento(6)

        self.controlador.enviarEventoBoton(self.btnMenu)

    def desactivarBotonesMenuPrincipal(self):
        """
        Desactiva los botones del menu principal
        """
        self.btnEncriptar.modificarActivo(False)
        self.btnTutorial.modificarActivo(False)
        self.btnPuntaje.modificarActivo(False)
        self.btnSalir.modificarActivo(False)

    def activarBotonesMenuPrincipal(self):
        """
        Activa los botones del menu principal
        """
        self.btnEncriptar.modificarActivo(True)
        self.btnTutorial.modificarActivo(True)
        self.btnPuntaje.modificarActivo(True)
        self.btnSalir.modificarActivo(True)

    def desactivarBotonesMenuSalida(self):
        """
        Desactiva los botones del menu de Salida
        """
        self.btnSi.modificarActivo(False)
        self.btnNo.modificarActivo(False)

    def activarBotonesMenuSalida(self):
        """
        Activa los botones del menu de Salida
        """
        self.btnSi.modificarActivo(True)
        self.btnNo.modificarActivo(True)

    def desactivarBotonesPuntuacion(self):
        """
        Desactiva los botones de la puntuacion
        """
        self.btnMenu.modificarActivo(False)

    def activarBotonesPuntuacion(self):
        """
        Activa los botones de la puntuacion
        """
        self.btnMenu.modificarActivo(True)

    def run(self):
        """
        El metodo run cargara la ventana, ademas tendra el ciclo principal para el juego en general
        """
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        #Centrar ventana

        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

        #Se empiezan a mostrar las cosas
        pygame.display.set_caption(self.titulo)
        self.cargaCreditosInicio()
        self.menu()
        self.menuSalida()
        self.vistaPuntuacion()
        tutorial = Tutorial(self.controlador)

        #While principal, es el enfocado de correr los procesos del juego
        while True:
            for eventos in pygame.event.get():
                self.controlador.evePrincipal(eventos)

            if self.etapa == 0:
                #En la seccion que muestra los logos de todo
                self.screen.fill(self.color_fondo)
                self.Logo1.ponerImagen(self.screen)
                pygame.display.flip()
                pygame.time.wait(3000)

                self.screen.fill(self.color_fondo)
                self.Logo2.ponerImagen(self.screen)
                pygame.display.flip()
                pygame.time.wait(3000)

                self.screen.fill(self.color_fondo)
                self.Logo3.ponerImagen(self.screen)
                pygame.display.flip()
                pygame.time.wait(3000)

                self.imagen_fondo_presentacion.ponerImagen(self.screen)
                self.titulopresentacion.pintar(self.screen)
                self.subtitulopresentacion.pintar(self.screen)
                pygame.display.flip()
                pygame.time.wait(3000)

                self.screen.fill(self.color_fondo)
                self.etapa = 1
            if self.etapa == 1:
                #Activar los botones si estan desactivados
                self.activarBotonesMenuPrincipal()
                self.desactivarBotonesMenuSalida()
                self.desactivarBotonesPuntuacion()
                tutorial.desactivarBotones()

                #En el menu
                self.fondo_menu.ponerImagen(self.screen)
                self.titulomenu.pintar(self.screen)

                self.btnEncriptar.pintar(self.screen)
                self.btnTutorial.pintar(self.screen)
                self.btnPuntaje.pintar(self.screen)
                self.btnSalir.pintar(self.screen)
                if not self.controlador.getEventoEjecutado() == 0:
                    self.etapa = self.controlador.getEventoEjecutado()
            if (self.etapa == 2 or self.etapa == 8 or self.etapa == 9 or self.etapa == 10
                or self.etapa == 11 or self.etapa == 12 or self.etapa == 13
                or self.etapa == 14 or self.etapa == 15):
                #Tutorial
                self.desactivarBotonesMenuPrincipal()
                self.desactivarBotonesMenuSalida()
                self.desactivarBotonesPuntuacion()
                tutorial.activarBotones()

                if (self.etapa == 2):
                    tutorial.pintar(self.screen)
                else:
                    tutorial.pintar(self.screen, self.etapa-7)

                self.etapa = self.controlador.getEventoEjecutado()
            if self.etapa == 3:
                #juego
                pass
            if self.etapa == 4:
                #Puntuacion
                self.activarBotonesPuntuacion()
                self.desactivarBotonesMenuPrincipal()
                self.desactivarBotonesMenuSalida()
                tutorial.desactivarBotones()

                self.fondo_puntuacion.ponerImagen(self.screen)
                self.titulomenu.pintar(self.screen)
                self.lblPuntuacion.pintar(self.screen)

                #tabla
                self.tablanum.pintar(self.screen)
                self.tablajug.pintar(self.screen)
                self.tablafecha.pintar(self.screen)
                self.tablapuntaje.pintar(self.screen)

                self.tablanum1.pintar(self.screen)
                self.tablajug1.pintar(self.screen)
                self.tablafecha1.pintar(self.screen)
                self.tablapuntaje1.pintar(self.screen)

                self.tablanum2.pintar(self.screen)
                self.tablajug2.pintar(self.screen)
                self.tablafecha2.pintar(self.screen)
                self.tablapuntaje2.pintar(self.screen)

                self.tablanum3.pintar(self.screen)
                self.tablajug3.pintar(self.screen)
                self.tablafecha3.pintar(self.screen)
                self.tablapuntaje3.pintar(self.screen)

                self.tablanum4.pintar(self.screen)
                self.tablajug4.pintar(self.screen)
                self.tablafecha4.pintar(self.screen)
                self.tablapuntaje4.pintar(self.screen)

                self.tablanum5.pintar(self.screen)
                self.tablajug5.pintar(self.screen)
                self.tablafecha5.pintar(self.screen)
                self.tablapuntaje5.pintar(self.screen)

                self.tablanum6.pintar(self.screen)
                self.tablajug6.pintar(self.screen)
                self.tablafecha6.pintar(self.screen)
                self.tablapuntaje6.pintar(self.screen)

                self.tablanum7.pintar(self.screen)
                self.tablajug7.pintar(self.screen)
                self.tablafecha7.pintar(self.screen)
                self.tablapuntaje7.pintar(self.screen)

                self.btnMenu.pintar(self.screen)

                self.etapa = self.controlador.getEventoEjecutado()
            if self.etapa == 5:
                #Salir
                self.activarBotonesMenuSalida()
                self.desactivarBotonesMenuPrincipal()
                self.desactivarBotonesPuntuacion()
                tutorial.desactivarBotones()

                self.fondo_menu.ponerImagen(self.screen)
                self.titulomenu.pintar(self.screen)
                self.mensaje_salida.pintar(self.screen)

                self.btnSi.pintar(self.screen)
                self.btnNo.pintar(self.screen)

                self.etapa = self.controlador.getEventoEjecutado()

            pygame.display.flip()
                #Se envian los evento para que el los procese
