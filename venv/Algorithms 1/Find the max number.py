# Find the max number from 3 values.
# Example: 124, 21, 32. Result = 124.

def max_value (mylist):
    # return max(mylist)
    # One way of answering it
    # if mylist[0] > mylist[1] and mylist[0] > mylist[-1]:
    #     return  mylis[0]

    max = 0

    for i in mylist:
        if i > max:
            max = i

    return max






print(max_value ([124, 21, 32, 1024]))