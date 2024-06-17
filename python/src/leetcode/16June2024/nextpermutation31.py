from itertools import permutations
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)

        # Step 1: Find the largest index k such that nums[k] < nums[k + 1]
        k = n - 2
        while k >= 0 and nums[k] >= nums[k + 1]:
            k -= 1

        if k == -1:
            nums.reverse()
            return

        # Step 2: Find the largest index l greater than k such that nums[k] < nums[l]
        l = n - 1
        while l > k and nums[l] <= nums[k]:
            l -= 1

        # Step 3: Swap nums[k] and nums[l]
        nums[k], nums[l] = nums[l], nums[k]

        # Step 4: Reverse the sequence from nums[k + 1] to the end
        left, right = k + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        print(nums)


if __name__ == "__main__":
    s = Solution()
    print(s.nextPermutation([1, 2, 3]))
    print(s.nextPermutation([2, 3, 1, 5, 6, 4]))
