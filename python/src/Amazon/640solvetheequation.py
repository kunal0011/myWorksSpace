"""
LeetCode 640: Solve the Equation
Solve a given equation and return the value of 'x' in the form "x=#value".
The equation contains only '+', '-' operations, variables 'x' and integers.

If there is no solution, return "No solution".
If there are infinite solutions, return "Infinite solutions".
If there is exactly one solution, return it as "x=#value".
"""

class Solution:
    def solveEquation(self, equation: str) -> str:
        def parse(expr):
            x_coeff, const = 0, 0
            curr_num, sign = 0, 1
            i = 0
            
            while i < len(expr):
                if expr[i] == '+':
                    sign = 1
                elif expr[i] == '-':
                    sign = -1
                elif expr[i].isdigit():
                    curr_num = curr_num * 10 + int(expr[i])
                elif expr[i] == 'x':
                    if i > 0 and expr[i-1].isdigit():
                        x_coeff += sign * curr_num
                    else:
                        x_coeff += sign
                    curr_num = 0
                else:  # Handle any other characters (if needed)
                    const += sign * curr_num
                    curr_num = 0
                i += 1
            
            const += sign * curr_num  # Add the last number if exists
            return x_coeff, const

        # Split and solve the equation
        left, right = equation.split('=')
        left_x, left_const = parse(left)
        right_x, right_const = parse(right)
        
        # Move all terms to left side: ax = b
        x_coeff = left_x - right_x
        const = right_const - left_const
        
        if x_coeff == 0:
            return "Infinite solutions" if const == 0 else "No solution"
        return f"x={const // x_coeff}"


def test_equation_solver():
    """Test driver for the equation solver"""
    test_cases = [
        ("x+5-3+x=6+x-2", "x=2"),
        ("x=x", "Infinite solutions"),
        ("2x=x", "x=0"),
        ("2x+3x-6x=x+2", "x=-1"),
        ("x=x+2", "No solution"),
        ("x=1", "x=1"),
        ("2x+3=x+2", "x=-1"),
        ("0x=0", "Infinite solutions"),
        ("x+1=x+2", "No solution"),
        ("2x=x+2", "x=2")
    ]
    
    solution = Solution()
    for i, (equation, expected) in enumerate(test_cases, 1):
        result = solution.solveEquation(equation)
        status = "✓" if result == expected else "✗"
        print(f"Test {i}: {status}")
        print(f"Equation: {equation}")
        print(f"Expected: {expected}")
        print(f"Got: {result}\n")


if __name__ == "__main__":
    test_equation_solver()
