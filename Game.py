#import Moduls
#import network

class World():
	def __init__(self):
		a = []
		with open('Cletki.txt', 'r') as CLETKI:
			for line in CLETKI:
				a += {tuple(line.split()[:2]) : tuple(line.split()[2:])}
		print(a('1', '1'))

	#def askter(x,y):
	#	return self.Moduls.terry(a[x,y])

world = World()