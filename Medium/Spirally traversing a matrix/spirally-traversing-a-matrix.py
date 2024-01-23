#User function Template for python3

class Solution:
    def spirallyTraverse(self,mat, r, c): 
        
        top = 0
        left = 0
        right = c-1
        bottom = r-1
        res = []
        
        while left <= right and top <= bottom:#todo condition
            #first row
            for i in range(left, right+1):
                res.append(mat[top][i])
            top +=1
            
            #right row
            for i in range(top, bottom+1):
                res.append(mat[i][right])
            right -= 1
            
            #botom row
            if top <= bottom:
                for i in range(right, left-1, -1):
                    res.append(mat[bottom][i])
                bottom -= 1
            
            # left row
            if left <= right:
                for i in range(bottom, top-1, -1):
                    res.append(mat[i][left])
                left += 1
        
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        r,c = map(int, input().strip().split())
        values = list(map(int, input().strip().split()))
        k = 0
        matrix =[]
        for i in range(r):
            row=[]
            for j in range(c):
                row.append(values[k])
                k+=1
            matrix.append(row)
        obj = Solution()
        ans = obj.spirallyTraverse(matrix,r,c)
        for i in ans:
            print(i,end=" ")
        print()

# } Driver Code Ends