class Solution:
    def nCr(self, n, r):
        MOD = 1000000007
        
        # Function to calculate n! modulo MOD
        def factorial(n):
            result = 1
            for i in range(1, n + 1):
                result = (result * i) % MOD
            return result

        # Function to calculate modular inverse using Fermat's Little Theorem
        def modInverse(x):
            return pow(x, MOD - 2, MOD)

        # Function to calculate nCr modulo MOD using Lucas Theorem
        def lucas(n, r):
            if r == 0:
                return 1
            ni = n % MOD
            ri = r % MOD
            return (lucas(n // MOD, r // MOD) * factorial(ni) * modInverse(factorial(ri)) * modInverse(factorial(ni - ri))) % MOD

        if r > n:
            return 0

        return lucas(n, r)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, r = [int(x) for x in input().split()]
        
        ob = Solution()
        print(ob.nCr(n, r))
# } Driver Code Ends