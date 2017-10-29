Class CL:
	A["1;1"]:
		text = 'Base cl 11'
	A["1;2"]:
		text = 'Base cl 12'
	A["2;1"]:
		text = 'Base cl 21'
	A["2;2"]:
		text = 'Base cl 22'
	A["2;3"]:
		text = 'Base cl 23'

def terry(x):
	return(CL.A[x].text)
