from tools import Tools

Tools = Tools() # Create an instance of the Tools class
class Challenges:
  """
  Reverse a string

  Last update: Oct. 2023

  Description:
  Challenge from the 
  Master the Coding Interview: Data Structures + Algorithms
  https://www.udemy.com/course/master-the-coding-interview-data-structures-algorithms/
  """
  def Reverse_String(self, string):
    reversed_string = Tools.reverse_string(string)  # Call the method on the instance
    print(reversed_string)  # Print the result