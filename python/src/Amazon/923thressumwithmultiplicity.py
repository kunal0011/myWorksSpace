from collections import Counter
import itertools


class Solution:
    def threeSumMulti(self, A: list[int], target: int) -> int:
        MOD = 10**9 + 7
        count = Counter(A)
        keys = sorted(count)
        ans = 0

        # Iterate over all combinations of 3 distinct keys
        for i, x in enumerate(keys):
            count_x = count[x]
            for j in range(i, len(keys)):
                y = keys[j]
                count_y = count[y]
                for k in range(j, len(keys)):
                    z = keys[k]
                    count_z = count[z]

                    if x + y + z == target:
                        if x == y == z:
                            ans += count_x * (count_x - 1) * (count_x - 2) // 6
                        elif x == y:
                            ans += count_x * (count_x - 1) // 2 * count_z
                        elif y == z:
                            ans += count_y * (count_y - 1) // 2 * count_x
                        else:
                            ans += count_x * count_y * count_z

        return ans % MOD


# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    A1 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
    target1 = 8
    print(sol.threeSumMulti(A1, target1))  # Expected output: 20

    # Test case 2
    A2 = [1, 1, 1, 1, 1]
    target2 = 3
    print(sol.threeSumMulti(A2, target2))  # Expected output: 10
