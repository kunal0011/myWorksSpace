class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        left, right = 1, x // 2 + 1

        while left <= right:
            mid = left + (right - left) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1

        # When the loop exits, right will be the largest integer whose square is <= x
        return right

# Test cases


def test_my_sqrt():
    solution = Solution()

    # Test case 1: perfect square
    assert solution.mySqrt(4) == 2, f"Test case 1 failed: {solution.mySqrt(4)}"

    # Test case 2: not a perfect square
    assert solution.mySqrt(8) == 2, f"Test case 2 failed: {solution.mySqrt(8)}"

    # Test case 3: zero input
    assert solution.mySqrt(0) == 0, f"Test case 3 failed: {solution.mySqrt(0)}"

    # Test case 4: larger number
    assert solution.mySqrt(
        10000) == 100, f"Test case 4 failed: {solution.mySqrt(10000)}"

    print("All test cases passed!")


# Run the tests
test_my_sqrt()
