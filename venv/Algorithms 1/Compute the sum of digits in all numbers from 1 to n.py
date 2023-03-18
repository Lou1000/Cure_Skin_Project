# Compute the sum of digits in all numbers from 1 to n. When a function gets a number n, find the sum of digits in all numbers from 1 to n.
# Example: n = 5. Result = 1 + 2 + 3 + 4 + 5 = 15


def sum_of_digits(n):

    result = 0

    for digit in range(1, n + 1):
        result = result + digit

    print(result)

sum_of_digits(5)


