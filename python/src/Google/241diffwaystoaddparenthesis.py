from typing import List


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        # Base case: if the expression is a number, return it as an integer
        if expression.isdigit():
            return [int(expression)]

        results = []

        # Iterate through the expression
        for i, char in enumerate(expression):
            if char in "+-*":
                # Divide the expression into left and right parts
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i + 1:])

                # Combine the results from left and right parts
                for l in left:
                    for r in right:
                        if char == '+':
                            results.append(l + r)
                        elif char == '-':
                            results.append(l - r)
                        elif char == '*':
                            results.append(l * r)

        return results
