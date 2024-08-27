import math
from typing import List


class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        result = []

        # Iterate over all possible denominators from 2 to n
        for d in range(2, n + 1):
            # Iterate over possible numerators from 1 to d-1
            for num in range(1, d):
                # Check if gcd of num and d is 1
                if math.gcd(num, d) == 1:
                    result.append(f"{num}/{d}")

        return result
