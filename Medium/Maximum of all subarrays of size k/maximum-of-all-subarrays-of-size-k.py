from collections import deque

class Solution:
    def max_of_subarrays(self, arr, n, k):
        result = []
        dq = deque()

        for i in range(n):
            # Remove elements that are out of the current window
            while dq and dq[0] < i - k + 1:
                dq.popleft()

            # Remove elements that are smaller than the current element
            while dq and arr[dq[-1]] < arr[i]:
                dq.pop()

            # Add the current element index to the deque
            dq.append(i)

            # Add the maximum of the current window to the result
            if i >= k - 1:
                result.append(arr[dq[0]])

        return result


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys
from collections import deque

#Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,k = map(int,input().strip().split())
        arr = list(map(int,input().strip().split()))
        ob=Solution()
        res = ob.max_of_subarrays(arr,n,k)
        for i in range (len (res)):
            print (res[i], end = " ")
        print()
# } Driver Code Ends