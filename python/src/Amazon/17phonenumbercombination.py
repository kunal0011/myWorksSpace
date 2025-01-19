from typing import List


# Problem Statement:

# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

# A mapping of digit to letters(just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

# 2 -> "abc"
# 3 -> "def"
# 4 -> "ghi"
# 5 -> "jkl"
# 6 -> "mno"
# 7 -> "pqrs"
# 8 -> "tuv"
# 9 -> "wxyz"
# Example:

# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

# Constraints:

# 0 <= digits.length <= 4
# digits[i] is a digit in the range['2', '9'].


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        # Mapping of digits to letters
        phone_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(index, current_combination):
            if index == len(digits):
                result.append(current_combination)
                return
            for letter in phone_map[digits[index]]:
                backtrack(index + 1, current_combination + letter)

        result = []
        backtrack(0, "")
        return result
