class Solution:
    def findDuplicates(self, nums):
        res = []

        for num in nums:
            # Use the absolute value as index
            index = abs(num) - 1

            # If the number at this index is negative, it's a duplicate
            if nums[index] < 0:
                res.append(index + 1)
            else:
                # Otherwise, mark it as visited by negating the value
                nums[index] = -nums[index]

        return res
