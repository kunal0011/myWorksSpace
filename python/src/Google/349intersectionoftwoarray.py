from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Convert both lists to sets
        set1 = set(nums1)
        set2 = set(nums2)

        # Find the intersection of both sets
        intersection = set1 & set2

        # Convert the result to a list
        return list(intersection)


# Example usage:
solution = Solution()
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(solution.intersection(nums1, nums2))  # Output: [2]

nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
print(solution.intersection(nums1, nums2))  # Output: [9, 4]
