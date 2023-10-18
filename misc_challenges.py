class Challenges:
  """
  Reverse a string

  Last update: Oct. 2023

  Description:
  Challenge from the 
  Master the Coding Interview: Data Structures + Algorithms
  https://www.udemy.com/course/master-the-coding-interview-data-structures-algorithms/
  """
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
