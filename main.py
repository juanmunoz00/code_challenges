from functools import reduce
import numpy as np
import random

from misc_challenges import Challenges
from tools import Tools

Challenges = Challenges()  # Create an instance of the Challenges class.

runChallenge = Challenges.QUICK_SORT

if (runChallenge == Challenges.REVERSE_STRING):
  ## Reverse a string
  #list1 = ['1','2','3'] #For testing purposes
  hiMyName = "Hi my name is Juan"
  Challenges.Reverse_String(hiMyName)

if ( runChallenge == Challenges.MERGED_SORTED_ARRAY ):
  ## Merge two sorted arrays into one sorted array.
  list1 = [0,3,4,31]
  list2 = [4,6,30]
  Challenges.Merge_Sorted_Arrays(list1, list2)

if ( runChallenge == Challenges.FIND_RECURRING_CHARACTER ):
  # Generates a 10-elements list of random integers between 20 and 40 as the input list.
  num = 10
  start = 20
  end = 40
  list1 = reduce(lambda acc, x: acc + [np.random.randint(start, end)], range(num), [])
  
  Challenges.Find_Recurring_Character(list1)

if ( runChallenge == Challenges.FACTORIAL_OF_A_NUMBER):
  #USE_FACTORIAL_WITH_LOOPS
  #USE_FACTORIAL_WITH_RECURSSION
  number = random.randint(2,20)
  # Iterative
  #Challenges.Iterative_or_Recursive(Challenges.FACTORIAL_SEQUENCE, Challenges.USE_ITERATIVE, number)
  #Challenges.Iterative_or_Recursive(Challenges.FACTORIAL_SEQUENCE, Challenges.USE_RECURSSION, number)

  # Recursive
  #Challenges.Iterative_or_Recursive(Challenges.FIBONACCI_SEQUENCE, Challenges.USE_ITERATIVE, number)
  Challenges.Iterative_or_Recursive(Challenges.FIBONACCI_SEQUENCE, Challenges.USE_RECURSSION, number)


if ( runChallenge == Challenges.QUICK_SORT ):
  numList = [0,9,3,8,2,7,5]
  if( len(numList) > 5 ):
    listSize = len(numList)
    pivotNumber = numList[listSize - 1]
    Challenges.Quick_Sort(numList, pivotNumber, iteration=1)
  else:
    print(f'The length of the numbers list must be greater than 5')