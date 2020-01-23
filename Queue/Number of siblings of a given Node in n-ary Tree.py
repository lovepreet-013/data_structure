from queue import Queue 

class newNode: 
	def __init__(self,data): 
		self.child = [] 
		self.key = data 

def numberOfSiblings(root, x): 
	if (root == None): 
		return 0

	q = Queue() 
	q.put(root) 

	while (not q.empty()): 
		
		p = q.queue[0] 
		q.get() 

		for i in range(len(p.child)): 
			
			if (p.child[i].key == x): 
				return len(p.child) - 1
			q.put(p.child[i]) 

if __name__ == '__main__': 

	root = newNode(50) 
	(root.child).append(newNode(2)) 
	(root.child).append(newNode(30)) 
	(root.child).append(newNode(14)) 
	(root.child).append(newNode(60)) 
	(root.child[0].child).append(newNode(15)) 
	(root.child[0].child).append(newNode(25)) 
	(root.child[0].child[1].child).append(newNode(70)) 
	(root.child[0].child[1].child).append(newNode(100)) 
	(root.child[1].child).append(newNode(6)) 
	(root.child[1].child).append(newNode(1)) 
	(root.child[2].child).append(newNode(7)) 
	(root.child[2].child[0].child).append(newNode(17)) 
	(root.child[2].child[0].child).append(newNode(99)) 
	(root.child[2].child[0].child).append(newNode(27)) 
	(root.child[3].child).append(newNode(16)) 

	x = 100

	print(numberOfSiblings(root, x)) 
