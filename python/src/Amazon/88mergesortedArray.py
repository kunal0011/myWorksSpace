"""
LeetCode 88. Merge Sorted Array

Problem Statement:
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n,
representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should
be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

Example 1:
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6].

Example 2:
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].

Constraints:
- nums1.length == m + n
- nums2.length == n
- 0 <= m, n <= 200
- 1 <= m + n <= 200
- -109 <= nums1[i], nums2[j] <= 109
"""


class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Start from the end of both arrays
        p1 = m - 1  # pointer for nums1
        p2 = n - 1  # pointer for nums2
        p = m + n - 1  # pointer for merged array

        # While there are elements to compare
        while p2 >= 0:
            # If p1 >= 0 and nums1[p1] > nums2[p2], use nums1[p1]
            # Otherwise, use nums2[p2]
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1


def visualize_merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """Helper function to visualize the merge process"""
    print("\nMerge Process:")
    print(f"nums1: {nums1}")
    print(f"nums2: {nums2}")

    # Create a copy for demonstration
    nums1_copy = nums1.copy()
    p1 = m - 1
    p2 = n - 1
    p = m + n - 1

    while p2 >= 0:
        if p1 >= 0 and nums1_copy[p1] > nums2[p2]:
            nums1_copy[p] = nums1_copy[p1]
            print(f"Taking {nums1_copy[p1]} from nums1")
            p1 -= 1
        else:
            nums1_copy[p] = nums2[p2]
            print(f"Taking {nums2[p2]} from nums2")
            p2 -= 1
        p -= 1
        print(f"Current state: {nums1_copy}")

    print(f"Final result: {nums1_copy}")


def test_merge():
    solution = Solution()

    test_cases = [
        {
            "nums1": [1, 2, 3, 0, 0, 0],
            "m": 3,
            "nums2": [2, 5, 6],
            "n": 3,
            "expected": [1, 2, 2, 3, 5, 6],
            "description": "Standard case"
        },
        {
            "nums1": [1],
            "m": 1,
            "nums2": [],
            "n": 0,
            "expected": [1],
            "description": "Empty nums2"
        },
        {
            "nums1": [0],
            "m": 0,
            "nums2": [1],
            "n": 1,
            "expected": [1],
            "description": "Empty nums1"
        },
        {
            "nums1": [4, 5, 6, 0, 0, 0],
            "m": 3,
            "nums2": [1, 2, 3],
            "n": 3,
            "expected": [1, 2, 3, 4, 5, 6],
            "description": "nums1 all greater"
        },
        {
            "nums1": [1, 2, 3, 0, 0, 0],
            "m": 3,
            "nums2": [4, 5, 6],
            "n": 3,
            "expected": [1, 2, 3, 4, 5, 6],
            "description": "nums2 all greater"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        nums1 = test_case["nums1"].copy()
        m = test_case["m"]
        nums2 = test_case["nums2"].copy()
        n = test_case["n"]
        expected = test_case["expected"]
        description = test_case["description"]

        print(f"\nTest case {i}: {description}")
        visualize_merge(nums1, m, nums2, n)

        solution.merge(nums1, m, nums2, n)

        assert nums1 == expected, \
            f"Expected {expected}, but got {nums1}"
        print("✓ Test case passed!")


if __name__ == "__main__":
    test_merge()
    print("\nAll test cases passed! 🎉")
