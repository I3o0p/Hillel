my_list1 = [12, 3, 4, 10]
my_list2 = [1]
my_list3 = []
my_list4 = [12, 3, 4, 10, 8]


last_element = my_list1.pop()
my_list1.insert(0, last_element)


last_element = my_list2.pop()
my_list2.insert(0, last_element)

if my_list3:
    last_element = my_list3.pop()
    my_list3.insert(0, last_element)


last_element = my_list4.pop()
my_list4.insert(0, last_element)

print(my_list1)
print(my_list2)
print(my_list3)
print(my_list4)
