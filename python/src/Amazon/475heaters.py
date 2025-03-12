"""
LeetCode 475 - Heaters

Problem Statement:
-----------------
Winter is coming! During the contest, your first job is to design a standard heater with a fixed warm radius to warm all the houses.

Every house can be warmed, as long as the house is within the heater's warm radius range.
Given the positions of houses and heaters on a horizontal line, return the minimum radius standard of heaters so that those heaters could cover all houses.

Notice that all the heaters follow your radius standard, and the warm radius will be the same.

Examples:
--------
Input: houses = [1,2,3], heaters = [2]
Output: 1
Explanation: The only heater was placed in the position 2, and if we use the radius 1, all houses can be warmed.

Input: houses = [1,2,3,4], heaters = [1,4]
Output: 1
Explanation: The two heaters were placed at positions 1 and 4.
We need at least a radius of 1 to cover all houses.

Input: houses = [1,5], heaters = [2]
Output: 3
Explanation: The heater was placed at position 2. We need a radius of 3 to warm both houses.

Constraints:
-----------
* 1 <= houses.length, heaters.length <= 3 * 10^4
* 1 <= houses[i], heaters[i] <= 10^9
* All integers are unique
"""

from typing import List
import bisect


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        """
        Find the minimum radius needed for heaters to warm all houses.
        
        Algorithm:
        1. Sort both houses and heaters arrays for binary search
        2. For each house:
           - Find the closest heater using binary search
           - Calculate distances to left and right heaters
           - Take the minimum of these distances
        3. The required radius is the maximum of all minimum distances
        
        Time Complexity: O(nlogn + mlogm) where n = len(houses), m = len(heaters)
        - O(nlogn) for sorting houses
        - O(mlogm) for sorting heaters
        - O(nlogm) for binary search for each house
        
        Space Complexity: O(1) - only constant extra space needed
        """
        # Sort both arrays to enable binary search
        houses.sort()
        heaters.sort()
        max_radius = 0
        
        for house in houses:
            # Find insertion point for current house in heaters array
            idx = bisect.bisect_left(heaters, house)
            
            # Calculate distances to nearest heaters on both sides
            left_dist = float('inf') if idx == 0 else house - heaters[idx - 1]
            right_dist = float('inf') if idx == len(heaters) else heaters[idx] - house
            
            # Update max_radius if necessary
            curr_min_dist = min(left_dist, right_dist)
            max_radius = max(max_radius, curr_min_dist)
        
        return max_radius


def test_heaters():
    """
    Comprehensive test driver for heaters problem
    """
    test_cases = [
        (
            [1, 2, 3],
            [2],
            1,
            "Basic test case with one central heater"
        ),
        (
            [1, 2, 3, 4],
            [1, 4],
            1,
            "Two heaters at ends"
        ),
        (
            [1, 5],
            [2],
            3,
            "One heater with distant houses"
        ),
        (
            [1],
            [1],
            0,
            "House and heater at same position"
        ),
        (
            [1, 2, 3, 4, 5],
            [1, 3, 5],
            1,
            "Multiple heaters spaced evenly"
        ),
        (
            [1, 10, 20],
            [2, 19],
            2,
            "Sparse distribution"
        ),
        (
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            [2, 5, 8],
            2,
            "Multiple heaters with multiple houses"
        ),
        (
            [1],
            [2],
            1,
            "Single house and distant heater"
        ),
        (
            [1, 999],
            [499, 500, 501],
            498,
            "Large distance between houses"
        ),
        (
            [1, 2, 3, 4],
            [1, 2, 3, 4],
            0,
            "Each house has its own heater"
        )
    ]
    
    solution = Solution()
    
    for i, (houses, heaters, expected, description) in enumerate(test_cases, 1):
        result = solution.findRadius(houses.copy(), heaters.copy())
        status = "PASSED" if result == expected else "FAILED"
        print(f"\nTest case {i}: {status}")
        print(f"Description: {description}")
        print(f"Houses: {houses}")
        print(f"Heaters: {heaters}")
        print(f"Expected radius: {expected}")
        print(f"Got radius: {result}")
        if result != expected:
            print(f"Note: Check distance calculation logic")
        print("-" * 40)

if __name__ == "__main__":
    test_heaters()
