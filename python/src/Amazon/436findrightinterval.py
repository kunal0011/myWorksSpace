"""
LeetCode 436 - Find Right Interval

Problem Statement:
-----------------
You are given an array of intervals, where intervals[i] = [starti, endi] and each starti is unique.

The right interval for an interval i is an interval j such that startj >= endi and startj is minimized. 
Note that i may equal j.

Return an array of right interval indices for each interval i. If no right interval exists for interval i, 
then put -1 at index i.

Key Points:
----------
1. All start times are unique
2. Need to find smallest start time that's >= current end time
3. Uses binary search for efficient lookup
4. Need to maintain original indices while sorting
5. Result array should maintain original order

Examples:
--------
Input: intervals = [[1,2]]
Output: [-1]
Explanation: There is only one interval in the collection, so it outputs -1.

Input: intervals = [[3,4],[2,3],[1,2]]
Output: [-1,0,1]
Explanation:
- For [3,4], no interval has start >= 4, so we put -1.
- For [2,3], intervals[0] has start 3 >= 3, so we put 0.
- For [1,2], intervals[1] has start 2 >= 2, so we put 1.

Constraints:
-----------
* 1 <= intervals.length <= 2 * 10^4
* intervals[i].length == 2
* -10^6 <= starti <= endi <= 10^6
* The start point of each interval is unique
"""

from typing import List
import bisect


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        """
        Find the right interval indices for each interval using binary search.
        
        Algorithm:
        1. Create sorted list of (start_time, original_index) pairs
        2. For each interval, use binary search to find smallest start >= current end
        3. Return -1 if no such interval exists
        
        Time Complexity: O(n log n) for sorting and binary search
        Space Complexity: O(n) for storing starts array
        """
        # Create sorted list of (start, index) pairs
        starts = sorted((interval[0], i) for i, interval in enumerate(intervals))
        
        result = []
        for interval in intervals:
            # Find smallest start time >= current end time
            end = interval[1]
            idx = bisect.bisect_left(starts, (end,))
            
            # If found, add its original index, else add -1
            result.append(starts[idx][1] if idx < len(starts) else -1)
            
        return result


def test_find_right_interval():
    """
    Test driver for the find right interval problem
    """
    test_cases = [
        (
            [[1, 2]],
            [-1]  # Single interval case
        ),
        (
            [[3, 4], [2, 3], [1, 2]],
            [-1, 0, 1]  # Multiple intervals, mixed results
        ),
        (
            [[1, 4], [2, 3], [3, 4]],
            [-1, 2, -1]  # Multiple intervals with same end time
        ),
        (
            [[1, 2], [2, 3], [3, 4], [4, 5]],
            [1, 2, 3, -1]  # Sequential intervals
        ),
        (
            [[4, 5], [2, 3], [1, 2], [3, 4]],
            [-1, 3, 1, 0]  # Unsorted intervals
        ),
        (
            [[1, 1]],
            [-1]  # Start equals end
        ),
        (
            [[1, 2], [2, 2], [3, 3]],
            [1, 2, -1]  # Some intervals with equal start and end
        ),
        (
            [[-5, -4], [-4, -3], [-3, -2], [-2, -1]],
            [1, 2, 3, -1]  # Negative values
        )
    ]
    
    solution = Solution()
    
    for i, (intervals, expected) in enumerate(test_cases, 1):
        result = solution.findRightInterval(intervals)
        status = "PASSED" if result == expected else "FAILED"
        print(f"Test case {i}: {status}")
        print(f"Input intervals: {intervals}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print("-" * 40)

if __name__ == "__main__":
    test_find_right_interval()
