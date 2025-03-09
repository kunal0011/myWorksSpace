"""
LeetCode 301 - Remove Invalid Parentheses

Problem Statement:
Given a string s that contains parentheses and letters, remove the minimum number 
of invalid parentheses to make the input string valid.
Return all possible results in any order.

Logic:
1. Use BFS approach to try removing one parenthesis at a time
2. Key steps:
   - Start with original string
   - For each level, try removing one parenthesis
   - If valid string found at current level, add to results
   - Continue only if no valid string found
3. Helper function is_valid checks:
   - Count of open parentheses >= 0 always
   - Final count should be 0
4. Use set to avoid duplicates
"""

from collections import deque
from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def is_valid(string):
            count = 0
            for char in string:
                if char == '(':
                    count += 1
                elif char == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0

        queue = deque([s])
        visited = set([s])
        found = False
        result = []

        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                current = queue.popleft()

                if is_valid(current):
                    result.append(current)
                    found = True

                if found:
                    continue

                # Generate all possible states by removing one parenthesis
                for i in range(len(current)):
                    if current[i] not in '()':
                        continue
                    next_state = current[:i] + current[i+1:]
                    if next_state not in visited:
                        visited.add(next_state)
                        queue.append(next_state)

            if found:
                break

        return result

def test_remove_invalid_parentheses():
    solution = Solution()
    
    # Test cases
    test_cases = [
        ("()())()", ["(())()", "()()()"]),    # Multiple valid solutions
        ("(a)())()", ["(a())()", "(a)()()"]), # With letters
        (")(", [""]),                         # All invalid
        ("", [""]),                           # Empty string
        ("(()", ["()"]),                      # Remove opening parenthesis
        (")))", [""]),                        # All closing parentheses
        ("()", ["()"])                        # Already valid
    ]
    
    for i, (s, expected) in enumerate(test_cases):
        result = solution.removeInvalidParentheses(s)
        result.sort()  # Sort for comparison
        expected.sort()
        assert result == expected, f"Test case {i + 1} failed: input='{s}', expected {expected}, got {result}"
        print(f"Test case {i + 1} passed: input='{s}', result={result}")

if __name__ == "__main__":
    test_remove_invalid_parentheses()
    print("All test cases passed!")
