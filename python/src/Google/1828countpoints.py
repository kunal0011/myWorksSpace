class Solution:
    def countPoints(self, points: list[list[int]], queries: list[list[int]]) -> list[int]:
        result = []

        for qx, qy, qr in queries:
            count = 0
            for px, py in points:
                if (qx - px) ** 2 + (qy - py) ** 2 <= qr ** 2:
                    count += 1
            result.append(count)

        return result
