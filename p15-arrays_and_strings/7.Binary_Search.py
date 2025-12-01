#Following code is a simple binary search using python lang.


def biSearch(arr: list, target: int) -> int:
    sorted_arr = sorted(arr)

    start = 0
    end = len(sorted_arr) - 1

    while start <= end:
        mid = (start + end) // 2

        if sorted_arr[mid] == target:
            return mid          # or return sorted_arr[mid] if you want the value
        elif sorted_arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    # target not found
    return None 

arr = [2, 4, 6, 8, 10]
target = 11
print(biSearch(arr, target))


def run_tests():
    tests = [
        ([0, 1, 2, 3, 4, 5], 3, 3),
        ([0, 1, 2, 3, 4, 5], 0, 0),
        ([0, 1, 2, 3, 4, 5], 5, 5),
        ([2, 4, 6, 8, 10], 1, -1),
        ([2, 4, 6, 8, 10], 11, -1),
        ([5], 5, 0),
        ([5], 3, -1),
        ([1, 2, 2, 2, 3], 2, "any of [1, 2, 3]"),
        ([], 3, -1),
        (list(range(0, 1000000)), 999999, 999999)
    ]

    for i, (arr, target, correct) in enumerate(tests, 1):
        result = biSearch(arr, target)
        print(f"Test {i}: arr={arr[:10]}{'...' if len(arr) > 10 else ''}, target={target}")
        print(f"  biSearch result: {result}")
        print(f"  The test correct answer is: {correct}\n")

# Run all tests
run_tests()
