def insertion_sort(elements):
    for i in range(1, len(elements)):
        current_element = elements[i]
        j = i - 1
        while j >= 0 and current_element < elements[j]:
            # Swapping elements from left to right
            elements[j + 1], elements[j] = elements[j], elements[j + 1]
            j -= 1
        elements[j + 1] = current_element


def insertion_srt(elements):
    new_list = [elements[0]]

    for i in range(1, len(elements)):

        new_list.append(elements[i])

        j = len(new_list) - 1

        while j > 0 and new_list[j] < new_list[j - 1]:
            new_list[j], new_list[j - 1] = new_list[j - 1], new_list[j]
            j -= 1


if __name__ == '__main__':
    numbers = [11, 9, 29, 7, 2, 15, 28]

    insertion_sort(numbers)

    print(f"List of numbers after using bubble_sort() -> {numbers}")
