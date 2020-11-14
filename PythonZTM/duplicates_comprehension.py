#Find all the duplicates in a list using comprehension

my_list = ['a', 'b', 'c', 'b', 'm', 'n', 'n']
# duplicates = []

# for item in my_list:
#     if my_list.count(item) > 1:
#         if item not in duplicates:
#             duplicates.append(item)

# print(duplicates)

duplicates1 = list(set(char for char in my_list if my_list.count(char) > 1))
print(duplicates1)


