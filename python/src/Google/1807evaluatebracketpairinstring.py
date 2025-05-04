"""
LeetCode 1807. Evaluate the Bracket Pairs of a String

Problem Statement:
You are given a string s that contains some bracket pairs, with each pair containing a non-empty key.
- For example, in the string "(name)is(age)yearsold", there are two bracket pairs that contain the keys "name" and "age".
You know the values of a wide range of keys. You are also given a knowledge list where each knowledge[i] = [keyi, valuei] 
indicates that key keyi has a value of valuei.
Return the string after replacing all bracket pairs with the corresponding value. If a bracket pair contains an unknown key, 
replace it with a question mark "?" (without quotes).

Time Complexity: O(n) where n is length of string
Space Complexity: O(n) for result list and O(m) for knowledge dictionary where m is length of knowledge list
"""

from typing import List


class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        # Logic:
        # 1. Convert knowledge list to dictionary for O(1) lookups
        # 2. Iterate through string:
        #    - For non-bracket chars, add directly to result
        #    - For bracket pairs, extract key and replace with value from dictionary
        #    - If key not found, replace with "?"
        # 3. Join and return final result

        # Convert the knowledge list into a dictionary
        knowledge_dict = {k: v for k, v in knowledge}

        result = []
        i = 0
        while i < len(s):
            if s[i] == '(':
                i += 1
                key = []
                # Capture the key inside the brackets
                while s[i] != ')':
                    key.append(s[i])
                    i += 1
                # Move past the closing ')'
                i += 1
                key = ''.join(key)
                # Append the corresponding value or "?" if the key is not found
                result.append(knowledge_dict.get(key, '?'))
            else:
                # Append non-bracket characters directly to the result
                result.append(s[i])
                i += 1

        return ''.join(result)


# Test driver
if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = [
        ("(name)is(age)yearsold",
         [["name", "bob"], ["age", "two"]],
         "bobistwoyearsold"),

        ("hi(name)",
         [["a", "b"]],
         "hi?"),

        ("(a)(a)(a)aaa",
         [["a", "yes"]],
         "yesyesyesaaa"),

        ("(a)(b)",
         [["a", "b"], ["b", "a"]],
         "ba"),

        ("hi(a)hi(b)hi(c)",
         [["a", "hello"], ["b", "world"], ["c", "!"]],
         "hihellohiworldhi!")
    ]

    for i, (s, knowledge, expected) in enumerate(test_cases):
        result = solution.evaluate(s, knowledge)
        print(f"Test case {i + 1}:")
        print(f"Input string: {s}")
        print(f"Knowledge base: {knowledge}")
        print(f"Result: {result}")
        print(f"Expected: {expected}")
        print(f"Correct: {result == expected}")
        print()
