from collections import Counter
from typing import List


class Solution:
    def findLHS(self, nums: List[int]) -> int:

        ccounter_nums = Counter(nums)

        #print(ccounter_nums)

        max_len = 0

        for k,v in ccounter_nums.items():
            countm = 0
            if k-1 in ccounter_nums:
                countm = ccounter_nums[k-1]+v
            countp = 0
            if k+1 in ccounter_nums:
                countp += ccounter_nums[k+1]+v
            max_len = max(max_len, max(countm,countp))

        return max_len           
                


if __name__ == '__main__':
    s = Solution()
    print(s.findLHS([1,3,2,2,5,2,3,7]))
    print(s.findLHS([1,1,1,1]))
    print(s.findLHS([1,2,3,4]))