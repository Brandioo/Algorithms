def linear_search(numbers_list, number_to_find):
    for index, element in enumerate(numbers_list):
        if element == number_to_find:
            return index
    return -1


if __name__ == '__main__':
    numbers = [12, 15, 17, 19, 24, 45, 67, 21]

    number = 21

    position = linear_search(numbers, number)
    print(f"Number found at index {position} using linear search")
