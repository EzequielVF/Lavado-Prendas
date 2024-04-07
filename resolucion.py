import time

class Lavanderia:
	def __init__(self):
		self.nroLavadoActual = 0
		self.prendas = []

class Prenda:
	def __init__(self,nro):
		self.nro = nro
		self.tiempo = 0
		self.incompatibilidades = {}
		self.lavada = False

def main():
	inicio = time.time()
	
 
	fin = time.time()
	print(fin-inicio)
 
main()