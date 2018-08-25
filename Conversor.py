#Es evidente lo que hacemos en la siguiente linea

def convertira_segundos(hs, mins, segs):
	#return segs+mins*60+hs*3000
	total=segs
	total+=mins*60
	total+=hs*3000
	return total
print(convertira_segundos(0,1,30))