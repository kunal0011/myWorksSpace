class Solution:
    def maxDistance(self, colors):
        n = len(colors)

        # Check maximum distance from the start and end
        max_dist_start = 0
        max_dist_end = 0

        # From start to end
        for i in range(n):
            if colors[i] != colors[n - 1]:  # Compare with last element
                max_dist_start = max(max_dist_start, n - 1 - i)

        # From end to start
        for i in range(n - 1, -1, -1):
            if colors[i] != colors[0]:  # Compare with first element
                max_dist_end = max(max_dist_end, i)

        return max(max_dist_start, max_dist_end)


# Testing the solution
if __name__ == "__main__":
    solution = Solution()

    # Test case
    colors = [1, 1, 2, 3, 2, 1]
    print("Maximum Distance:", solution.maxDistance(
        colors))  # Expected output: 4
