class newNode: 
  def __init__(self, key): 
    self.key= key 
    self.left = None
    self.right = None
  
def printList(head): 
  while (head != None): 
    print(head.key, end = " ") 
    head = head.next
      
  print() 
  
def detectLoop( head): 
  temp = "" 
  while (head != None): 
        
    if (head.next == None): 
      return False
            
    if (head.next == temp): 
      return True

    nex = head.next
    head.next = temp 
    head = nex 
  
  return False
  
# Driver Code 
head = newNode(1)  
head.next = newNode(2)  
head.next.next = newNode(3)  
head.next.next.next = newNode(4)  
head.next.next.next.next = newNode(5)  
  
# Create a loop for testing(5 is pointing to 3) 
head.next.next.next.next.next = head.next.next
  
found = detectLoop(head)  
if (found): 
    print("Loop Found") 
else: 
    print("No Loop") 