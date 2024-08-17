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
