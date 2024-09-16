class Solution:
    def countTriples(self, n: int) -> int:
        count = 0

        # Iterate through all values of a, b, c
        for c in range(1, n + 1):
            for a in range(1, c):
                for b in range(a, c):
                    if a * a + b * b == c * c:
                        count += 2  # (a, b, c) and (b, a, c) are both valid

        return count


# Testing the solution
if __name__ == "__main__":
    solution = Solution()

    # Test case
    n = 5
    print("Count of Square Sum Triples:",
          solution.countTriples(n))  # Expected output: 2
