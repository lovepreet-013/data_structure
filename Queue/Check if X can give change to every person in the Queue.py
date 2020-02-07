def isChangeable(notes, n): 
	
	fiveCount = 0
	tenCount = 0
	
	for i in range(n): 
		
		if (notes[i] == 5): 
			fiveCount += 1
		elif(notes[i] == 10): 
			
			if (fiveCount > 0): 
				fiveCount -= 1
				tenCount += 1
			else: 
				return 0
		else: 
			
			if (fiveCount > 0 and tenCount > 0): 
				fiveCount -= 1
				tenCount -= 1
				
			elif (fiveCount >= 3): 
				fiveCount -= 3
			else: 
				return 0
	return 1

a = [5, 5, 5, 10, 20 ] 
n = len(a) 

if (isChangeable(a, n)): 
	print("YES") 
else: 
	print("NO") 

