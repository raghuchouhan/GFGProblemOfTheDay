class Solution:
    def countWays(self, n, exp):
        mod = 1003
        def f(i, j, isTrue, dp):
            if i > j:
                return 0
            if i == j:
                if isTrue == 1:
                    return int(exp[i] == 'T')
                else:
                    return int(exp[i] == 'F')
            if dp[i][j][isTrue] != -1:
                return dp[i][j][isTrue]
            ways = 0
            for ind in range(i + 1, j, 2):
                lT = f(i, ind - 1, 1, dp)
                lF = f(i, ind - 1, 0, dp)
                rT = f(ind + 1, j, 1, dp)
                rF = f(ind + 1, j, 0, dp)
                if exp[ind] == '&':
                    if isTrue:
                        ways = (ways + (lT * rT) % mod) % mod
                    else:
                        ways = (ways + (lF * rT) % mod + (lT * rF) % mod + (lF * rF) % mod) % mod
                elif exp[ind] == '|':
                    if isTrue:
                        ways = (ways + (lF * rT) % mod + (lT * rF) % mod + (lT * rT) % mod) % mod
                    else:
                        ways = (ways + (lF * rF) % mod) % mod
                else:
                    if isTrue:
                        ways = (ways + (lF * rT) % mod + (lT * rF) % mod) % mod
                    else:
                        ways = (ways + (lF * rF) % mod + (lT * rT) % mod) % mod
            dp[i][j][isTrue] = ways
            return ways
        dp = [[[ -1 for _ in range(2)] for _ in range(n)] for _ in range(n)]
        return f(0, n - 1, 1, dp)



#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        S = input()
        
        ob = Solution()
        print(ob.countWays(N, S))
# } Driver Code Ends