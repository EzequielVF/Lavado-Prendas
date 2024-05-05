import time

class Lavanderia:
	def __init__(self):
		self.nroLavadoActual = 0
		self.prendas = []
		self.cola = []
		self.cantidad_prendas = 0
		self.prendas_lavadas = 0
	
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
		self.prendas.sort()
		archivo = open("respuestasTP2.txt","w")
		i = 0
		lavado = 1
		colores = [-1] * self.cantidad_prendas
		for i in range(self.cantidad_prendas):
			if colores[i] == -1:
				colores[i] =  lavado
				self.prendas[i].lavado = lavado
				for j in range(self.cantidad_prendas):
					if colores[j] == -1 and self.prendas[i].es_compatible_con(self.prendas[j].nro) == True:
						colores[j] =  lavado
						self.prendas[j].lavado = lavado
				lavado += 1

		prendas_ordenadas = sorted(self.prendas, key=lambda x: x.lavado)
		for prenda in prendas_ordenadas:
			archivo.write(str(prenda.nro) + " " + str(prenda.lavado) + "\n")
		#while(self.prendas_lavadas <= self.cantidad_prendas - 1):
		#	if (self.prendas[i].prenda_lavada() == False) and (self.cola_incompatible(self.prendas[i].nro) == False):
		#		self.cola.append(self.prendas[i])
		#	i = i + 1
		#	if i == self.cantidad_prendas:
		#		for j in self.cola:
		#			j.lavar_prenda()
		#			self.prendas_lavadas = self.prendas_lavadas + 1
		#			archivo.write(str(j.nro) + " " + str(lavado) + "\n")
		#		self.cola = []
		#		lavado = lavado + 1
		#		i = 0
		archivo.close()
	
	def lavado_compatible(self, i, j):
		for x in range(i):
			if self.prendas[x].es_compatible_con(self.prendas[j].nro) == False:
				return False
		return True
 		
	def cola_incompatible(self, nro):
		if len(self.cola) == 0:
			return False
		flag = False
		for i in self.cola:
			aux = i.es_compatible_con(nro)
			if aux == False:
				flag = True
				break
		return flag
 	
class Prenda:
	def __init__(self,nro):
		self.nro = nro
		self.tiempo = 0
		self.incompatibilidades = {}
		self.lavada = False
		self.lavado = 0
	
	def devolver_lista_incomp(self):
		return self.incompatibilidades
 
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
  
	def prenda_lavada(self):
		return self.lavada

	def lavar_prenda(self):
		self.lavada = True

	def __lt__(self, other):
		return len(self.incompatibilidades) > len(other.incompatibilidades)
  
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