class Solution:
    def isBoomerang(self, points: list[list[int]]) -> bool:
        (x1, y1), (x2, y2), (x3, y3) = points
        return (y2 - y1) * (x3 - x1) != (y3 - y1) * (x2 - x1)
