#!/urs/bin/env python
# -*- coding: utf-8 -*-

#modulos
import os
import sys
import pygame
from pygame.locals import *
from utils import Utils
from boton import Boton

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
        self.titulo = "MENS4JE S3CRET0"
        """Titulo de la ventana"""
        self.screen = None
        """Enfocado en la ventana como tal"""
        self.controlador = ctrl
        """Es quien maneja los eventos"""
        self.herrami = Utils()
        """Tiene metodos herramientas que funcionan practicamente en todo el proceso"""
        self.etapa = 0
        """Es quien da la seccion en la que vamos en el programa"""

    def menu(self):
        """
        Seccion del menu para el video juego
        """
        self.fondo_menu = self.herrami.load_image("view/img/fondo-ramas.jpg")
        self.titulomenu, self.titulomenurect = self.herrami.texto("MENSAJE SECRETO", 310, 100)
        #Todos los botones con sus respectivas posiciones
        self.btnDesencriptar = Boton("Desencriptar")
        self.btnDesencriptar.modificarPosicion(210, 150)
        self.btnEncriptar = Boton("Encriptar")
        self.btnEncriptar.modificarPosicion(210, 210)
        self.btnTutorial = Boton("Tutorial")
        self.btnTutorial.modificarPosicion(210, 270)
        self.btnPuntaje = Boton("Puntajes")
        self.btnPuntaje.modificarPosicion(210, 330)
        self.btnSalir = Boton("Salir")
        self.btnSalir.modificarPosicion(210, 390)


    def cargaCreditosInicio(self):
        """
        Cargara algunas imagenes que se mostraran en la mitad de la pantalla para el inicio del juego
        """
        self.Logo1 = self.herrami.load_image("view/img/UD-logo.gif")
        self.Logo2 = self.herrami.load_image("view/img/python-logo.png")
        self.Logo3 = self.herrami.load_image("view/img/pygame-logo.jpg")

    def run(self):
        """
        El metodo run cargara la ventana, ademas tendra el ciclo principal para el juego en general
        """
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption(self.titulo)
        self.cargaCreditosInicio()
        self.menu()
        #While principal, es el enfocado de correr los procesos del juego
        while True:
            for eventos in pygame.event.get():
                self.controlador.evePrincipal(eventos)

            if self.etapa == 0:
                #En la seccion que muestra los logos de todo
                self.screen.blit(self.Logo1, (180, 150))
                pygame.display.flip()
                pygame.time.wait(3000)
                self.screen.fill((0,0,0))
                self.screen.blit(self.Logo2, (230, 200))
                pygame.display.flip()
                pygame.time.wait(3000)
                self.screen.fill((0,0,0))
                self.screen.blit(self.Logo3, (120, 100))
                pygame.display.flip()
                pygame.time.wait(3000)
                self.screen.fill((0,0,0))
                self.etapa = 1
            if self.etapa == 1:
                #En el menu
                self.screen.blit(self.fondo_menu, (0, 0))
                self.screen.blit(self.titulomenu,self.titulomenurect)

                self.btnDesencriptar.pintar(self.screen)
                self.btnEncriptar.pintar(self.screen)
                self.btnTutorial.pintar(self.screen)
                self.btnPuntaje.pintar(self.screen)
                self.btnSalir.pintar(self.screen)
            if self.etapa == 2:
                #En el juego
                pass

            pygame.display.flip()
                #Se envian los evento para que el los procese
