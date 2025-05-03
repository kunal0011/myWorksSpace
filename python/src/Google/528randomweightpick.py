"""
LeetCode 528 - Random Pick with Weight

You are given a 0-indexed array of positive integers w where w[i] describes the weight of the ith index.
You need to implement the function pickIndex(), which randomly picks an index in the range [0, w.length - 1]
(inclusive) and returns it. The probability of picking an index i is w[i] / sum(w).

Logic:
- Create a prefix sum array where each element represents cumulative sum up to that index
- When picking an index:
  1. Generate random number between 1 and total sum
  2. Use binary search to find the index where this number would fit in prefix sums
  3. This ensures probability of picking index i is proportional to w[i]

Time Complexity: 
- Constructor: O(n) to build prefix sums
- pickIndex: O(log n) using binary search
Space Complexity: O(n) for prefix sums array
"""

import random
import bisect


class Solution:
    def __init__(self, w: list[int]):
        # Create a cumulative sum array
        self.prefix_sums = []
        cumulative_sum = 0
        for weight in w:
            cumulative_sum += weight
            self.prefix_sums.append(cumulative_sum)
        self.total_sum = cumulative_sum

    def pickIndex(self) -> int:
        # Generate a random number in the range [1, total_sum]
        target = random.randint(1, self.total_sum)

        # Use binary search to find the target within the prefix_sums array
        index = bisect.bisect_left(self.prefix_sums, target)
        return index


def run_test_cases():
    # Test Case 1: Basic weights
    print("Test Case 1: weights = [1, 3]")
    solution1 = Solution([1, 3])
    frequency = {0: 0, 1: 0}
    trials = 10000

    for _ in range(trials):
        index = solution1.pickIndex()
        frequency[index] += 1

    print(f"After {trials} trials:")
    print(
        f"Index 0 picked: {frequency[0]} times ({frequency[0]/trials*100:.2f}%) - Expected ~25%")
    print(
        f"Index 1 picked: {frequency[1]} times ({frequency[1]/trials*100:.2f}%) - Expected ~75%")

    # Test Case 2: Equal weights
    print("\nTest Case 2: weights = [1, 1, 1]")
    solution2 = Solution([1, 1, 1])
    frequency = {0: 0, 1: 0, 2: 0}

    for _ in range(trials):
        index = solution2.pickIndex()
        frequency[index] += 1

    print(f"After {trials} trials:")
    for i in range(3):
        print(
            f"Index {i} picked: {frequency[i]} times ({frequency[i]/trials*100:.2f}%) - Expected ~33.33%")


if __name__ == "__main__":
    run_test_cases()
