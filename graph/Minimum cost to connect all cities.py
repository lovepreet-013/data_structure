def minnode(n, keyval, mstset): 
	mini = 999999999999
	mini_index = None
	
	for i in range(n): 
		if (mstset[i] == False and
			keyval[i] < mini): 
			mini = keyval[i] 
			mini_index = i 
	return mini_index 

def findcost(n, city): 

	parent = [None] * n 
	
	keyval = [None] * n 
	
	mstset = [None] * n 
	
	for i in range(n): 
		keyval[i] = 9999999999999
		mstset[i] = False
	
	parent[0] = -1
	keyval[0] = 0
	
	for i in range(n - 1): 
	
		u = minnode(n, keyval, mstset) 
	
		mstset[u] = True
	
		for v in range(n): 
			if (city[u][v] and mstset[v] == False and
				city[u][v] < keyval[v]): 
				keyval[v] = city[u][v] 
				parent[v] = u 
	
	cost = 0
	for i in range(1, n): 
		cost += city[parent[i]][i] 
	print(cost) 

if __name__ == '__main__': 

	n1 = 5
	city1 = [[0, 1, 2, 3, 4], 
			[1, 0, 5, 0, 7], 
			[2, 5, 0, 6, 0], 
			[3, 0, 6, 0, 0], 
			[4, 7, 0, 0, 0]] 
	findcost(n1, city1) 
	
	n2 = 6
	city2 = [[0, 1, 1, 100, 0, 0], 
			[1, 0, 1, 0, 0, 0], 
			[1, 1, 0, 0, 0, 0], 
			[100, 0, 0, 0, 2, 2], 
			[0, 0, 0, 2, 0, 2], 
			[0, 0, 0, 2, 2, 0]] 
	findcost(n2, city2) 

