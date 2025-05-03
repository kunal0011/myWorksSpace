"""
LeetCode 320 - Generalized Abbreviation

Problem Statement:
Write a function to generate all possible abbreviations of a word.
A word's abbreviation can be constructed by taking any number of non-overlapping and non-adjacent substrings 
and replacing them with their respective lengths.

For example, "word" can be abbreviated as:
- "word" (no letters abbreviated)
- "1ord" (first letter abbreviated)
- "w1rd" (second letter abbreviated)
- "wo1d" (third letter abbreviated)
- "wor1" (fourth letter abbreviated)
- "2rd" (first two letters abbreviated)
- "w2d" (middle two letters abbreviated)
- "wo2" (last two letters abbreviated)
- "1o1d" (first and third letters abbreviated)
- "1or1" (first and fourth letters abbreviated)
- "w1r1" (second and fourth letters abbreviated)
- "3d" (first three letters abbreviated)
- "w3" (last three letters abbreviated)
- "4" (entire word abbreviated)
"""

class Solution:
    def generateAbbreviations(self, word: str):
        res = []

        def backtrack(pos, current, count):
            # If we've processed all characters in the word
            if pos == len(word):
                # If count is not zero, append it to the result
                if count > 0:
                    current += str(count)
                res.append(current)
                return

            # Option 1: Abbreviate the current character (increase count)
            backtrack(pos + 1, current, count + 1)

            # Option 2: Don't abbreviate, add the count and the character to the result
            if count > 0:
                current += str(count)
            backtrack(pos + 1, current + word[pos], 0)

        backtrack(0, "", 0)
        return res

def run_tests():
    solution = Solution()
    
    test_cases = [
        ("word", [
            "word", "1ord", "w1rd", "wo1d", "wor1", "2rd", 
            "w2d", "wo2", "1o1d", "1or1", "w1r1", "3d", 
            "w3", "4"
        ]),
        ("a", ["a", "1"]),
        ("", [""]),
        ("code", [
            "code", "1ode", "c1de", "co1e", "cod1", "2de", 
            "c2e", "co2", "1o1e", "1od1", "c1d1", "3e", 
            "c3", "4"
        ])
    ]
    
    for i, (word, expected) in enumerate(test_cases, 1):
        result = sorted(solution.generateAbbreviations(word))
        expected = sorted(expected)
        print(f"\nTest case {i}:")
        print(f"Input word: {word}")
        print(f"Expected abbreviations: {expected}")
        print(f"Actual abbreviations: {result}")
        print(f"{'✓ Passed' if result == expected else '✗ Failed'}")

if __name__ == "__main__":
    run_tests()
