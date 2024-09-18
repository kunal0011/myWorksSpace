class Solution:
    def isMonotonic(self, A: list[int]) -> bool:
        increasing = decreasing = True

        for i in range(1, len(A)):
            if A[i] > A[i - 1]:
                decreasing = False
            if A[i] < A[i - 1]:
                increasing = False

        return increasing or decreasing


# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    A1 = [1, 2, 2, 3]
    print(sol.isMonotonic(A1))  # Expected output: True

    # Test case 2
    A2 = [6, 5, 4, 4]
    print(sol.isMonotonic(A2))  # Expected output: True

    # Test case 3
    A3 = [1, 3, 2]
    print(sol.isMonotonic(A3))  # Expected output: False
