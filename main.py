from functools import reduce
import numpy as np
import random

from misc_challenges import Challenges
from tools import Tools

Challenges = Challenges()  # Create an instance of the Challenges class.

runChallenge = Challenges.HOW_SUM
## HOW_SUM
if ( runChallenge == Challenges.HOW_SUM ):
  """
  m = target sum
  n = number of elements

  Brute Force:
    time: O(n^m * m)
    space: O(m)

  Memoized:
    time: O(n*m^2)
    space: O(m^2)
  """
  numbers = [7,14]#[2,3,5]#[2,4]#[5,3,4,7]
  targetSum = 300#8#7

  if( Challenges.howSum(targetSum, numbers) == None ):
    print(f'No solution found for {targetSum} using {numbers}')
  else:
    print(f'The number: {targetSum} can be added with { Challenges.howSum(targetSum, numbers) } in numbers: {numbers} ')

## CAN_SUM
if ( runChallenge == Challenges.CAN_SUM ):
  numbers = [7,14]#[2,4]#[2,3]#[5,3,4,7]
  targetSum = 300#7
  print(f'Can sum: {targetSum} with numbers: {numbers}? = { Challenges.canSum(targetSum, numbers) }')

## GRID_TRAVELER
if ( runChallenge == Challenges.GRID_TRAVELER ):
  # returns 1
  #m = 1
  #n = 1

  # returns 3
  #m = 2
  #n = 3

  # returns 3
  #m = 3
  #n = 2

  # returns 6
  #m = 3
  #n = 3

  # returns 2333606220
  m = 18
  n = 18
  
  print(f'{ Challenges.Grid_Traveler(m, n) }')

## DY_PO_RECURSIVE_FIBONACCI
if ( runChallenge == Challenges.DY_PO_RECURSIVE_FIBONACCI ):  
  """
  n = 6 # 8  

  n = 7  # 13  
  n = 8  # 21

  n = 50 # 12586269025
  """
  #n = 20 # 6765
  n = 50 # 12586269025
  print(f'Fibonacci of {n} is: {Challenges.DyPo_Fib(n)}')

## DYNAMIC_PROGRAMMIG_1
if ( runChallenge == Challenges.DYNAMIC_PROGRAMMIG_1 ): 
  nums = []
  for n in range(10):
    nums.append(random.randint(3,9))

  Challenges.MemoizedAddTo80(nums)

## LEETCODE_3SUM
if ( runChallenge == Challenges.LEETCODE_3SUM ):
  #nums = [-1,0,1,2,-1,-4]
  nums = [0,0,0]
  Challenges.Solved_3Sum(nums)

## QUICK_SORT
if ( runChallenge == Challenges.QUICK_SORT ):
  #numList = [0,9,3,8,2,7,5]
  numList = [random.randint(0,9) for i in range(5)]
  if( len(numList) > 4 ):
    listSize = len(numList)
    pivotNumber = numList[listSize - 1]
    Challenges.Quick_Sort(numList, leftPivotNumber = 0, rightPivotNumber = pivotNumber, iteration_stop=10)
  else:
    print(f'The length of the numbers list must be greater than 5')

## FACTORIAL_OF_A_NUMBER
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

## FIND_RECURRING_CHARACTER
if ( runChallenge == Challenges.FIND_RECURRING_CHARACTER ):
  # Generates a 10-elements list of random integers between 20 and 40 as the input list.
  num = 10
  start = 20
  end = 40
  list1 = reduce(lambda acc, x: acc + [np.random.randint(start, end)], range(num), [])

  Challenges.Find_Recurring_Character(list1)

## MERGED_SORTED_ARRAY
if ( runChallenge == Challenges.MERGED_SORTED_ARRAY ):
  ## Merge two sorted arrays into one sorted array.
  list1 = [0,3,4,31]
  list2 = [4,6,30]
  Challenges.Merge_Sorted_Arrays(list1, list2)

## REVERSE_STRING
if (runChallenge == Challenges.REVERSE_STRING):
  ## Reverse a string
  #list1 = ['1','2','3'] #For testing purposes
  hiMyName = "Hi my name is Juan"
  Challenges.Reverse_String(hiMyName)


