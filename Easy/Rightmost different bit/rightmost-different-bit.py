#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math




    
# } Driver Code Ends
class Solution:
    
    # Function to find the first position with different bits.
    def posOfRightMostDiffBit(self, m, n):
        # If both numbers are the same, return -1.
        if m == n:
            return -1
        
        # XOR the two numbers to find the differing bits.
        xor_result = m ^ n
        
        # Find the position of the rightmost set bit in the XOR result.
        pos = 1
        while (xor_result & 1) == 0:
            xor_result >>= 1
            pos += 1
        
        return pos


#{ 
 # Driver Code Starts.
    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        mn=[int(x) for x in input().strip().split()]
        m=mn[0]
        n=mn[1]
        ob=Solution()
        print(math.floor(ob.posOfRightMostDiffBit(m,n)))
        
        
        
        
        T-=1
    
    




if __name__=="__main__":
    main()
# } Driver Code Ends