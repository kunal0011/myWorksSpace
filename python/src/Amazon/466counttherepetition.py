class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        if not set(s2).issubset(set(s1)):
            return 0

        s1_count, s2_count = 0, 0
        index_s2 = 0
        recall = {}

        while s1_count < n1:
            for char in s1:
                if char == s2[index_s2]:
                    index_s2 += 1
                if index_s2 == len(s2):
                    s2_count += 1
                    index_s2 = 0

            s1_count += 1

            # Check if there's a cycle
            if index_s2 in recall:
                prev_s1_count, prev_s2_count = recall[index_s2]
                cycle_s1 = s1_count - prev_s1_count
                cycle_s2 = s2_count - prev_s2_count

                remaining_s1 = n1 - s1_count
                cycles = remaining_s1 // cycle_s1

                s1_count += cycles * cycle_s1
                s2_count += cycles * cycle_s2
            else:
                recall[index_s2] = (s1_count, s2_count)

        return s2_count // n2
