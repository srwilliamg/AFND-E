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
					if resp == 'N':
						break
				transition.append(alpha)
				alpha = []
				qresp = raw_input('Desea ingresar un nuevo estado destino de {}? S/N: '.format(x))
				if qresp == 'N':
					break
			self.automata[x] = transition
			transition = []

	def getTransitions(self):
		print(self.automata);

	def findPath(self, state, symbol): #Encuentra todos los estado a los que se llega respectoa un símbolo
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

	def fullPath(self,state, symbol): #Encuentra todos los estado que efecto al estado indicado respectoa un símbolo
		queue = []
		if self.visited[state]:
			return []
		else:
			aux = self.findPath(state,symbol)
			self.visited[state] = True
			queue = queue + aux
			print("queue : {}".format(queue))
			if len(queue) == 0:
				return queue
			else:
				for q in queue:
					print("q : {}".format(q))
					queue = queue + self.fullPath(q, symbol)
		return queue

if __name__ == '__main__':
	a = AFNDE(["A","B","C","D","E","F"], ["a","b","c","d","e","x"], "A", "E",
	{
		'A':[['B', 'a'],['B', 'x'],['F', 'x']],
		'B':[['C','c'],['C', 'x'],['A', 'x']],
		'C':[['D', 'd'],['D', 'x']],
		'D':[['E','e'],['E', 'x']],
		'F':[['F','x'],['E', 'x']],
		'E':[['','']]
	})
	a.getTransitions()
	print (a.findPath("A","x"))
	print (a.fullPath("A","x"))