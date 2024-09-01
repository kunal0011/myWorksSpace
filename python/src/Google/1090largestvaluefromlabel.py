from collections import defaultdict


class Solution:
    def largestValsFromLabels(self, values: list[int], labels: list[int], numWanted: int, useLimit: int) -> int:
        items = sorted(zip(values, labels), reverse=True)
        label_count = defaultdict(int)
        total_value = 0
        count = 0

        for value, label in items:
            if label_count[label] < useLimit:
                total_value += value
                label_count[label] += 1
                count += 1
                if count == numWanted:
                    break

        return total_value
