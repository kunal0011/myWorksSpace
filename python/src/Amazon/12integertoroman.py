"""
Problem 12: Integer to Roman

Convert an integer to a Roman numeral.

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

Roman numerals are usually written largest to smallest from left to right. 
However, there are six instances where subtraction is used:
- I can be placed before V (5) and X (10) to make 4 and 9. 
- X can be placed before L (50) and C (100) to make 40 and 90. 
- C can be placed before D (500) and M (1000) to make 400 and 900.

Example 1:
Input: num = 3
Output: "III"
Explanation: 3 is represented as 3 ones.

Example 2:
Input: num = 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.

Example 3:
Input: num = 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

Constraints:
1 <= num <= 3999

Time Complexity: O(1) - since the input is constrained to 3999
Space Complexity: O(1) - output string size is bounded
"""

from collections import OrderedDict


class Solution:
    def intToRoman(self, num: int) -> str:
        # Using OrderedDict to maintain insertion order of symbols
        roman_values = OrderedDict([
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I')
        ])

        result = []

        # Iterate through roman values in descending order
        for value, symbol in roman_values.items():
            # While the number is greater than or equal to current value
            while num >= value:
                result.append(symbol)
                num -= value

        return ''.join(result)


def test_int_to_roman():
    solution = Solution()

    # Test cases: (number, expected_result, description)
    test_cases = [
        (3, "III", "Basic case with repetition"),
        (4, "IV", "Subtraction case - 4"),
        (9, "IX", "Subtraction case - 9"),
        (58, "LVIII", "Multiple symbols case"),
        (1994, "MCMXCIV", "Complex case with multiple subtractions"),
        (3999, "MMMCMXCIX", "Maximum possible number"),
        (1000, "M", "Even thousand"),
        (2023, "MMXXIII", "Current year"),
        (444, "CDXLIV", "Multiple subtraction patterns"),
        (999, "CMXCIX", "Three subtraction patterns")
    ]

    print("\nRunning Integer to Roman Tests:")
    print("=" * 50)

    passed = 0
    total = len(test_cases)

    for i, (num, expected, desc) in enumerate(test_cases, 1):
        result = solution.intToRoman(num)
        status = "PASS" if result == expected else "FAIL"
        color = "\033[92m" if status == "PASS" else "\033[91m"

        print(f"\nTest Case {i}: {desc}")
        print(f"Input Number: {num}")
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
    test_int_to_roman()
