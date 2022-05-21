# Problem: Find index of all the occurances of a number from sorted list
# Solution here tries to find an index of a number using binary search. Now since the list is sorted,
# it can do left and right scan from the initial index to find all occurances of a given element
# This method is not most efficient and I want you to figure out even a better way of doing it. In
# any case below method is still effective
import bisect


def binary_search(numbers_list, number_to_find):
    left_index = 0
    right_index = len(numbers_list) - 1

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = numbers_list[mid_index]

        if mid_number == number_to_find:
            return mid_index

        if mid_number < number_to_find:  # this means number is in right-hand side of the list
            left_index = mid_index + 1
        else:  # number to find is on left-hand side of the list
            right_index = mid_index - 1

    return -1


def find_all_occurances(numbers, number_to_find):
    index = binary_search(numbers, number_to_find)
    indices = [index]
    # find indices on left-hand side
    i = index - 1
    while i >= 0:
        if numbers[i] == number_to_find:
            indices.append(i)
        else:
            break
        i = i - 1

    # find indices on right-hand side
    i = index + 1
    while i < len(numbers):
        if numbers[i] == number_to_find:
            indices.append(i)
        else:
            break
        i = i + 1

    return sorted(indices)


if __name__ == '__main__':
    nums = [1, 4, 6, 9, 11, 15, 15, 15, 17, 21, 34, 34, 56]
    num_to_find = 15

    # Solution 1
    # left_index = bisect.bisect_left(nums, 15)
    # right_index = bisect.bisect_right(nums, 15)
    # indices = list(range(left_index, right_index))

    # Solution 2
    indices = find_all_occurances(nums, num_to_find)
    print(f"Indices of occurances of {num_to_find} are {indices}")