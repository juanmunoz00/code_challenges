from functools import reduce
import numpy as np
import random

from misc_challenges import Challenges
from tools import Tools

Challenges = Challenges()  # Create an instance of the Challenges class.

runChallenge = Challenges.FACTORIAL_OF_A_NUMBER

if (runChallenge == 1):
  ## Reverse a string
  #list1 = ['1','2','3'] #For testing purposes
  hiMyName = "Hi my name is Juan"
  Challenges.Reverse_String(hiMyName)

if ( runChallenge == 2 ):
  ## Merge two sorted arrays into one sorted array.
  list1 = [0,3,4,31]
  list2 = [4,6,30]
  Challenges.Merge_Sorted_Arrays(list1, list2)

if ( runChallenge == 3 ):
  # Generates a 10-elements list of random integers between 20 and 40 as the input list.
  num = 10
  start = 20
  end = 40
  list1 = reduce(lambda acc, x: acc + [np.random.randint(start, end)], range(num), [])
  
  Challenges.Find_Recurring_Character(list1)


if ( runChallenge == 4 ):
  Challenges.Factorial_Of_A_Number(random.randint(0,9), int(Challenges.USE_FACTORIAL_WITH_LOOPS))
  #Challenges.Factorial_Of_A_Number(6, Challenges.Factorial_With_Recurssion)