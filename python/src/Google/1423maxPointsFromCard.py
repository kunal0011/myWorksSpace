"""
LeetCode 1423: Maximum Points You Can Obtain from Cards

There are several cards arranged in a row, and each card has an associated number of points.
In one step, you can take one card from the beginning or from the end of the row.
You have to take exactly k cards.
Your score is the sum of the points of the cards you have taken.
Given the integer array cardPoints and the integer k, return the maximum score you can obtain.

Time Complexity: O(k)
Space Complexity: O(1)
"""
from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        total_sum = sum(cardPoints)

        if k == n:
            return total_sum  # If k equals the number of cards, take all cards

        # Find the minimum sum of n-k cards
        window_size = n - k
        current_window_sum = sum(cardPoints[:window_size])
        min_window_sum = current_window_sum

        for i in range(1, k + 1):
            current_window_sum += cardPoints[window_size +
                                             i - 1] - cardPoints[i - 1]
            min_window_sum = min(min_window_sum, current_window_sum)

        # The maximum score is the total sum minus the minimum subarray sum
        return total_sum - min_window_sum


def test_max_score():
    solution = Solution()

    # Test case 1
    cardPoints1 = [1, 2, 3, 4, 5, 6, 1]
    k1 = 3
    assert solution.maxScore(cardPoints1, k1) == 12, "Test case 1 failed"

    # Test case 2
    cardPoints2 = [2, 2, 2]
    k2 = 2
    assert solution.maxScore(cardPoints2, k2) == 4, "Test case 2 failed"

    # Test case 3
    cardPoints3 = [9, 7, 7, 9, 7, 7, 9]
    k3 = 7
    assert solution.maxScore(cardPoints3, k3) == 55, "Test case 3 failed"

    print("All test cases passed!")


if __name__ == "__main__":
    test_max_score()
