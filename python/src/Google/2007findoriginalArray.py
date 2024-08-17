from collections import Counter
from typing import List


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 != 0:
            return []

        changed.sort()
        freq_map = Counter(changed)
        original = []

        for x in changed:
            if freq_map[x] == 0:
                continue
            if freq_map[2 * x] == 0:
                return []

            original.append(x)
            freq_map[x] -= 1
            freq_map[2 * x] -= 1

        return original
