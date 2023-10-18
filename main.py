from misc_challenges import Challenges
from tools import Tools

Challenges = Challenges()  # Create an instance of the Challenges class

runChallenge = 2

if (runChallenge == 1):
  ## Reverse a string
  #list1 = ['1','2','3'] #For testing purposes
  hiMyName = "Hi my name is Juan"
  Challenges.Reverse_String(hiMyName)

if ( runChallenge == 2 ):
  ## Merge two sorted arrays
  list1 = [0,3,4,31]
  list2 = [4,6,30]
  Challenges.Merge_Sorted_Arrays(list1, list2)
