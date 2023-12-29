class Solution:
    def maxLen(self, n, arr):
        # Initialize a HashMap to store the running sum and its index.
        sum_map = {}
        max_length = 0
        current_sum = 0

        for i in range(n):
            # Add the current element to the running sum.
            current_sum += arr[i]

            # Check if the current sum is 0.
            if current_sum == 0:
                max_length = i + 1

            # If the current sum is already in the HashMap, update the max_length.
            if current_sum in sum_map:
                max_length = max(max_length, i - sum_map[current_sum])
            else:
                # Store the current sum along with its index in the HashMap.
                sum_map[current_sum] = i

        return max_length





#{ 
 # Driver Code Starts
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxLen(n ,arr))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends