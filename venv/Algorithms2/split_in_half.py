# Given a string. Split it into two equal parts. Swap these parts and return the result.
# If the string has odd characters, the first part should be one character greater than the second part.
# Example: string = 'bbbbbcaaaaa'. Result = ‘aaaaabbbbbc’.


def split_reverse(string):
        # see if it contains the string is odd or even number of character
        # result_1 = None
        # result_2 = None
        if len(string) % 2 == 0:
                # find the middle
                middle = len(string) // 2
                # split the string into two parts
                first_part = string[:middle]
                second_part = string[middle:]
                # swap the part and save the result
                result_1 = second_part + first_part
                return result_1
        else:
                # find the middle
                middle = len(string) // 2 + 1
                # split the string into two parts
                first_part = string[:middle]
                second_part = string[middle:]
                # swap the part and save the result
                result_2 = second_part + first_part
                return result_2

print(split_reverse('dogs'))
print(split_reverse('pie'))
print(split_reverse('bbbbbcaaaaa'))
# 'dogs' => 'gsdo'
# 'cars' => 'rsca'
# 'house' => 'sehou'
# 'homework' => 'workhome'
# 'bbbbbcaaaaa' => 'aaaaabbbbbc'
