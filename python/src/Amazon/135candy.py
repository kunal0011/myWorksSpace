class Solution:
    def candy(self, ratings):
        # Number of children
        n = len(ratings)
        if n == 0:
            return 0

        # Initialize a candies array where each child gets at least one candy
        candies = [1] * n

        # Left-to-right pass
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        # Right-to-left pass
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        # The total candies is the sum of the candies array
        return sum(candies)

# Test the solution with different cases


def test_solution():
    solution = Solution()

    # Test case 1: simple increasing and decreasing ratings
    ratings = [1, 0, 2]
    expected = 5  # [2, 1, 2]
    assert solution.candy(
        ratings) == expected, f"Test case 1 failed: {solution.candy(ratings)}"

    # Test case 2: uniform ratings
    ratings = [1, 1, 1]
    expected = 3  # [1, 1, 1]
    assert solution.candy(
        ratings) == expected, f"Test case 2 failed: {solution.candy(ratings)}"

    # Test case 3: increasing ratings
    ratings = [1, 2, 3]
    expected = 6  # [1, 2, 3]
    assert solution.candy(
        ratings) == expected, f"Test case 3 failed: {solution.candy(ratings)}"

    # Test case 4: decreasing ratings
    ratings = [3, 2, 1]
    expected = 6  # [3, 2, 1]
    assert solution.candy(
        ratings) == expected, f"Test case 4 failed: {solution.candy(ratings)}"

    # Test case 5: zigzag ratings
    ratings = [1, 2, 2]
    expected = 4  # [1, 2, 1]
    assert solution.candy(
        ratings) == expected, f"Test case 5 failed: {solution.candy(ratings)}"

    print("All test cases passed!")


# Run the test function
test_solution()
