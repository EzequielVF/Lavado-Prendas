import time

class Lavanderia:
	def __init__(self):
		self.nroLavadoActual = 0
		self.prendas = []
		self.cola = []
		self.cantidad_prendas = 0
		self.prendas_lavadas = 0
	
	def priorizacion(self):
		tiempo_prenda = 0
		for i in range(self.cantidad_prendas):
			tiempo_prenda = self.prendas[i].tiempo_lavado()
			for j in range(self.cantidad_prendas):
				if self.prendas[j].te_lavas_en_menos_tiempo(tiempo_prenda) and (self.prendas[i].es_compatible_con(j+1)):
					self.prendas[i].es_mas_pesada()
    
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
		while(self.prendas_lavadas <= self.cantidad_prendas - 1):
			if (self.prendas[i].prenda_lavada() == False) and (self.cola_incompatible(self.prendas[i].nro) == False):
				self.cola.append(self.prendas[i])
			i = i + 1
			if i == self.cantidad_prendas:
				for j in self.cola:
					j.lavar_prenda()
					self.prendas_lavadas = self.prendas_lavadas + 1
					archivo.write(str(j.nro) + " " + str(lavado) + "\n")
				self.cola = []
				lavado = lavado + 1
				i = 0
		archivo.close()
			
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
		self.prendas_mas_pesadas = 0
	
	def te_lavas_en_menos_tiempo(self, nro):
		if self.tiempo < nro:
			return True
		return False
  
	def tiempo_lavado(self):
		return self.tiempo
 
	def es_mas_pesada(self):
		self.prendas_mas_pesadas = self.prendas_mas_pesadas + 1
  
	def cargar_incompatibilidad(self, nro):
		self.incompatibilidades.setdefault(nro, None)		
  
	def cargar_tiempo(self, nro):
		self.tiempo = nro
  
	def es_compatible_con(self, nro):
		if nro in self.incompatibilidades:
			return False
		return True
  
	def prenda_lavada(self):
		return self.lavada

	def lavar_prenda(self):
		self.lavada = True

	def __lt__(self, other):
		if self.prendas_mas_pesadas != other.prendas_mas_pesadas:
			return self.prendas_mas_pesadas < other.prendas_mas_pesadas
		if self.tiempo != other.tiempo:
			return self.tiempo > other.tiempo
		else:
			return len(self.incompatibilidades) < len(other.incompatibilidades)
  
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
	lavanderia.priorizacion()	
	lavanderia.lavar()
	fin = time.time()
	print(fin-inicio)
 
main()