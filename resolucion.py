import time

class Lavanderia:
	def __init__(self):
		self.prendas = []
		self.cantidad_prendas = 0
	
	def cargar_prendas(self, nro):
		self.cantidad_prendas = nro
		for i in range(nro):
			self.prendas.append(Prenda(i+1))
 
	def cargar_incompatibilidad(self, prenda, prenda2):
		if self.prendas[prenda-1].es_compatible_con(prenda2):
			self.prendas[prenda-1].cargar_incompatibilidad(prenda2)
		
		if self.prendas[prenda2-1].es_compatible_con(prenda):
			self.prendas[prenda2-1].cargar_incompatibilidad(prenda)
	
	def cargar_tiempo(self, prenda, tiempo):
		self.prendas[prenda-1].cargar_tiempo(tiempo)
 
	def lavar(self):
		archivo = open("respuestasTP3.txt","w")
		self.prendas.sort()
		lavado = 1
		colores = [-1] * self.cantidad_prendas
		for i in range(self.cantidad_prendas):
			if colores[i] == -1:
				colores[i] =  lavado
				archivo.write(str(self.prendas[i].nro) + " " + str(lavado) + "\n")	
				for j in range(self.cantidad_prendas):
					if j == i:
						continue
					if colores[j] == -1 and self.lavado_compatible(j, lavado, colores):
						colores[j] =  lavado
						archivo.write(str(self.prendas[j].nro) + " " + str(lavado) + "\n")		
				lavado += 1
		archivo.close()
		return (lavado-1,colores)
	
	def lavado_compatible(self, j, lavado_actual, colores):
		for x in range(j):
			if self.prendas[x].es_compatible_con(self.prendas[j].nro) == False and colores[x] == lavado_actual:
				return False
		return True

	def tiempo_lavado(self, colores, lavados):
		tiempo_x_lavado = [0]*(lavados+1)
		for x in range(self.cantidad_prendas):
			if self.prendas[x].tiempo > tiempo_x_lavado[colores[x]]:
				tiempo_x_lavado[colores[x]] = self.prendas[x].tiempo
		return sum(tiempo_x_lavado)
		
class Prenda:
	def __init__(self,nro):
		self.nro = nro
		self.tiempo = 0
		self.incompatibilidades = {}
 
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
		if self.tiempo != other.tiempo:
			return self.tiempo > other.tiempo
		else:
			return len(self.incompatibilidades) >= len(other.incompatibilidades)
			
  
def leer_archivo():
	archivo = open("tercer_problema.txt","r")
	#aux = open("inputtp2paracplex.txt","w") #Lineas usadas para generarme el archivo .dat para probar la solucion de CPLEX con el input del TP2
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
			#aux.write("<" + str(linea[1]) + "," + str(linea[2]) + ">," + "\n")
		else:
			lavanderia.cargar_tiempo(int(linea[1]), int(linea[2]))
			#aux.write("<" + str(linea[1]) + "," + str(linea[2]) + ">," + "\n")
		linea = archivo.readline()
	return lavanderia

def main():
	inicio = time.time()
	lavanderia = leer_archivo()
	resultado = lavanderia.lavar()
	fin = time.time()
	print("Se hicieron: " + str(resultado[0]) + " lavados.")
	lavanderia.tiempo_lavado(resultado[1], resultado[0])	
	print("El tiempo que tardo en lavar todo es: " + str(lavanderia.tiempo_lavado(resultado[1], resultado[0])))
	print("El tiempo que tardo en correr el script es: " + str(fin-inicio) + " segs.")
 
main()