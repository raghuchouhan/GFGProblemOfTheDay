#User function Template for python3
class Pair:
    def __init__(self, val, ind):
        self.val = val
        self.ind = ind
#User function Template for python3
class Solution:
    
    #we are sorting in descending order
    def merge(self, arr, left, mid, right, res):
        i = left
        j = mid+1
        temp = []
        
        while (i <= mid) and (j <= right):
            if arr[i].val > arr[j].val:
                temp.append(arr[i])
                #main logic for increase count
                res[arr[i].ind] += (right-j+1)
                i += 1
            else:
                temp.append(arr[j])
                j += 1
        
        while i <= mid:
            temp.append(arr[i])
            i+=1
        
        while j <= right:
            temp.append(arr[j])
            j+= 1
        
        k = 0
        for i in range(left, right+1):
            arr[i] = temp[k]
            k += 1
        
    
    def merge_sort(self, arr, left, right, res):
        if left < right:
            mid = (left+right)//2
            self.merge_sort(arr, left, mid, res)
            self.merge_sort(arr, mid+1, right, res)
            self.merge(arr, left, mid, right, res)
            

	def constructLowerArray(self,arr, n):
		# code here
		if not arr:
		    return []
		
		res = [0]*n
		arr2 = []
		for ind, ele in enumerate(arr):
		    arr2.append(Pair(ele, ind))
		    
		self.merge_sort(arr2, 0, n-1, res)
		return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.constructLowerArray(arr, n)
        for x in ans:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends