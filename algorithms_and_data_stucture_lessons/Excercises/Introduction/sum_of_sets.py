"""
    You are given hundred numbers divided in ten sets in the following order.
    Set 1: 1-10
    Set 2: 11-20
    Set 3: 21-30
    …
    Set 10: 91-100

    Find the sum of each set
"""

""" Setting up the data for Excercise """
# globals is used to create the lists with dynamic names
g = globals()
number_of_sets = 10
# For range to start from 1 and end at 10
for set_number in range(1, number_of_sets + 1):
    first_set_number = (set_number * 10) - 9
    last_set_number = set_number * 10
    # This command is used to create the sets dinamically
    g[f'set_{set_number}'] = [number for number in range(first_set_number, last_set_number + 1)]

# Printing the sets to see the data is correct
for set_number in range(1, number_of_sets + 1):
    set_name = f'set_{set_number}'
    print(f'{set_name}: {g[set_name]} \n')

""" Solution """
count = 1
i = 1
while i <= 10:
    sum_of_set = 0
    j = 1
    while j <= 10:
        sum_of_set += count
        count += 1
        j += 1
    print(f'Sum of set_{i} is = {sum_of_set} \n')
    i += 1

