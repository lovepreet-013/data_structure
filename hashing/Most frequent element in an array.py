import math as mt 

def mostFrequent(arr, n): 

	Hash = dict() 
	for i in range(n): 
		if arr[i] in Hash.keys(): 
			Hash[arr[i]] += 1
		else: 
			Hash[arr[i]] = 1

	max_count = 0
	res = -1
	for i in Hash: 
		if (max_count < Hash[i]): 
			res = i 
			max_count = Hash[i] 
		
	return res 

arr = [ 1, 5, 2, 1, 3, 2, 1] 
n = len(arr) 
print(mostFrequent(arr, n)) 