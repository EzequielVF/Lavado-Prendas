import time

class Lavanderia:
	def __init__(self):
		self.prendas = []
		self.cantidad_prendas = 0
	
	def cargar_prendas(self, nro):
		self.cantidad_prendas = nro
		for i in range(nro):
			self.prendas.append(Prenda(i+1))
 
	def cargar_incompatibilidad(self, prenda, incompatibilidad):
		if self.prendas[prenda-1].es_compatible_con(incompatibilidad):
			self.prendas[prenda-1].cargar_incompatibilidad(incompatibilidad)
		
		if self.prendas[incompatibilidad-1].es_compatible_con(prenda):
			self.prendas[incompatibilidad-1].cargar_incompatibilidad(prenda)
	
	def cargar_tiempo(self, prenda, tiempo):
		self.prendas[prenda-1].cargar_tiempo(tiempo)
 
	def lavar(self):
		archivo = open("respuestasTP2.txt","w")
		self.prendas.sort()
		lavado = 1
		colores = [-1] * self.cantidad_prendas
		for i in range(self.cantidad_prendas):
			if colores[i] == -1:
				colores[i] =  lavado
				self.prendas[i].lavado = lavado
				for j in range(self.cantidad_prendas):
					if j == i:
						continue
					if colores[j] == -1 and self.lavado_compatible(j, lavado, colores):
						colores[j] =  lavado
						self.prendas[j].lavado = lavado
				lavado += 1
		prendas_ordenadas = sorted(self.prendas, key=lambda x: x.lavado)
		for prenda in prendas_ordenadas:
			archivo.write(str(prenda.nro) + " " + str(prenda.lavado) + "\n")
		archivo.close()
	
	def lavado_compatible(self, j, lavado_actual, colores):
		for x in range(j):
			if self.prendas[x].es_compatible_con(self.prendas[j].nro) == False and colores[x] == lavado_actual:
				return False
		return True		
 	
class Prenda:
	def __init__(self,nro):
		self.nro = nro
		self.tiempo = 0
		self.incompatibilidades = {}
		self.lavado = 0
 
	def cargar_incompatibilidad(self, nro):
		self.incompatibilidades.setdefault(nro, None)		
  
	def cargar_tiempo(self, nro):
		self.tiempo = nro
  
	def es_compatible_con(self, nro):
		if nro == self.nro:
			return False
		if nro in self.incompatibilidades:
			return False
		return True

	def __lt__(self, other):
		if self.incompatibilidades != other.incompatibilidades:
			return len(self.incompatibilidades) > len(other.incompatibilidades)		
		else:
			return self.tiempo > other.tiempo
			
  
def leer_archivo():
	archivo = open("segundo_problema.txt","r")
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
		else:
			lavanderia.cargar_tiempo(int(linea[1]), int(linea[2]))
		linea = archivo.readline()
	return lavanderia

def main():
	inicio = time.time()
	lavanderia = leer_archivo()
	lavanderia.lavar()
	fin = time.time()
	print(fin-inicio)
 
main()