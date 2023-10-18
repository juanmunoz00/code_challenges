from tools import Tools

Tools = Tools() # Create an instance of the Tools class
class Challenges:
  def Reverse_String(self, string):
    reversed_string = Tools.reverse_string(string)  # Call the method on the instance
    print(reversed_string)  # Print the result