#!/usr/bin/python

# Programa para hallar el rango de una matriz m x n
# Donde m y n son números enteros, mayores o iguales a 1
# 	y menores o iguales a 8

class Matriz(object):
	"""
		Matriz con filas y n columnas con propiedad de rango
	"""
	def __init__(self):
		self.filas = 1
		self.columnas = 1
		self.rango = 1

	def calcular_rango(self):
		self.rango = 0

	def get_filas(self):
		return self.filas

	def set_filas(self, filas):
		self.filas = filas

	def get_columnas(self):
		return self.columnas

	def set_columnas(self, columnas):
		self.columnas = columnas


def main():
    print('Vamoa a Calcular el rango')

    filas = input('Ingresa cantidad de filas: \t')
    columnas = input('Ingrese cantidad de columnas: \t')
    matriz = Matriz()
    matriz.set_filas(filas)
    matriz.set_filas(columnas)


if __name__ == '__main__':
	main()