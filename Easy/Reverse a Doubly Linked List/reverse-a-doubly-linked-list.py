class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Solution:
    def reverseDLL(self, head):
        current = head
        new_head = None

        # Traverse the list and swap next and prev pointers for each node
        while current:
            temp = current.next
            current.next = current.prev
            current.prev = temp

            # Update new head to the current node
            new_head = current

            # Move to the next node
            current = temp

        return new_head

# Helper function to print the doubly linked list
def printDLL(head):
    current = head
    while current:
        print(current.data, end=" ")
        current = current.next
    print()



#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
class Node: 
    def __init__(self, data): 
        self.data = data  
        self.next = None
        self.prev = None
  
class DoublyLinkedList: 
    def __init__(self): 
        self.head = None
   
    def push(self, new_data,tail):
        if not self.head:
            self.head=Node(new_data)
            return self.head
        Nnode=Node(new_data)
        Nnode.prev=tail
        tail.next=Nnode
        return Nnode
        
    def printList(self, node): 
        while(node is not None): 
            print (node.data,end=' ') 
            node = node.next
            

            
if __name__ == '__main__':
    t=int(input())
    
    for tcs in range(t):
        n=int(input())
        arr=[int(x) for x in input().split()]
        
        
        dll=DoublyLinkedList()
        tail=None
        
        for e in arr:
            tail=dll.push(e,tail)
        
        ob = Solution()
        resHead=ob.reverseDLL(dll.head)
        dll.printList(resHead)
        print()
        
# } Driver Code Ends