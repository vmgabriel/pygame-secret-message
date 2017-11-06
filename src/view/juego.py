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
from model.conector import Conexion

"""
Formulario enfocado en la carga del juego

@author: Dalia Muñoz - Gabriel Vargas
@version: 0.1
@license: GPL
@contact: vmgabriel96@gmail.com
"""

class Juego(object):
    """Clase que carga todo lo referente al juego"""
    def __init__(self, ctrl):
        self.controlador = ctrl

        self.fondo = "view/img/fondos/Espera-espectral.jpg"

        self.construir()

        self.vida_actuales = 2
        self.puntuacion = 0
        self.dificultad = 1
        # 1 -> Facil
        # 2 -> medio
        # 3 -> Dificil
        # Para implementar

        self.consulta_query = "SELECT * FROM Palabra;"
        self.conexion = Conexion()
        self.palabras = self.conexion.enviar_consulta(self.consulta_query)
        print self.palabras

    def construir(self):
        """
        Metodo que va a generar la construccion grafica del juego
        """
        self.fondo = Imagen(self.fondo, (0, 0))
        self.fondo.cambiarEscala(0.5)
        self.titulo = Titulo("KACH!", 120, 450, 70, 2, (36, 32, 163))
        self.lblNivel = Titulo("Nivel 1", 550, 30, 40, 2, (36, 32, 163))

        self.cuadro = Boton("")
        self.cuadro.modificarPosicion(10, 50)
        self.cuadro.modificarTamano(620,200)
        self.cuadro.modificarPosicionTexto(30, 27)
        self.cuadro.modificarColor1(234, 234, 216)
        self.cuadro.modificarColorLetra1(21, 67, 96)
        self.cuadro.modificarColor2(234, 234, 216)
        self.cuadro.modificarColorLetra2(21, 67, 96)
        self.cuadro.modificarColor3(234, 234, 216)
        self.cuadro.modificarColorLetra3(21, 67, 96)
        self.cuadro.modificarEvento(0)

        self.cuadro_corazon = Boton("Vidas:")
        self.cuadro_corazon.modificarPosicion(10, 360)
        self.cuadro_corazon.modificarTamano(180,40)
        self.cuadro_corazon.modificarPosicionTexto(30, 20)
        self.cuadro_corazon.modificarColor1(255, 255, 255)
        self.cuadro_corazon.modificarColorLetra1(21, 67, 96)
        self.cuadro_corazon.modificarColor2(255, 255, 255)
        self.cuadro_corazon.modificarColorLetra2(21, 67, 96)
        self.cuadro_corazon.modificarColor3(255, 255, 255)
        self.cuadro_corazon.modificarColorLetra3(21, 67, 96)
        self.cuadro_corazon.modificarEvento(0)

        self.cuadro_tiempo = Boton("Tiempo:")
        self.cuadro_tiempo.modificarPosicion(10, 10)
        self.cuadro_tiempo.modificarTamano(180,40)
        self.cuadro_tiempo.modificarPosicionTexto(30, 20)
        self.cuadro_tiempo.modificarColor1(255, 255, 255)
        self.cuadro_tiempo.modificarColorLetra1(21, 67, 96)
        self.cuadro_tiempo.modificarColor2(255, 255, 255)
        self.cuadro_tiempo.modificarColorLetra2(21, 67, 96)
        self.cuadro_tiempo.modificarColor3(255, 255, 255)
        self.cuadro_tiempo.modificarColorLetra3(21, 67, 96)
        self.cuadro_tiempo.modificarEvento(0)

        self.lblTiempo = Titulo("30", 120, 32, 20, 2, (20, 90, 50))

        self.cuadro_Puntuacion = Boton("Puntuacion:")
        self.cuadro_Puntuacion.modificarPosicion(450, 360)
        self.cuadro_Puntuacion.modificarTamano(180,40)
        self.cuadro_Puntuacion.modificarPosicionTexto(50, 20)
        self.cuadro_Puntuacion.modificarColor1(255, 255, 255)
        self.cuadro_Puntuacion.modificarColorLetra1(21, 67, 96)
        self.cuadro_Puntuacion.modificarColor2(255, 255, 255)
        self.cuadro_Puntuacion.modificarColorLetra2(21, 67, 96)
        self.cuadro_Puntuacion.modificarColor3(255, 255, 255)
        self.cuadro_Puntuacion.modificarColorLetra3(21, 67, 96)
        self.cuadro_Puntuacion.modificarEvento(0)

        self.lblPuntuacion = Titulo("0", 590, 380, 20, 2, (36, 32, 163))

        img_vidas="view/img/corazon.jpg"
        self.vida1 = Imagen(img_vidas, (65, 360))
        self.vida1.cambiarEscala(0.25)
        self.vida2 = Imagen(img_vidas, (105, 360))
        self.vida2.cambiarEscala(0.25)
        self.vida3 = Imagen(img_vidas, (145, 360))
        self.vida3.cambiarEscala(0.25)

        self.btnOpcion1 = Boton("Opcion1")
        self.btnOpcion1.modificarPosicion(30, 280)
        self.btnOpcion1.modificarTamano(140,50)
        self.btnOpcion1.modificarPosicionTexto(40, 27)
        self.btnOpcion1.modificarColor1(234, 234, 216)
        self.btnOpcion1.modificarColorLetra1(21, 67, 96)
        self.btnOpcion1.modificarColor2(209, 210, 179)
        self.btnOpcion1.modificarColorLetra2(21, 67, 96)
        self.btnOpcion1.modificarColor3(91, 202, 213)
        self.btnOpcion1.modificarColorLetra3(21, 67, 96)
        self.btnOpcion1.modificarEvento(8)
        self.btnOpcion2 = Boton("Opcion2")
        self.btnOpcion2.modificarPosicion(180, 280)
        self.btnOpcion2.modificarTamano(140,50)
        self.btnOpcion2.modificarPosicionTexto(40, 27)
        self.btnOpcion2.modificarColor1(234, 234, 216)
        self.btnOpcion2.modificarColorLetra1(21, 67, 96)
        self.btnOpcion2.modificarColor2(209, 210, 179)
        self.btnOpcion2.modificarColorLetra2(21, 67, 96)
        self.btnOpcion2.modificarColor3(91, 202, 213)
        self.btnOpcion2.modificarColorLetra3(21, 67, 96)
        self.btnOpcion2.modificarEvento(9)
        self.btnOpcion3 = Boton("Opcion3")
        self.btnOpcion3.modificarPosicion(330, 280)
        self.btnOpcion3.modificarTamano(140,50)
        self.btnOpcion3.modificarPosicionTexto(40, 27)
        self.btnOpcion3.modificarColor1(234, 234, 216)
        self.btnOpcion3.modificarColorLetra1(21, 67, 96)
        self.btnOpcion3.modificarColor2(209, 210, 179)
        self.btnOpcion3.modificarColorLetra2(21, 67, 96)
        self.btnOpcion3.modificarColor3(91, 202, 213)
        self.btnOpcion3.modificarColorLetra3(21, 67, 96)
        self.btnOpcion3.modificarEvento(10)
        self.btnOpcion4 = Boton("Opcion4")
        self.btnOpcion4.modificarPosicion(480, 280)
        self.btnOpcion4.modificarTamano(140,50)
        self.btnOpcion4.modificarPosicionTexto(40, 27)
        self.btnOpcion4.modificarColor1(234, 234, 216)
        self.btnOpcion4.modificarColorLetra1(21, 67, 96)
        self.btnOpcion4.modificarColor2(209, 210, 179)
        self.btnOpcion4.modificarColorLetra2(21, 67, 96)
        self.btnOpcion4.modificarColor3(91, 202, 213)
        self.btnOpcion4.modificarColorLetra3(21, 67, 96)
        self.btnOpcion4.modificarEvento(11)

        self.btnInicio = Boton("Salir")
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

        #Enviar al controlador
        self.controlador.enviarEventoBoton(self.btnOpcion1)
        self.controlador.enviarEventoBoton(self.btnOpcion2)
        self.controlador.enviarEventoBoton(self.btnOpcion3)
        self.controlador.enviarEventoBoton(self.btnOpcion4)
        self.controlador.enviarEventoBoton(self.btnInicio)

    def activar_botones(self):
        self.btnOpcion1.modificarActivo(True)
        self.btnOpcion2.modificarActivo(True)
        self.btnOpcion3.modificarActivo(True)
        self.btnOpcion4.modificarActivo(True)
        self.btnInicio.modificarActivo(True)

    def desactivar_botones(self):
        self.btnOpcion1.modificarActivo(False)
        self.btnOpcion2.modificarActivo(False)
        self.btnOpcion3.modificarActivo(False)
        self.btnOpcion4.modificarActivo(False)
        self.btnInicio.modificarActivo(False)

    def reiniciar(self):
        self.vida_actuales = 2
        self.puntuacion = 0
        self.dificultad = 1

    def perder(self):
        print("Perdiste wey!!, que malo eres")

    def pintar(self,screen, tiempo):
        """
        Pinta en pantalla la parte grafica

        @param screen: Pantalla en la que se va a pintar
        @type screen: Surface
        """
        self.fondo.ponerImagen(screen)
        self.titulo.pintar(screen)
        self.lblNivel.pintar(screen)

        self.cuadro.pintar(screen)
        self.cuadro_corazon.pintar(screen)

        self.cuadro_tiempo.pintar(screen)
        self.cuadro_Puntuacion.pintar(screen)

        self.lblPuntuacion.pintar(screen)
        self.lblTiempo.modificarTexto(str(tiempo))
        self.lblTiempo.pintar(screen)

        if (self.vida_actuales == 2):
            self.vida1.ponerImagen(screen)
            self.vida2.ponerImagen(screen)
            self.vida3.ponerImagen(screen)
        elif (self.vida_actuales == 1):
            self.vida1.ponerImagen(screen)
            self.vida2.ponerImagen(screen)
        elif (self.vida_actuales == 0):
            self.vida1.ponerImagen(screen)
        else:
            #GAME OVER
            pass

        self.btnOpcion1.pintar(screen)
        self.btnOpcion2.pintar(screen)
        self.btnOpcion3.pintar(screen)
        self.btnOpcion4.pintar(screen)
        self.btnInicio.pintar(screen)

    def modificar_tiempo(self, tiempo):
        self.tiempo = tiempo

    def quitar_vida(self):
        self.vida_actuales -=1

    def get_vidas_actuales(self):
        return self.vida_actuales

    def invertirPalabra(self, palabra):
        """
        Invierte Palabra::
            "Hola" -> "aloH"

        @param palabra: palabra que se va a invertir
        @type palabra: str

        @return: Palabra convertida
        @rtype: str
        """
        return ''.join(reversed(palabra))

    def invetirOracion(self, Oracion):
        """
        Invierte Oracion, pero retorna una lista::
            "Hola Mundo" -> ["aloH", "odnuM"]

        @param palabra: Oracion que se va a invertir
        @type palabra: str

        @return: Lista con Oracion Convertida
        @rtype: list
        """
        lista = Oracion.split()
        return list(map(self.invertirPalabra, lista))

    def lista_to_str_espaciado(self, lista):
        """
        Imprime con espaciado una lista::
            ["aloH", "odnuM"] -> "aloH odnuM"

        @param lista: Lista que se va a convertir
        @type lista: list

        @return: Oracion de la lista con espacios
        @rtype: str
        """
        return " ".join(lista)

    def encriptar_atbash(self, message):
        """
        Metodo que encripta con metodo atbash::
            Con el alfabeto
            A B C D E F G H I J K L M N Ñ O P Q R S T U V W X Y Z
            Z Y X W V U T S R Q P O Ñ N M L K J I H G F E D C B A
            ----------------------------------------------------
            Lo que trata de hacer es modificar la letra de arriba con la
            respectiva de abajo, el ejemplo:
             "HOLA MUNDO" -> "SLOZ ÑFNWL"

        @param message: mensaje a Encriptar
        @type message: str

        @return: mensaje encriptado
        @rtype: str
        """
        alphabet = u'A B C D E F G H I J K L M N Ñ O P Q R S T U V W X Y Z a b c d e f g h i j k l m n ñ o p q r s t u v w x y z 0 1 2 3 4 5 6 7 8 9'.split()
        backward = u'Z Y X W V U T S R Q P O Ñ N M L K J I H G F E D C B A z y x w v u t s r q p o ñ n m l k j i h g f e d c b a 9 8 7 6 5 4 3 2 1 0'.split()
        cipher = []

        for letter in message:
            if letter in alphabet:
                for i in xrange(len(alphabet)):
                    if alphabet[i] == letter:
                        pos = i
                cipher.append(backward[pos])
            else:
                cipher.append(letter)

        newMessage = ''.join(cipher)
        return newMessage

    def desencriptar_atbash(self, message):
        """
        Metodo para desencriptar con metodo atbash::
            Con el alfabeto
            A B C D E F G H I J K L M N Ñ O P Q R S T U V W X Y Z
            Z Y X W V U T S R Q P O Ñ N M L K J I H G F E D C B A
            ----------------------------------------------------
            Lo que trata de hacer es modificar la letra de arriba con la
            respectiva de abajo, el ejemplo:
             "SLOZ ÑFNWL" -> "HOLA MUNDO"

        @param message: mensaje a Desencriptar
        @type message: str

        @return: mensaje Desencriptado
        @rtype: str
        """
        alphabet = u'A B C D E F G H I J K L M N Ñ O P Q R S T U V W X Y Z a b c d e f g h i j k l m n ñ o p q r s t u v w x y z 0 1 2 3 4 5 6 7 8 9'.split()
        backward = u'Z Y X W V U T S R Q P O Ñ N M L K J I H G F E D C B A z y x w v u t s r q p o ñ n m l k j i h g f e d c b a 9 8 7 6 5 4 3 2 1 0'.split()
        cipher = []

        for letter in message:
            if letter in backward:
                for i in xrange(len(backward)):
                    if backward[i] == letter:
                        pos = i
                cipher.append(alphabet[pos])
            else:
                cipher.append(letter)

        newMessage = ''.join(cipher)
        return newMessage

    def codificar_polibi_5(self, char):
        """
        Codifica una letra en formato polibi::
            "H" -> (3,3) como ejemplo

        @param char: caracter a convertir
        @type char: str
        @return: Tupla con el valor convertido en polibi
        @rtype: (a, b)
        """
        alfabeto = "abcdefghiklmnopqrstuvwxyz"
        tup = (0,0)
        if char:
            if alfabeto.find(char) <= 5:
                tup = (1, alfabeto.find(char) + 1)
            elif alfabeto.find(char) <= 10:
                tup = (2, (alfabeto.find(char) + 1) - 5)
            elif alfabeto.find(char) <= 15:
                tup = (3, (alfabeto.find(char) + 1) - 10)
            elif alfabeto.find(char) <= 20:
                tup = (4, (alfabeto.find(char) + 1) - 15)
            elif alfabeto.find(char) <= 25:
                tup = (5, (alfabeto.find(char) + 1) - 20)
        return "".join(map(str, tup))

    def encriptar_str_polibi_5(self, texto):
        """
        Encripta una palabra a codigo polibi::
            "HOLA" -> [(1,2),(2,3),(3,4),(4,5)]

        @param texto: Palabra a encriptar
        @type texto: str
        @return: Lista encriptada en polibi
        @rtype: [(a,b),(c,d)]
        """
        return " ".join(map(self.codificar_polibi_5, texto))

    def encriptar_polibi_5(self, mensaje):
        """
        Encripta una palabra convertida y las une como una lista, imprime un str
        ::
            "HOLA MUNDO" -> "(1,1),(1,2),(1,3),(1,4)-(2,1),(2,2),(2,3),(2,4),(2,5)"

        @param mensaje: Mensaje a encriptar
        @type mensaje: str
        @return: str con mensaje encriptado
        @rtype: str
        """
        mensaje = mensaje.replace("j", "i")
        lista = mensaje.split()
        lista = map(self.encriptar_str_polibi_5, lista)
        return "-".join(lista)
        #return self.lista_to_str_espaciado(lista)

    def CodificarCesar(self, Palabra, Avance):
        """
        Codifica Mensaje con codficacion atbas, sin embargo, el orden del abecderio
        no es el mismo::
        A B C D E F G H I J K L M N Ñ O P Q R S T U V W X Y Z
        Y X W V U T S R Q P O Ñ N M L K J I H G F E D C B A Z
        ------------------------------------------------------

        @param Palabra: Palabra a criptar
        @type Palabra: str
        @param Avance: avance o cambio de orden del abecedario
        @type Avance: int

        @return: Palabra invertida
        @rtype: str
        """
        alfabetoMinus = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
        'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        alfabetoMayus = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
        'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        Clave = ''
        Tope = len(alfabetoMayus)
        Posicion = 0
        for letra in Palabra:
            for i in range(Tope):
                if (i + Avance < Tope):
                    Posicion = i + Avance
                else:
                    Posicion = abs((Tope - i) - Avance)
                if letra == alfabetoMinus[i]:
                    Clave = Clave + alfabetoMinus[Posicion]
                elif letra == alfabetoMayus[i]:
                    Clave = Clave + alfabetoMayus[Posicion]
        return Clave
