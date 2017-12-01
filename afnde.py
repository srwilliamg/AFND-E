# -*- coding: utf-8 -*-
class AFNDE(object):
	def __init__(self, estados, alfabeto, estadoInicial, estadoFinal, automata = {}):
		super(AFNDE, self).__init__()

		self.alfabeto = alfabeto
		self.estadoFinal = estadoFinal
		self.estadoInicial = estadoInicial
		self.estados = estados
		self.automata = automata
		self.visited = {}
		self.clausuras = {}
		self.tabla = {}

		if 	len(self.estados) == 0 or len(self.estados) == 0 or len(self.alfabeto) == 0 :
			return "No se ha ingresado alguno de los argumentos"

		if len(self.automata) == 0:
			self.setTransitions()

		self.initVisited()

	def initVisited(self):
		for q in self.automata:
			self.visited[q] = False

	def setTransitions(self):
		transition = []
		alpha = []
		for x in self.estados:
			if x == self.estadoFinal:
				self.automata[x] = [[]]
				continue
			print('Ingrese el estado destino y el símbolo de {}'.format(x))
			while True:
				q = raw_input('Ingresa el estado destino: ')
				alpha += [q]
				while True:
					a = raw_input('Ingresa el símbolo: ')
					alpha += [a]
					resp = raw_input('Desea ingresar una nueva transición? S/N: ')
					if resp == 'N' or resp == 'n':
						break
				transition.append(alpha)
				alpha = []
				qresp = raw_input('Desea ingresar un nuevo estado destino de {}? S/N: '.format(x))
				if qresp == 'N' or qresp == 'n':
					break
			self.automata[x] = transition
			transition = []

	def getTransitions(self):
		print(self.automata);

	def findPath(self, state, symbol): #Encuentra todos los estados a los que se llega desde un estado(state) respecto a un símbolo(symbol)
		lista = []
		if state == self.estadoFinal:
			return []
		else:
			for l in self.automata[state]:
				for s in l:
					if s == symbol:
						lista.append(l[0])
						#print("findP: {}".format(lista))
			return lista

	def fullPath(self,state, symbol): #Encuentra todos los estado que efecta al estado indicado (state) respecto a un símbolo (symbol)
		queue = []
		if self.visited[state]:
			return []
		else:
			aux = self.findPath(state,symbol)
			self.visited[state] = True
			queue = queue + aux
			#print("queue : {}".format(queue))
			if len(queue) == 0:
				return queue
			else:
				for q in queue:
					#print("q : {}".format(q))
					queue = queue + self.fullPath(q, symbol)
		return queue

	def clausurasE(self):
		for estado in self.estados:
			cl = self.fullPath(estado,"e")
			print ("C{}: {}".format(estado, cl))
			self.clausuras[estado] = cl
			self.initVisited()

	def tableE(self):
		for estado in self.estados:
			for alpha in self.alfabeto:
				pe = self.findPath(estado,alpha)
				print("{}{}: {}".format(estado,alpha,pe))
				self.tabla[(estado,alpha)] = pe

	def conversion(self, state, symbol):
		if len(self.tabla[(state,symbol)]) == 0:
			if len(self.tabla[(state, "e")]) == 0:
				return []
			else:
				lista = []
				for x in self.tabla[(state, "e")]:
					lista = lista + self.conversion(x,symbol)
				return lista
		else:
			return self.tabla[(state,symbol)]

	def convFunct(self):
		convert = []
		for estado in self.estados:
			for alpha in self.alfabeto:
				if alpha=="e":
					continue
				convert = convert + [[alpha,estado] +self.conversion(estado, alpha)]
		print(convert)

if __name__ == '__main__':
	a = AFNDE(["0","1","2","3","4","5","6","7","8","9","10"], ["e","a","b"], "0", "10",
	{
		"0":[["1","e"],["7","e"]],
		"1":[["2","e"],["4","e"]],
		"2":[["3","a"]],
		"3":[["6","e"]],
		"4":[["5","b"]],
		"5":[["6","e"]],
		"6":[["1","e"],["7","e"]],
		"7":[["8","a"]],
		"8":[["9","b"]],
		"9":[["10","b"]],
		"10":[['','']]
	})
	#a.getTransitions()
	a.clausurasE()
	print("te")
	a.tableE()
	print("PATH")
	print(a.fullPath("1","a"))
	print("Conversion")
	a.convFunct()