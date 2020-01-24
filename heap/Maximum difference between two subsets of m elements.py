def find_difference(arr, n, m): 
	max = 0; min = 0
	
	arr.sort(); 
	j = n-1
	for i in range(m): 
		min += arr[i] 
		max += arr[j] 
		j = j - 1
	
	return (max - min) 

if __name__ == "__main__": 
	arr = [1, 2, 3, 4, 5] 
	n = len(arr) 
	m = 4

	print(find_difference(arr, n, m)) 

