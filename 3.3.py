my_list1 = [1, 2, 3, 4, 5, 6]
my_list2 = [1, 2, 3]
my_list3 = [1, 2, 3, 4, 5]
my_list4 = [1]
my_list5 = []

middle_index1 = (len(my_list1) + 1) // 2
result1 = [my_list1[:middle_index1], my_list1[middle_index1:]]

middle_index2 = (len(my_list2) + 1) // 2
result2 = [my_list2[:middle_index2], my_list2[middle_index2:]]

middle_index3 = (len(my_list3) + 1) // 2
result3 = [my_list3[:middle_index3], my_list3[middle_index3:]]

middle_index4 = (len(my_list4) + 1) // 2
result4 = [my_list4[:middle_index4], my_list4[middle_index4:]]

middle_index5 = (len(my_list5) + 1) // 2
result5 = [my_list5[:middle_index5], my_list5[middle_index5:]]

print(f" {my_list1} => {result1}")
print(f" {my_list2} => {result2}")
print(f" {my_list3} => {result3}")
print(f" {my_list4} => {result4}")
print(f" {my_list5} => {result5}")