# You are given an array nums of non-negative integers and an integer k.

# An array is called special if the bitwise OR of all of its elements is at least k.

# Return the length of the shortest special non-empty 
# subarray
#  of nums, or return -1 if no special subarray exists.

 

# Example 1:

# Input: nums = [1,2,3], k = 2

# Output: 1

# Explanation:

# The subarray [3] has OR value of 3. Hence, we return 1.

# Example 2:

# Input: nums = [2,1,8], k = 10

# Output: 3

# Explanation:

# The subarray [2,1,8] has OR value of 11. Hence, we return 3.

# Example 3:

# Input: nums = [1,2], k = 0

# Output: 1

# Explanation:

# The subarray [1] has OR value of 1. Hence, we return 1.

 

# Constraints:

# 1 <= nums.length <= 50
# 0 <= nums[i] <= 50
# 0 <= k < 64

from typing import List


class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:


        for i in range(1,len(nums)+1):
            k2 = len(nums)-i
            for j in range(0,k2+1):
                or1 = 0
                for k1 in range(j,j+i):
                    or1 = or1 | nums[k1]
                if or1>=k:
                    return i
        return -1

class Solution1:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cnt = [0] * 32
        ans = n + 1
        s = i = 0
        for j, x in enumerate(nums):
            s |= x
            for h in range(32):
                if x >> h & 1:
                    cnt[h] += 1
            while s >= k and i <= j:
                ans = min(ans, j - i + 1)
                y = nums[i]
                for h in range(32):
                    if y >> h & 1:
                        cnt[h] -= 1
                        if cnt[h] == 0:
                            s ^= 1 << h
                i += 1
        return -1 if ans > n else ans


if __name__ == '__main__':
    s = Solution1()
    print(s.minimumSubarrayLength([1,2,3],2))
    print(s.minimumSubarrayLength([2,1,8],10))
    print(s.minimumSubarrayLength([1,2],0))