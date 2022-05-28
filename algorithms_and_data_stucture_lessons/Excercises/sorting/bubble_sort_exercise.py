def bubble_sort(elements, key=None):
    size = len(elements)

    for i in range(size - 1):
        swapped = False
        for j in range(size - 1 - i):
            if elements[j][key] > elements[j + 1][key]:
                elements[j][key], elements[j + 1][key] = elements[j + 1][key], elements[j][key]
                swapped = True

        if not swapped:
            break


if __name__ == '__main__':
    data = [
        {'name': 'alex', 'transaction_amount': 1000, 'device': 'iphone-12'},
        {'name': 'mathew', 'transaction_amount': 400, 'device': 'iphone-13'},
        {'name': 'john', 'transaction_amount': 200, 'device': 'iphone-11'},
        {'name': 'steve', 'transaction_amount': 800, 'device': 'iphone-8'},
    ]

    bubble_sort(data, key='transaction_amount')
    for row in data:
        print(row)

    print('\n')

    bubble_sort(data, key='name')
    for row in data:
        print(row)
