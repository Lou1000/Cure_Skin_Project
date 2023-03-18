# Count odd and even numbers. Count odd and even digits of the whole number.
# Example: number is 34560, then 3 digits will be even (4, 6, and 0) and 2 odd digits (3 and 5).


def count_odd_even_nums (num):

    even_num = []
    odd_num = []

    # 3456 -> 3 -> 4 -> 5 -> 6

    for number in str(num):
        # number = 3

        if (int(number) % 2 == 0):
            even_num.append(int(number))
        else:
            odd_num.append(int(number))

    return even_num, odd_num


new_even_list, new_odd_list = count_odd_even_nums(34560)
print(new_odd_list)
print(new_even_list)
