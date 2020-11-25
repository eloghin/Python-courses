# Given an array of integers that is already sorted in ascending order, find two numbers such that 
# they add up to a specific target number.

# Given an array of integers, find if the array contains any duplicates.

# Your function should return true if any value appears at least twice in 
# the array, and it should return false if every element is distinct.


"""""
SOL 1
"""""

dict_duplicates = {}

for item in nums:
    if item in dict_duplicates:
        return True
    else: 
        dict_duplicates[item] = 1
        
return False

"""""
SOL 2
"""""

#         num = list(set(nums)) #To remove duplicates

#         if len(num) == len(nums): 
#             return False
#         return True