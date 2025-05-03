"""
LeetCode 335 - Self Crossing

Problem Statement:
You are given an array of integers distance.
You start at point (0,0) on a 2D plane and move in a straight line based on the integer array distance:
- distance[0] indicates you move north distance[0] units
- distance[1] indicates you move west distance[1] units
- distance[2] indicates you move south distance[2] units
- distance[3] indicates you move east distance[3] units
And so on, alternating between north, west, south, and east.

Return true if your path crosses itself, and false if it doesn't.
"""

from typing import List


class Solution:
    def isSelfCrossing(self, distance: List[int]) -> bool:
        n = len(distance)

        for i in range(3, n):
            # First type: current line crosses the line 3 steps ahead of it
            if distance[i] >= distance[i-2] and distance[i-1] <= distance[i-3]:
                return True

            # Second type: current line crosses the line 4 steps ahead of it
            if i >= 4 and distance[i-1] == distance[i-3] and distance[i] + distance[i-4] >= distance[i-2]:
                return True

            # Third type: current line crosses the line 5 steps ahead of it
            if i >= 5 and distance[i-2] >= distance[i-4] and distance[i] + distance[i-4] >= distance[i-2] and distance[i-1] <= distance[i-3] and distance[i-1] + distance[i-5] >= distance[i-3]:
                return True

        return False


def run_tests():
    solution = Solution()
    
    test_cases = [
        ([2,1,1,2], True),
        ([1,2,3,4], False),
        ([1,1,1,1], True),
        ([1,1,2,2,3,3,4,4], False),
        ([1,1,2,1,1], True),
        ([3,3,3,2,1,1], False)
    ]
    
    for i, (distance, expected) in enumerate(test_cases, 1):
        result = solution.isSelfCrossing(distance)
        print(f"\nTest case {i}:")
        print(f"Distance array: {distance}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print(f"{'✓ Passed' if result == expected else '✗ Failed'}")

if __name__ == "__main__":
    run_tests()
