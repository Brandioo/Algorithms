if __name__ == '__main__':

    elements = [1, 6, 3, 4, 7]

    size = len(elements)

    for i in range(size - 1):
        swaped = False

        for j in range(size - 1 - i):
            if elements[j] > elements[j + 1]:
                # Change the elements value with each other
                elements[j], elements[j + 1] = elements[j + 1], elements[j]
                swaped = True

        if not swaped:
            break

    print(elements)
