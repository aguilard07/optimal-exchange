def fillChangeMatrix(N, coins):
	change = {}
	previousCoin = 0
	for coin in coins:
		change[coin] = []
		for value in range(1,N+1):
			index = value -1
			if coin == 1:
				change[coin].append(value)
			else:				
				if (coin > value):
					change[coin].append(change[previousCoin][index])
				else:
					if(coin == value):
						change[coin].append(1)
					else:	
						leftAmount = value-coin
						a = change[previousCoin][index]
						b = change[coin][leftAmount - 1] + 1
						result = min([a,b])
						change[coin].append(result) 
		previousCoin = coin
	return change

def refineChangeMatrix(change, N, coins):
	refinedChange = {}
	previousCoin = 0
	for coin in coins:
		refinedChange[coin] = []
		for value in range(1,N+1):
			index = value - 1
			if coin == 1:
				refinedChange[coin].append(value)
			else:
				leftAmount = abs(value - coin)
				a = change[coins[-1]][value - 1]
				b = change[coins[-1]][leftAmount-1] + 1
				c = refinedChange[previousCoin][value - 1]
				d = refinedChange[previousCoin][leftAmount-1] + 1				
				if (len(refinedChange[coin]) < leftAmount ):
					e = 1000
				else:
					e = refinedChange[coin][leftAmount-1] + 1			
				
				result = (min([a,b,c,d,e]))
				refinedChange[coin].append(result)		
		previousCoin = coin
	return refinedChange