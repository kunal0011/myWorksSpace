class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0

        i = 0  # Pointer for the next unique element position

        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                # Move the unique element to the position after i
                nums[i] = nums[j]

        return i + 1
