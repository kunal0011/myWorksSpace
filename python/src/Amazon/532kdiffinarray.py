from collections import Counter
from typing import List


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            # The absolute difference can't be negative, so no pairs can be found.
            return 0

        count = 0
        freq = Counter(nums)  # Count the frequency of each number in the list

        if k == 0:
            # If k == 0, we're looking for duplicates, i.e., numbers that appear at least twice
            for num in freq:
                if freq[num] > 1:
                    count += 1
        else:
            # If k > 0, we need to check if num + k exists for each unique num
            for num in freq:
                if num + k in freq:
                    count += 1

        return count


# Test case
if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    nums = [3, 1, 4, 1, 5]
    k = 2
    print(sol.findPairs(nums, k))  # Expected output: 2

    # Test case 2
    nums = [1, 2, 3, 4, 5]
    k = 1
    print(sol.findPairs(nums, k))  # Expected output: 4

    # Test case 3
    nums = [1, 3, 1, 5, 4]
    k = 0
    print(sol.findPairs(nums, k))  # Expected output: 1
