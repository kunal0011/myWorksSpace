"""
LeetCode 856: Score of Parentheses

Given a balanced parentheses string s, return the score of the string.

The score of a balanced parentheses string is based on the following rule:
- "()" has score 1
- AB has score A + B, where A and B are balanced parentheses strings
- (A) has score 2 * A, where A is a balanced parentheses string

Constraints:
- 2 <= s.length <= 50
- s consists of only '(' and ')'
- s is a balanced parentheses string
"""

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]  # Stack to keep track of scores at each depth
        
        for char in s:
            if char == '(':
                stack.append(0)  # New depth level
            else:
                # Pop current depth's score
                score = stack.pop()
                # Add to previous depth: max(2*score, 1)
                stack[-1] += max(2 * score, 1)
                
        return stack[0]

def validate_string(s: str) -> bool:
    """Validate string according to constraints"""
    if not 2 <= len(s) <= 50:
        return False
    if not all(c in '()' for c in s):
        return False
    # Check if balanced
    count = 0
    for c in s:
        count += 1 if c == '(' else -1
        if count < 0:
            return False
    return count == 0

def test_parentheses_score():
    """Test function for Score of Parentheses"""
    test_cases = [
        ("()", 1),
        ("(())", 2),
        ("()()", 2),
        ("(()(()))", 6),
        ("((()))", 4),
        ("(()())", 4),
        ("((()())())", 8)
    ]
    
    solution = Solution()
    
    for i, (s, expected) in enumerate(test_cases, 1):
        is_valid = validate_string(s)
        result = solution.scoreOfParentheses(s)
        
        print(f"\nTest case {i}:")
        print(f"Input string: {s}")
        print(f"Length: {len(s)}")
        print(f"Expected score: {expected}")
        print(f"Calculated score: {result}")
        print(f"Valid input: {'✓' if is_valid else '✗'}")
        print(f"Test passed: {'✓' if result == expected else '✗'}")
        
        # Show nesting levels
        depth = 0
        max_depth = 0
        depths = []
        for c in s:
            if c == '(':
                depth += 1
                max_depth = max(max_depth, depth)
            else:
                depths.append(depth)
                depth -= 1
        print(f"Maximum nesting depth: {max_depth}")
        print(f"Nesting levels at closing brackets: {depths}")

if __name__ == "__main__":
    test_parentheses_score()
