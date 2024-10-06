class Solution:
    def singleNonDuplicate(self, nums) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            # Ensure mid is always even
            if mid % 2 == 1:
                mid -= 1

            # If nums[mid] == nums[mid + 1], the single element is on the right
            if nums[mid] == nums[mid + 1]:
                left = mid + 2
            else:
                right = mid

        # At the end, left will point to the single element
        return nums[left]

# Test cases


def test_single_non_duplicate():
    solution = Solution()

    # Test case 1
    nums = [1, 1, 2, 2, 3, 3, 4, 4, 5]
    assert solution.singleNonDuplicate(
        nums) == 5, f"Test case 1 failed: {solution.singleNonDuplicate(nums)}"

    # Test case 2
    nums = [1, 1, 2, 3, 3, 4, 4, 5, 5]
    assert solution.singleNonDuplicate(
        nums) == 2, f"Test case 2 failed: {solution.singleNonDuplicate(nums)}"

    # Test case 3
    nums = [1, 2, 2, 3, 3, 4, 4, 5, 5]
    assert solution.singleNonDuplicate(
        nums) == 1, f"Test case 3 failed: {solution.singleNonDuplicate(nums)}"

    # Test case 4
    nums = [1, 1, 2]
    assert solution.singleNonDuplicate(
        nums) == 2, f"Test case 4 failed: {solution.singleNonDuplicate(nums)}"

    print("All test cases passed!")


# Run the tests
test_single_non_duplicate()
