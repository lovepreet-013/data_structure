MAX = 1000
tree = [0] * (4 * MAX) 

arr = [0] * MAX

def gcd(a: int, b: int): 
	if a == 0: 
		return b 
	return gcd(b % a, a) 

def lcm(a: int, b: int): 
	return (a * b) // gcd(a, b) 

def build(node: int, start: int, end: int): 

	if start == end: 
		tree[node] = arr[start] 
		return

	mid = (start + end) // 2

	build(2 * node, start, mid) 
	build(2 * node + 1, mid + 1, end) 

	left_lcm = tree[2 * node] 
	right_lcm = tree[2 * node + 1] 

	tree[node] = lcm(left_lcm, right_lcm) 

def query(node: int, start: int, 
		end: int, l: int, r: int): 

	if end < l or start > r: 
		return 1

	if l <= start and r >= end: 
		return tree[node] 

	mid = (start + end) // 2
	left_lcm = query(2 * node, start, mid, l, r) 
	right_lcm = query(2 * node + 1, 
					mid + 1, end, l, r) 
	return lcm(left_lcm, right_lcm) 

if __name__ == "__main__": 

	arr[0] = 5
	arr[1] = 7
	arr[2] = 5
	arr[3] = 2
	arr[4] = 10
	arr[5] = 12
	arr[6] = 11
	arr[7] = 17
	arr[8] = 14
	arr[9] = 1
	arr[10] = 44

	build(1, 0, 10) 

	print(query(1, 0, 10, 2, 5)) 

	print(query(1, 0, 10, 5, 10)) 

	print(query(1, 0, 10, 0, 10)) 

