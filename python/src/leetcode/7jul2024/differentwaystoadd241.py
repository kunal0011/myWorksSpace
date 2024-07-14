from typing import List


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def compute(left, right, op):
            if op == '+':
                return left + right
            elif op == '-':
                return left - right
            elif op == '*':
                return left * right

        def ways(expression):
            if expression.isdigit():
                return [int(expression)]

            if expression in memo:
                return memo[expression]

            results = []
            for i in range(len(expression)):
                if expression[i] in "+-*":
                    left_results = ways(expression[:i])
                    right_results = ways(expression[i+1:])

                    for left in left_results:
                        for right in right_results:
                            results.append(compute(left, right, expression[i]))

            memo[expression] = results
            return results

        memo = {}
        return ways(expression)


# Example usage
solution = Solution()
expression = "2*3-4*5"
print(solution.diffWaysToCompute(expression))
