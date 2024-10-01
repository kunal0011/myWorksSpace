from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr):
        # Step 1: Count the occurrences of each element in arr
        count = Counter(arr)

        # Step 2: Get the set of occurrences
        occurrences = set(count.values())

        # Step 3: Compare the length of occurrences with the length of the count dictionary
        return len(occurrences) == len(count)
