"""

Given an array, rotate the array to the right by k steps, where k is non-negative.

Follow up:

    Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
    Could you do it in-place with O(1) extra space?



Do not return anything, modify nums in-place instead.
"""

k = k % len(nums) # in case k > len(nums)
nums[:] = list(nums[-k:] + nums[:-k]) # in-place modification