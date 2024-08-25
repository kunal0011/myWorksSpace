from typing import List


class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = []
        to_remove = len(nums) - k

        for num in nums:
            # Pop from the stack while conditions are met
            while stack and num < stack[-1] and to_remove > 0:
                stack.pop()
                to_remove -= 1
            # Add current number to the stack
            stack.append(num)

        # Return only the first k elements of the stack
        return stack[:k]
