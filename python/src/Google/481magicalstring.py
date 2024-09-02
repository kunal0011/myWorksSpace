class Solution:
    def magicalString(self, n: int) -> int:
        if n == 0:
            return 0
        if n <= 3:
            return 1

        s = [1, 2, 2]
        idx = 2

        while len(s) < n:
            s.extend([3 - s[-1]] * s[idx])
            idx += 1

        return s[:n].count(1)
