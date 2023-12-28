class Solution:
    def palindromicPartition(self, string):
        n = len(string)
        
        # Function to check if a substring is a palindrome
        def is_palindrome(s, start, end):
            return s[start:end + 1] == s[start:end + 1][::-1]
        
        # Initialize a table to store minimum cuts
        min_cuts = [float('inf')] * n
        
        for i in range(n):
            for j in range(i, -1, -1):
                if is_palindrome(string, j, i):
                    if j == 0:
                        min_cuts[i] = 0
                    else:
                        min_cuts[i] = min(min_cuts[i], min_cuts[j - 1] + 1)
                        
        return min_cuts[n - 1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        string = input()
        
        ob = Solution()
        print(ob.palindromicPartition(string))
# } Driver Code Ends