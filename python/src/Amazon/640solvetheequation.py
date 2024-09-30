class Solution:
    def solveEquation(self, equation: str) -> str:
        # Function to parse one side of the equation
        def parse(expr):
            x_coeff = 0  # Coefficient of x
            const = 0    # Constant value

            # Add + at the beginning to handle the first term properly
            expr = expr.replace("-", "+-")
            terms = expr.split("+")

            for term in terms:
                if "x" in term:
                    if term == "x":
                        x_coeff += 1
                    elif term == "-x":
                        x_coeff -= 1
                    else:
                        x_coeff += int(term[:-1])
                elif term:
                    const += int(term)

            return x_coeff, const

        # Split the equation into left and right expressions
        left, right = equation.split("=")

        # Parse both sides to get the x coefficients and constants
        left_x, left_const = parse(left)
        right_x, right_const = parse(right)

        # Combine the coefficients and constants from both sides
        x_coeff = left_x - right_x
        const = right_const - left_const

        # Determine the solution based on the coefficients
        if x_coeff == 0:
            if const == 0:
                return "Infinite solutions"
            else:
                return "No solution"
        else:
            return f"x={const // x_coeff}"


# Test the solution with some test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1: equation = "x+5-3+x=6+x-2"
    equation = "x+5-3+x=6+x-2"
    # Expected output: "x=2"
    print(f"Solution for '{equation}': {solution.solveEquation(equation)}")

    # Test case 2: equation = "x=x"
    equation = "x=x"
    # Expected output: "Infinite solutions"
    print(f"Solution for '{equation}': {solution.solveEquation(equation)}")

    # Test case 3: equation = "2x=x"
    equation = "2x=x"
    # Expected output: "x=0"
    print(f"Solution for '{equation}': {solution.solveEquation(equation)}")

    # Test case 4: equation = "2x+3x-6x=x+2"
    equation = "2x+3x-6x=x+2"
    # Expected output: "x=-1"
    print(f"Solution for '{equation}': {solution.solveEquation(equation)}")

    # Test case 5: equation = "x=x+2"
    equation = "x=x+2"
    # Expected output: "No solution"
    print(f"Solution for '{equation}': {solution.solveEquation(equation)}")
