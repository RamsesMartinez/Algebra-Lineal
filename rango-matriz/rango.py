#!/usr/bin/python3
# -*- coding: <utf-8> -*-
"""
Programa para hallar el rango de una matriz m x n
donde m y n son numers enteros mayores o iguales a 1
y menores o iguales a 8
"""
__licence__ = "MIT"
__author__ = "Ramśes Martínez Ortiz"


from time import sleep

class Matriz(object):
    """
    Matriz de mxn filas y columnas con propiedad de rango.
    """

    def __init__(self):
        self.__numero_filas = 1
        self.__numero_columnas = 1
        self.__matriz = None

    def calcular_rango(self):
        self.__rango = 0

    def get_numero_filas(self):
        return self.__numero_filas

    def set_numero_filas(self, filas:int):
        self.__numero_filas = filas

    def get_numero_columnas(self):
        return self.__numero_columnas

    def set_numero_columnas(self, columnas:int):
        self.__numero_columnas = columnas

    def set_matriz(self):
        self.__matriz = [[None] * self.__numero_columnas for i in range(self.__numero_filas)]
        for i in range(self.__numero_filas):
            for j in range(self.__numero_columnas):
                mensaje = 'Elemento de la celda (%s,%s):\t' % (i, j)
                self.__matriz[i][j] = self.__get_numero(mensaje)
    
    def __get_numero(self, mensaje):
        while True:
            try:
                return int(input(mensaje))
            except ValueError:
                print('Ingresa un número válido')
        
    def print_matriz(self):
        for i in range(self.__numero_filas):
            for j in range(self.__numero_columnas):
                print('[%s,%s]' % (i+1, j+1), end='\t')    
            print()

def main():
    print('Vamoa a Calcular el rango de una matriz\n')

    filas = int(input('Ingresa cantidad de filas: \t'))
    columnas = int(input('Ingrese cantidad de columnas: \t'))

    matriz = Matriz()
    print()
    matriz.set_numero_filas(filas)
    matriz.set_numero_columnas(columnas)
    matriz.set_matriz()
    print('\nAsí quedó tu matriz:')
    matriz.print_matriz()

    print('\nCALCULANDO EL RANGO...')
    sleep(1)
    print('LISTO!')

if __name__ == '__main__':
    main()
