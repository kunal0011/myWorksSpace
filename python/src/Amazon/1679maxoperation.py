from collections import defaultdict


class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        count_map = defaultdict(int)
        operations = 0

        for num in nums:
            complement = k - num
            if count_map[complement] > 0:
                operations += 1
                count_map[complement] -= 1  # Use up the complement
            else:
                count_map[num] += 1  # Store the current number for future use

        return operations


# Testing the solution
if __name__ == "__main__":
    solution = Solution()

    # Test cases
    nums = [1, 2, 3, 4]
    k = 5
    print("Max number of k-sum pairs:",
          solution.maxOperations(nums, k))  # Expected output: 2

    nums = [3, 1, 3, 4, 3]
    k = 6
    print("Max number of k-sum pairs:",
          solution.maxOperations(nums, k))  # Expected output: 1
