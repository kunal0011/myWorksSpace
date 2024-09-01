class Solution:
    def trimMean(self, arr: list[int]) -> float:
        arr.sort()
        n = len(arr)
        trim = n // 20
        trimmed_arr = arr[trim: n - trim]
        return sum(trimmed_arr) / len(trimmed_arr)
