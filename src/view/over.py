#!/urs/bin/env python
# -*- coding: utf-8 -*-

#modulos
import os
import sys
import pygame
import time
from pygame.locals import *
from boton import Boton
from imagenes import Imagen
from titulo import Titulo
from textbox import TextBox
from model.conector import Conexion

class Terminar:
    def __init__(self):
        self.puntuacion = 0
        self.color_fondo = (255, 255, 255)

        self.construir()
        self.desactivarTextBox()

        self.final = False

    def construir(self):
        self.titulo = Titulo("KACH!", 320, 50, 70, 1, (126, 81, 9))
        self.titulo_terminado = Titulo("Juego Terminado!", 320, 100, 40, 3, (14, 98, 81))
        self.titulo_puntaje = Titulo("Su puntaje es:", 320, 150, 30, 4, (36, 32, 163))
        self.lblPuntuacion = Titulo("0", 300, 260, 180, 2, (0, 0, 0))
        self.lblinstrucciones = Titulo("Presione <Enter> para continuar",320, 440, 30, 4, (126, 81, 9))
        self.lblindicacion = Titulo("Ingrese Alias:",320, 360, 25, 3, (14, 98, 81))
        self.input = TextBox((220,380,200,30),command=self.enviar_reporte,
                              clear_on_enter=True,inactive_on_enter=False)

    def activarTextBox(self):
        self.input.active = True

    def desactivarTextBox(self):
        self.input.active = False

    def pintar(self,screen):
        screen.fill(self.color_fondo)
        self.titulo.pintar(screen)

        self.titulo_terminado.pintar(screen)
        self.titulo_puntaje.pintar(screen)
        self.lblPuntuacion.pintar(screen)
        self.lblindicacion.pintar(screen)
        self.lblinstrucciones.pintar(screen)

        self.input.update()
        self.input.draw(screen)

    def eventos(self,evento):
        self.input.get_event(evento)

    def enviar_reporte(self,id,final):
        if (final != ""):
            self.conexion = Conexion()
            fecha = time.strftime("%y-%m-%d")
            self.conexion.enviar_registro(self.query_envio(),(final,fecha,self.puntuacion))
            self.final = True

    def modificar_puntuacion(self, puntuacion):
        self.puntuacion = puntuacion
        self.lblPuntuacion.modificarTexto(str(puntuacion))

    def getFinal(self):
        return self.final

    def reiniciar(self):
        self.final = False

    def query_envio(self):
        return ("INSERT INTO Jugador(nombre,fecha,puntuacion) VALUES (%s, %s, %s);")
