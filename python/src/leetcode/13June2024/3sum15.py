from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l = []
        ### This solution time linit Exceeded
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         for k in range(j + 1, len(nums)):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 l1 = [nums[i],nums[j],nums[k]]
        #                 l1.sort()
        #                 if l1 not in l:
        #                     l.append(l1)
        # return l
        # s = set()

        nums.sort()
        result = []
        n = len(nums)

        for i in range(n - 2):
            # Skip the same element to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Initialize two pointers
            left, right = i + 1, n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    # Move left and right to the next different numbers to avoid duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return result


if __name__ == "__main__":
    s = Solution()
    print(s.threeSum([3, 0, -2, -1, 1, 2]))
