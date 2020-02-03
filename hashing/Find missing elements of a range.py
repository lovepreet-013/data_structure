from bisect import bisect_left 

def printMissing(arr, n, low, high): 
	
	arr.sort() 
	
	ptr = bisect_left(arr, low) 
	index = ptr 
	
	i = index 
	x = low 
	while (i < n and x <= high): 
		if(arr[i] != x): 
			print(x, end =" ") 

		else: 
			i = i + 1
		x = x + 1

	while (x <= high): 
		print(x, end =" ") 
		x = x + 1



arr = [1, 3, 5, 4] 
n = len(arr) 
low = 1
high = 10
printMissing(arr, n, low, high); 

