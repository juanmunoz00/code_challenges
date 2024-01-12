from functools import reduce
import numpy as np
import random
from icecream import ic

from misc_challenges import Challenges
from tools import Tools
from linked_lists import Nodes

Challenges = Challenges()  # Create an instance of the Challenges class.
Tools = Tools()  # Create an instance of the Tools class.



runChallenge = Challenges.LINKED_LISTS

if runChallenge == Challenges.LINKED_LISTS:
  try:
    node1 = Nodes("3")
    node2 = Nodes("5")
    node3 = Nodes("7")
  
    #Link the lists
    node1.nextNode = node2
    node2.nextNode = node3
  
    #Print the list
    currentNode = node1
    while True:
      #print(f' { currentNode.value } ->')
      print( currentNode.value, end = ' -> ')
      if ( currentNode.nextNode == None ):
        print("None")
        break
        
      currentNode = currentNode.nextNode
      
  except Exception as e: print(e)

if runChallenge == Challenges.REMOVE_DISIMILAR_ELEMENTS:
  arr1 = [1,2,5,6] #exp: 0
  arr2 = [2,2,2,5,1,2] #exp: 2
  arr_3 = [3, 3, 3, 3, 3] #exp: 5
  arr_4 = [1, 2, 3, 4, 5, 6, 7, 8, 10, 10, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19] #exp: 10
  arr_5 = [1] #exp: 1
  arr_6 = [] #exp: 0
  arr = arr_3
  
  minimum_possible = Challenges.remove_disimilar_elements(arr)

  if minimum_possible == None: print('No minimum possible')
  ic(minimum_possible)

if runChallenge == Challenges.LEETCODE_2SUM_RECURSIVE:  
  nums = [2,7,11,15]
  target = 9
  i = 0
  output = Challenges.LEETCODE_2SUM_RECURSIVE(nums, target, i)
  ic(output)

if runChallenge == Challenges.LEETCODE_2SUM_BF:
  nums = [3,3]
  target = 6
  output_list = []
  twoSum = Challenges.LEETCODE_2SUM_BF(nums, target, output_list)
  ic( twoSum )

if ( runChallenge == Challenges.BASIC_GRAPH_TRAVERSE_USING_BFS ):
  adj_list = {
    "A":["B", "D"],
    "B":["A", "C"],
    "C":["B"],
    "D":["A", "E", "F"],
    "E":["D", "F", "G"],
    "F":["D", "E", "H"],
    "G":["E", "H"],
    "H":["G", "F"]
  }

  Tools.BFS(adj_list)

if ( runChallenge == Challenges.SOLVE_MAZE_WITH_BFS ):
  maze = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0]
  ]
  
  # Start and exit points
  start_point = (0, 0)
  exit_point = (4, 5)
  
  # Call BFS function
  Challenges.SolveMazeWithBFS(maze, start_point, exit_point)

"""
## THREESUMGRAPHTRAVERSE
if ( runChallenge == Challenges.THREESUMGRAPHTRAVERSE):
  start = True
  targetSum = 1
  numbers = [-1,0,1,2,-1,-4]
  print(f'{Challenges.ThreeSumGraphTraverse(start, targetSum, numbers)}')
"""

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


