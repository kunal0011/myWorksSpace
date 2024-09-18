class Solution:
    def stoneGame(self, piles: list[int]) -> bool:
        # Alex always wins when both play optimally.
        return True


# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    piles1 = [5, 3, 4, 5]
    print(sol.stoneGame(piles1))  # Expected output: True

    # Test case 2
    piles2 = [3, 7, 2, 3]
    print(sol.stoneGame(piles2))  # Expected output: True
