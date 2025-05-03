class Solution:
    def maximumScore(self, s: str, a: str, x: int, b: str, y: int) -> int:
        """
        Calculates the maximum score by removing substrings a and b from s.

        Args:
            s: The input string.
            a: The first substring to remove.
            x: The score for removing substring a.
            b: The second substring to remove.
            y: The score for removing substring b.

        Returns:
            The maximum score achievable.
        """

        def solve(s, first, first_score, second, second_score):
            """Helper function to calculate the score given a specific order."""
            stack = []
            score = 0
            for char in s:
                stack.append(char)
                while len(stack) >= 2:
                    top = stack[-2] + stack[-1]
                    if top == first:
                        score += first_score
                        stack.pop()
                        stack.pop()
                    elif top == second:
                        score += second_score
                        stack.pop()
                        stack.pop()
                    else:
                        break  # No match, stop checking
            return score

        # Try both removal orders to find the maximum score
        return max(solve(s, a, x, b, y), solve(s, b, y, a, x))