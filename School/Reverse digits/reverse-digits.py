class Solution:
    def reverse_digit(self, n):
        # Convert the number to a string, reverse it, and convert it back to an integer
        reversed_number = int(str(n)[::-1])
        return reversed_number



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.reverse_digit(n)
		print(ans)
# } Driver Code Ends