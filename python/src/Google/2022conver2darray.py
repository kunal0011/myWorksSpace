class Solution:
    def construct2DArray(self, original: list[int], m: int, n: int) -> list[list[int]]:
        if m * n != len(original):
            return []

        result = []
        for i in range(0, len(original), n):
            result.append(original[i:i + n])

        return result
