import time

class Lavanderia:
	def __init__(self):
		self.nroLavadoActual = 0
		self.prendas = []
  
	def cargar_prendas(self, nro):
		for i in range(nro):
			self.prendas.append(Prenda(i))
   
	def cargar_incompatibilidad(self, prenda, incompatibilidad):
		self.prendas[prenda-1].cargar_incompatibilidad(incompatibilidad)
		
class Prenda:
	def __init__(self,nro):
		self.nro = nro
		self.tiempo = 0
		self.incompatibilidades = {}
		self.lavada = False
  
	def cargar_incompatibilidad(self, nro):
		self.incompatibilidades.setdefault(nro, None)
  
 
def leer_archivo():
	archivo = open("primer_problema.txt","r")
	linea = archivo.readline()
	lavanderia = Lavanderia()
	while(linea!= ""):
		linea = (linea.strip()).split()
		if(linea[0] == 'c'):
			linea = archivo.readline()
			continue
		elif(linea[0] == 'p'):
			lavanderia.cargar_prendas(int(linea[2]))
		elif(linea[0] == 'e'):
			lavanderia.cargar_incompatibilidad(int(linea[1]), int(linea[2]))
		linea = archivo.readline()
  
	return lavanderia
     

def main():
	inicio = time.time()
	lavanderia = leer_archivo()
 
	fin = time.time()
	print(fin-inicio)
 
main()