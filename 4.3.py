def create_new_list(lst):
    if len(lst) < 3:
        raise ValueError("Список повинен містити принаймні 3 елементи.")
    return [lst[0], lst[2], lst[-2]]


examples = [
    [1, 2, 3, 4, 5, 6, 7, 9],
    [1, 1, 2, 1],
    [6, 3, 7]
]

for example in examples:
    new_list = create_new_list(example)
    print(f"{example} => {new_list}")
