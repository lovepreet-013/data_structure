def findRepeating(arr, n): 
	s = set() 
	for i in range(n): 
		if arr[i] in s: 
			return arr[i] 
		s.add(arr[i]) 
	
	return -1

arr = [9, 8, 2, 6, 1, 8, 5, 3] 
n = len(arr) 
print(findRepeating(arr, n)) 

