class Solution:
    def minSteps(self, n: int) -> int:
        # Start with 0 steps
        steps = 0
        # Start checking factors from 2 to n
        factor = 2

        # We reduce n by dividing it by its factors
        while n > 1:
            # If factor divides n, we use this factor
            while n % factor == 0:
                steps += factor
                n //= factor
            # Move to the next potential factor
            factor += 1

        return steps


# Test the solution with some test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1: n = 3
    n = 3
    # Expected output: 3
    print(f"Minimum steps to get {n} 'A's: {solution.minSteps(n)}")

    # Test case 2: n = 1
    n = 1
    # Expected output: 0
    print(f"Minimum steps to get {n} 'A's: {solution.minSteps(n)}")

    # Test case 3: n = 6
    n = 6
    # Expected output: 5
    print(f"Minimum steps to get {n} 'A's: {solution.minSteps(n)}")
