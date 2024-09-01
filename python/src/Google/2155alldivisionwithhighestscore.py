class Solution:
    def maxScoreIndices(self, nums: list[int]) -> list[int]:
        n = len(nums)
        max_score = -1
        scores = []

        # Calculate prefix sums of zeros and ones
        zeros = [0] * (n + 1)
        ones = [0] * (n + 1)

        for i in range(n):
            zeros[i + 1] = zeros[i] + (1 if nums[i] == 0 else 0)
            ones[i + 1] = ones[i] + (1 if nums[i] == 1 else 0)

        for i in range(n + 1):
            score = zeros[i] + (ones[n] - ones[i])
            if score > max_score:
                max_score = score
                scores = [i]
            elif score == max_score:
                scores.append(i)

        return scores
