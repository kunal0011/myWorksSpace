class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        # Stack to keep track of scores
        stack = []

        # Initialize the current score to 0
        current_score = 0

        for char in S:
            if char == '(':
                # Push the current score to stack and reset current score
                stack.append(current_score)
                current_score = 0
            else:
                # Pop from stack, calculate score
                last_score = stack.pop()
                # If current score is 0, it means we encountered (), so we add 1
                # Otherwise, we multiply the current score by 2 (for (A))
                current_score = last_score + max(2 * current_score, 1)

        return current_score


# Test the solution with some test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Example 1 from the problem
    S = "()"
    result = solution.scoreOfParentheses(S)
    print(f"Score of parentheses '{S}': {result}")  # Expected output: 1

    # Test case 2: Example 2 from the problem
    S = "(())"
    result = solution.scoreOfParentheses(S)
    print(f"Score of parentheses '{S}': {result}")  # Expected output: 2

    # Test case 3: Example 3 from the problem
    S = "()()"
    result = solution.scoreOfParentheses(S)
    print(f"Score of parentheses '{S}': {result}")  # Expected output: 2

    # Test case 4: More complex example
    S = "(()(()))"
    result = solution.scoreOfParentheses(S)
    print(f"Score of parentheses '{S}': {result}")  # Expected output: 6
