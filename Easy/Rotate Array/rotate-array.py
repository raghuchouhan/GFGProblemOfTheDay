class Solution:
    # Function to rotate an array by d elements in the counter-clockwise direction.
    def rotateArr(self, A, D, N):
        # Taking the modulo to handle cases where D is greater than N.
        D = D % N

        # Reverse the first part of the array (0 to D-1).
        self.reverse(A, 0, D - 1)

        # Reverse the second part of the array (D to N-1).
        self.reverse(A, D, N - 1)

        # Reverse the entire array to get the final result.
        self.reverse(A, 0, N - 1)

    # Helper function to reverse a portion of the array from index start to end.
    def reverse(self, arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
def main():
    T=int(input())
    
    while(T>0):
        nd=[int(x) for x in input().strip().split()]
        N=nd[0]
        D=nd[1]
        A=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.rotateArr(A,D,N)
        
        for i in A:
            print(i,end=" ")
            
        print()
       
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends