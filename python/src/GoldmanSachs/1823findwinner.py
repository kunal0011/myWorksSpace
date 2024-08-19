class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        def find_winner(n, k):
            if n == 1:
                return 0
            return (find_winner(n - 1, k) + k) % n

        # Since the function above is 0-indexed, add 1 to get the correct winner
        return find_winner(n, k) + 1


if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    n1, k1 = 5, 2
    print(solution.findTheWinner(n1, k1))  # Output: 3

    # Test case 2
    n2, k2 = 6, 5
    print(solution.findTheWinner(n2, k2))  # Output: 1

    # Test case 3
    n3, k3 = 7, 3
    print(solution.findTheWinner(n3, k3))  # Output: 4
