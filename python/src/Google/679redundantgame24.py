from typing import List


class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        EPSILON = 1e-6

        def dfs(nums):
            if len(nums) == 1:
                return abs(nums[0] - 24) < EPSILON

            # Iterate over every possible pair of numbers
            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i != j:
                        # Prepare a new list for the next recursion
                        newNums = []
                        # Add all numbers except nums[i] and nums[j] into newNums
                        for k in range(len(nums)):
                            if k != i and k != j:
                                newNums.append(nums[k])

                        # Try all operations
                        for op in ['+', '-', '*', '/']:
                            # Apply each operation and append the result to newNums
                            if op == '+':
                                newNums.append(nums[i] + nums[j])
                            elif op == '-':
                                newNums.append(nums[i] - nums[j])
                            elif op == '*':
                                newNums.append(nums[i] * nums[j])
                            elif op == '/' and abs(nums[j]) > EPSILON:
                                newNums.append(nums[i] / nums[j])
                            else:
                                continue

                            # Recur to see if this path leads to 24
                            if dfs(newNums):
                                return True

                            # Undo the addition for backtracking
                            newNums.pop()
            return False

        return dfs(nums)
