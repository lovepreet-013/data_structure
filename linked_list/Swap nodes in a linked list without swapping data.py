class LinkedList(object): 
  def __init__(self): 
    self.head = None
  
  
  class Node(object): 
    def __init__(self, d): 
      self.data = d 
      self.next = None
  
    def swapNodes(self, x, y): 
        if x == y: 
            return 
        prevX = None
        currX = self.head 
        while currX != None and currX.data != x: 
            prevX = currX 
            currX = currX.next
  
        prevY = None
        currY = self.head 
        while currY != None and currY.data != y: 
            prevY = currY 
            currY = currY.next
  
        if currX == None or currY == None: 
            return 
        if prevX != None: 
            prevX.next = currY 
        else: 
            self.head = currY 
  
        if prevY != None: 
            prevY.next = currX 
        else: 
            self.head = currX 
  
        temp = currX.next
        currX.next = currY.next
        currY.next = temp 
  
    def push(self, new_data): 
        new_Node = self.Node(new_data) 
        new_Node.next = self.head 
        self.head = new_Node 
  
    def printList(self): 
        tNode = self.head 
        while tNode != None: 
            print tNode.data, 
            tNode = tNode.next
  
llist = LinkedList() 

llist.push(7) 
llist.push(6) 
llist.push(5) 
llist.push(4) 
llist.push(3) 
llist.push(2) 
llist.push(1) 
print "Linked list before calling swapNodes() "
llist.printList() 
llist.swapNodes(4, 3) 
print "\nLinked list after calling swapNodes() "
llist.printList() 
