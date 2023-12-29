#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys
import heapq
from collections import  defaultdict
import math


# } Driver Code Ends
from heapq import heappush, heappop

class Solution:
    def __init__(self):
        # Two heaps to maintain the lower and upper halves of the stream
        self.min_heap = []  # Min heap for upper half
        self.max_heap = []  # Max heap for lower half

    def balanceHeaps(self):
        # Balance the two heaps size, such that the difference is not more than one
        if len(self.min_heap) > len(self.max_heap) + 1:
            heappush(self.max_heap, -heappop(self.min_heap))
        elif len(self.max_heap) > len(self.min_heap):
            heappush(self.min_heap, -heappop(self.max_heap))

    def getMedian(self):
        # Return the median of the data received till now
        if len(self.min_heap) == len(self.max_heap):
            return (self.min_heap[0] - self.max_heap[0]) / 2
        else:
            return float(self.min_heap[0])

    def insertHeaps(self, x):
        # Insert value into the heap and balance the heaps
        if not self.max_heap or x <= -self.max_heap[0]:
            heappush(self.max_heap, -x)
        else:
            heappush(self.min_heap, x)
        self.balanceHeaps()

#{ 
 # Driver Code Starts.

if __name__ == '__main__':
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        ob=Solution()
        for i in range(n):
            x=int(input())
            ob.insertHeaps(x)
            print(math.floor(ob.getMedian()))

# } Driver Code Ends