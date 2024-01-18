#User function Template for python3

class Solution:
    def commonElements (self,A, B, C, n1, n2, n3):
        # your code here
        set_1 = set(A)
        set_2 = set(B)
        set_3 = set(C)
        com_ele_set_1 = set_1.intersection(set_2)
        com_ele_set_final = com_ele_set_1.intersection(set_3)
        com_list = list(com_ele_set_final)
        com_list.sort()
        return com_list


#{ 
 # Driver Code Starts
#Initial Template for Python 3


t = int (input ())
for tc in range (t):
    n1, n2, n3 = list(map(int,input().split()))
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    C = list(map(int,input().split()))
    
    ob = Solution()
    
    res = ob.commonElements (A, B, C, n1, n2, n3)
    
    if len (res) == 0:
        print (-1)
    else:
        for i in range (len (res)):
            print (res[i], end=" ")
        print ()

# } Driver Code Ends