class Solution:
    def reachNumber(self, target: int) -> int:
        # Ensure the target is positive, as it's symmetric
        target = abs(target)

        # Initialize variables
        steps = 0
        total = 0

        # Keep taking steps until the sum is at least as large as the target
        while total < target or (total - target) % 2 != 0:
            steps += 1
            total += steps

        return steps


# Test the Solution
if __name__ == "__main__":
    # Initialize the Solution class
    solution = Solution()

    # Test cases
    target = 3
    # Output: 2
    print(f"Minimum steps to reach {target}: {solution.reachNumber(target)}")

    target = 2
    # Output: 3
    print(f"Minimum steps to reach {target}: {solution.reachNumber(target)}")
