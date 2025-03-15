"""
LeetCode 921: Minimum Add to Make Parentheses Valid

A parentheses string is valid if and only if:
- It is the empty string,
- It can be written as AB (A concatenated with B), where A and B are valid strings, or
- It can be written as (A), where A is a valid string.

You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.
Return the minimum number of moves required to make s valid.

Constraints:
- 1 <= s.length <= 1000
- s[i] is either '(' or ')'
"""

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = 0  # Track open parentheses
        adds = 0   # Count needed additions
        
        for char in s:
            if char == '(':
                stack += 1
            else:  # char == ')'
                if stack > 0:
                    stack -= 1  # Match with existing open parenthesis
                else:
                    adds += 1   # Need to add an open parenthesis
                    
        return adds + stack  # Total additions = unmatched close + remaining open

def validate_string(s: str) -> bool:
    """Validate string according to constraints"""
    if not 1 <= len(s) <= 1000:
        return False
    return all(c in '()' for c in s)

def visualize_parentheses(s: str) -> str:
    """Create visual representation of parentheses matching"""
    depth = 0
    result = []
    matches = []
    unmatched = []
    
    for i, c in enumerate(s):
        if c == '(':
            depth += 1
            result.append(f"{c}{depth}")
            matches.append(depth)
        else:
            if matches:
                match = matches.pop()
                result.append(f"{c}{match}")
            else:
                result.append(f"{c}?")
                unmatched.append(i)
                
    return ' '.join(result), matches, unmatched

def test_min_add_to_valid():
    """Test function for Minimum Add to Make Parentheses Valid"""
    test_cases = [
        ("())", 1),
        ("(((", 3),
        ("()", 0),
        ("()))((", 4),
        (")))", 3),
        ("((())", 1),
        ("())()(((", 4)
    ]
    
    solution = Solution()
    
    for i, (s, expected) in enumerate(test_cases, 1):
        is_valid = validate_string(s)
        result = solution.minAddToMakeValid(s)
        
        print(f"\nTest case {i}:")
        print(f"Input string: {s}")
        
        # Visualize matching
        vis, unmatched_open, unmatched_close = visualize_parentheses(s)
        print("Parentheses matching:")
        print(vis)
        print(f"Unmatched '(': {len(unmatched_open)}")
        print(f"Unmatched ')': {len(unmatched_close)}")
        
        print(f"\nAdditions needed: {result}")
        print(f"Expected additions: {expected}")
        print(f"Valid input: {'✓' if is_valid else '✗'}")
        print(f"Test passed: {'✓' if result == expected else '✗'}")
        
        # Additional statistics
        print("\nString analysis:")
        print(f"Length: {len(s)}")
        print(f"Opening parentheses: {s.count('(')}")
        print(f"Closing parentheses: {s.count(')')}")
        print(f"Balance: {s.count('(') - s.count(')')}")

if __name__ == "__main__":
    test_min_add_to_valid()
