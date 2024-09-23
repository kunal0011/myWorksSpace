from typing import List


class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m, k, n = len(mat1), len(mat1[0]), len(mat2[0])
        result = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(k):
                if mat1[i][j] != 0:
                    for l in range(n):
                        if mat2[j][l] != 0:
                            result[i][l] += mat1[i][j] * mat2[j][l]

        return result
