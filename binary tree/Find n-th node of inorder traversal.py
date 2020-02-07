class newNode: 

	def __init__(self, data): 
		self.data = data 
		self.left = None
		self.right = None
		self.visited = False

count = [0] 

def NthInorder(node, n): 

	if (node == None): 
		return

	if (count[0] <= n): 

		NthInorder(node.left, n) 
		count[0] += 1

		if (count[0] == n): 
			print(node.data, end = " ") 

		NthInorder(node.right, n) 
						
if __name__ == '__main__': 

	root = newNode(10) 
	root.left = newNode(20) 
	root.right = newNode(30) 
	root.left.left = newNode(40) 
	root.left.right = newNode(50) 

	n = 4

	NthInorder(root, n) 

