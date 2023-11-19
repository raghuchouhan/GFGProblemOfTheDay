class Solution:
    def reverseWords(self, S):
        # Split the string into words using '.' as a separator
        words = S.split('.')
        
        # Reverse the list of words
        reversed_words = words[::-1]
        
        # Join the reversed words into a string using '.' as a separator
        result = '.'.join(reversed_words)
        
        return result 


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = str(input())
        obj = Solution()
        print(obj.reverseWords(s))

# } Driver Code Ends