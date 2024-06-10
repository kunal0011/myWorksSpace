
from collections import defaultdict
from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = defaultdict(list)

        for i in range(len(nums)):
                d[nums[i]].append(i)
        #print(d)

        for k1, v in d.items():
             if len(v) >= 2:
                    for vi in range(len(v)):
                          for vj in range(vi+1,len(v)):
                                if v[vj]-v[vi] <= k:
                                      return True
        return False

class Solution1:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mp = {}
        for i, v in enumerate(nums):
            if v in mp and i - mp[v] <= k:
                return True
            mp[v] = i
        return False

if __name__ == '__main__':

     s = Solution1()
     print(s.containsNearbyDuplicate([1,2,3,1],3))
     print(s.containsNearbyDuplicate([1,0,1,1],1))
     print(s.containsNearbyDuplicate([1,2,3,1,2,3],2))