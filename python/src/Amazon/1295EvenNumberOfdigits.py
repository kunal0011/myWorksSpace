class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        count = 0
        for num in nums:
            # Convert the number to a string and check the length
            if len(str(num)) % 2 == 0:
                count += 1
        return count


# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    nums1 = [12, 345, 2, 6, 7896]
    result1 = sol.findNumbers(nums1)
    assert result1 == 2, f"Test case 1 failed: {result1}"

    # Test case 2
    nums2 = [555, 901, 482, 1771]
    result2 = sol.findNumbers(nums2)
    assert result2 == 1, f"Test case 2 failed: {result2}"

    print("All test cases passed!")
