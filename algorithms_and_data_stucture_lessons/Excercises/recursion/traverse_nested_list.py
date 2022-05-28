""" Function that counts the number of leaf elements in a nested list """

names = [
    "Adam",
    [
        "Bob",
        [
            "Chet",
            "Cat",
        ],
        "Barb",
        "Bert"
    ],
    "Alex",
    [
        "Bea",
        "Bill"
    ],
    "Ann"
]


def count_leaf_items(item_list):
    """
        Recursively counts and returns
        the number of leaf items in a (potentiallynested) list.
    """
    count = 0
    for item in item_list:
        if isinstance(item, list):
            count += count_leaf_items(item)
        else:
            count += 1

    return count


# For better understanding
def count_leaf_items_expained(item_list):
    """Recursively counts and returns the
       number of leaf items in a (potentially
       nested) list.
    """
    print(f"List: {item_list}")
    count = 0
    for item in item_list:
        if isinstance(item, list):
            print("Encountered sublist")
            count += count_leaf_items_expained(item)
        else:
            print(f"Counted leaf item \"{item}\"")
            count += 1

    print(f"-> Returning count {count}")
    return count
