"""
You are given a list of numbers, obtained by rotating a sorted list an unknown number of times.
Write a function to determine the minimum number of times the original sorted list was rotated to obtain the given list.
You can assume that the list does not contain duplicates.
Your function should run in O(log n) time.


We define "rotating" the list as removing the last element of the list and adding it before the first element.
Eg:
-> The list [3, 4, 5, 1, 2] was obtained by rotating the sorted list [1, 2, 3, 4, 5] 2 times.
-> The list [7, 8, 9, 1, 2, 3, 4, 5, 6] was obtained by rotating the sorted list [1, 2, 3, 4, 5, 6, 7, 8, 9] 3 times.
"""
