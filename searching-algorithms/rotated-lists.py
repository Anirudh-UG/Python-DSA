"""
You are given a list of numbers, obtained by rotating a sorted list an unknown number of times.
Write a function to determine the minimum number of times the original sorted list was rotated to obtain the given list.
You can assume that the list does not contain duplicates.
Your function should run in O(log n) time.


We define "rotating" the list as removing the last element of the list and adding it before the first element.
Eg:
-> The list [3, 4, 5, 1, 2] was obtained by rotating the sorted list [1, 2, 3, 4, 5] 2 times.
-> The list [7, 8, 9, 1, 2, 3, 4, 5, 6] was obtained by rotating the sorted list [1, 2, 3, 4, 5, 6, 7, 8, 9] 3 times.

Examples:
-> [3, 4, 5, 1, 2] -> 2
-> [7, 8, 9, 1, 2, 3, 4, 5, 6] -> 3
-> [1, 2, 3, 4, 5] -> 0
-> [2, 3, 4, 5, 1] -> 4
-> [] -> -1
"""


def linear_count_rotations(nums) -> int:
    """
    This function counts the number of rotations of a sorted list.
    It does this by iterating through the list and checking if the current element is greater than the last element.
    If it is, then the list has been rotated.
    It returns the number of rotations, if the list is empty, it returns -1.
    The Time Complexity of this function is O(n) because it iterates through the list once.
    """
    if not nums:
        return -1

    # Find the index where the sorted order breaks (minimum element)
    for i in range(len(nums)):
        # Check if current element is smaller than previous element
        if i > 0 and nums[i] < nums[i - 1]:
            return i
        # Also check if we're at the end and first element > last element
        if i == len(nums) - 1 and nums[0] < nums[-1]:
            return 0  # This means it's not rotated but we need to return proper count

    # If no break found, array is not rotated
    return 0


def binary_count_rotations(nums) -> int:
    """
    This function counts the number of rotations of a sorted list.
    It does this by using a binary search to find the smallest element of the list.
    The number of times the list is rotated is the index of the smallest element.
    If the list is empty, it returns -1.
    The Time Complexity of this function is O(log n) because it uses a binary search to find the pivot point.
    """
    if not nums:
        return -1

    left = 0
    right = len(nums) - 1

    # If array is not rotated
    if nums[left] <= nums[right]:
        return 0

    while left < right:
        mid = (left + right) // 2
        # Add bounds check to prevent index error
        if mid > 0 and nums[mid] < nums[mid - 1]:
            return mid
        elif nums[mid] < nums[right]:
            right = mid
        else:
            left = mid + 1
    return left


if __name__ == "__main__":
    test_cases = []
    # Test case when the list is rotated < n//2 times
    test_cases.append({"input": [3, 4, 5, 1, 2], "output": 3})

    # Test case when the list is rotated > n//2 times
    test_cases.append({"input": [2, 3, 4, 5, 1], "output": 4})

    # Test case when the list is not rotated
    test_cases.append({"input": [1, 2, 3, 4, 5], "output": 0})

    # Test case when the list is empty
    test_cases.append({"input": [], "output": -1})

    # Test case when the list is rotated n-1 times
    test_cases.append({"input": [2, 3, 4, 5, 6, 7, 8, 1], "output": 7})

    # Test case when the list contains only one element
    test_cases.append({"input": [1], "output": 0})

    for test_case in test_cases:
        print(
            "Linear Search",
            linear_count_rotations(test_case["input"]) == test_case["output"],
            end="\t",
        )
        print()
        print(
            "Binary Search",
            binary_count_rotations(test_case["input"]) == test_case["output"],
            end="\t",
        )
        print()
