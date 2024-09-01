class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        # Convert both lists to sets to get unique elements
        set1 = set(nums1)
        set2 = set(nums2)

        # Find elements in set1 but not in set2
        distinct_nums1 = list(set1 - set2)

        # Find elements in set2 but not in set1
        distinct_nums2 = list(set2 - set1)

        # Return the result as a list of two lists
        return [distinct_nums1, distinct_nums2]
