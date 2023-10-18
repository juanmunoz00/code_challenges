from tools import Tools

Tools = Tools() # Create an instance of the Tools class

class Challenges:
  REVERSE_STRING = 1
  MERGED_SORTED_ARRAY = 2
  FIND_RECURRING_CHARACTER = 3
  
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
  

      
    