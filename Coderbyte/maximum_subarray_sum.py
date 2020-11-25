"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has 
the largest sum and return its sum.

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and 
conquer approach, which is more subtle.
"""

########
#SOL 1
########

current_sum = nums[0]
global_sum = nums[0]


for num in nums[1:]:
    
    if current_sum + num > num:
        current_sum += num
    else:
        current_sum = num
        
    if current_sum > global_sum:
        global_sum = current_sum

    
print(global_sum)

########
#SOL 2
########

#         current_subarray = [nums[0]]
#         global_subarray = [nums[0]]


#         for num in nums[1:]:
    
#             if sum(current_subarray) + num > num:
#                 current_subarray.append(num)
#             else:
#                 current_subarray = [num]  

#             if sum(current_subarray) > sum(global_subarray):
#                 global_subarray = list(current_subarray)

#		  print (sum(global_subarray))