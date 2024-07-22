def sewei(lst):
    if not lst:
        return 0
    sewei = sum(lst[::2])
    last = lst[-1]
    return sewei * last

list1 = [1, 3, 5]
list2 = [6]
list3 = []

print(sewei(list1))
print(sewei(list2))
print(sewei(list3))
