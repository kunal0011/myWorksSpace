"""
LeetCode 1736. Latest Time by Replacing Hidden Digits

Problem Statement:
You are given a string time in the form of hh:mm, where some of the digits in the string are hidden
(represented by ?). The valid times are those inclusively between 00:00 and 23:59.
Return the latest valid time you can get from time by replacing the hidden digits.

Time Complexity: O(1) as we process a fixed length string
Space Complexity: O(1) as we use constant extra space
"""


class Solution:
    def maximumTime(self, time: str) -> str:
        # Logic:
        # 1. Process each ? from left to right
        # 2. For first hour digit (time[0]):
        #    - If second digit is ? or ≤ 3, use 2
        #    - Otherwise, use 1
        # 3. For second hour digit (time[1]):
        #    - If first digit is 2, max is 3
        #    - Otherwise, max is 9
        # 4. For first minute digit (time[3]), always use 5
        # 5. For second minute digit (time[4]), always use 9

        # Convert the string into a list to make modifications easier
        time = list(time)

        # Determine the first digit of the hour
        if time[0] == '?':
            if time[1] == '?' or time[1] <= '3':
                time[0] = '2'
            else:
                time[0] = '1'

        # Determine the second digit of the hour
        if time[1] == '?':
            if time[0] == '2':
                time[1] = '3'
            else:
                time[1] = '9'

        # Determine the first digit of the minute
        if time[3] == '?':
            time[3] = '5'

        # Determine the second digit of the minute
        if time[4] == '?':
            time[4] = '9'

        # Join the list back into a string and return the result
        return ''.join(time)


# Test driver
if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = [
        "2?:?0",     # Expected: "23:50"
        "0?:3?",     # Expected: "09:39"
        "1?:22",     # Expected: "19:22"
        "?4:03",     # Expected: "14:03"
        "??:??",     # Expected: "23:59"
    ]

    for i, test_time in enumerate(test_cases):
        result = solution.maximumTime(test_time)
        print(f"Test case {i + 1}:")
        print(f"Input time: {test_time}")
        print(f"Latest possible time: {result}")
        # Verify the time is valid
        hour = int(result[:2])
        minute = int(result[3:])
        print(
            f"Verification - Hour: {hour} (valid: 0-23), Minute: {minute} (valid: 0-59)")
        print()
