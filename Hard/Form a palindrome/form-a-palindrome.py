class Solution:
    def countMin(self, Str):
        n = len(Str)
        dp = [[0] * n for _ in range(n)]

        for gap in range(1, n):
            for i in range(n - gap):
                j = i + gap
                if Str[i] == Str[j]:
                    dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = min(dp[i+1][j], dp[i][j-1]) + 1

        return dp[0][n-1]



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        Str = input()
        

        solObj = Solution()

        print(solObj.countMin(Str))
# } Driver Code Ends