class Solution:
    # Function to find triplets with zero sum.
    def findTriplets(self, arr, n):
        # Sorting the array for efficient solution
        arr.sort()
        # Fixing one element and finding other two using two pointers approach
        for i in range(n-2):
            left, right = i + 1, n - 1
            while left < right:
                curr_sum = arr[i] + arr[left] + arr[right]
                # If triplet with zero sum is found, return 1
                if curr_sum == 0:
                    return 1
                # If sum is less than zero, move left pointer to the right
                elif curr_sum < 0:
                    left += 1
                # If sum is greater than zero, move right pointer to the left
                else:
                    right -= 1
        # If no triplet is found, return 0
        return 0


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

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n=int(input())
        a=list(map(int,input().strip().split()))
        if(Solution().findTriplets(a,n)):
            print(1)
        else:
            print(0)
# } Driver Code Ends