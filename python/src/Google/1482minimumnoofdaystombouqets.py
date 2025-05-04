"""
LeetCode 1482. Minimum Number of Days to Make m Bouquets

Problem Statement:
You are given an integer array bloomDay, an integer m and an integer k.
You want to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden.
The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] and then can be used in exactly one bouquet.
Return the minimum number of days you need to wait to be able to make m bouquets from the garden. If it is impossible to make m bouquets return -1.

Time Complexity: O(n * log(maxDay)) where n is length of bloomDay array
Space Complexity: O(1) as we only use constant extra space
"""

from typing import List


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        # Logic:
        # 1. Use binary search to find minimum days needed
        # 2. For each mid point (days), check if we can make m bouquets:
        #    - Count consecutive bloomed flowers
        #    - When k flowers are found, that's one bouquet
        #    - If we can make m bouquets, try fewer days
        #    - If we can't, try more days
        # 3. Binary search range: min(bloomDay) to max(bloomDay)

        # Helper function to determine if we can make m bouquets in 'days'
        def canMakeBouquets(days: int) -> bool:
            bouquets = 0
            flowers = 0
            for bloom in bloomDay:
                if bloom <= days:
                    flowers += 1
                    # If we have enough flowers for a bouquet
                    if flowers == k:
                        bouquets += 1
                        flowers = 0  # Reset the flower counter for the next bouquet
                else:
                    flowers = 0  # Reset if a flower hasn't bloomed

                if bouquets >= m:
                    return True

            return bouquets >= m

        # Edge case: if there are not enough flowers to make m bouquets
        if len(bloomDay) < m * k:
            return -1

        # Binary search for the minimum day
        left, right = min(bloomDay), max(bloomDay)

        while left < right:
            mid = (left + right) // 2
            if canMakeBouquets(mid):
                right = mid  # Try for fewer days
            else:
                left = mid + 1  # Increase the days

        return left if canMakeBouquets(left) else -1


# Test driver
if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = [
        ([1, 10, 3, 10, 2], 3, 1),     # Expected: 3
        ([1, 10, 3, 10, 2], 3, 2),     # Expected: -1
        ([7, 7, 7, 7, 12, 7, 7], 2, 3),  # Expected: 12
        ([1000, 2000, 3000, 4000], 2, 2)  # Expected: 3000
    ]

    for i, (bloomDay, m, k) in enumerate(test_cases):
        result = solution.minDays(bloomDay, m, k)
        print(f"Test case {i + 1}:")
        print(f"Bloom days: {bloomDay}")
        print(f"m (bouquets needed): {m}")
        print(f"k (flowers per bouquet): {k}")
        print(f"Minimum days needed: {result}")
        print()
