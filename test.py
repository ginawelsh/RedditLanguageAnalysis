# [3, 41, 12, 9, 74, 15]
# Create a loop that would find the largest number

largest_num = 0
list = [3, 41, 12, 9, 74, 15]

def find_largest(n):
    for i in range(len(list)):
        if list[i] > list[i-1]:
            largest_num = list[i]
    return largest_num


