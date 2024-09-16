class Solution:
    def check(self, nums: list[int]) -> bool:
        count = 0
        n = len(nums)

        # Count the number of "rotations" where the order breaks
        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                count += 1
            if count > 1:
                return False

        return True


# Testing the solution
if __name__ == "__main__":
    solution = Solution()

    # Test cases
    nums = [3, 4, 5, 1, 2]
    # Expected output: True
    print("Is sorted and rotated:", solution.check(nums))

    nums = [2, 1, 3, 4]
    # Expected output: False
    print("Is sorted and rotated:", solution.check(nums))

    nums = [1, 2, 3]
    # Expected output: True
    print("Is sorted and rotated:", solution.check(nums))
