class Solution:
    def minMoves(self, nums: list[int]) -> int:
        # The minimum number of moves is the sum of differences between all elements and the minimum element.
        min_num = min(nums)
        return sum(num - min_num for num in nums)


if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    nums1 = [1, 2, 3]
    print(solution.minMoves(nums1))  # Output: 3

    # Test case 2
    nums2 = [1, 1, 1]
    print(solution.minMoves(nums2))  # Output: 0

    # Test case 3
    nums3 = [5, 6, 8, 8]
    print(solution.minMoves(nums3))  # Output: 7

    # Test case 4
    nums4 = [10, 10, 10, 10]
    print(solution.minMoves(nums4))  # Output: 0
