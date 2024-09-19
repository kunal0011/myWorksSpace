class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        def is_self_dividing(n: int) -> bool:
            original = n
            while n > 0:
                digit = n % 10
                if digit == 0 or original % digit != 0:
                    return False
                n //= 10
            return True

        result = []
        for num in range(left, right + 1):
            if is_self_dividing(num):
                result.append(num)
        return result


# Test the function
if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    left_1, right_1 = 1, 22
    # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
    print(sol.selfDividingNumbers(left_1, right_1))

    # Test case 2
    left_2, right_2 = 47, 85
    print(sol.selfDividingNumbers(left_2, right_2))  # Output: [48, 55, 66, 77]
