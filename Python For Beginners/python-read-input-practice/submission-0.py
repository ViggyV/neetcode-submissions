def add_two_numbers() -> int:
    my_input = input()

    res = my_input.split(',')
    return int(res[0]) + int(res[1])


# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
