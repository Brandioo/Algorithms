def swap(a, b, arr):
    # Using the temporaty variable to swap elements.
    if a != b:
        temp = arr[a]
        arr[a] = arr[b]
        arr[b] = temp


def partition(mylist, start_index, end_index):
    pivot_index = start_index
    pivot = mylist[pivot_index]

    while start_index < end_index:
        while start_index < len(mylist) and mylist[start_index] <= pivot:
            start_index += 1

        while mylist[end_index] > pivot:
            end_index -= 1

        if start_index < end_index:
            swap(start_index, end_index, mylist)
    swap(pivot_index, end_index, mylist)
    return end_index


def quick_sort(mylist, start_index, end_index):
    if start_index < end_index:
        partition_index = partition(mylist, start_index, end_index)
        quick_sort(mylist, start_index, partition_index - 1)
        quick_sort(mylist, partition_index + 1, end_index)


if __name__ == '__main__':
    mylist = [34, 54, 23, 56, 10, 20, 30, 21]
    quick_sort(mylist, 0, len(mylist) - 1)
    print(mylist)
