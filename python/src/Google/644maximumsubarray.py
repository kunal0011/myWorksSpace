class Solution:
    def maxAverage(self, nums, k):
        def can_find_larger_average(mid):
            cum_sum = [0] * (len(nums) + 1)
            for i in range(len(nums)):
                cum_sum[i + 1] = cum_sum[i] + nums[i] - mid

            min_prefix = 0
            for i in range(k, len(cum_sum)):
                if cum_sum[i] - min_prefix >= 0:
                    return True
                min_prefix = min(min_prefix, cum_sum[i - k + 1])
            return False

        left, right = min(nums), max(nums)
        while right - left > 1e-5:
            mid = (left + right) / 2
            if can_find_larger_average(mid):
                left = mid
            else:
                right = mid

        return left
