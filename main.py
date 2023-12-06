from functools import reduce
import numpy as np
import random

from misc_challenges import Challenges
from tools import Tools

Challenges = Challenges()  # Create an instance of the Challenges class.

runChallenge = Challenges.DY_PO_RECURSIVE_FIBONACCI

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
  number = random.randint(2,3000)
  # Iterative
  #Challenges.Iterative_or_Recursive(Challenges.FACTORIAL_SEQUENCE, Challenges.USE_ITERATIVE, number)
  #Challenges.Iterative_or_Recursive(Challenges.FACTORIAL_SEQUENCE, Challenges.USE_RECURSSION, number)

  # Recursive
  #Challenges.Iterative_or_Recursive(Challenges.FIBONACCI_SEQUENCE, Challenges.USE_ITERATIVE, number)
  Challenges.Iterative_or_Recursive(Challenges.FIBONACCI_SEQUENCE, Challenges.USE_RECURSSION, number)

if ( runChallenge == Challenges.QUICK_SORT ):
  #numList = [0,9,3,8,2,7,5]
  numList = [random.randint(0,9) for i in range(5)]
  if( len(numList) > 4 ):
    listSize = len(numList)
    pivotNumber = numList[listSize - 1]
    Challenges.Quick_Sort(numList, leftPivotNumber = 0, rightPivotNumber = pivotNumber, iteration_stop=10)
  else:
    print(f'The length of the numbers list must be greater than 5')

if ( runChallenge == Challenges.LEETCODE_3SUM ):
  #nums = [-1,0,1,2,-1,-4]
  nums = [0,0,0]
  Challenges.Solved_3Sum(nums)

if ( runChallenge == Challenges.DYNAMIC_PROGRAMMIG_1 ): 
  nums = []
  for n in range(10):
    nums.append(random.randint(3,9))

  Challenges.MemoizedAddTo80(nums)

if ( runChallenge == Challenges.DY_PO_RECURSIVE_FIBONACCI ):  
  #n = 6 # 8  
  n = 7  # 13
  """
  n = 8  # 21
  n = 50 # 12586269025
  """
  print(f'Fibonacci of {n} is: {Challenges.DyPo_Fib(n)}')