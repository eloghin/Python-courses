# create a superlist inherited from lis
class SuperList(list):
	def __len__(self):
		return 1000

super_list1 = SuperList()

print(len(super_list1))

super_list1.append(5)
super_list1.extend([1,2,3,4,6,7])
print(super_list1)
print(super_list1[5])
print(issubclass(list, object))
print(issubclass(SuperList, list))
