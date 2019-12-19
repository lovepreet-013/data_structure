class Node: 
    def __init__(self, new_data): 
      self.data = new_data 
      self.next = None
      
class LinkedList: 
    def __init__(self): 
      self.head = None
    def push(self, new_data): 
      new_node = Node(new_data) 
      new_node.next = self.head 
      self.head = new_node 
  
    def printNthFromLast(self, n): 
      temp = self.head 
          
      length = 0
      while temp is not None: 
        temp = temp.next
        length += 1

      if n > length:  
        print('Location is greater than the' + ' length of LinkedList') 
        return
      temp = self.head 
      for i in range(0, length - n): 
        temp = temp.next
      print(temp.data) 
  
llist = LinkedList()  
llist.push(20)  
llist.push(4)  
llist.push(15)  
llist.push(35) 
llist.printNthFromLast(4) 
  
