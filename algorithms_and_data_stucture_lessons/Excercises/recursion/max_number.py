""" Function to find the maximum number from a list using recursion """


def get_max(arr, n):
    if n == 1:
        return arr[0]
    # If there is single element, return it.
    # Else return maximum of first element
    # and maximum of remaining array.
    else:
        return max(
            get_max(arr[1:], n - 1),
            arr[0]
        )


numbers_list = [12, 1234, 45, 67, 1]
list_length = len(numbers_list)
print("Maximum element of array: ", get_max(numbers_list, list_length))
