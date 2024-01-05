from icecream import ic
from collections import deque
from queue import Queue

class Tools:
  # Based on YT tutorial 2.1 BFS: Breadth First Search Implementation in Python | Graph Data Structure of Apr 6, 2020
  def BFS(self, adj_list):

    try:
      visited = {} #visited nodes
      level = {} #distance
      parent = {} #to keep the minimum distance
      bfs_traversal_output = []
      queue = Queue() #queue for BFS

      #initialze
      for node in adj_list.keys():
        visited[node] = False
        parent[node] = None
        level[node] = -1

      #source node
      s = "A"
      visited[s] = True
      level[s] = 0
      queue.put(s)

      """
      ic(visited)
      ic(parent)
      ic(level)
      ic(queue)
      """

      # Loop until the queue is empty
      while not queue.empty():
        u = queue.get() # The next-first element in the queue which represent a vertex
        bfs_traversal_output.append(u) # How the graph has been traversed

        for v in adj_list[u]: # Iterate through all the adjacent vertices of the current vertex
          # Check if the adjacent vertex has not been visited. If not, mark it as visited and enqueue it.
          if not visited[v]:
            visited[v] = True
            parent[v] = u # u is the node that was obtained from the queue that has not been visited.
            level[v] = level[u] + 1 # The distance between the source node and the adjacent node.
            queue.put(v) # v will now be added to the queue so it can be traversed.
        
      ic(bfs_traversal_output)
    
    except Exception as e: print(e)

  
  def reverse_string(self, string):
    if not isinstance(string, str):
      return "Input is not a string"
    # Create an empty list named reversed. The list will be used to store the characters of the input string in reverse order.
    reversed = []
  
    # The loop iterates over a range of numbers, starting from the length of the string minus one (the last index) and ending at -1. The -1 as the step size means that it will decrement the index with each iteration, effectively moving backward through the string.
  
    for i in range(len(string) - 1, -1, -1):      
      # Each character of the input string is accessed by its index (starting from the end of the string), and it is added to the reversed list.
      reversed.append(string[i])
  
    # The reversed list is converted to a string and returned.
    return "".join(reversed)