class Solution:
    def seriesSum(self, n):
        # Formula for the sum of the series: n * (n + 1) / 2
        return n * (n + 1) // 2
 


#{ 
 # Driver Code Starts
                               #Initial Template for Python 3


# Driver code 
if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        n=int(input())
        ob = Solution()
        ans = ob.seriesSum(n)
        print(ans)
        tc=tc-1
# } Driver Code Ends