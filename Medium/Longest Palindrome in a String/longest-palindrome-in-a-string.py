class Solution:
    def longestPalin(self, S):
        start = 0
        max_length = 1
        
        for i in range(1, len(S)):
            # Check for odd length palindrome
            low = i - 1
            high = i + 1
            while low >= 0 and high < len(S) and S[low] == S[high]:
                if high - low + 1 > max_length:
                    start = low
                    max_length = high - low + 1
                low -= 1
                high += 1
            
            # Check for even length palindrome
            low = i - 1
            high = i
            while low >= 0 and high < len(S) and S[low] == S[high]:
                if high - low + 1 > max_length:
                    start = low
                    max_length = high - low + 1
                low -= 1
                high += 1
        
        return S[start:start + max_length]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()

        ob = Solution()

        ans = ob.longestPalin(S)

        print(ans)
# } Driver Code Ends