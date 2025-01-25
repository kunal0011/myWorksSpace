from typing import List

"""
LeetCode 57. Insert Interval

Problem Statement:
You are given an array of non-overlapping intervals intervals where 
intervals[i] = [starti, endi] represent the start and the end of the ith interval
and intervals is sorted in ascending order by starti. You are also given an interval
newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order
by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

Constraints:
- 0 <= intervals.length <= 10^4
- intervals[i].length == 2
- 0 <= starti <= endi <= 10^5
- intervals is sorted by starti in ascending order
- newInterval.length == 2
- 0 <= start <= end <= 10^5
"""


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i = 0
        n = len(intervals)

        # Add all intervals that come before newInterval
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        # Merge overlapping intervals
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        # Add the merged interval
        result.append(newInterval)

        # Add remaining intervals
        while i < n:
            result.append(intervals[i])
            i += 1

        return result


def explain_insert(intervals: List[List[int]], newInterval: List[int]) -> None:
    """
    Function to explain the interval insertion process step by step
    """
    print(f"\nInserting interval {newInterval} into {intervals}")
    print("=" * 50)

    result = []
    i = 0
    n = len(intervals)

    # Phase 1: Add intervals before newInterval
    print("\nPhase 1: Adding intervals before new interval")
    while i < n and intervals[i][1] < newInterval[0]:
        result.append(intervals[i])
        print(f"Adding interval {intervals[i]} (comes before new interval)")
        i += 1
    print(f"Current result: {result}")

    # Phase 2: Merge overlapping intervals
    print("\nPhase 2: Merging overlapping intervals")
    merged_interval = newInterval.copy()
    overlapping_found = False

    while i < n and intervals[i][0] <= newInterval[1]:
        overlapping_found = True
        old_start, old_end = merged_interval
        merged_interval[0] = min(merged_interval[0], intervals[i][0])
        merged_interval[1] = max(merged_interval[1], intervals[i][1])
        print(f"Merging with interval {intervals[i]}")
        print(
            f"Updated merged interval: {old_start},{old_end} -> {merged_interval}")
        i += 1

    if not overlapping_found:
        print("No overlapping intervals found")

    # Add merged interval
    result.append(merged_interval)
    print(f"Adding merged interval: {merged_interval}")
    print(f"Current result: {result}")

    # Phase 3: Add remaining intervals
    print("\nPhase 3: Adding remaining intervals")
    while i < n:
        result.append(intervals[i])
        print(f"Adding remaining interval {intervals[i]}")
        i += 1

    print(f"\nFinal result: {result}")
    return result


def test_insert_interval():
    """
    Test function to verify the solution with various test cases
    """
    solution = Solution()

    test_cases = [
        {
            "intervals": [[1, 3], [6, 9]],
            "newInterval": [2, 5],
            "expected": [[1, 5], [6, 9]],
            "description": "Basic case with one merge"
        },
        {
            "intervals": [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]],
            "newInterval": [4, 8],
            "expected": [[1, 2], [3, 10], [12, 16]],
            "description": "Multiple merges"
        },
        {
            "intervals": [],
            "newInterval": [5, 7],
            "expected": [[5, 7]],
            "description": "Empty intervals"
        },
        {
            "intervals": [[1, 5]],
            "newInterval": [2, 3],
            "expected": [[1, 5]],
            "description": "Completely contained interval"
        },
        {
            "intervals": [[1, 5]],
            "newInterval": [6, 8],
            "expected": [[1, 5], [6, 8]],
            "description": "No overlap"
        },
        {
            "intervals": [[3, 5], [6, 7], [8, 10]],
            "newInterval": [1, 2],
            "expected": [[1, 2], [3, 5], [6, 7], [8, 10]],
            "description": "Insert at beginning"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        intervals = test_case["intervals"]
        newInterval = test_case["newInterval"]
        expected = test_case["expected"]
        description = test_case["description"]

        print(f"\nRunning test case {i}: {description}")
        print(f"Input intervals: {intervals}")
        print(f"New interval: {newInterval}")

        result = solution.insert(intervals.copy(), newInterval.copy())

        assert result == expected, \
            f"\nTest case {i} failed!\nExpected: {expected}\nGot: {result}"
        print(f"✓ Test case {i} passed!")


if __name__ == "__main__":
    try:
        test_insert_interval()
        print("\nAll test cases passed successfully! 🎉")

        # Explain with detailed examples
        explain_insert([[1, 3], [6, 9]], [2, 5])
        explain_insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8])
    except AssertionError as e:
        print(f"Test failed! {str(e)}")
