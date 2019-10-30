import sys
from changemaker import *
testCases = []

if(len(sys.argv) < 2):
	print('Por favor, ingrese la ruta del archivo de entrada de datos')
else:
	#Abriendo archivo para añadir datos:
	output = open('output.txt','a')
	#Abriendo el archivo.
	try:
		f = open(sys.argv[1], 'r')
	except Exception as e:
		print('No es un parámetro adecuado')
	else:
		
		
		#Determinando el numero de casos. 
		nCases = int(f.readline())

		#Separando los datos y convirtiendolos a enteros
		for i in range(0,nCases):
			testCases.append(f.readline())
			testCases[i] = testCases[i].split();
			for j in range(0,len(testCases[i])):
				testCases[i][j] = int(testCases[i][j])

		f.close()		
		#Borrando los resultados de una anterior operación
		f = open('output.txt','w')
		f.close()
		f = open('output.txt','a')


		#Resolviendo cada caso
		for case in testCases:
			N = case[0] #Rango a evaluar.
			K = case[1] #Número de denominaciones.
			coins = []  #Lista de monedas.

			#Obteniendo cada denominación
			for i in range(2,len(case)):
				coins.append(case[i])
			
			#Llenando matriz para todas las posibilidades de formar los montos
			changes = fillChangeMatrix(N = N, coins = coins)
			#Refinando los cambios teniendo en cuenta el vuelto:
			refinedChange = refineChangeMatrix(changes, N, coins)

			total = sum(refinedChange[coins[-1]])
			average = round(total/N,2)
			maxcoins = max(refinedChange[coins[-1]])
			#Escribiendo los datos en el archivo
			f.write("{} {} \n".format(str(average),str(maxcoins)))
	f.close()

