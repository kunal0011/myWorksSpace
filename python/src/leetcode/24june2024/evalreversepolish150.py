from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
                stack.append(int(token))
            else:
                operand1 = stack.pop()
                operand2 = stack.pop()
                if token == '+':
                    stack.append(operand2 + operand1)
                elif token == '-':
                    stack.append(operand2 - operand1)
                elif token == '*':
                    stack.append(operand2 * operand1)
                elif token == '/':
                    # Division in Python truncates towards zero, which matches the requirement
                    stack.append(int(operand2 / operand1))

        return stack.pop()


# Example usage:
sol = Solution()
# Output: 9 (equivalent to (2 + 1) * 3)
print(sol.evalRPN(["2", "1", "+", "3", "*"]))
# Output: 6 (equivalent to 4 + (13 / 5))
print(sol.evalRPN(["4", "13", "5", "/", "+"]))
print(sol.evalRPN(["10", "6", "9", "3", "+", "-11", "*",
      "/", "*", "17", "+", "5", "+"]))  # Output: 22
