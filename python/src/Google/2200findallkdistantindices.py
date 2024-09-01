class Solution:
    def findKDistantIndices(self, nums: list[int], key: int, k: int) -> list[int]:
        result = set()

        # Find all indices where nums[j] == key
        for j in range(len(nums)):
            if nums[j] == key:
                # Add all indices i where |i - j| <= k
                for i in range(max(0, j - k), min(len(nums), j + k + 1)):
                    result.add(i)

        # Return the sorted list of indices
        return sorted(result)
