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

"""
Formulario que cargue la seccion del tutorial

@author: Dalia Muñoz - Gabriel Vargas
@version: 0.1
@license: GPL
@contact: vmgabriel96@gmail.com
"""

class Tutorial:
    """Clase enfocada en todo lo que carga el tutorial"""
    def __init__(self, ctrl):
        """
        Constructor del Tutorial

        @param ctrl: controlador del los eventos
        @type ctrl: Controlador
        """
        self.controlador = ctrl
        self.fondo = "view/img/fondos/España.jpg"
        self.textos = []
        self.textoActual = 0

        #Cargar Mensajes y ponerlos en la matriz de los textos
        self.construir()
        self.construirTabla1()

        #Imagen ATBAS
        self.ImagenAtbas = Imagen("view/img/codigoAtbas.png", (10, 270))
        self.ImagenAtbas.cambiarEscala(0.65)

        #Cifra de Polibi
        self.tablaPolibi = Imagen("view/img/polibi.png", (285, 240))
        self.tablaPolibi.cambiarEscala(0.5)
        self.manoPolibi = Imagen("view/img/polibiManoEje.png", (380, 300))
        self.manoPolibi.cambiarEscala(0.4)
        self.polibiEje = Imagen("view/img/polibiCodi.png", (300,160))
        self.polibiEje.cambiarEscala(0.5)

        #Cesar
        self.cesar = Imagen("view/img/Cesar.png", (10, 230))
        self.cesar.cambiarEscala(0.65)
        self.cesarEjemplo = Imagen("view/img/cesarEjemplo.png", (300, 330))
        self.cesarEjemplo.cambiarEscala(0.5)

        #Rejilla
        self.rejilla = Imagen("view/img/Rejilla.png", (350, 300))
        self.rejilla.cambiarEscala(0.6)
        self.rejillaEjemplo = Imagen("view/img/RejillaEjemplo.png", (340, 180))
        self.rejillaEjemplo.cambiarEscala(0.6)

    def mensajes(self):
        """Mensajes que se podran mostrar en el tutorial"""
        texto1 = []
        texto1.append(Titulo("Existen diferentes metodos para", 420, 120, 17, 2, (36, 32, 163)))
        texto1.append(Titulo("transformar un mensaje.", 420, 140, 17, 2, (36, 32, 163)))
        texto1.append(Titulo("A lo largo de la historia se han creado", 420, 160, 17, 2, (36, 32, 163)))
        texto1.append(Titulo("diferentes formas de codificar la", 420, 180, 17, 2, (36, 32, 163)))
        texto1.append(Titulo("informacion.", 420, 200, 17, 2, (36, 32, 163)))
        texto1.append(Titulo("En este juego veremos 7 metodos de", 420, 220, 17, 2, (36, 32, 163)))
        texto1.append(Titulo("<<Encriptar>> y <<Desencriptar>> un mensaje.", 420, 240, 17, 2, (36, 32, 163)))
        texto1.append(Titulo("-Oculto en la Tabla", 420, 260, 17, 2, (36, 32, 163)))
        texto1.append(Titulo("-Invertir", 420, 280, 17, 2, (36, 32, 163)))
        texto1.append(Titulo("-Codigo ATBAS", 420, 300, 17, 2, (36, 32, 163)))
        texto1.append(Titulo("-Cifra de Polibi", 420, 320, 17, 2, (36, 32, 163)))
        texto1.append(Titulo("-Cifra de Cesar", 420, 340, 17, 2, (36, 32, 163)))
        texto1.append(Titulo("-Rejilla Giratoria", 420, 360, 17, 2, (36, 32, 163)))
        self.textos.append(texto1)

        texto1 = []
        texto1.append(Titulo("Oculto en la Tabla", 420, 120, 17, 2, (36, 32, 163)))
        texto1.append(Titulo("El objetivo de oculto en la tabla es relacionar", 420, 140, 17, 2, (36, 32, 163)))
        texto1.append(Titulo("un significado con respecto a otro asi si:", 420, 160, 17, 2, (36, 32, 163)))
        texto1.append(Titulo("Asi relacionariamos <<Estrella>> con <<Entrar>>", 420, 280, 17, 2, (36, 32, 163)))
        self.textos.append(texto1)

        texto1 = []
        texto1.append(Titulo("Invertir", 420, 120, 17, 2, (36, 32, 163)))
        texto1.append(Titulo("El objetivo de este metodo es invertir las", 420, 140, 17, 2, (36, 32, 163)))
        texto1.append(Titulo("palabras para que estas no sean legibles", 420, 160, 17, 2, (36, 32, 163)))
        texto1.append(Titulo("a simple vista y que por ende esten del", 420, 180, 17, 2, (36, 32, 163)))
        texto1.append(Titulo("todo complicadas, un ejemplo que se puede", 420, 200, 17, 2, (36, 32, 163)))
        texto1.append(Titulo("apreciar:", 420, 220, 17, 2, (36, 32, 163)))
        texto1.append(Titulo("<<Mensaje Secreto>> a la hora de invertir", 420, 260, 17, 2, (36, 32, 163)))
        texto1.append(Titulo("seria <<Ejasnem Oterces>>", 420, 280, 17, 2, (36, 32, 163)))
        self.textos.append(texto1)

        texto1 = []
        texto1.append(Titulo("Codigo Atbas", 420, 120, 17, 2, (36, 32, 163)))
        texto1.append(Titulo("El codigo ATBAS es un codigo utilizado en algunos", 420, 140, 17, 2, (36, 32, 163)))
        texto1.append(Titulo("textos religiosos hebreos, el objetivo de este", 420, 160, 17, 2, (36, 32, 163)))
        texto1.append(Titulo("metodo es desorganizar el abecedario para que", 420, 180, 17, 2, (36, 32, 163)))
        texto1.append(Titulo("las palabras del uno sean diferentes que las", 420, 200, 17, 2, (36, 32, 163)))
        texto1.append(Titulo("del otro tomando con un significado el que valga", 420, 220, 17, 2, (36, 32, 163)))
        texto1.append(Titulo("para que esta regla se cumpla, este necesita de", 420, 240, 17, 2, (36, 32, 163)))
        texto1.append(Titulo("una tabla de valores como el mostrado:", 420, 260, 17, 2, (36, 32, 163)))
        texto1.append(Titulo("Asi si, <<Criptografia>> seria <<Xirkgltizurz>>", 420, 380, 17, 2, (36, 32, 163)))
        self.textos.append(texto1)

        texto1 = []
        texto1.append(Titulo("Cifra de Polibi", 420, 120, 17, 2, (36, 32, 163)))
        texto1.append(Titulo("Descrito por el historiador del siglo III a.C.,", 420, 140, 17, 2, (36, 32, 163)))
        texto1.append(Titulo("para codificar cada letra utiliza una tabla de", 420, 160, 17, 2, (36, 32, 163)))
        texto1.append(Titulo("doble entrada, en la que cada letra viene", 420, 180, 17, 2, (36, 32, 163)))
        texto1.append(Titulo("representada por dos numeros:", 420, 200, 17, 2, (36, 32, 163)))
        self.textos.append(texto1)

        texto1 = []
        texto1.append(Titulo("Cifra de Polibi", 420, 120, 17, 2, (36, 32, 163)))
        texto1.append(Titulo("Ejemplo:", 420, 140, 17, 2, (36, 32, 163)))
        texto1.append(Titulo("Se pueden utilizar algunos esquemas graficos", 420, 240, 17, 2, (36, 32, 163)))
        texto1.append(Titulo("para  codificar, las manos en este caso", 420, 260, 17, 2, (36, 32, 163)))
        self.textos.append(texto1)

        texto1 = []
        texto1.append(Titulo("Cifra de Cesar", 420, 120, 17, 2, (36, 32, 163)))
        texto1.append(Titulo("El metodo de Cesar consiste en desplazar", 420, 140, 17, 2, (36, 32, 163)))
        texto1.append(Titulo("cualquier alfabeto. La clave del codigo sera el", 420, 160, 17, 2, (36, 32, 163)))
        texto1.append(Titulo("numero de lugares que se desplaza. Muy similar", 420, 180, 17, 2, (36, 32, 163)))
        texto1.append(Titulo("al codigo ATBAS, un ejemplo seria:", 420, 200, 17, 2, (36, 32, 163)))
        texto1.append(Titulo("La codificacion seria de la siguiente manera:", 420, 300, 17, 2, (36, 32, 163)))
        self.textos.append(texto1)

        texto1 = []
        texto1.append(Titulo("Rejilla Giratoria", 420, 120, 17, 2, (36, 32, 163)))
        texto1.append(Titulo("Lo primero que debe hacerse es fabricar una", 420, 140, 17, 2, (36, 32, 163)))
        texto1.append(Titulo("tapadera. La rejilla se construye de forma que:", 420, 160, 17, 2, (36, 32, 163)))
        texto1.append(Titulo("-Tenga tantos huecos como la cuarta parte del", 420, 180, 17, 2, (36, 32, 163)))
        texto1.append(Titulo("total de la rejilla", 420, 200, 17, 2, (36, 32, 163)))
        texto1.append(Titulo("-Al girar hasta cuatro veces, una casilla no", 420, 220, 17, 2, (36, 32, 163)))
        texto1.append(Titulo("puede quedar destapada dos veces", 420, 240, 17, 2, (36, 32, 163)))
        texto1.append(Titulo("-Todas las casillas han de quedar destapadas", 420, 260, 17, 2, (36, 32, 163)))
        texto1.append(Titulo("alguna vez", 420, 280, 17, 2, (36, 32, 163)))
        self.textos.append(texto1)

        texto1 = []
        texto1.append(Titulo("Rejilla Giratoria", 420, 120, 17, 2, (36, 32, 163)))
        texto1.append(Titulo("seria para mostrar una tabla del estilo:", 420, 140, 17, 2, (36, 32, 163)))
        texto1.append(Titulo("la idea es tapar cada uno de los cuadros no", 420, 300, 17, 2, (36, 32, 163)))
        texto1.append(Titulo("necesarios", 420, 320, 17, 2, (36, 32, 163)))
        self.textos.append(texto1)

    def construirTabla1(self):
        """Metodo que construye la primera tabla"""
        self.tablaPalabra = Boton("Palabra")
        self.tablaPalabra.modificarPosicion(340, 180)
        self.tablaPalabra.modificarTamano(100, 40)
        self.tablaPalabra.modificarPosicionTexto(50, 20)
        self.tablaPalabra.modificarColor1(203, 67, 53)
        self.tablaPalabra.modificarColor2(176, 58, 46)
        self.tablaPalabra.modificarColor3(203, 67, 53)
        self.tablaPalabra.modificarColorLetra1(23, 32, 42)
        self.tablaPalabra.modificarColorLetra2(23, 32, 42)
        self.tablaPalabra.modificarColorLetra3(23, 32, 42)
        self.tablaPalabra.modificarEvento(0)
        self.tablaCodigo = Boton("Codigo")
        self.tablaCodigo.modificarPosicion(443, 180)
        self.tablaCodigo.modificarTamano(100, 40)
        self.tablaCodigo.modificarPosicionTexto(50, 20)
        self.tablaCodigo.modificarColor1(203, 67, 53)
        self.tablaCodigo.modificarColor2(176, 58, 46)
        self.tablaCodigo.modificarColor3(203, 67, 53)
        self.tablaCodigo.modificarColorLetra1(23, 32, 42)
        self.tablaCodigo.modificarColorLetra2(23, 32, 42)
        self.tablaCodigo.modificarColorLetra3(23, 32, 42)
        self.tablaCodigo.modificarEvento(0)
        self.tablaPalabra1 = Boton("Entrar")
        self.tablaPalabra1.modificarPosicion(340,223)
        self.tablaPalabra1.modificarTamano(100,40)
        self.tablaPalabra1.modificarPosicionTexto(50, 20)
        self.tablaPalabra1.modificarColor1(241, 148, 138)
        self.tablaPalabra1.modificarColor2(236, 112, 99)
        self.tablaPalabra1.modificarColor3(241, 148, 138)
        self.tablaPalabra1.modificarColorLetra1(23, 32, 42)
        self.tablaPalabra1.modificarColorLetra2(23, 32, 42)
        self.tablaPalabra1.modificarColorLetra3(23, 32, 42)
        self.tablaPalabra1.modificarEvento(0)
        self.tablaCodigo1 = Boton("Estrella")
        self.tablaCodigo1.modificarPosicion(443,223)
        self.tablaCodigo1.modificarTamano(100,40)
        self.tablaCodigo1.modificarPosicionTexto(50, 20)
        self.tablaCodigo1.modificarColor1(217, 136, 128)
        self.tablaCodigo1.modificarColor2(205, 97, 85)
        self.tablaCodigo1.modificarColor3(217, 136, 128)
        self.tablaCodigo1.modificarColorLetra1(23, 32, 42)
        self.tablaCodigo1.modificarColorLetra2(23, 32, 42)
        self.tablaCodigo1.modificarColorLetra3(23, 32, 42)
        self.tablaCodigo1.modificarEvento(0)

        self.controlador.enviarEventoBoton(self.tablaCodigo)
        self.controlador.enviarEventoBoton(self.tablaCodigo1)
        self.controlador.enviarEventoBoton(self.tablaPalabra)
        self.controlador.enviarEventoBoton(self.tablaPalabra1)

    def activarBotones(self):
        """Activa el conjunto de botones"""
        self.btnContinuar.modificarActivo(True)
        self.btnInicio.modificarActivo(True)
        self.activarTabla()

    def desactivarBotones(self):
        """Desactiva el conjunto de botones"""
        self.btnContinuar.modificarActivo(False)
        self.btnInicio.modificarActivo(False)
        self.desactivarTabla()

    def activarTabla(self):
        """Activa el conjunto de botones de la tabla"""
        self.tablaCodigo.modificarActivo(True)
        self.tablaCodigo1.modificarActivo(True)
        self.tablaPalabra.modificarActivo(True)
        self.tablaPalabra1.modificarActivo(True)

    def desactivarTabla(self):
        """Desactiva el conjunto de botones de la tabla"""
        self.tablaCodigo.modificarActivo(False)
        self.tablaCodigo1.modificarActivo(False)
        self.tablaPalabra.modificarActivo(False)
        self.tablaPalabra1.modificarActivo(False)

    def construir(self):
        """
        Se encargara de construir toda la parte grafica
        """
        self.fondo = Imagen(self.fondo, (0, 0))
        self.fondo.cambiarEscala(0.5)
        self.titulo = Titulo("KACH!", 120, 450, 70, 2, (36, 32, 163))
        self.lblTutorial = Titulo("Tutorial", 450, 30, 40, 2, (36, 32, 163))

        self.btnContinuar = Boton("Continuar")
        self.btnContinuar.modificarPosicion(280, 420)
        self.btnContinuar.modificarTamano(160,50)
        self.btnContinuar.modificarPosicionTexto(40, 27)
        self.btnContinuar.modificarColor1(234, 234, 216)
        self.btnContinuar.modificarColorLetra1(21, 67, 96)
        self.btnContinuar.modificarColor2(209, 210, 179)
        self.btnContinuar.modificarColorLetra2(21, 67, 96)
        self.btnContinuar.modificarColor3(91, 202, 213)
        self.btnContinuar.modificarColorLetra3(21, 67, 96)
        self.btnContinuar.modificarEvento(7)
        self.btnInicio = Boton("Inicio")
        self.btnInicio.modificarPosicion(460, 420)
        self.btnInicio.modificarTamano(160,50)
        self.btnInicio.modificarPosicionTexto(30, 27)
        self.btnInicio.modificarColor1(234, 234, 216)
        self.btnInicio.modificarColorLetra1(21, 67, 96)
        self.btnInicio.modificarColor2(209, 210, 179)
        self.btnInicio.modificarColorLetra2(21, 67, 96)
        self.btnInicio.modificarColor3(91, 202, 213)
        self.btnInicio.modificarColorLetra3(21, 67, 96)
        self.btnInicio.modificarEvento(6)

        self.cuadro = Boton("")
        self.cuadro.modificarPosicion(200, 100)
        self.cuadro.modificarTamano(430,300)
        self.cuadro.modificarPosicionTexto(30, 27)
        self.cuadro.modificarColor1(234, 234, 216)
        self.cuadro.modificarColorLetra1(21, 67, 96)
        self.cuadro.modificarColor2(234, 234, 216)
        self.cuadro.modificarColorLetra2(21, 67, 96)
        self.cuadro.modificarColor3(234, 234, 216)
        self.cuadro.modificarColorLetra3(21, 67, 96)
        self.cuadro.modificarEvento(0)

        self.mensajes()

        #Eventos de los botones
        self.controlador.enviarEventoBoton(self.btnContinuar)
        self.controlador.enviarEventoBoton(self.btnInicio)

    def pintar(self, screen, paso = 0):
        """
        Se encargara de mostrar toda la parte grafica

        @param screen: Pantalla en la que se va a pintar
        @type screen: Surface
        """
        self.fondo.ponerImagen(screen)
        self.titulo.pintar(screen)
        self.lblTutorial.pintar(screen)

        self.btnInicio.pintar(screen)
        self.btnContinuar.pintar(screen)

        self.cuadro.pintar(screen)
        if (paso == 0):
            self.textoActual = 0
            for x in self.textos[self.textoActual]:
                x.pintar(screen)
        elif (paso == 1):
            self.textoActual = 1
            for x in self.textos[self.textoActual]:
                x.pintar(screen)

            self.tablaCodigo.pintar(screen)
            self.tablaPalabra.pintar(screen)
            self.tablaCodigo1.pintar(screen)
            self.tablaPalabra1.pintar(screen)
        elif (paso == 2):
            self.textoActual = 2
            for x in self.textos[self.textoActual]:
                x.pintar(screen)
        elif (paso == 3):
            self.textoActual = 3
            for x in self.textos[self.textoActual]:
                x.pintar(screen)

            self.ImagenAtbas.ponerImagen(screen)
        elif (paso == 4):
            self.textoActual = 4
            for x in self.textos[self.textoActual]:
                x.pintar(screen)

            self.tablaPolibi.ponerImagen(screen)
        elif (paso == 5):
            self.textoActual = 5
            for x in self.textos[self.textoActual]:
                x.pintar(screen)

            self.manoPolibi.ponerImagen(screen)
            self.polibiEje.ponerImagen(screen)
        elif (paso == 6):
            self.textoActual = 6
            for x in self.textos[self.textoActual]:
                x.pintar(screen)

            self.cesar.ponerImagen(screen)
            self.cesarEjemplo.ponerImagen(screen)
        elif (paso == 7):
            self.textoActual = 7
            for x in self.textos[self.textoActual]:
                x.pintar(screen)

            self.rejilla.ponerImagen(screen)
        else:
            self.textoActual = 8
            for x in self.textos[self.textoActual]:
                x.pintar(screen)

            self.rejillaEjemplo.ponerImagen(screen)
