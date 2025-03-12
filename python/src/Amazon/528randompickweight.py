"""
LeetCode 528 - Random Pick with Weight

You are given a 0-indexed array of positive integers w where w[i] describes the weight of the ith index.

You need to implement the function pickIndex(), which randomly picks an index in the range [0, w.length - 1] 
(inclusive) and returns it. The probability of picking an index i is w[i] / sum(w), i.e., the weight of the 
ith index divided by the sum of all weights.

For example:
- If w = [1, 3], the probability of picking index 0 is 1/(1 + 3) = 0.25 (i.e., 25%), 
  and the probability of picking index 1 is 3/(1 + 3) = 0.75 (i.e., 75%).

Example 1:
Input
["Solution","pickIndex"]
[[[1]],[]]
Output
[null,0]
Explanation
Solution solution = new Solution([1]);
solution.pickIndex(); // return 0. The only option is to return 0 since there is only one element in w.

Example 2:
Input
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
Output
[null,1,1,1,1,0]
Explanation
Solution solution = new Solution([1, 3]);
solution.pickIndex(); // return 1. It's returning the second element (index = 1) that has probability of 3/4.
solution.pickIndex(); // return 1
solution.pickIndex(); // return 1
solution.pickIndex(); // return 1
solution.pickIndex(); // return 0. It's returning the first element (index = 0) that has probability of 1/4.
"""

from typing import List
import random
import bisect
from collections import Counter

class Solution:
    def __init__(self, w: List[int]):
        """
        Initialize data structure with weights array.
        Time complexity: O(n)
        Space complexity: O(n)
        """
        self.prefix_sums = []
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.prefix_sums.append(prefix_sum)
        self.total_sum = prefix_sum

    def pickIndex(self) -> int:
        """
        Returns random index based on weights.
        Time complexity: O(log n)
        Space complexity: O(1)
        """
        target = random.random() * self.total_sum
        return bisect.bisect_left(self.prefix_sums, target)

    def pickIndex_alternative(self) -> int:
        """
        Alternative implementation using binary search directly.
        This shows how bisect_left works under the hood.
        """
        target = random.random() * self.total_sum
        left, right = 0, len(self.prefix_sums) - 1
        
        # Binary search for the first prefix sum larger than target
        while left < right:
            mid = left + (right - left) // 2
            if self.prefix_sums[mid] <= target:
                left = mid + 1
            else:
                right = mid
                
        return left


def test_random_pick_with_weight():
    """
    Test function to verify both solution approaches.
    We'll test the distribution of picked indices to ensure they match expected probabilities.
    """
    def run_distribution_test(weights: List[int], num_trials: int = 10000) -> bool:
        solution = Solution(weights)
        
        # Count occurrences of each index
        counts = Counter()
        for _ in range(num_trials):
            counts[solution.pickIndex()] += 1
            
        # Calculate actual vs expected probabilities
        total_weight = sum(weights)
        expected_probs = [w/total_weight for w in weights]
        actual_probs = [counts[i]/num_trials for i in range(len(weights))]
        
        # Check if distributions are roughly equal (within 5% margin)
        margin = 0.05
        return all(abs(actual - expected) < margin 
                  for actual, expected in zip(actual_probs, expected_probs))

    test_cases = [
        [1],                    # Single weight
        [1, 3],                # Two weights
        [1, 1, 1, 1],          # Equal weights
        [10, 20, 30, 40],      # Increasing weights
        [100, 50, 25, 12, 6],  # Decreasing weights
        [1, 10000],            # Large difference in weights
    ]
    
    for i, weights in enumerate(test_cases, 1):
        # Test distribution
        distribution_ok = run_distribution_test(weights)
        
        print(f"Test {i}:")
        print(f"Weights: {weights}")
        print(f"Distribution Test: {'✓' if distribution_ok else '✗'}")
        
        # Additional verification: specific picks
        solution = Solution(weights)
        picks = [solution.pickIndex() for _ in range(5)]
        print(f"Sample picks: {picks}")
        print(f"All picks valid: {'✓' if all(0 <= p < len(weights) for p in picks) else '✗'}\n")
        
        # Test alternative implementation
        solution_alt = Solution(weights)
        picks_alt = [solution_alt.pickIndex_alternative() for _ in range(5)]
        print(f"Alternative implementation picks: {picks_alt}")
        print(f"All alternative picks valid: {'✓' if all(0 <= p < len(weights) for p in picks_alt) else '✗'}\n")


if __name__ == "__main__":
    test_random_pick_with_weight()