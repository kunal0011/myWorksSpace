"""
LeetCode 224 - Basic Calculator

Problem Statement:
Given a string s representing a valid expression, implement a basic calculator to evaluate it,
and return the result of the evaluation. The expression can contain:
- Digits (0-9)
- '+' or '-' operators
- '(' or ')' parentheses
- Some spaces between components

Solution Logic:
1. Use stack to handle nested parentheses
2. Track current result and sign
3. For each character:
   - If digit: build number and add to result with sign
   - If '+': set sign to 1
   - If '-': set sign to -1
   - If '(': push current result and sign to stack
   - If ')': pop and compute nested expression
4. Time: O(n), Space: O(n)
"""

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        current_number = 0
        current_result = 0
        sign = 1  # 1 for positive, -1 for negative
        result = 0

        i = 0
        while i < len(s):
            char = s[i]

            if char.isdigit():
                current_number = 0
                while i < len(s) and s[i].isdigit():
                    current_number = current_number * 10 + int(s[i])
                    i += 1
                result += sign * current_number
                continue  # to skip the increment in the for loop

            elif char == '+':
                sign = 1
            elif char == '-':
                sign = -1
            elif char == '(':
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif char == ')':
                result = stack.pop() * result + stack.pop()

            i += 1

        return result

def test_calculator():
    solution = Solution()
    
    # Test Case 1: Basic arithmetic
    expr1 = "1 + 1"
    print("Test 1: Basic arithmetic")
    print(f"Expression: {expr1}")
    print(f"Result: {solution.calculate(expr1)}")  # Expected: 2
    
    # Test Case 2: With parentheses
    expr2 = "(1+(4+5+2)-3)+(6+8)"
    print("\nTest 2: With parentheses")
    print(f"Expression: {expr2}")
    print(f"Result: {solution.calculate(expr2)}")  # Expected: 23
    
    # Test Case 3: Negative numbers
    expr3 = "-2+ 1"
    print("\nTest 3: Negative numbers")
    print(f"Expression: {expr3}")
    print(f"Result: {solution.calculate(expr3)}")  # Expected: -1
    
    # Test Case 4: Nested parentheses
    expr4 = "(1-(2+3)-(4+5))"
    print("\nTest 4: Nested parentheses")
    print(f"Expression: {expr4}")
    print(f"Result: {solution.calculate(expr4)}")  # Expected: -13

if __name__ == "__main__":
    test_calculator()
