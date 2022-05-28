def merge_sort(elements):
    if len(elements) <= 1:
        return elements

    mid = len(elements) // 2
    left = elements[:mid]
    right = elements[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge_two_sorted_lists(left, right)


def merge_two_sorted_lists(a, b):
    sorted_list = []
    i = j = 0

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            sorted_list.append(a[i])
            i += 1
        else:
            sorted_list.append(b[j])
            j += 1

    while i < len(a):
        sorted_list.append(a[i])
        i += 1

    while j < len(b):
        sorted_list.append(b[j])
        j += 1

    return sorted_list


if __name__ == '__main__':
    arr = [10, 3, 15, 7, 23, 98, 29]

    merge_sort(arr)

    print(f"List of numbers after using merge_sort() -> {arr}")
