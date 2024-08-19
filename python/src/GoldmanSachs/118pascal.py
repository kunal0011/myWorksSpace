from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []

        for i in range(numRows):
            # Start each row with 1
            row = [1] * (i + 1)
            # Fill in the values in between the 1s
            for j in range(1, i):
                row[j] = res[i - 1][j - 1] + res[i - 1][j]
            # Append the row to the result
            res.append(row)

        return res


if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    numRows1 = 5
    print(solution.generate(numRows1))
    # Output:
    # [
    #     [1],
    #     [1, 1],
    #     [1, 2, 1],
    #     [1, 3, 3, 1],
    #     [1, 4, 6, 4, 1]
    # ]

    # Test case 2
    numRows2 = 1
    print(solution.generate(numRows2))
    # Output:
    # [
    #     [1]
    # ]

    # Test case 3
    numRows3 = 3
    print(solution.generate(numRows3))
    # Output:
    # [
    #     [1],
    #     [1, 1],
    #     [1, 2, 1]
    # ]

    # Test case 4
    numRows4 = 0
    print(solution.generate(numRows4))
    # Output:
    # []
