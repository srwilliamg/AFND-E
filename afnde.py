# -*- coding: utf-8 -*-
class AFNDE(object):
	def __init__(self, estados, alfabeto, estadoInicial, estadoFinal):
		super(AFNDE, self).__init__()

		self.alfabeto = alfabeto
		self.estadoFinal = estadoFinal
		self.estadoInicial = estadoInicial
		self.estados = estados
		#self.transiciones = transiciones
		self.automata = {}

		if 	len(self.estados) == 0 or len(self.estados) == 0 or len(self.alfabeto) == 0 :
			return "No se ha ingresado alguno de los argumentos"

		self.setTransitions()

	def setTransitions(self):
		transitions = {}
		alpha = []
		for x in self.estados:
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
				qresp = raw_input('Desea ingresar un nuevo estado destino de {}? S/N: '.format(x))
				if qresp == 'N':
					break
			transitions[x] = alpha
			alpha = []
		self.automata = transitions

	def getTransitions(self):
		print(self.automata);




if __name__ == '__main__':
	a = AFNDE(["A","B"], ["x","y"],"A","B")
	a.getTransitions()