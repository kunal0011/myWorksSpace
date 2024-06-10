# 643. Maximum Average Subarray I
# Easy
# Topics
# Companies
# You are given an integer array nums consisting of n elements, and an integer k.

# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

 

# Example 1:

# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
# Example 2:

# Input: nums = [5], k = 1
# Output: 5.00000
 

# Constraints:

# n == nums.length
# 1 <= k <= n <= 105
# -104 <= nums[i] <= 104


from math import inf
from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        size = len(nums)
        max_avg = float('-inf')
        left = 0

        # This is returning time limit exceeded
        # for i in range(0,size-k+1):
        #     sum = 0
        #     for j in range(i,i+k):
        #         sum += nums[j]
        #     avg = sum/k
        #     max_avg = max(max_avg,avg)
        sum = 0
        for right in range(size):
            sum += nums[right]

            if right - left + 1 == k:
                max_avg = max(max_avg,sum/k)
                sum -= nums[left]
                left += 1
                
        return max_avg        

class Solution1:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s = sum(nums[:k])
        ans = s
        for i in range(k, len(nums)):
            s += nums[i] - nums[i - k]
            ans = max(ans, s)
        return ans / k
    
if __name__ == '__main__':
    s= Solution1()
    print(s.findMaxAverage([1,12,-5,-6,50,3],4))
    print(s.findMaxAverage([5],1))
