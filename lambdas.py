def alter(values, check):
    return [val for val in values if check(val)]


my_list = [1, 2, 3, 4, 5]
another_list = alter(my_list, lambda x: x != 5)
print(another_list)


def check_not_five(x):
    return x != 5


another_list = alter(my_list, check_not_five)
print(another_list)
