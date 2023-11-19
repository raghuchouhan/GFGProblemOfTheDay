class Solution:
    def isPalindrome(self, S):
        # Removing spaces and converting to lowercase for case-insensitivity.
        S = S.replace(" ", "").lower()

        # Using two pointers to check if the string is a palindrome.
        left, right = 0, len(S) - 1

        while left < right:
            if S[left] != S[right]:
                return 0  # Not a palindrome
            left += 1
            right -= 1

        return 1  # Palindrome


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		S = input()
		ob = Solution()
		answer = ob.isPalindrome(S)
		print(answer)

# } Driver Code Ends