class Solution:
    
    #Function to find the smallest positive number missing from the array.
    def missingNumber(self, arr, n):
        i = 0
        while i < n:
            # If the current element is in the valid range and not in its correct position.
            if 1 <= arr[i] <= n and arr[i] != arr[arr[i] - 1]:
                # Swap the current element with the one at its correct position.
                arr[arr[i] - 1], arr[i] = arr[i], arr[arr[i] - 1]
            else:
                i += 1
        
        # Finding the first index where the element is not in its correct position.
        for i in range(n):
            if arr[i] != i + 1:
                return i + 1
        
        # If all elements are in their correct positions, return the next positive integer.
        return n + 1


#{ 
 # Driver Code Starts
#Initial Template for Python 3


import math


def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            print(ob.missingNumber(arr,n))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends