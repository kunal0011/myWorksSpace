class Solution:
    def heightChecker(self, heights):
        # Create a sorted version of the heights
        sorted_heights = sorted(heights)

        # Count how many students are out of order
        count = 0
        for original, sorted_ in zip(heights, sorted_heights):
            if original != sorted_:
                count += 1

        return count


# Example usage
solution = Solution()
print(solution.heightChecker([1, 1, 4, 2, 1, 3]))  # Output: 3
print(solution.heightChecker([5, 1, 2, 3, 4]))     # Output: 5
