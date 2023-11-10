class Solution:
    def printMinNumberForPattern(self, S):
        result = ""
        next_num = 1
        stack = []

        for char in S:
            if char == 'I':
                stack.append(next_num)
                next_num += 1
                while stack:
                    result += str(stack.pop())
            else:
                stack.append(next_num)
                next_num += 1
        
        stack.append(next_num)
        while stack:
            result += str(stack.pop())

        return result


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        S=str(input())

        ob = Solution()
        print(ob.printMinNumberForPattern(S))
# } Driver Code Ends