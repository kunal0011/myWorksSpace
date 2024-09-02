from typing import List


class Solution:
    def isConvex(self, points: List[List[int]]) -> bool:
        def cross_product(p1, p2, p3):
            # Calculate the cross product of vector p1p2 and p2p3
            return (p2[0] - p1[0]) * (p3[1] - p2[1]) - (p2[1] - p1[1]) * (p3[0] - p2[0])

        n = len(points)
        prev_cross = 0

        for i in range(n):
            p1 = points[i]
            p2 = points[(i + 1) % n]
            p3 = points[(i + 2) % n]
            curr_cross = cross_product(p1, p2, p3)

            if curr_cross != 0:
                if curr_cross * prev_cross < 0:
                    return False
                prev_cross = curr_cross

        return True
