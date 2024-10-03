class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        # Start filling nums1 from the end
        last = m + n - 1

        # Pointers for nums1 and nums2
        i = m - 1  # Last element in nums1's valid part
        j = n - 1  # Last element in nums2

        # Merge in reverse order
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[last] = nums1[i]
                i -= 1
            else:
                nums1[last] = nums2[j]
                j -= 1
            last -= 1

        # If nums2 still has elements left, place them in nums1
        while j >= 0:
            nums1[last] = nums2[j]
            j -= 1
            last -= 1

# Test the Solution class


def test_solution():
    sol = Solution()

    # Test case 1
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    sol.merge(nums1, 3, nums2, 3)
    assert nums1 == [1, 2, 2, 3, 5, 6]

    # Test case 2
    nums1 = [1]
    nums2 = []
    sol.merge(nums1, 1, nums2, 0)
    assert nums1 == [1]

    # Test case 3
    nums1 = [0]
    nums2 = [1]
    sol.merge(nums1, 0, nums2, 1)
    assert nums1 == [1]

    print("All test cases passed!")


# Run the tests
test_solution()
