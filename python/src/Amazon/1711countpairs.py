from collections import defaultdict


class Solution:
    def countPairs(self, deliciousness: list[int]) -> int:
        MOD = 10**9 + 7
        count_map = defaultdict(int)
        # Powers of two from 1 to 2^21 (since deliciousness[i] <= 2^20)
        power_of_twos = [2**i for i in range(22)]
        count = 0

        for d in deliciousness:
            for target in power_of_twos:
                count += count_map[target - d]
                count %= MOD
            count_map[d] += 1

        return count


# Testing the solution
if __name__ == "__main__":
    solution = Solution()

    # Test case
    deliciousness = [1, 3, 5, 7, 9]
    print("Count of good meals:", solution.countPairs(
        deliciousness))  # Expected output: 4
