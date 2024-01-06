class Solution:
    def maxLength(self, S):
        stack = [-1]  # Initialize stack with -1 to represent the base of the stack
        max_length = 0
        
        for i in range(len(S)):
            if S[i] == '(':
                stack.append(i)  # Push the index of opening parenthesis to the stack
            else:
                stack.pop()  # Pop the opening parenthesis from the stack
                
                if not stack:  # If stack becomes empty, push the current index to represent the new base
                    stack.append(i)
                else:
                    max_length = max(max_length, i - stack[-1])  # Calculate the length of valid substring
        
        return max_length



#{ 
 # Driver Code Starts
# Initial Template for Python3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S = input()
        
        ob = Solution()
        print(ob.maxLength(S))
# } Driver Code Ends