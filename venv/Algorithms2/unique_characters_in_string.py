# Unique Characters in String
# Given a string, determine if it consists of all unique characters.
# For example, the string 'abcde' has all unique characters and should return True.
# The string 'aabcde' contains duplicate characters and should return False.
# Hint: https://www.w3schools.com/python/python_sets.asp


def unique_string(string):
    for character in string:
        if string.count(character) > 1:
            return False

    return True


print(unique_string('aabcde'))
print(unique_string('abcde'))
