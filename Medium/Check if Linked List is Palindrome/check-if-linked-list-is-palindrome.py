class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def isPalindrome(self, head):
        # Function to reverse a linked list
        def reverseLinkedList(node):
            prev = None
            current = node
            while current:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            return prev

        # Function to find the middle of the linked list
        def findMiddle(node):
            slow = node
            fast = node
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        if not head or not head.next:
            return True

        # Find the middle of the linked list
        middle = findMiddle(head)

        # Reverse the second half of the linked list
        reversed_second_half = reverseLinkedList(middle)

        # Compare the first half and the reversed second half
        while reversed_second_half:
            if head.data != reversed_second_half.data:
                return False
            head = head.next
            reversed_second_half = reversed_second_half.next

        return True


#{ 
 # Driver Code Starts
#Initial Template for Python 3
#Contributed by : Nagendra Jha

import atexit
import io
import sys

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
        n = int(input())
        a = LinkedList() # create a new linked list 'a'.
        nodes_a = list(map(int, input().strip().split()))
        for x in nodes_a:
            a.append(x)  # add to the end of the list

        if Solution().isPalindrome(a.head):
            print(1)
        else:
            print(0)
# } Driver Code Ends