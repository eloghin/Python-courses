# Given an array of integers nums and an integer target, return indices of the two numbers such 
# that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# *******
# SOL 1
# *******
# answer = []

# dict_ans = {}

# for i in range(len(nums)):
#     dif = target - nums[i]
#     if nums[i] in dict_ans:
#         answer.extend([dict_ans[nums[i]], i])
#         return answer
#     else:
#         dict_ans.update({dif: i})

# return(answer)

*******
SOL 2
*******
dict_ans = {}
for i, num in enumerate(nums):
    dif = target - num
    if dif not in dict_ans:
        dict_ans[num] = i
    else:
        return [dict_ans[dif], i]