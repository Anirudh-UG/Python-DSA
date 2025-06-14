"""
Alice has some cards with numbers written on them. She arranges the cards in decreasing order, and lays them out face down in a sequence on a table.
She challenges Bob to pick out the card containing a given number by turning over as few cards as possible.
Write a function to help Bob locate the card.
"""


def locate_card_linear_search(cards, target):
    """
    We implement the linear search algorithm, Which is a brute force solution to locate the card.
    The time complexity is O(n) since we iterate throughout the list in the worst case.
    """
    position = 0
    while position < len(cards):
        if cards[position] == target:
            return position
        position += 1
    return -1


def test_location(cards, target, mid):
    """
    This function is used to test the location of the target in the list.
    This handles the case where the target is repeated multiple times.
    """
    mid_number = cards[mid]
    if mid_number == target:
        if mid - 1 >= 0 and cards[mid - 1] == target:
            return "left"
        else:
            return "found"
    elif mid_number < target:
        return "left"
    else:
        return "right"


def locate_card_binary_search(cards, target):
    """
    We implement the binary search algorithm, Which is a more efficient solution to locate the card.
    The time complexity is O(log n) since we divide the list in half each time.
    """
    left, right = 0, len(cards) - 1
    while left <= right:
        middle = (left + right) // 2
        result = test_location(cards, target, middle)
        if result == "found":
            return middle
        elif result == "left":
            right = middle - 1
        elif result == "right":
            left = middle + 1
    return -1


if __name__ == "__main__":
    test_cases = []

    # target appears in the middle
    test_cases.append(
        {"input": {"cards": [13, 11, 10, 7, 4, 3, 1, 0], "target": 7}, "output": 3}
    )

    # target appears in the first position
    test_cases.append({"input": {"cards": [4, 2, 1, -1], "target": 4}, "output": 0})

    # target appears in the last position
    test_cases.append(
        {"input": {"cards": [3, -1, -9, -12], "target": -12}, "output": 3}
    )

    # card contains only one element, target
    test_cases.append({"input": {"cards": [6], "target": 6}, "output": 0})

    # card is empty
    test_cases.append({"input": {"cards": [], "target": 6}, "output": -1})

    # cards does not contain target
    test_cases.append({"input": {"cards": [9, 7, 5, 2, -9], "target": 4}, "output": -1})

    # repeating numbers in the list
    test_cases.append(
        {
            "input": {"cards": [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], "target": 3},
            "output": 7,
        }
    )

    # the list contains negative numbers
    test_cases.append(
        {
            "input": {
                "cards": [-4, -2, 0, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6],
                "target": 4,
            },
            "output": 3,
        }
    )

    # the target is repeated multiple times (we calculate the first occurrence)
    test_cases.append(
        {
            "input": {
                "cards": [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
                "target": 6,
            },
            "output": 2,
        }
    )

    for test in test_cases:
        print(
            "Linear Search: ",
            locate_card_linear_search(**test["input"]) == test["output"],
        )
        print(
            "Binary Search: ",
            locate_card_binary_search(**test["input"]) == test["output"],
        )
