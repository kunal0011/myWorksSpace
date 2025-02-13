"""
LeetCode 135. Candy

Problem Statement:
There are n children standing in a line. Each child is assigned a rating value given in an integer array ratings.
You are giving candies to these children subjected to the following requirements:
- Each child must have at least one candy.
- Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.

Example 1:
Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.

Example 2:
Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.

Constraints:
- n == ratings.length
- 1 <= n <= 2 * 10^4
- 0 <= ratings[i] <= 2 * 10^4
"""

from typing import List, Tuple


class Solution:
    def candy(self, ratings: List[int]) -> int:
        """
        Two-pass solution with O(n) space.
        Time complexity: O(n)
        Space complexity: O(n)
        """
        n = len(ratings)
        candies = [1] * n  # Initialize with 1 candy each

        # Forward pass: compare with left neighbor
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1

        # Backward pass: compare with right neighbor
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1] + 1)

        return sum(candies)

    def candyWithDistribution(self, ratings: List[int]) -> Tuple[int, List[int]]:
        """
        Returns both total candies and distribution array.
        Time complexity: O(n)
        Space complexity: O(n)
        """
        n = len(ratings)
        candies = [1] * n

        # Forward pass
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1

        # Backward pass
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1] + 1)

        return sum(candies), candies


def visualize_distribution(ratings: List[int], candies: List[int]) -> None:
    """
    Helper function to visualize candy distribution.
    """
    print("\nCandy Distribution:")
    print("Index | Rating | Candies")
    print("-" * 25)

    max_rating = max(ratings)
    max_candies = max(candies)

    for i, (rating, candy) in enumerate(zip(ratings, candies)):
        # Create visual bars for ratings and candies
        rating_bar = "█" * int(20 * rating / max_rating)
        candy_bar = "▓" * int(20 * candy / max_candies)

        print(f"{i:5d} | {rating:6d} {rating_bar}")
        print(f"      | {candy:6d} {candy_bar}")
        print("-" * 25)


def verify_distribution(ratings: List[int], candies: List[int]) -> bool:
    """
    Helper function to verify if distribution satisfies all conditions.
    """
    # Check minimum candy condition
    if any(candy < 1 for candy in candies):
        return False

    # Check neighbor condition
    for i in range(len(ratings)):
        if i > 0 and ratings[i] > ratings[i-1] and candies[i] <= candies[i-1]:
            return False
        if i < len(ratings)-1 and ratings[i] > ratings[i+1] and candies[i] <= candies[i+1]:
            return False

    return True


def test_candy():
    """
    Test function with various test cases.
    """
    test_cases = [
        {
            "ratings": [1, 0, 2],
            "expected": 5,
            "description": "Basic case"
        },
        {
            "ratings": [1, 2, 2],
            "expected": 4,
            "description": "Equal ratings"
        },
        {
            "ratings": [1, 3, 2, 2, 1],
            "expected": 7,
            "description": "Peak in middle"
        },
        {
            "ratings": [1, 2, 3, 4, 5],
            "expected": 15,
            "description": "Increasing sequence"
        },
        {
            "ratings": [5, 4, 3, 2, 1],
            "expected": 15,
            "description": "Decreasing sequence"
        }
    ]

    solution = Solution()

    for i, test_case in enumerate(test_cases, 1):
        print(f"\n{'='*80}")
        print(f"Test Case {i}: {test_case['description']}")
        print(f"Ratings: {test_case['ratings']}")

        # Test both implementations
        result1 = solution.candy(test_case['ratings'])
        total_candies, distribution = solution.candyWithDistribution(
            test_case['ratings'])

        print(f"\nResults:")
        print(f"Total candies needed: {total_candies}")

        # Visualize distribution
        visualize_distribution(test_case['ratings'], distribution)

        # Verify distribution
        is_valid = verify_distribution(test_case['ratings'], distribution)
        print(f"\nDistribution validity check: {'✓' if is_valid else '✗'}")

        assert result1 == test_case['expected'], \
            f"Basic approach failed. Expected {test_case['expected']}, got {result1}"
        assert total_candies == test_case['expected'], \
            f"Distribution approach failed. Expected {test_case['expected']}, got {total_candies}"
        assert is_valid, "Invalid candy distribution!"

        print("✓ Test case passed!")

    print("\nAll test cases passed! 🎉")


if __name__ == "__main__":
    test_candy()
