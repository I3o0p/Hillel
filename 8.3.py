def find_unique_value(some_list):
    element_count = {}
    for element in some_list:
        if element in element_count:
            element_count[element] += 1
        else:
            element_count[element] = 1

    for element, count in element_count.items():
        if count == 1:
            return element

assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
print("ОК")
