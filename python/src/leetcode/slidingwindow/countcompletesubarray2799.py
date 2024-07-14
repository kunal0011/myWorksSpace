from typing import List


class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        num_distinct = len(set(nums))  # Number of distinct elements in nums

        left = 0
        freq = {}
        result = 0

        for right in range(len(nums)):
            # Add nums[right] to frequency map
            freq[nums[right]] = freq.get(nums[right], 0) + 1

            # Contract the window from the left until the window is complete
            while len(freq) == num_distinct:
                result += 1  # All subarrays ending at right are complete
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left += 1

        return result


# Example usage:
sol = Solution()
nums1 = [1, 2, 1, 2, 3]
print(sol.countCompleteSubarrays(nums1))  # Output: 7

nums2 = [1, 2, 3, 4, 5]
print(sol.countCompleteSubarrays(nums2))  # Output: 5

nums3 = [1, 1, 1, 1, 1]
print(sol.countCompleteSubarrays(nums3))  # Output: 5
