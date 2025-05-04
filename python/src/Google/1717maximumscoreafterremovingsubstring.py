"""
LeetCode 1717. Maximum Score From Removing Substrings

Problem Statement:
You are given a string s and two integers x and y. You can perform two types of operations any number of times:
- Remove substring "ab" and gain x points. For example, when removing "ab" from "cabxbae" it becomes "cxbae".
- Remove substring "ba" and gain y points. For example, when removing "ba" from "cabxbae" it becomes "cabxe".
Return the maximum points you can gain after applying the above operations on s.

Time Complexity: O(n) where n is the length of string s
Space Complexity: O(n) for stack storage
"""


class Solution:
    def maximumScore(self, s: str, a: str, x: int, b: str, y: int) -> int:
        # Logic:
        # 1. Use stack to track characters and find substrings
        # 2. Try both orders of removal (ab then ba, and ba then ab)
        # 3. For each order:
        #    - Process string left to right
        #    - When a matching substring is found, remove it and add score
        # 4. Return maximum score from both orders

        def solve(s, first, first_score, second, second_score):
            """Helper function to calculate the score given a specific order."""
            stack = []
            score = 0
            for char in s:
                stack.append(char)
                while len(stack) >= 2:
                    top = stack[-2] + stack[-1]
                    if top == first:
                        score += first_score
                        stack.pop()
                        stack.pop()
                    elif top == second:
                        score += second_score
                        stack.pop()
                        stack.pop()
                    else:
                        break  # No match, stop checking
            return score

        # Try both removal orders to find the maximum score
        return max(solve(s, a, x, b, y), solve(s, b, y, a, x))


# Test driver
if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = [
        ("cdbcbbaaabab", "ab", 4, "ba", 5),    # Expected: 19
        ("aabbaaxybbaabb", "ab", 3, "ba", 4),  # Expected: 20
        ("abab", "ab", 2, "ba", 1),            # Expected: 4
        ("bbaaabab", "ab", 4, "ba", 5),        # Expected: 18
        ("aabbaa", "ab", 4, "ba", 4)           # Expected: 16
    ]

    for i, (s, a, x, b, y) in enumerate(test_cases):
        result = solution.maximumScore(s, a, x, b, y)
        print(f"Test case {i + 1}:")
        print(f"String: {s}")
        print(f"Remove '{a}' for {x} points")
        print(f"Remove '{b}' for {y} points")
        print(f"Maximum score: {result}")

        # Show process for better understanding
        print("Trying both orders:")
        s1 = s
        s2 = s
        print(f"Order 1 ('{a}' then '{b}'): ", end="")
        while a in s1 or b in s1:
            if a in s1:
                s1 = s1.replace(a, "", 1)
                print(f"{s1} -> ", end="")
            if b in s1:
                s1 = s1.replace(b, "", 1)
                print(f"{s1} -> ", end="")
        print("done")
        print()
