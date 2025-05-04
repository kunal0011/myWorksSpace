"""
LeetCode 1544. Make The String Great

Problem Statement:
Given a string s of lower and upper case English letters.
A good string is a string which doesn't have two adjacent characters:
- where s[i] is a lowercase letter and s[i+1] is the same letter but in uppercase, or vice-versa.
To make the string good, you can choose two adjacent characters that make the string bad and remove them.
Return the string after making it good. The answer is guaranteed to be unique.

Time Complexity: O(n) where n is length of string
Space Complexity: O(n) for stack storage
"""


class Solution:
    def makeGood(self, s: str) -> str:
        # Logic:
        # 1. Use stack to track characters
        # 2. For each character:
        #    - If stack is empty or current char doesn't make bad string with top, push
        #    - If current char makes bad string with stack top (diff of 32 in ASCII), pop
        # 3. Bad string occurs when same letter in different cases are adjacent
        #    (ASCII difference of 32 between upper and lower case of same letter)

        stack = []
        for char in s:
            if stack and abs(ord(stack[-1]) - ord(char)) == 32:
                stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)


# Test driver
if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = [
        "leEeetcode",    # Expected: "leetcode"
        "abBAcC",        # Expected: ""
        "s",             # Expected: "s"
        "Pp",            # Expected: ""
        "aBbAcC"         # Expected: ""
    ]

    for i, test_str in enumerate(test_cases):
        result = solution.makeGood(test_str)
        print(f"Test case {i + 1}:")
        print(f"Input string: {test_str}")
        print(f"Good string: {result}")
        print(f"Explanation: ")
        if not result:
            print("All characters were removed to make the string good")
        else:
            print(
                f"'{result}' is the final good string with no adjacent bad characters")
        print()
