class Solution:
    # Function to return the count of number of elements in the union of two arrays.
    def doUnion(self, a, n, b, m):
        # Creating sets from arrays to get distinct elements.
        set_a = set(a)
        set_b = set(b)

        # Taking the union of the sets and returning the count.
        union_set = set_a.union(set_b)
        return len(union_set)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        
        n,m=[int(x) for x in input().strip().split()]
        
        a=[int(x) for x in input().strip().split()]
        b=[int(x) for x in input().strip().split()]
        ob=Solution()
        
        print(ob.doUnion(a,n,b,m))
# } Driver Code Ends