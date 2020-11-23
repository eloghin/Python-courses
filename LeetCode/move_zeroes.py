# 
# ******
# SOL 1
# ******       
# i, j = 0, 0
#  while i < len(nums):
#  	while nums[i] == 0 and i<len(nums)-1:
#     	i += 1
#  	aux = nums[j]
#  	nums[j] = nums[i]
#  	nums[i] = aux   
#  	i += 1
#  	j += 1
        
    
# ******  
# SOL 2
# ******
# j = 0

# for i in range(len(nums)):
# 	if nums[i] != 0:
#     	aux = nums[j]
#     	nums[j] = nums[i]
#     	nums[i] = aux      
#     	j += 1  



******
SOL 3
******
nums = [0,1,0,0,3,0,0,12]	

j = 0

#bring all the non-zero values at the beggining of the list, respecting their order
for i in range(len(nums)):
    if nums[i] != 0:
        nums[j] = nums[i]      
        j += 1 
        
#fill the rest of the list with zeroes
for i in range(j, len(nums)):
    nums[i] = 0