class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # The formula calculates how many odd numbers are between low and high
        return (high + 1) // 2 - low // 2


# Testing
solution = Solution()
low, high = 3, 7
print("Python Test Result:", solution.countOdds(
    low, high))  # Output should be 3
