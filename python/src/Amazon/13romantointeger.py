"""
Problem 13: Roman to Integer

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two ones added together. 
12 is written as XII, which is simply X + II. 
The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. 
However, there are six instances where subtraction is used:
- I can be placed before V (5) and X (10) to make 4 and 9. 
- X can be placed before L (50) and C (100) to make 40 and 90. 
- C can be placed before D (500) and M (1000) to make 400 and 900.

Example 1:
Input: s = "III"
Output: 3
Explanation: III = 3.

Example 2:
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V = 5, III = 3.

Example 3:
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

Constraints:
1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].

Time Complexity: O(n) where n is the length of the input string
Space Complexity: O(1) as we use a fixed-size dictionary
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        # Roman numeral to integer mapping
        roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        prev_value = 0

        # Iterate through the Roman numeral string from right to left
        for char in reversed(s):
            current_value = roman_to_int[char]

            # If current value is smaller than previous, subtract it
            if current_value < prev_value:
                total -= current_value
            else:
                total += current_value

            prev_value = current_value

        return total


def test_roman_to_int():
    solution = Solution()

    # Test cases: (roman_numeral, expected_result, description)
    test_cases = [
        ("III", 3, "Simple addition"),
        ("IV", 4, "Simple subtraction"),
        ("IX", 9, "Single subtraction"),
        ("LVIII", 58, "Multiple symbols"),
        ("MCMXCIV", 1994, "Complex subtraction patterns"),
        ("MMMCMXCIX", 3999, "Maximum valid number"),
        ("I", 1, "Single symbol"),
        ("MMXXIII", 2023, "Current year"),
        ("CDXLIV", 444, "Multiple subtraction patterns"),
        ("CMXCIX", 999, "Three subtraction patterns")
    ]

    print("\nRunning Roman to Integer Tests:")
    print("=" * 50)

    passed = 0
    total = len(test_cases)

    for i, (roman, expected, desc) in enumerate(test_cases, 1):
        result = solution.romanToInt(roman)
        status = "PASS" if result == expected else "FAIL"
        color = "\033[92m" if status == "PASS" else "\033[91m"

        print(f"\nTest Case {i}: {desc}")
        print(f"Input Roman: {roman}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print(f"Status: {color}{status}\033[0m")

        if result == expected:
            passed += 1

    print("\n" + "=" * 50)
    print(f"\nTest Summary:")
    print(f"Total Tests: {total}")
    print(f"Passed: {passed}")
    print(f"Failed: {total - passed}")
    success_rate = (passed / total) * 100
    print(f"Success Rate: {success_rate:.2f}%")


if __name__ == "__main__":
    test_roman_to_int()
