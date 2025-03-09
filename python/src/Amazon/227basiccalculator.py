"""
LeetCode 227 - Basic Calculator II

Problem Statement:
Given a string s which represents an expression, evaluate this expression and return its value.
The integer division should truncate toward zero.
You may assume that the given expression is always valid and can contain:
- integers (at least one digit)
- '+', '-', '*', '/' operators
- spaces ' '

Solution Logic:
1. Use stack to handle multiplication and division
2. Process number until non-digit character
3. Apply previous operator to stack:
   - For +: push number
   - For -: push -number
   - For * or /: pop last number, compute, push result
4. Time: O(n), Space: O(n)
"""

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        op = '+'
        n = len(s)

        for i in range(n):
            if s[i].isdigit():
                num = num * 10 + int(s[i])

            if (not s[i].isdigit() and s[i] != ' ') or i == n - 1:
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '*':
                    stack.append(stack.pop() * num)
                elif op == '/':
                    stack.append(int(stack.pop() / num))

                op = s[i]
                num = 0

        return sum(stack)

def test_calculator():
    solution = Solution()
    
    # Test Case 1: Basic arithmetic
    expr1 = "3+2*2"
    print("Test 1: Basic arithmetic")
    print(f"Expression: {expr1}")
    print(f"Result: {solution.calculate(expr1)}")  # Expected: 7
    
    # Test Case 2: With spaces
    expr2 = " 3/2 "
    print("\nTest 2: Division")
    print(f"Expression: {expr2}")
    print(f"Result: {solution.calculate(expr2)}")  # Expected: 1
    
    # Test Case 3: Complex expression
    expr3 = " 3+5 / 2 "
    print("\nTest 3: Mixed operations")
    print(f"Expression: {expr3}")
    print(f"Result: {solution.calculate(expr3)}")  # Expected: 5
    
    # Test Case 4: Multiple operations
    expr4 = "1*2-3/4+5*6-7*8+9/10"
    print("\nTest 4: Complex expression")
    print(f"Expression: {expr4}")
    print(f"Result: {solution.calculate(expr4)}")  # Expected: -39

if __name__ == "__main__":
    test_calculator()
