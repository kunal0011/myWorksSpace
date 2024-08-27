from collections import Counter


class Solution:
    def relativeSortArray(self, arr1, arr2):
        # Step 1: Count the occurrences of each element in arr1
        count = Counter(arr1)
        result = []

        # Step 2: Place elements from arr2 in the correct order
        for num in arr2:
            if num in count:
                result.extend([num] * count[num])
                del count[num]

        # Step 3: Sort remaining elements and append them
        remaining = sorted(count.elements())
        result.extend(remaining)

        return result
