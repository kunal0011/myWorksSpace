"""
LeetCode 678: Valid Parenthesis String

Problem Statement:
Given a string s containing only three types of characters: '(', ')' and '*', 
return true if s is valid. The following rules define a valid string:
1. Any left parenthesis '(' must have a corresponding right parenthesis ')'.
2. Any right parenthesis ')' must have a corresponding left parenthesis '('.
3. Left parenthesis '(' must go before the corresponding right parenthesis ')'.
4. '*' could be treated as a left parenthesis '(' or a right parenthesis ')' or an empty string "".

Key insight: Track the minimum and maximum possible open parentheses count.
"""

class Solution:
    def checkValidString(self, s: str) -> bool:
        # Track the minimum and maximum number of open parentheses possible
        min_open = max_open = 0
        
        for char in s:
            if char == '(':
                min_open += 1
                max_open += 1
            elif char == ')':
                min_open -= 1
                max_open -= 1
            else:  # char is '*'
                min_open -= 1  # * could be ')'
                max_open += 1  # * could be '('
            
            # If max_open becomes negative, we have too many ')'
            if max_open < 0:
                return False
            
            # min_open can't be negative, reset to 0 if it does
            min_open = max(0, min_open)
        
        # Valid if we can have 0 open parentheses
        return min_open <= 0 <= max_open

def test_valid_parenthesis_string():
    solution = Solution()
    
    # Test cases: [input_string, expected_result, description]
    test_cases = [
        ("()", True, "Basic valid case"),
        ("(*)", True, "Simple case with star"),
        ("(*))", True, "Star can be empty"),
        ("(**)", True, "Multiple stars"),
        (")(", False, "Invalid order"),
        ("(()", False, "Unclosed parenthesis"),
        ("((*)", True, "Star can be right parenthesis"),
        ("***", True, "All stars"),
        ("", True, "Empty string"),
        ("(((*)", False, "Too many open parentheses"),
        ("(((******))", True, "Complex valid case"),
        ("(())((())()()(*)", False, "Complex invalid case"),
        ("*((*", False, "Invalid with stars"),
        ("(*))", True, "Star as empty string")
    ]
    
    for i, (s, expected, description) in enumerate(test_cases, 1):
        result = solution.checkValidString(s)
        assert result == expected, \
            f"Test {i} failed: {description}\nInput: {s}\nExpected: {expected}, Got: {result}"
        print(f"\nTest {i}: {description}")
        print(f"Input: {s}")
        print(f"Expected: {expected}, Got: {result}")
        print("-" * 50)

if __name__ == "__main__":
    test_valid_parenthesis_string()
