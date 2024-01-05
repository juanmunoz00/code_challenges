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

      ic(visited)
      ic(parent)
      ic(level)
      

    
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