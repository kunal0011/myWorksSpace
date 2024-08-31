from collections import defaultdict


class Solution:
    def isPossible(self, nums: list[int]) -> bool:
        # Frequency map to count occurrences of each number in nums
        freq = defaultdict(int)
        # Append map to track the number of subsequences that can be extended with a given number
        append = defaultdict(int)

        # Populate the frequency map
        for num in nums:
            freq[num] += 1

        # Iterate through the array to build subsequences
        for num in nums:
            if freq[num] == 0:
                continue

            # If we can append `num` to an existing subsequence ending in `num-1`
            if append[num - 1] > 0:
                append[num - 1] -= 1
                append[num] += 1
            # Otherwise, try to start a new subsequence with `num, num+1, num+2`
            elif freq[num + 1] > 0 and freq[num + 2] > 0:
                freq[num + 1] -= 1
                freq[num + 2] -= 1
                append[num + 2] += 1
            else:
                return False

            # Decrement the frequency of `num` as it is used
            freq[num] -= 1

        return True
