#!/urs/bin/env python
# -*- coding: utf-8 -*-

#modulos
import psycopg2, psycopg2.extras
import sys

"""
Conexion a Base de Datos

@author: Dalia Muñoz - Gabriel Vargas
@version: 0.1
@license: GPL
@contact: vmgabriel96@gmail.com
"""

class Conexion:
    """
    Clase para la consolidacion con la base de datos
    """
    base = ""
    user = ""
    password = ""
    host = ""
    conn = None

    def __init__(self):
        self.base = "Kach"
        self.user = "postgres"
        self.password = "admin"
        self.host = "localhost"

    def enviar_registro(self, query, iny):
        try:
            self.conector()
            cur = self.conn.cursor()
            cur.execute(query, iny)
            self.conn.commit()
            cur.close()
        except psycopg2.DatabaseError, e:
            if self.conn:
                self.conn.rollback()

            print 'Error %s' % e
            sys.exit(1)
        finally:
            self.conn.close()

    def enviar_consulta(self, query):
        try:
            self.conector()
            cur = self.conn.cursor()
            cur.execute(query)
            datos = cur.fetchall()
            cur.close()
            return datos
        except psycopg2.DatabaseError, e:
            if self.conn:
                self.conn.rollback()

            print 'Error %s' % e
            sys.exit(1)
        finally:
            self.conn.close()

    def conector(self):
        self.conn = psycopg2.connect(database = self.base, user = self.user,
            password = self.password, host = self.host)
