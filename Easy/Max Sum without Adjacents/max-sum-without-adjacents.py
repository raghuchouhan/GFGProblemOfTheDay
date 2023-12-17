class Solution:
	
	def findMaxSum(self, arr, n):
	    # Base cases
	    if n == 0:
	        return 0
	    if n == 1:
	        return arr[0]
	    
	    # Initialize the first and second values.
	    incl = arr[0]
	    excl = 0
	    
	    # Iterate through the array to find the maximum sum.
	    for i in range(1, n):
	        # Calculate the current inclusive sum.
	        new_incl = excl + arr[i]
	        
	        # Update inclusive and exclusive sums for the next iteration.
	        excl = max(incl, excl)
	        incl = new_incl
	    
	    # Return the maximum of the last inclusive and exclusive sums.
	    return max(incl, excl)



#{ 
 # Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMaxSum(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends