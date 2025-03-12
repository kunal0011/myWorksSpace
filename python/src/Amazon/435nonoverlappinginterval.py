"""
LeetCode 435 - Non-overlapping Intervals

Problem Statement:
-----------------
Given an array of intervals intervals where intervals[i] = [starti, endi], return the 
minimum number of intervals you need to remove to make the rest of the intervals 
non-overlapping.

Key Points:
----------
1. Intervals can be in any order
2. Need to find minimum number of intervals to remove
3. Two intervals [a,b] and [c,d] are overlapping if b > c
4. Uses greedy approach by sorting by end time
5. Similar to activity selection problem

Examples:
--------
Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.

Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.

Constraints:
-----------
* 1 <= intervals.length <= 10^5
* intervals[i].length == 2
* -5 * 10^4 <= starti < endi <= 5 * 10^4
"""

from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        Find minimum number of intervals to remove to make rest non-overlapping.
        
        Algorithm:
        1. Sort intervals by end time (greedy approach)
        2. Keep track of last non-overlapping interval's end time
        3. If current interval starts before last end time, it overlaps
        4. When overlap found, increment counter (we remove the current interval)
        5. When no overlap, update end time to current interval's end time
        
        Time Complexity: O(n log n) due to sorting
        Space Complexity: O(1) for in-place sorting
        """
        if not intervals:
            return 0

        # Sort intervals by end time for greedy approach
        intervals.sort(key=lambda x: x[1])
        n = len(intervals)
        count = 0          # Count of intervals to remove
        end = float('-inf')  # End time of last non-overlapping interval

        for start, finish in intervals:
            if start >= end:
                # No overlap, update end time
                end = finish
            else:
                # Overlap found, need to remove this interval
                count += 1

        return count


def test_erase_overlap_intervals():
    """
    Test driver for the non-overlapping intervals problem
    """
    test_cases = [
        (
            [[1,2], [2,3], [3,4], [1,3]],
            1  # Remove [1,3]
        ),
        (
            [[1,2], [1,2], [1,2]],
            2  # Remove two [1,2]
        ),
        (
            [[1,2], [2,3]],
            0  # Already non-overlapping
        ),
        (
            [[1,100], [11,22], [1,11], [2,12]],
            2  # Complex case with multiple overlaps
        ),
        (
            [],
            0  # Empty case
        ),
        (
            [[1,2]],
            0  # Single interval
        ),
        (
            [[1,5], [2,3], [3,4], [4,5]],
            2  # Nested intervals
        ),
        (
            [[-100,-2], [-1,0], [0,2], [1,3]],
            1  # Intervals with negative values
        )
    ]
    
    solution = Solution()
    
    for i, (intervals, expected) in enumerate(test_cases, 1):
        result = solution.eraseOverlapIntervals(intervals)
        status = "PASSED" if result == expected else "FAILED"
        print(f"Test case {i}: {status}")
        print(f"Input intervals: {intervals}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print("-" * 40)

if __name__ == "__main__":
    test_erase_overlap_intervals()
