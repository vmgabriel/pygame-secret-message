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
        self.titulomenu = Titulo("KACH!", 100, 50)
        #Todos los botones con sus respectivas posiciones
        self.btnEncriptar = Boton("Jugar")
        self.btnEncriptar.modificarPosicion(400, 140)
        self.btnTutorial = Boton("Tutorial")
        self.btnTutorial.modificarPosicion(400, 220)
        self.btnPuntaje = Boton("Puntajes")
        self.btnPuntaje.modificarPosicion(400, 300)
        self.btnSalir = Boton("Salir")
        self.btnSalir.modificarPosicion(400, 380)


    def cargaCreditosInicio(self):
        """
        Cargara algunas imagenes que se mostraran en la mitad de la pantalla para el inicio del juego
        """
        self.Logo1 = Imagen("view/img/UD-logo.gif", (220, 130))
        self.Logo2 = Imagen("view/img/python-logo.png", (210, 130), True)
        self.Logo3 = Imagen("view/img/pygame-logo.jpg", (120, 100))

        self.titulopresentacion = Titulo("KACH!", 320, 180, 40, 1, (255, 195, 0))
        self.subtitulopresentacion = Titulo("Diversion Oculta!", 320, 250,
            30, 2, (255, 195, 0))

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

                self.screen.fill((0, 12, 192))
                self.titulopresentacion.pintar(self.screen)
                self.subtitulopresentacion.pintar(self.screen)
                pygame.display.flip()
                pygame.time.wait(3000)

                self.screen.fill(self.color_fondo)
                self.etapa = 1
            if self.etapa == 1:
                #En el menu
                self.fondo_menu.ponerImagen(self.screen)
                self.titulomenu.pintar(self.screen)

                self.btnEncriptar.pintar(self.screen)
                self.btnTutorial.pintar(self.screen)
                self.btnPuntaje.pintar(self.screen)
                self.btnSalir.pintar(self.screen)
            if self.etapa == 2:
                #En el juego
                pass

            pygame.display.flip()
                #Se envian los evento para que el los procese
