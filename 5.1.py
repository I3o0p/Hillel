import string
import keyword

examples = [
    "_",
    "__",
    "___",
    "x",
    "get_value",
    "get value",
    "get!value",
    "some_super_puper_value",
    "Get_value",
    "get_Value",
    "getValue",
    "3m",
    "m3",
    "assert",
    "assert_exception"
]

for name in examples:
    is_valid = True

    if name in keyword.kwlist:
        is_valid = False

    if name.count('_') > 1:
        is_valid = False

    if name[0].isdigit():
        is_valid = False

    for char in name:
        if char in string.punctuation and char != '_':
            is_valid = False
        if char.isupper():
            is_valid = False

    print(f"{name} => {is_valid}")
