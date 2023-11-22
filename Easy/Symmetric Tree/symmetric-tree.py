class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
    # Helper function to check if two subtrees are mirrors of each other
    def isMirror(self, left, right):
        # Base case: Both subtrees are None, so they are mirrors
        if not left and not right:
            return True
        # If one subtree is None and the other is not, they are not mirrors
        if not left or not right:
            return False
        # Check if the values are equal and the left subtree of one is the mirror of the right subtree of the other
        return (
            left.data == right.data
            and self.isMirror(left.left, right.right)
            and self.isMirror(left.right, right.left)
        )

    # Main function to check if the tree is symmetric
    def isSymmetric(self, root):
        # Base case: An empty tree is symmetric
        if not root:
            return True
        # Check if the left and right subtrees are mirrors of each other
        return self.isMirror(root.left, root.right)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Contributed by Sudarshan Sharma
from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root
    
    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        ob = Solution()
        if ob.isSymmetric(root):
            print("True")
        else:
            print("False")
        
        

# } Driver Code Ends