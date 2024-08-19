class Solution:
    def lastRemaining(self, n: int) -> int:
        head = 1
        step = 1
        left = True
        remaining = n

        while remaining > 1:
            if left or remaining % 2 == 1:
                head += step
            remaining //= 2
            step *= 2
            left = not left

        return head


if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    n1 = 9
    print(solution.lastRemaining(n1))  # Output: 6

    # Test case 2
    n2 = 1
    print(solution.lastRemaining(n2))  # Output: 1

    # Test case 3
    n3 = 24
    print(solution.lastRemaining(n3))  # Output: 14

    # Test case 4
    n4 = 1000000
    print(solution.lastRemaining(n4))  # Output: 481152
