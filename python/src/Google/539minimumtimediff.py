"""
LeetCode 539 - Minimum Time Difference

Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes difference 
between any two time points in the list.

Logic:
1. Convert each time to minutes since midnight (00:00)
2. Sort the converted minutes
3. Compare adjacent times and also first with last (for circular comparison)
4. Find minimum difference considering the circular nature of time (24 hours)

Time Complexity: O(n log n) due to sorting
Space Complexity: O(n) to store converted minutes
"""


class Solution:
    def findMinDifference(self, timePoints: list[str]) -> int:
        def convert_to_minutes(time: str) -> int:
            hours, minutes = map(int, time.split(':'))
            return hours * 60 + minutes

        # Convert all times to minutes
        minutes = sorted(convert_to_minutes(time) for time in timePoints)

        # Initialize minimum difference with the difference between last and first time
        # considering the circular nature (24 hours = 1440 minutes)
        n = len(minutes)
        min_diff = min(minutes[0] - minutes[-1] +
                       1440, minutes[-1] - minutes[0])

        # Compare adjacent times
        for i in range(1, n):
            diff = minutes[i] - minutes[i-1]
            min_diff = min(min_diff, diff)

        return min_diff


def run_test_cases():
    solution = Solution()
    test_cases = [
        {
            "timePoints": ["23:59", "00:00"],
            "expected": 1,
            "explanation": "Between 23:59 and 00:00 there is 1 minute"
        },
        {
            "timePoints": ["00:00", "23:59", "00:00"],
            "expected": 0,
            "explanation": "Two times are same (00:00)"
        },
        {
            "timePoints": ["00:00", "04:00", "22:00"],
            "expected": 120,
            "explanation": "Minimum difference is between 22:00 and 00:00"
        },
        {
            "timePoints": ["12:12", "00:13"],
            "expected": 721,
            "explanation": "Between 00:13 and 12:12"
        }
    ]

    for i, test in enumerate(test_cases, 1):
        result = solution.findMinDifference(test["timePoints"])
        print(f"\nTest Case {i}:")
        print(f"Time Points: {test['timePoints']}")
        print(f"Expected: {test['expected']} minutes")
        print(f"Got: {result} minutes")
        print(f"Explanation: {test['explanation']}")
        print(f"{'✓ Passed' if result == test['expected'] else '✗ Failed'}")


if __name__ == "__main__":
    run_test_cases()
