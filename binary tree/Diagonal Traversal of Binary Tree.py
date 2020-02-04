class Node: 

	def __init__(self, data): 
		self.data = data 
		self.left = None
		self.right = None


def diagonalPrintUtil(root, d, diagonalPrintMap): 
	
	if root is None: 
		return

	try : 
		diagonalPrintMap[d].append(root.data) 
	except KeyError: 
		diagonalPrintMap[d] = [root.data] 

	diagonalPrintUtil(root.left, d+1, diagonalPrintMap) 
	
	diagonalPrintUtil(root.right, d, diagonalPrintMap) 



def diagonalPrint(root): 

	diagonalPrintMap = dict() 
	
	diagonalPrintUtil(root, 0, diagonalPrintMap) 

	print "Diagonal Traversal of binary tree : "
	for i in diagonalPrintMap: 
		for j in diagonalPrintMap[i]: 
			print j, 
		print "" 


root = Node(8) 
root.left = Node(3) 
root.right = Node(10) 
root.left.left = Node(1) 
root.left.right = Node(6) 
root.right.right = Node(14) 
root.right.right.left = Node(13) 
root.left.right.left = Node(4) 
root.left.right.right = Node(7) 

diagonalPrint(root) 

