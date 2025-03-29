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
# Instead of directly picking k cards from the beginning or end, you can think about the problem in a complementary way:

# Instead of finding the maximum k cards from either end, find the minimum sum of the n-k cards in the middle (since you can only pick cards from the beginning or end).
# The idea is that the sum of the k cards you pick is the total sum of all cards minus the sum of the n-k cards that you do not pick.
# The problem then reduces to finding the minimum sum of a subarray of length n-k.
# Steps:
# Calculate the total sum of all cards.
# Calculate the sum of the first n-k cards.
# Slide this window across the array from the start to the end, updating the minimum sum found.
# The result is the total sum of all cards minus the minimum sum of the n-k subarray.
