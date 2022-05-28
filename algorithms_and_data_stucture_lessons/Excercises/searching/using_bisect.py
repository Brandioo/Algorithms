import bisect

if __name__ == '__main__':
    nums = [1, 2, 2, 2, 4, 7, 9]

    print(f"Index to insert using bisect() - {bisect.bisect(nums, 3)}")

    print(f"Index to insert using bisect_left() - {bisect.bisect_left(nums, 2)}")

    print(f"Index to insert using bisect_right() - {bisect.bisect_right(nums, 2)}")

    print(f"Index to insert using bisect() - {bisect.bisect(nums, 12)}")

    bisect.insort(nums, 3)
    print(f"Numbers list after inserting 3, {nums}")

    bisect.insort(nums, 12)
    print(f"Numbers list after inserting 12, {nums}")

    bisect.insort_left(nums, 2)
    print(f"Numbers list after inserting left 2, {nums}")