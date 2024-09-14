import math
from typing import List


class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        def find_divisors(x):
            for i in range(int(math.sqrt(x)), 0, -1):
                if x % i == 0:
                    return [i, x // i]
            return []

    # Find divisors for num+1 and num+2
        divisors1 = find_divisors(num + 1)
        divisors2 = find_divisors(num + 2)

        # Return the pair with the smaller difference between the divisors
        if abs(divisors1[1] - divisors1[0]) < abs(divisors2[1] - divisors2[0]):
            return divisors1
        else:
            return divisors2
