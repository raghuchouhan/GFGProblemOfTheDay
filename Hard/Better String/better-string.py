#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
class Solution:
    def betterString(self, str1, str2):
        # Function to count distinct subsequences
        def countDistinctSubsequences(s):
            n = len(s)
            # Initialize an array to store the count of distinct subsequences
            dp = [0] * (n + 1)
            # An empty string has 1 distinct subsequence (empty subsequence)
            dp[0] = 1

            # Map to store the last occurrence of each character
            lastOccurrence = {}

            # Iterate through the string to fill the dp array
            for i in range(1, n + 1):
                dp[i] = 2 * dp[i - 1]  # Double the count from the previous character

                # If the current character has occurred before, subtract the count
                if s[i - 1] in lastOccurrence:
                    dp[i] -= dp[lastOccurrence[s[i - 1]] - 1]

                # Update the last occurrence of the current character
                lastOccurrence[s[i - 1]] = i

            return dp[n]

        # Get the counts of distinct subsequences for each string
        count1 = countDistinctSubsequences(str1)
        count2 = countDistinctSubsequences(str2)

        # Return the better string based on the counts
        return str1 if count1 >= count2 else str2

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        str1 = input()
        str2 = input()
        ob = Solution()
        res = ob.betterString(str1, str2)
        print(res)
# } Driver Code Ends