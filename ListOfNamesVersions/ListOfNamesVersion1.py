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

count = 0
for el in names:
    if isinstance(el, list):
        for i in el:
            if isinstance(i,list):
                for j in i:
                    if isinstance(j, list):
                        count += len(j)
                    else:
                        count += 1
            else:
                count += 1
    else:
        count += 1

print(count)