
class Solution:
    def nthFibonacci(self, n: int) -> int:
        # Base cases for n = 0 and n = 1
        if n == 0:
            return 0
        elif n == 1:
            return 1
        
        # Initialize an array to store Fibonacci numbers
        fib = [0] * (n + 1)
        
        # Base values
        fib[0] = 0
        fib[1] = 1

        # Calculate Fibonacci numbers up to n using dynamic programming
        for i in range(2, n + 1):
            fib[i] = (fib[i - 1] + fib[i - 2]) % 1000000007
        
        # Return the nth Fibonacci number
        return fib[n]
        



#{ 
 # Driver Code Starts
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        obj = Solution()
        res = obj.nthFibonacci(n)
        
        print(res)
        

# } Driver Code Ends