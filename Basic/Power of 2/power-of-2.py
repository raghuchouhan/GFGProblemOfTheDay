class Solution:
    def isPowerofTwo(self, n):
        # Check if n is a positive integer
        if n <= 0:
            return False

        # Check if there is exactly one set bit in the binary representation of n
        return n & (n - 1) == 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        ob=Solution()
        if ob.isPowerofTwo(n):
            print("YES")
        else:
            print("NO")
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends