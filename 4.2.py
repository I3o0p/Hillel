lists = [
    [1, 3, 5],
    [6],
    []
]

for lst in lists:
    if not lst:
        result = 0
    else:
        sewei = sum(lst[::2])
        last = lst[-1]
        result = sewei * last
    print(result)
