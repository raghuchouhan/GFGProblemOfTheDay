from typing import List
from queue import Queue

class Solution:
    # Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        # Initializing a list to store the BFS traversal.
        bfs_result = []

        # Creating a boolean array to mark visited nodes.
        visited = [False] * V

        # Initializing a queue for BFS traversal.
        queue = Queue()

        # Starting BFS from the 0th vertex.
        queue.put(0)
        visited[0] = True

        # BFS traversal loop.
        while not queue.empty():
            # Getting the front element from the queue.
            u = queue.get()
            bfs_result.append(u)

            # Exploring the adjacent vertices.
            for v in adj[u]:
                if not visited[v]:
                    queue.put(v)
                    visited[v] = True

        return bfs_result


#{ 
 # Driver Code Starts


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
		ob = Solution()
		ans = ob.bfsOfGraph(V, adj)
		for i in range(len(ans)):
		    print(ans[i], end = " ")
		print()
        

# } Driver Code Ends