from typing import List

class Solution1:
    def countPairs(self, nums: List[int], target: int) -> int:   
            nums.sort()  # Sort the array first
            count = 0
            left = 0
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] < target:
                    # If the sum is less than target, then all the pairs with the current left pointer and any index to the right of it will also satisfy the condition.
                    count += right - left
                    left += 1
                else:
                    # If the sum is greater than or equal to the target, we move the right pointer to the left to decrease the sum.
                    right -= 1

            return count







class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        count:int = 0
        for i in range(len(nums)):
             for j in range(i+1,len(nums)):
                  if nums[i]+nums[j]<target:
                       count+=1
                       
        return count
    

if __name__ == '__main__':
        s = Solution1()
        print(s.countPairs([-1,1,2,3,1],2))
        print(s.countPairs([-6,2,5,-2,-7,-1,3],-2))



