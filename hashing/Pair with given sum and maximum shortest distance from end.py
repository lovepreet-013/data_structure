def find_maximum(a, n, k): 
	
	b = dict() 
	
	for i in range(n): 
		x = a[i] 
		
		d = min(1 + i, n - i) 
		if x not in b.keys(): 
			b[x] = d 
		else: 

			b[x] = min(d, b[x]) 
	
	ans = 10**9
	for i in range(n): 
		x = a[i] 
		
		if (x != (k - x) and (k - x) in b.keys()):		 
			ans = min(max(b[x], b[k - x]), ans) 

	return ans 

a = [3, 5, 8, 6, 7] 
K = 11
n = len(a) 
print(find_maximum(a, n, K)) 

