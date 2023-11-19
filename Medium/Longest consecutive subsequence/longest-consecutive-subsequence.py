class Solution:
    # Function to return the length of the longest subsequence of consecutive integers.
    def findLongestConseqSubseq(self, arr, N):
        # Create a set to store the elements of the array for efficient lookups.
        num_set = set(arr)
        
        max_length = 0

        # Iterate through the array to find the start of a subsequence.
        for num in arr:
            # If the current number is the start of a subsequence, expand the subsequence.
            if num - 1 not in num_set:
                current_num = num
                current_length = 1

                # Increment the current number until the end of the subsequence is reached.
                while current_num + 1 in num_set:
                    current_num += 1
                    current_length += 1

                # Update the maximum length if the current subsequence is longer.
                max_length = max(max_length, current_length)

        return max_length


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        n=int(input())
        a = list(map(int, input().strip().split()))
        print(Solution().findLongestConseqSubseq(a,n))
# } Driver Code Ends