#functions that return the highest even number in a list

def highest_even1(li):
    li.sort(reverse=True)
    for number in li:
        if number%2 ==0:
            return number
    
def highest_even2(li):
    even_list = []
    for item in li:
        if item%2 == 0:
            even_list.append(item)
    return(max(even_list))
            
print(highest_even1([10,2,3,4,8,11]))
print(highest_even2([10,2,3,4,8,11]))
