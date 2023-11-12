# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Function to find the Nth node from the end
def getNthFromLast(head, n):
    # Initialize two pointers
    slow = head
    fast = head

    # Move fast pointer N nodes ahead
    for _ in range(n):
        if fast is None:
            return -1  # N is greater than the length of the linked list

        fast = fast.next

    # Move both pointers until fast reaches the end
    while fast is not None:
        slow = slow.next
        fast = fast.next

    # 'slow' now points to the Nth node from the end
    return slow.data if slow is not None else -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3


import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())
    
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        n,nth_node = map(int, input().strip().split())
        a = LinkedList() # create a new linked list 'a'.
        nodes_a = list(map(int, input().strip().split()))
        for x in nodes_a:
            a.append(x)  # add to the end of the list
        print(getNthFromLast(a.head,nth_node))
# } Driver Code Ends