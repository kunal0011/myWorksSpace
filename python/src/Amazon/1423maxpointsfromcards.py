class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        n = len(cardPoints)
        # Total points of all cards
        total_points = sum(cardPoints)

        # Length of the subarray that we don't take
        window_size = n - k

        # Initial sum of the first window of size n - k
        min_subarray_sum = sum(cardPoints[:window_size])
        current_window_sum = min_subarray_sum

        # Sliding window to find the minimum sum of a subarray of size n - k
        for i in range(1, n - window_size + 1):
            # Move the window by subtracting the element that goes out and adding the new element
            current_window_sum = current_window_sum - \
                cardPoints[i - 1] + cardPoints[i + window_size - 1]
            min_subarray_sum = min(min_subarray_sum, current_window_sum)

        # The maximum score is the total points minus the minimum sum of the subarray we found
        return total_points - min_subarray_sum
