class Solution:
    def simpleInterest(self, P, R, T):
        # Simple Interest formula: SI = (P * R * T) / 100
        SI = (P * R * T) / 100
        return SI




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        P,R,T=map(int,input().strip().split(' '))
        ob=Solution()
        print('%.2f'%ob.simpleInterest(P,R,T))
# } Driver Code Ends