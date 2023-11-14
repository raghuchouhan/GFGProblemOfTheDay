# Node class for creating linked list nodes
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Solution class with the getMiddle function
class Solution:
    # Function to find the middle of the linked list
    def findMid(self, head):
        # Initialize two pointers, slow and fast
        slow = head
        fast = head

        # Traverse the linked list with different speeds for slow and fast pointers
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # At this point, the slow pointer is at the middle of the linked list
        if slow:
            return slow.data
        else:
            return -1



#{ 
 # Driver Code Starts
# Initial Template for Python3

# Node Class    
class node:
    def __init__(self):
        self.data = None
        self.next = None

# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insert(self, data):
        if self.head == None:
            self.head = node()
            self.tail = self.head
            self.head.data = data
        else:
            new_node = node()
            new_node.data = data
            new_node.next = None
            self.tail.next = new_node
            self.tail = self.tail.next

def printlist(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print('')

# Driver Program
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        list1 = Linked_List()
        n = int(input())
        values = list(map(int, input().strip().split()))
        for i in values:
            list1.insert(i)
        ob = Solution()
        print(ob.findMid(list1.head))


# } Driver Code Ends