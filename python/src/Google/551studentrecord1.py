"""
LeetCode 551 - Student Attendance Record I

You are given a string s representing an attendance record for a student where each character signifies:
- 'A': Absent
- 'L': Late
- 'P': Present

The student is eligible for an attendance award if they meet both criteria:
1. The student was absent ('A') for strictly fewer than 2 days total
2. The student was never late ('L') for 3 or more consecutive days

Return true if the student is eligible for an attendance award, or false otherwise.

Logic:
1. Count total number of 'A's - must be less than 2
2. Check for 3 consecutive 'L's - must not exist
- Using string count() and substring search is optimal for short strings
- For very long strings, we could iterate once through the string

Time Complexity: O(n) where n is length of string
Space Complexity: O(1)
"""


class Solution:
    def checkRecord(self, s: str) -> bool:
        # Check if there's more than 1 'A' or if there are more than 2 consecutive 'L's
        return s.count('A') <= 1 and 'LLL' not in s


def run_test_cases():
    solution = Solution()
    test_cases = [
        {
            "record": "PPALLP",
            "expected": True,
            "explanation": "One absent (A) and two late (L) days, not consecutive"
        },
        {
            "record": "PPALLL",
            "expected": False,
            "explanation": "Three consecutive late (L) days"
        },
        {
            "record": "PPALLAP",
            "expected": False,
            "explanation": "Two absent (A) days"
        },
        {
            "record": "LALL",
            "expected": True,
            "explanation": "One absent day, late days not consecutive"
        }
    ]

    for i, test in enumerate(test_cases, 1):
        result = solution.checkRecord(test["record"])
        print(f"\nTest Case {i}:")
        print(f"Attendance Record: {test['record']}")
        print(f"Expected: {test['expected']}")
        print(f"Got: {result}")
        print(f"Explanation: {test['explanation']}")
        print(f"{'✓ Passed' if result == test['expected'] else '✗ Failed'}")


if __name__ == "__main__":
    run_test_cases()
