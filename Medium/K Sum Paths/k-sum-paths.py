from collections import defaultdict

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
    def sumK(self, root, k):
        # Helper function to perform recursive traversal
        def dfs(node, current_sum, running_sums):
            if not node:
                return 0

            current_sum += node.data
            count_paths = running_sums[current_sum - k]

            running_sums[current_sum] += 1

            count_paths += dfs(node.left, current_sum, running_sums)
            count_paths += dfs(node.right, current_sum, running_sums)

            running_sums[current_sum] -= 1  # Backtrack to remove the current node's contribution

            return count_paths

        running_sums = defaultdict(int)
        running_sums[0] = 1  # Initialize with a dummy value for the root
        count_paths = dfs(root, 0, running_sums)

        return count_paths


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(100000)
from collections import deque
from collections import defaultdict
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
        d=int(input())
        ob = Solution()
        print(ob.sumK(root,d))
        
# } Driver Code Ends