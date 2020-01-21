from queue import Queue 

class newNode: 
	def __init__(self, data): 
		self.val = data 
		self.left = self.right = None
	
def averageOfLevels(root): 

	q = Queue() 
	q.put(root) 
	while (not q.empty()): 

		Sum = 0
		count = 0
		temp = Queue() 
		while (not q.empty()): 
			n = q.queue[0] 
			q.get() 
			Sum += n.val 
			count += 1
			if (n.left != None): 
				temp.put(n.left) 
			if (n.right != None): 
				temp.put(n.right) 
		q = temp 
		print((Sum * 1.0 / count), end = " ") 

if __name__ == '__main__': 

	root = None
	root = newNode(4) 
	root.left = newNode(2) 
	root.right = newNode(9) 
	root.left.left = newNode(3) 
	root.left.right = newNode(8) 
	root.right.right = newNode(7) 
	averageOfLevels(root) 

