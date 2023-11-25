class Solution:
    def shuffleArray(self, arr, n):
        mid = n // 2
        i, j = 1, mid

        while j < n:
            arr.insert(i, arr.pop(j))
            i += 2
            j += 1



#{ 
 # Driver Code Starts
if __name__ == '__main__': 
    
    t=int(input())
    for _ in range(0,t):
        n=int(input())
        a = list(map(int,input().split()))
        ob = Solution()
        ob.shuffleArray(a,n)
        print(*a)
# } Driver Code Ends