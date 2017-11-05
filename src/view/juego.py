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
