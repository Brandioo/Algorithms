def bubble_sort(elements):
    size = len(elements)

    for i in range(size - 1):
        swapped = False

        for j in range(size - 1 - i):
            if elements[j] > elements[j + 1]:
                # Change the elements value with each other
                elements[j], elements[j + 1] = elements[j + 1], elements[j]
                swapped = True
        # To make algorithm more efficent
        if not swapped:
            break


if __name__ == '__main__':
    numbers = [5, 9, 2, 1, 67, 34, 88, 34]

    bubble_sort(numbers)

    print(f"List of numbers after using bubble_sort() -> {numbers}")
