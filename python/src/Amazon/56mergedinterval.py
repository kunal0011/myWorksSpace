from typing import List

"""
LeetCode 56. Merge Intervals

Problem Statement:
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Constraints:
- 1 <= intervals.length <= 10^4
- intervals[i].length == 2
- 0 <= starti <= endi <= 10^4
"""


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort intervals based on start time
        intervals.sort(key=lambda x: x[0])

        # Initialize result with first interval
        merged = [intervals[0]]

        # Process remaining intervals
        for current in intervals[1:]:
            # Get the last interval from merged list
            previous = merged[-1]

            # If current interval overlaps with previous
            if current[0] <= previous[1]:
                # Merge by updating end time of previous interval
                previous[1] = max(previous[1], current[1])
            else:
                # No overlap, add current interval to result
                merged.append(current)

        return merged


def explain_merge(intervals: List[List[int]]) -> None:
    """
    Function to explain the interval merging process step by step
    """
    print(f"\nMerging intervals: {intervals}")
    print("=" * 50)

    if not intervals:
        print("Empty input")
        return []

    # Sort intervals
    intervals.sort(key=lambda x: x[0])
    print(f"Sorted intervals: {intervals}")

    merged = [intervals[0]]
    print(f"\nInitialize result with first interval: {merged}")

    for i, current in enumerate(intervals[1:], 1):
        previous = merged[-1]
        print(f"\nStep {i}:")
        print(f"Current interval: {current}")
        print(f"Previous merged interval: {previous}")

        if current[0] <= previous[1]:
            # Overlap found
            old_end = previous[1]
            previous[1] = max(previous[1], current[1])
            print(f"Overlap detected! Merging...")
            print(f"Updated end time from {old_end} to {previous[1]}")
            print(f"Current merged intervals: {merged}")
        else:
            # No overlap
            merged.append(current)
            print(f"No overlap. Adding new interval")
            print(f"Current merged intervals: {merged}")

    print(f"\nFinal merged intervals: {merged}")
    return merged


def test_merge_intervals():
    """
    Test function to verify the solution with various test cases
    """
    solution = Solution()

    test_cases = [
        {
            "intervals": [[1, 3], [2, 6], [8, 10], [15, 18]],
            "expected": [[1, 6], [8, 10], [15, 18]],
            "description": "Basic case with one merge"
        },
        {
            "intervals": [[1, 4], [4, 5]],
            "expected": [[1, 5]],
            "description": "Touching intervals"
        },
        {
            "intervals": [[1, 4], [2, 3]],
            "expected": [[1, 4]],
            "description": "Completely overlapping intervals"
        },
        {
            "intervals": [[1, 4], [0, 4]],
            "expected": [[0, 4]],
            "description": "Earlier start time"
        },
        {
            "intervals": [[1, 4], [2, 3], [3, 6]],
            "expected": [[1, 6]],
            "description": "Multiple overlapping intervals"
        },
        {
            "intervals": [[1, 1]],
            "expected": [[1, 1]],
            "description": "Single interval"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        intervals = test_case["intervals"]
        expected = test_case["expected"]
        description = test_case["description"]

        print(f"\nRunning test case {i}: {description}")
        print(f"Input intervals: {intervals}")

        result = solution.merge(intervals.copy())

        assert result == expected, \
            f"\nTest case {i} failed!\nExpected: {expected}\nGot: {result}"
        print(f"✓ Test case {i} passed!")


if __name__ == "__main__":
    try:
        test_merge_intervals()
        print("\nAll test cases passed successfully! 🎉")

        # Explain with detailed examples
        explain_merge([[1, 3], [2, 6], [8, 10], [15, 18]])
        explain_merge([[1, 4], [4, 5]])
    except AssertionError as e:
        print(f"Test failed! {str(e)}")
