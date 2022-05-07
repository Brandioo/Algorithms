g = globals()
number_of_sets = 10
# For range to start from 1 and end at 10
for set_number in range(1, number_of_sets + 1):
    first_set_number = (set_number * 10) - 9
    last_set_number = set_number * 10
    # This command is used to create the sets dinamically
    g[f'set_{set_number}'] = [number for number in range(first_set_number, last_set_number + 1)]


    count = 1
    i = 1
    while i < 10:
        sum_set = 0
        j = 1
        while j < 10:
            sum_set += count
            count += 1
            j += 1
        print(sum_set)
        i += 1