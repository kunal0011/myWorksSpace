from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)

        j = 2  # Pointer to place the next valid element
        for i in range(2, len(nums)):
            # If the current element is not equal to the element at position j-2, it means
            # it can be placed at the position j (as it is not the third occurrence of the same element)
            if nums[i] != nums[j - 2]:
                nums[j] = nums[i]
                j += 1

        return j


s = Solution()
s.removeDuplicates([1, 1, 1, 2, 2, 2, 3])
