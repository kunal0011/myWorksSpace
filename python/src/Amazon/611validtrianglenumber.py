class Solution:
    def triangleNumber(self, nums):
        # Sort the array
        nums.sort()
        count = 0
        n = len(nums)

        # Fix the third side and use two pointers for the other two
        for k in range(2, n):
            i, j = 0, k - 1
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    # All pairs (i, j), (i, j-1), ..., (i, i+1) are valid
                    count += j - i
                    j -= 1  # Move j left to find more pairs
                else:
                    i += 1  # Move i right to find a valid pair

        return count


# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    nums1 = [2, 2, 3, 4]
    print(sol.triangleNumber(nums1))  # Output: 3

    # Test case 2
    nums2 = [4, 2, 3, 4]
    print(sol.triangleNumber(nums2))  # Output: 4
