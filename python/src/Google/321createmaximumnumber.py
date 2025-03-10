class Solution:
    def maxNumber(self, nums1, nums2, k):
        def merge(nums1, nums2):
            return [max(nums1, nums2).pop(0) for _ in range(len(nums1) + len(nums2))]

        def getMaxArray(nums, t):
            drop = len(nums) - t
            stack = []
            for num in nums:
                while drop and stack and stack[-1] < num:
                    stack.pop()
                    drop -= 1
                stack.append(num)
            return stack[:t]

        return max(merge(getMaxArray(nums1, i), getMaxArray(nums2, k - i))
                   for i in range(k + 1)
                   if i <= len(nums1) and k - i <= len(nums2))
