class Solution:
    def largestSubarray(self, nums: list[int], k: int) -> list[int]:
        # We need to find the starting index of the largest subarray of length k
        max_index = 0
        for i in range(1, len(nums) - k + 1):
            if nums[i:i+k] > nums[max_index:max_index+k]:
                max_index = i
        return nums[max_index:max_index+k]
