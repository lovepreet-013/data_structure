from queue import Queue 

def checkSorted(n, q): 
	st = [] 
	expected = 1
	fnt = None

	while (not q.empty()): 
		fnt = q.queue[0] 
		q.get() 

		if (fnt == expected): 
			expected += 1

		else: 
			
			if (len(st) == 0): 
				st.append(fnt) 

			elif (len(st) != 0 and st[-1] < fnt): 
				return False

			else: 
				st.append(fnt) 

		while (len(st) != 0 and
				st[-1] == expected): 
			st.pop() 
			expected += 1

	if (expected - 1 == n and len(st) == 0): 
		return True

	return False

if __name__ == '__main__': 
	q = Queue() 
	q.put(5) 
	q.put(1) 
	q.put(2) 
	q.put(3) 
	q.put(4) 

	n = q.qsize() 

	if checkSorted(n, q): 
		print("Yes") 
	else: 
		print("No") 

