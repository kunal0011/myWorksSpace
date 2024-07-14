from typing import List


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        n = len(customers)

        # Calculate initially satisfied customers
        initially_satisfied = sum(customers[i]
                                  for i in range(n) if grumpy[i] == 0)

        # Calculate the additional satisfied customers we can gain
        max_additional_satisfied = 0
        current_additional_satisfied = 0
        left = 0

        for right in range(n):
            if grumpy[right] == 1:
                current_additional_satisfied += customers[right]

            # Slide the window
            if right - left + 1 > X:
                if grumpy[left] == 1:
                    current_additional_satisfied -= customers[left]
                left += 1

            # Update max_additional_satisfied
            max_additional_satisfied = max(
                max_additional_satisfied, current_additional_satisfied)

        return initially_satisfied + max_additional_satisfied


# Example usage:
sol = Solution()
customers = [1, 0, 1, 2, 1, 1, 7, 5]
grumpy = [0, 1, 0, 1, 0, 1, 0, 1]
X = 3
print(sol.maxSatisfied(customers, grumpy, X))  # Output: 16
