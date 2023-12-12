class Solution:
    ##Complete this function
    #Function to rearrange the array elements alternatively.
    def rearrange(self, arr, n):
        # Initialize pointers to the first and last elements.
        max_index = n - 1
        min_index = 0
        
        # Store the maximum element to be used later for dividing.
        max_element = arr[n - 1] + 1
        
        for i in range(n):
            # If the index is even, use the maximum element.
            if i % 2 == 0:
                arr[i] += (arr[max_index] % max_element) * max_element
                max_index -= 1
            # If the index is odd, use the minimum element.
            else:
                arr[i] += (arr[min_index] % max_element) * max_element
                min_index += 1
        
        # Update the array by dividing all elements by max_element.
        for i in range(n):
            arr[i] = arr[i] // max_element



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
            ob.rearrange(arr,n)
            
            for i in arr:
                print(i,end=" ")
            
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends