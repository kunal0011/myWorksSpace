from collections import Counter


class Solution:
    def largestUniqueNumber(self, A: list[int]) -> int:
        # Count the frequency of each number in the array
        count = Counter(A)

        # Initialize the result as -1 (in case there is no unique number)
        largest_unique = -1

        # Iterate over the count dictionary and find the largest number that occurs once
        for num, freq in count.items():
            if freq == 1 and num > largest_unique:
                largest_unique = num

        return largest_unique
