from tools import Tools
from datetime import datetime

Tools = Tools() # Create an instance of the Tools class

class Challenges:
  REVERSE_STRING = 1
  MERGED_SORTED_ARRAY = 2
  FIND_RECURRING_CHARACTER = 3
  FACTORIAL_OF_A_NUMBER = 4
  
  USE_FACTORIAL_WITH_LOOPS = 1
  USE_FACTORIAL_WITH_RECURSSION = 2
  
  def Reverse_String(self, string):
    # TODO: Lists validations

    try:
      reversed_string = Tools.reverse_string(string)  # Call the method on the instance
      print(reversed_string)  # Print the result
    except Exception as e: print(e)

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

  def Factorial_Of_A_Number(self, number, fx):
    # Compare side by side compute time

    timeOfNow = datetime.now()
    start_time = timeOfNow
    #print(f'Start time: {start_time}'	)
    #print('In Factorial_Of_A_Number. Number is: ' + str(number) + ' Fx is: ' + str(fx))
    if ( number > 0 and fx == self.USE_FACTORIAL_WITH_LOOPS ):
      #print(f'Factorial of {number} looping...')
      self.Factorial_With_Loops(number)

    if ( number > 0 and fx == self.USE_FACTORIAL_WITH_RECURSSION ):
      #print(f'Factorial of {number} recursive...')
      factorial = 1
      self.Factorial_With_Recursion(number, 1, 1)
    
    timeOfNow = datetime.now()    
    end_time = timeOfNow
    #print(f'End time: {end_time}'	)
    print(f'Total time: {end_time - start_time}')
    
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
      
  def Factorial_With_Loops(self, number):
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