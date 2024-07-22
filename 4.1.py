def move_zeros_to_end(lst):
    for i in lst:
        if i == 0:
            lst.remove(i)
            lst.append(i)
    return lst

original_list = [0, 1, 0, 12, 3]
original_list2 = [0]
original_list3 = [1, 0, 13, 0, 0, 0, 5]
original_list4 = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]

print(move_zeros_to_end(original_list))
print(move_zeros_to_end(original_list2))
print(move_zeros_to_end(original_list3))
print(move_zeros_to_end(original_list4))
