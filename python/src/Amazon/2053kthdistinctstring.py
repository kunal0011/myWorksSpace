from collections import Counter


class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        frequency_map = Counter(arr)

        # Iterate over the array and find the k-th distinct string
        for s in arr:
            if frequency_map[s] == 1:
                k -= 1
                if k == 0:
                    return s

        # If k-th distinct string is not found
        return ""
