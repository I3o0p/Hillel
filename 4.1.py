lists = [
    [0, 1, 0, 12, 3],
    [0],
    [1, 0, 13, 0, 0, 0, 5],
    [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
]

for lst in lists:
    for i in lst:
        if i == 0:
            lst.remove(i)
            lst.append(i)
    print(lst)
