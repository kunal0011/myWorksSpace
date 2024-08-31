from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        # Create an array to store the number of 1 bits for each number from 0 to n
        ans = [0] * (n + 1)

        # Iterate over each number from 1 to n
        for i in range(1, n + 1):
            # The number of 1 bits in i is 1 plus the number of 1 bits in i // 2
            ans[i] = ans[i >> 1] + (i & 1)

        return ans
