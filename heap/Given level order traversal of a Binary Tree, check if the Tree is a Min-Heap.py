def isMinHeap(level, n): 
	
	for i in range(int(n / 2) - 1, -1, -1): 
		
		if level[i] > level[2 * i + 1]: 
			return False

		if 2 * i + 2 < n: 
			
			if level[i] > level[2 * i + 2]: 
				return False
	return True

if __name__ == '__main__': 
	level = [10, 15, 14, 25, 30] 
	n = len(level) 
	if isMinHeap(level, n): 
		print("True") 
	else: 
		print("False") 

