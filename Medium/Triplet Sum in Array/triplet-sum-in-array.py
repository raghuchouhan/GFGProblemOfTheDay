class Solution:
    
    # Function to find if there exists a triplet in the array A[] which sums up to X.
    def find3Numbers(self, A, n, X):
        # Sorting the array to use the two-pointer approach.
        A.sort()

        # Fixing one element and using two pointers to find the other two elements.
        for i in range(n - 2):
            left, right = i + 1, n - 1

            while left < right:
                current_sum = A[i] + A[left] + A[right]

                # If the sum is equal to X, return True.
                if current_sum == X:
                    return True
                # If the sum is less than X, move the left pointer to the right.
                elif current_sum < X:
                    left += 1
                # If the sum is greater than X, move the right pointer to the left.
                else:
                    right -= 1

        # If no triplet is found, return False.
        return False


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
        n,X=map(int,input().strip().split())
        A=list(map(int,input().strip().split()))
        ob=Solution()
        if(ob.find3Numbers(A,n,X)):
            print(1)
        else:
            print(0)
# } Driver Code Ends