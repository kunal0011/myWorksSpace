from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False

        # Initialize a stack to keep track of possible 132 patterns
        stack = []
        # This variable holds the potential value for nums[k] in the 132 pattern
        third = float('-inf')

        # Traverse the array from right to left to simulate j and k
        for i in range(n - 1, -1, -1):
            # If nums[i] (which would be the candidate for nums[i]) is smaller than third (nums[k])
            if nums[i] < third:
                return True
            # Maintain a decreasing stack; stack[j] is the middle of the pattern
            while stack and nums[i] > stack[-1]:
                third = stack.pop()
            # Add the current element to the stack as a potential candidate for nums[j]
            stack.append(nums[i])

        return False
