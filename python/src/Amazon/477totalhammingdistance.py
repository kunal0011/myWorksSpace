from typing import List


class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        total_distance = 0
        n = len(nums)

        # There are at most 32 bits to consider (for 32-bit integers)
        for bit_position in range(32):
            count_ones = 0
            # Count how many numbers have a 1 at the current bit position
            for num in nums:
                if num & (1 << bit_position):
                    count_ones += 1

            count_zeros = n - count_ones
            # The Hamming distance contribution from this bit position
            total_distance += count_ones * count_zeros

        return total_distance


# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    nums = [4, 14, 2]
    print(sol.totalHammingDistance(nums))  # Expected output: 6

    # Test case 2
    nums = [1, 2, 3]
    print(sol.totalHammingDistance(nums))  # Expected output: 4
