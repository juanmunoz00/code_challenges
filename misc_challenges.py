from tools import Tools
from datetime import datetime
import math

Tools = Tools() # Create an instance of the Tools class

class Challenges:
  REVERSE_STRING = 1
  MERGED_SORTED_ARRAY = 2
  FIND_RECURRING_CHARACTER = 3
  FACTORIAL_OF_A_NUMBER = 4
  QUICK_SORT = 5
  MERGE_SORT = 6
  INSERT_SORT = 7
  LEETCODE_3SUM = 8
  DYNAMIC_PROGRAMMIG_1 = 9
  DY_PO_RECURSIVE_FIBONACCI = 10
  GRID_TRAVELER = 11
  CAN_SUM = 12
  HOW_SUM = 13
  
  USE_ITERATIVE = 1
  USE_RECURSSION = 2

  FACTORIAL_SEQUENCE = 1
  FIBONACCI_SEQUENCE = 2   
  
  ## Methods
  ## howSum
  """
  A funtion that returns an array of combinations that add up to a targetSum
  """
  def howSum(self, targetSum, numbers, memo = {}):
    try:
      if ( targetSum in memo ): return memo[targetSum]
      if (targetSum == 0): return []
      if (targetSum < 0): return None

      for n in numbers:
        remainder = targetSum - n
        reminderResult = self.howSum(remainder, numbers, memo)
        if ( reminderResult != None ):
          memo[targetSum] = [reminderResult, n]
          return memo[targetSum]
      
      memo[targetSum] = None
      return memo[targetSum]
    except Exception as e: 
      print(e)
      return False
  ## canSum
  """
  A function that returns a boolean indicating whether or not it is possible to generate the targetSum
  using numbers from the array.
  """
  def canSum(self, targetSum, numbers, memo = {}):
    try:
      if ( targetSum in memo ): return memo[targetSum]
      if (targetSum == 0): return True
      if (targetSum < 0): return False

      for n in numbers:
        remainder = targetSum - n
        if ( self.canSum(remainder, numbers, memo) == True ): 
          memo[targetSum] = True
          return True
 
      memo[targetSum] = False
      return False
    except Exception as e: 
      print(e)
      return False

  
  ## Grid Traverse
  ## How many ways are to reach from top left corner to bottom right corner
  def Grid_Traveler(self, m, n, memo = {}):
    try:
      key = str(m) + ',' + str(n)
      # Base cases
      if ( key in memo ): return memo[key]
      if (m == 1 and n == 1): return 1
      if (m == 0 or n == 0): return 0

      # Recursive case
      travel = self.Grid_Traveler(m - 1, n, memo) + self.Grid_Traveler(m, n-1, memo)
      memo[key] = travel
      return travel   

    except Exception as e: print(e)


  
  ## Fib2 - Another approach to Fibbonacci using recursion
  def DyPo_Fib(self, n, memo = {}):
    try:
      #print(f'({n})')
      if n in memo:
        return memo[n]
        
      if ( n <= 2 ): return 1
      
      fib = self.DyPo_Fib(n - 1, memo) + self.DyPo_Fib(n - 2, memo)  
      memo[n] = fib
      
      #print (f'Fib({n}) = {fib}') 
      return fib
      
    except Exception as e: print(e)
  
  def MemoizedAddTo80(self, nums):
    try:
      cache = {}
      for n in nums:
        if ( n in cache ):
          print(f'{n} is in cache')
        else:
          result = n + 80
          cache[n] = result
          print(f'{n} added to cache')
        
    except Exception as e: print(e)
  
  def Solved_3Sum(self, nums):    
    try:
      #List size.
      listSize = len(nums)
      
      # Initialize the indexes.
      i = 0
      # Initialize the lists
      triplets = []
      tripletsSum = []

      if ( sum(nums) == 0):
        triplets = nums
          
      else:
      
        # Set a fixed number (index) that will be swaped through the list until i = len - 2.
        while ( i < listSize - 2 ):
          j = i + 1
          k = j + 1        
          
          fixedNum = nums[i]
          #print(f'***** {fixedNum} *****')
          #print(f'j: {j}')
          #print(f'k: {k}')
          
          # Take the next 2 numbers (indexes) right of i and sum them. 
          # Add them to a list if the sum is equal to zero.        
          while ( ( j <= listSize - 2  ) and ( k <= listSize - 1 ) ):
            #print(f'######')          
            jValue = nums[j]
            kValue = nums[k]
            
            #print(f'j-index:[{j}] | j-value: {jValue}')
            #print(f'k-index:[{k}] | k-jalue: {kValue}')
            
            if( (fixedNum + jValue + kValue) == 0 ):
              tripletsSum = [fixedNum, jValue, kValue]
              triplets.append(tripletsSum)
              #print(f'Triplet: {triplets}')
            
            j += 1
            k = j+1
          
          i += 1
          #print(f'\nTriplets: {triplets}')
          
        
      print(triplets)
      #print(f'... and that is it !!!')
          
    except Exception as e: print(e)
  
  ## SortHalfList
  def Sort_Half_List(self, list, pivotNumber):
    try:
      leftSortedList = []
      rightSortedList = []

      #print(f'SHL_pivotNumber: {pivotNumber}')
      for i in range(len(list)):
        if ( list[i] <= pivotNumber):
          leftSortedList.append(list[i])
        else:
          rightSortedList.append(list[i])       
      
      return leftSortedList, rightSortedList
    except Exception as e: print(e)
  
  ## Quick Sort
  def Quick_Sort(self, list, leftPivotNumber, rightPivotNumber, iteration_stop):
    try:
      # Code starts here
      print(f'Initial unsorted list: {list}')
      #print(f'Initial leftPivotNumber: {leftPivotNumber}')
      #print(f'Initial rightPivotNumber: {rightPivotNumber}')

      leftSortedList, rightSortedList = self.Sort_Half_List(list, pivotNumber = rightPivotNumber)

      #print(f'leftSortedList = {leftSortedList}')
      #print(f'rightSortedList = {rightSortedList}')

      for i in range (iteration_stop):
        #if i == 3: break
        # Re-sort with new pivots
        if( len(leftSortedList) > 1 ): 
          leftPivotNumber = leftSortedList[- 2]
        if( len(rightSortedList) > 1 ): 
          rightPivotNumber = rightSortedList[- 2]

        #print(f'leftPivotNumber: {leftPivotNumber}')     
        #print(f'rightPivotNumber: {rightPivotNumber}')

        #print(f'##########################')
        leftSortedList1 = leftSortedList
        rightSortedList1  = rightSortedList

        #print(f'leftSortedList = {leftSortedList}')
        #print(f'rightSortedList = {rightSortedList}')

        #print(f'************************')
        leftSortedList, rightSortedList = self.Sort_Half_List(leftSortedList1, pivotNumber = leftPivotNumber)

        #print(f'leftSortedList = {leftSortedList}')
        #print(f'rightSortedList = {rightSortedList}')
        # Merged sorted list
        leftSortedList1= leftSortedList + rightSortedList
        #print(f'Merged left lists: {leftSortedList1}')

        #print(f'************************')      
        leftSortedList, rightSortedList = self.Sort_Half_List(rightSortedList1, pivotNumber = rightPivotNumber)

        #print(f'leftSortedList = {leftSortedList}')
        #print(f'rightSortedList = {rightSortedList}')
        ## Merged sorted list
        rightSortedList1= leftSortedList + rightSortedList
        #print(f'Merged left lists: {rightSortedList1}')

        leftSortedList = leftSortedList1
        rightSortedList = rightSortedList1

      finalMergedList = leftSortedList1 + rightSortedList1
      print(f'finalMergedList: {finalMergedList}')
      
      """
      # Re-sort with new pivots
      if( len(leftSortedList) > 1 ): 
        leftPivotNumber = leftSortedList[- 2]
      if( len(rightSortedList) > 1 ): 
        rightPivotNumber = rightSortedList[- 2]

      print(f'leftPivotNumber: {leftPivotNumber}')     
      print(f'rightPivotNumber: {rightPivotNumber}')

      print(f'##########################')
      leftSortedList1 = leftSortedList
      rightSortedList1  = rightSortedList

      print(f'leftSortedList = {leftSortedList}')
      print(f'rightSortedList = {rightSortedList}')

      print(f'************************')
      leftSortedList, rightSortedList = self.Sort_Half_List(leftSortedList1, pivotNumber = leftPivotNumber)

      print(f'leftSortedList = {leftSortedList}')
      print(f'rightSortedList = {rightSortedList}')
      # Merged sorted list
      leftSortedList1= leftSortedList + rightSortedList
      print(f'Merged left lists: {leftSortedList1}')

      print(f'************************')      
      leftSortedList, rightSortedList = self.Sort_Half_List(rightSortedList1, pivotNumber = rightPivotNumber)

      print(f'leftSortedList = {leftSortedList}')
      print(f'rightSortedList = {rightSortedList}')
      # Merged sorted list
      rightSortedList1= leftSortedList + rightSortedList
      print(f'Merged left lists: {rightSortedList1}')

      print(f'##########################')
      # Re-sort with new pivots
      if( len(leftSortedList1) > 1 ): 
        leftPivotNumber = leftSortedList1[- 2]
      if( len(rightSortedList1) > 1 ): 
        rightPivotNumber = rightSortedList1[- 2]

      print(f'************************')
      leftSortedList, rightSortedList = self.Sort_Half_List(leftSortedList1, pivotNumber = leftPivotNumber)

      print(f'leftSortedList = {leftSortedList}')
      print(f'rightSortedList = {rightSortedList}')
      # Merged sorted list
      leftSortedList1= leftSortedList + rightSortedList
      print(f'Merged left lists: {leftSortedList1}')

      print(f'************************')      
      leftSortedList, rightSortedList = self.Sort_Half_List(rightSortedList1, pivotNumber = rightPivotNumber)

      print(f'leftSortedList = {leftSortedList}')
      print(f'rightSortedList = {rightSortedList}')
      # Merged sorted list
      rightSortedList1= leftSortedList + rightSortedList
      print(f'Merged left lists: {rightSortedList1}')

      print(f'##########################')

      finalMergedList = leftSortedList1 + rightSortedList1
      print(f'finalMergedList: {finalMergedList}')
      """

      
      # Code ends here
    
    except Exception as e: print(e)
  
  ## Sorting - Merge
  def Merge_Sorted_Arrays(self, array1, array2):
    pass
 
  ## Iterative and Recursion
  def Iterative_or_Recursive(self, numeric_sequence, iterative_or_recursion, number_or_index):
    # Factorial
    if ( numeric_sequence == self.FACTORIAL_SEQUENCE ):
      if ( iterative_or_recursion == self.USE_ITERATIVE ):
        self.Factorial_Of_A_Number(number_or_index, self.USE_ITERATIVE)

      if ( iterative_or_recursion == self.USE_RECURSSION ):
        self.Factorial_Of_A_Number(number_or_index, self.USE_RECURSSION)

    # Fibbonacci
    if ( numeric_sequence == self.FIBONACCI_SEQUENCE ):
      if ( iterative_or_recursion == self.USE_ITERATIVE ):
        self.Index_Value_Of_Fibbonacci_Number_Iterative(number_or_index)

      if ( iterative_or_recursion == self.USE_RECURSSION ):
        timeOfNow = datetime.now()
        start_time = timeOfNow
        
        index = number_or_index
        i = 0
        currF = 0
        prevF = 1
        FibbonacciList = []
        
        self.Index_Value_Of_Fibbonacci_Number_Recursive(i, index, prevF, currF, FibbonacciList)
        #self.Index_Value_Of_Fibbonacci_Number_Recursive(number_or_index)
        timeOfNow = datetime.now()    
        end_time = timeOfNow
        #print(f'End time: {end_time}'	)
        print(f'Total time: {end_time - start_time}')

  def Index_Value_Of_Fibbonacci_Number_Iterative(self, index):
    timeOfNow = datetime.now()
    start_time = timeOfNow

    try:
      i = 0
      currF = 0
      prevF = 1
      FibbonacciList = []
      for i in range(index):        
        f = currF + prevF
        FibbonacciList.append(f)
        prevF = currF
        currF = f

      #print(FibbonacciList)
      print(f'The Fibbonacci number at index {index-1} is {FibbonacciList[index-1]}')
        
    except Exception as e: print(e)
    
  
    timeOfNow = datetime.now()    
    end_time = timeOfNow
    #print(f'End time: {end_time}'	)
    print(f'Total time: {end_time - start_time}')
  
  def Index_Value_Of_Fibbonacci_Number_Recursive(self, i, index, prevF, currF, FibbonacciList):    
    try:
      if ( i <= index ):          
        f = currF + prevF
        FibbonacciList.append(f)
        
        prevF = currF
        currF = f
        i += 1

        self.Index_Value_Of_Fibbonacci_Number_Recursive(i, index, prevF, currF, FibbonacciList)
      else:
        #print(FibbonacciList)
        print(f'The Fibbonacci number at index {index-1} is {FibbonacciList[index-1]}')

    except Exception as e: print(e)
  
  def Factorial_Of_A_Number(self, number, fx):
    # Compare side by side compute time

    timeOfNow = datetime.now()
    start_time = timeOfNow
    #print(f'Start time: {start_time}'	)
    #print('In Factorial_Of_A_Number. Number is: ' + str(number) + ' Fx is: ' + str(fx))
    if ( number > 0 and fx == self.USE_ITERATIVE ):
      #print(f'Factorial of {number} looping...')
      self.Factorial_Iterative(number)

    if ( number > 0 and fx == self.USE_RECURSSION ):
      #print(f'Factorial of {number} recursive...')
      factorial = 1
      self.Factorial_With_Recursion(number, 1, 1)

    timeOfNow = datetime.now()    
    end_time = timeOfNow
    #print(f'End time: {end_time}'	)
    print(f'Total time: {end_time - start_time}')
  
  def Factorial_Iterative(self, number):
    #print (f'Factorial of: ', number)
    try:  
      if number == 0:
        return 1
      else:
        i = 1
        factorial = 1
        for i in range(number):
          #print(f'',i)
          factorial = factorial * (i + 1)
  
        #print(f'Factorial: ', factorial	)
        print(f'Factorial (looping) of {number} is {factorial}')
        #return factorial
  
    except Exception as e: print(e)

  def Factorial_With_Recursion(self, number, i, factorial):
    try:      
      if i <= number:
        factorial = factorial * i
        #print(f'Factorial of {i} is: {factorial}')
        i += 1        
        self.Factorial_With_Recursion(number, i, factorial)
        #return factorial
      else:
      # End of the recursion
        print(f'Factorial (recursion) of {number} is: {factorial}')
    except Exception as e: print(e) 

  ## Hash tables
  def Find_Recurring_Character(self, array):
    print(array)
    #Define the dictionaty where the list elements will be stored.
    listDictionary = {}
    try:
      # Loop through the list and add each element to the dictionary.
      for n in array:
        # Since a dictionary cannot contain duplicate keys, if there's a recurrent key (repeated character) it will stop and exit the loop returning the recurrenct character.
        if n in listDictionary:
          print(f'The 1st recurring character is: ', str(n))
          return n
        else:
          listDictionary[n] = str(n)
      print(f'(Undefined) There is no recurring character in the list.'	)  
    except Exception as e: print(e)

  ## Arrays
  def Merge_Sorted_Arrays(self, array1, array2):
    # TODO: 
    #  Add validations to the lists to make sure they are integers.
    #  Add validation that if an element is repeated in the merged list, do not add it to the merges sorted list.
    print("Given lists: ")
    print(array1)
    print(array2)

    mergedSortedArray = array1+array2
    returnedMergedSortedArray = []
    print("Merged list: ")
    print(mergedSortedArray)    

    i, j = 0, 0

    try:
      for k in range(len(mergedSortedArray)):
          # Validates if the index i is less than the length of the array1
          # If the validation is correct, the value of the array1 at index i is added to the returnedMergedSortedArray
          if i < len(array1) and (j >= len(array2) or array1[i] < array2[j]):
              returnedMergedSortedArray.append(array1[i])
              i += 1
          else:
              returnedMergedSortedArray.append(array2[j])
              j += 1

      print("Merged and sorted list: ")
      print(returnedMergedSortedArray)
      return returnedMergedSortedArray
    except Exception as e: print(e)
  
  def Reverse_String(self, string):
    # TODO: Lists validations

    try:
      reversed_string = Tools.reverse_string(string)  # Call the method on the instance
      print(reversed_string)  # Print the result
    except Exception as e: print(e)






    
   
      
