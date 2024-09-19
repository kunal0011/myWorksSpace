from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total_sum = sum(nums)

        # If the total sum isn't divisible by k, partitioning isn't possible
        if total_sum % k != 0:
            return False

        target_sum = total_sum // k
        nums.sort(reverse=True)  # Sorting helps to speed up the process

        # If the largest number is greater than the target sum, partitioning is impossible
        if nums[0] > target_sum:
            return False

        # Initialize an array to track the current sum of each subset
        subset_sums = [0] * k

        # Backtracking function to check if we can partition the array into k subsets
        def backtrack(index):
            # If all numbers have been assigned, we successfully partitioned the array
            if index == len(nums):
                return True

            # Try to assign the current number to each subset
            for i in range(k):
                if subset_sums[i] + nums[index] <= target_sum:
                    subset_sums[i] += nums[index]
                    if backtrack(index + 1):
                        return True
                    # Backtrack
                    subset_sums[i] -= nums[index]

                # If the current subset is empty, there's no point in continuing with further subsets
                if subset_sums[i] == 0:
                    break

            return False

        return backtrack(0)


# Test the function
if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    nums1 = [4, 3, 2, 3, 5, 2, 1]
    k1 = 4
    print(sol.canPartitionKSubsets(nums1, k1))  # Output: True

    # Test case 2
    nums2 = [1, 2, 3, 4]
    k2 = 3
    print(sol.canPartitionKSubsets(nums2, k2))  # Output: False
