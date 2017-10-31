import WorldCL
import network
import socket

class World:
	def __init__(self):
		a = []
		with open('Cletki.txt',r) as CLETKI:
			for line in CLETKI:
				a.append(
					lambda line: 
					x=line.split()[0] 
					y=line.split()[1] 
					z=line.split()[2:]
					return([x,y,z])
				 	)
		for b in a: 
			print(b)
		g=input()

	def askter(x,y):
		return(self.WorldCL.terry(x,y))

world = World()