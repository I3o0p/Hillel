def common_elements():
    mult_of_3 = {i for i in range(100) if i % 3 == 0}
    mult_of_5 = {i for i in range(100) if i % 5 == 0}
    common_elements = mult_of_3 & mult_of_5
    return common_elements

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
