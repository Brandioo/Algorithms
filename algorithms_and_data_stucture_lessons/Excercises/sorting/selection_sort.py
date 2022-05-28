def selection_sort(elements):
    size = len(elements)
    for i in range(size - 1):
        min_index = i
        for j in range(min_index + 1, size):
            if elements[j] < elements[min_index]:
                min_index = j

        if i != min_index:
            elements[i], elements[min_index] = elements[min_index], elements[i]


def selection_sort_v2(elements):
    size = len(elements)
    for i in range(size - 1):
        min_index = i
        for j in range(i + 1, size):
            if elements[min_index] > elements[j]:
                min_index = j

        elements[i], elements[min_index] = elements[min_index], elements[i]


if __name__ == '__main__':
    numbers = [78, 12, 15, 8, 61, 53, 23, 27]

    selection_sort_v2(numbers)

    print(f"List of numbers after using selection_sort() -> {numbers}")
