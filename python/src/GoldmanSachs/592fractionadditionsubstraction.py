from fractions import Fraction


class Solution:
    def fractionAddition(self, expression: str) -> str:
        fractions = []
        num = ""

        # Preprocess to separate the fractions
        for i, c in enumerate(expression):
            if c in "+-" and i > 0:
                fractions.append(num)
                num = ""
            num += c
        fractions.append(num)  # append the last fraction

        # Sum all fractions
        result = sum(Fraction(f) for f in fractions)

        # Return the result in the form of "numerator/denominator"
        return f"{result.numerator}/{result.denominator}"


if __name__ == "__main__":
    # Test case 1
    expression1 = "-1/2+1/2"
    solution = Solution()
    print(solution.fractionAddition(expression1))  # Output: "0/1"

    # Test case 2
    expression2 = "-1/2+1/2+1/3"
    print(solution.fractionAddition(expression2))  # Output: "1/3"

    # Test case 3
    expression3 = "1/3-1/2"
    print(solution.fractionAddition(expression3))  # Output: "-1/6"
