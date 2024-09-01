class Solution:
    def getStrongest(self, arr: list[int], k: int) -> list[int]:
        arr.sort()
        median = arr[(len(arr) - 1) // 2]
        arr.sort(key=lambda x: (abs(x - median), x), reverse=True)
        return arr[:k]
