class Solution:
    def search(self, nums, target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            # To avoid overflow in some languages
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1  # Target not found

# Test cases


def test_binary_search():
    solution = Solution()

    # Test case 1
    nums1 = [-1, 0, 3, 5, 9, 12]
    target1 = 9
    expected_result_1 = 4  # nums[4] == 9
    assert solution.search(
        nums1, target1) == expected_result_1, "Test case 1 failed"

    # Test case 2
    nums2 = [-1, 0, 3, 5, 9, 12]
    target2 = 2
    expected_result_2 = -1  # 2 is not in the array
    assert solution.search(
        nums2, target2) == expected_result_2, "Test case 2 failed"

    # Test case 3
    nums3 = [5]
    target3 = 5
    expected_result_3 = 0  # Single element, target is at index 0
    assert solution.search(
        nums3, target3) == expected_result_3, "Test case 3 failed"

    print("All test cases passed!")


# Run the tests
test_binary_search()
