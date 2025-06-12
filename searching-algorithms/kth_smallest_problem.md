# Find K-th Smallest Element in Two Sorted Arrays

## Problem Statement

Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, find the **k-th smallest element** in the union of the two arrays.

You may assume that **k** is always valid, i.e., `1 ≤ k ≤ m + n`.

**Time Complexity Requirement:** Your solution must run in **O(log(min(m, n)))** time.

## Examples

```
Example 1:
Input: nums1 = [1, 3, 8], nums2 = [2, 4, 6, 7, 9], k = 4
Output: 4
Explanation: Merged array is [1, 2, 3, 4, 6, 7, 8, 9], 4th smallest is 4

Example 2:
Input: nums1 = [1, 2], nums2 = [3, 4], k = 1
Output: 1
Explanation: Merged array is [1, 2, 3, 4], 1st smallest is 1

Example 3:
Input: nums1 = [1, 2], nums2 = [3, 4], k = 3
Output: 3
Explanation: Merged array is [1, 2, 3, 4], 3rd smallest is 3

Example 4:
Input: nums1 = [], nums2 = [1], k = 1
Output: 1
Explanation: Only one array has elements

Example 5:
Input: nums1 = [1, 3, 5], nums2 = [2, 4, 6], k = 6
Output: 6
Explanation: Merged array is [1, 2, 3, 4, 5, 6], 6th smallest is 6
```

## Constraints
- `0 ≤ m, n ≤ 1000`
- `1 ≤ k ≤ m + n`
- `-10^6 ≤ nums1[i], nums2[i] ≤ 10^6`
- `nums1` and `nums2` are sorted in **non-decreasing** order

## Function Signature
```python
def findKthSmallest(nums1: List[int], nums2: List[int], k: int) -> int:
    pass
```

## Approach Ideas

### Approach 1: Merge and Select (Brute Force)
- Merge both arrays and return k-th element
- Time: O(m + n), Space: O(m + n)

### Approach 2: Two Pointers (Optimized Merge)
- Use two pointers to find k-th element without full merge
- Time: O(k), Space: O(1)

### Approach 3: Binary Search (Optimal)
- Use binary search on the smaller array
- Time: O(log(min(m, n))), Space: O(1)

## Key Insights
1. We need exactly k elements before our answer
2. Binary search on number of elements to take from each array
3. Ensure left partition ≤ right partition after the cut
4. Handle edge cases where one array is empty or exhausted

## Test Cases to Consider
```python
# Basic cases
nums1 = [1, 3, 8], nums2 = [2, 4, 6, 7, 9], k = 4  # Expected: 4
nums1 = [1, 2], nums2 = [3, 4], k = 1              # Expected: 1

# Edge cases
nums1 = [], nums2 = [1, 2, 3], k = 2               # Expected: 2
nums1 = [1], nums2 = [], k = 1                     # Expected: 1
nums1 = [1, 2, 3], nums2 = [4, 5, 6], k = 3       # Expected: 3

# Equal elements
nums1 = [1, 1, 2], nums2 = [1, 2, 2], k = 4       # Expected: 2

# Large k
nums1 = [1, 3, 5], nums2 = [2, 4, 6], k = 6       # Expected: 6
```

## Hints
1. Think about partitioning both arrays such that left partition has exactly k elements
2. Use binary search on the smaller array to find the optimal partition
3. Check if `max(left_partition) ≤ min(right_partition)`
4. Handle cases where partition is at the boundary (beginning/end of array)

## Follow-up Questions
1. How would you modify this to find the k-th largest element?
2. What if the arrays can contain duplicates?
3. Can you extend this to work with more than 2 sorted arrays?
4. How would you handle the case where k can be larger than m + n?

## Related Problems
- Median of Two Sorted Arrays (LeetCode 4)
- Merge k Sorted Lists (LeetCode 23)
- Find K Pairs with Smallest Sum (LeetCode 373)

---
*Difficulty: Hard*  
*Topics: Array, Binary Search, Divide and Conquer*  
*Companies: Google, Facebook, Amazon, Microsoft*