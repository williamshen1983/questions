

# Q1
def print_triangle(length):
    for each_layer in range(length):
        if each_layer == 0:
            print(" " * (length - 1) + "*")
        elif each_layer == length - 1:
            print("* " * length)
        else:
            print(" " * (length - each_layer - 1) + "*" + " " * (2 * each_layer - 1) + "*")


print_triangle(4)
print_triangle(1)
print_triangle(2)
print_triangle(0)
print_triangle(10)


# Q2


def sort_random(num):

    each_digit_times = [0] * 10

    for each_digit in num:
        each_digit_times[int(each_digit)] += 1

    temp_list = []

    for odd_digit in range(9, 0, -2):
        for _ in range(each_digit_times[odd_digit]):
            temp_list.append(str(odd_digit))

    for even_digit in range(0, 9, 2):
        for _ in range(each_digit_times[even_digit]):
            temp_list.append(str(even_digit))

    return ''.join(temp_list)


print(sort_random('417324689435'))
print(sort_random(''))
print(sort_random('135'))
print(sort_random('806'))
