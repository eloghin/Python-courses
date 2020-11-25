# Given an array of integers that is already sorted in ascending order, find two numbers such that 
# they add up to a specific target number.

# The function twoSum should return indices of the two numbers such that they add up to the target, 
# where index1 must be less than index2.

# Note:

#     Your returned answers (both index1 and index2) are not zero-based.
#     You may assume that each input would have exactly one solution and you may not use the same element twice.



*******
SOL 1
*******
dict_ans = {}
for i, num in enumerate(nums):
    dif = target - num
    if dif dif >= 0 and dif not in dict_ans:
        dict_ans[num] = i
    else:
        return [dict_ans[dif], i]
