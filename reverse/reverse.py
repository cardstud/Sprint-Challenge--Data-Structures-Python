class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node
         
    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node
        
    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        # reference to the head of the list
        self.head = None
        self.tail = None

    def add_to_head(self, value):
        node = Node(value)
        if self.head is not None:
            node.set_next(self.head)
        self.head = node  

    def contains(self, value):
        if not self.head:
            return False
        current = self.head
        # check to see if we're at a valid node
        while current:
            # return True if the current value we're looking at matches our target value
            if current.get_value() == value:
                return True
            # update our current node to the current node's next node
            current = current.get_next()
        # if we've gotten here, then the target node isn't in our list
        return False

    def reverse_list(self, node, prev):
        # if self.head is None:
        #     return None 
        prev = None

        current = self.head  
        while(current is not None): 
            next = current.next_node 
            current.next_node = prev  
            prev = current 
            current = next 
        self.head = prev 
 
    # Utility function to print the linked LinkedList 
    def printList(self): 
        temp = self.head 
        while(temp) != None: 
            print(temp.value, "-->", end="") 
            temp = temp.next_node 
     
# test the above 
llist = LinkedList() 
llist.add_to_head(20) 
llist.add_to_head(4) 
llist.add_to_head(15) 
llist.add_to_head(85) 
  
print ("Given Linked List")
llist.printList() 
llist.reverse_list(4, 15) 
print ("\nReversed Linked List")
llist.printList() 
