class Solution:
    
    # Function to check whether two strings are anagrams of each other or not.
    def isAnagram(self, a, b):
        # If lengths of the strings are different, they can't be anagrams.
        if len(a) != len(b):
            return False

        # Using dictionaries to count the frequency of characters in both strings.
        count_a = {}
        count_b = {}

        # Count the frequency of characters in string a.
        for char in a:
            count_a[char] = count_a.get(char, 0) + 1

        # Count the frequency of characters in string b.
        for char in b:
            count_b[char] = count_b.get(char, 0) + 1

        # Compare the counts of characters in both dictionaries.
        return count_a == count_b


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        a,b=map(str,input().strip().split())
        if(Solution().isAnagram(a,b)):
            print("YES")
        else:
            print("NO") 
# } Driver Code Ends