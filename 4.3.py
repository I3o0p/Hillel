lists = [
    [1, 2, 3, 4, 5, 6, 7, 9],
    [1, 1, 2, 1],
    [6, 3, 7]
]

for example in lists:
    if len(example) < 3:
        raise ValueError("Список повинен містити принаймні 3 елементи")

    new_list = [example[0], example[2], example[-2]]
    print(f"{example} => {new_list}")
