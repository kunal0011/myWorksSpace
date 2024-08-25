class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True

        left, right = 2, num // 2

        while left <= right:
            mid = (left + right) // 2
            guess_squared = mid * mid

            if guess_squared == num:
                return True
            elif guess_squared < num:
                left = mid + 1
            else:
                right = mid - 1

        return False
