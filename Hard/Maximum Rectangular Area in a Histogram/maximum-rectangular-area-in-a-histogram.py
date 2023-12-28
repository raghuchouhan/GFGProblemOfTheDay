class Solution:
    # Function to find largest rectangular area possible in a given histogram.
    def getMaxArea(self, histogram):
        n = len(histogram)
        stack = []
        max_area = 0
        i = 0

        while i < n:
            if not stack or histogram[i] >= histogram[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                top = stack.pop()
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, histogram[top] * width)

        while stack:
            top = stack.pop()
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, histogram[top] * width)

        return max_area


#{ 
 # Driver Code Starts
#Initial Template for Python 3

# by Jinay Shah 

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        a = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.getMaxArea(a))
# } Driver Code Ends