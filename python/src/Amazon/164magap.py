from typing import List


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        # Step 1: Find min and max
        min_num, max_num = min(nums), max(nums)

        # If all numbers are the same, max gap is 0
        if min_num == max_num:
            return 0

        # Step 2: Calculate bucket size and number of buckets
        n = len(nums)
        bucket_size = max(1, (max_num - min_num) // (n - 1))  # At least size 1
        bucket_count = (max_num - min_num) // bucket_size + 1

        # Step 3: Initialize buckets, each bucket will store the min and max values
        buckets = [[None, None] for _ in range(bucket_count)]

        # Step 4: Distribute the numbers into buckets
        for num in nums:
            idx = (num - min_num) // bucket_size
            if buckets[idx][0] is None:
                buckets[idx][0] = buckets[idx][1] = num
            else:
                buckets[idx][0] = min(buckets[idx][0], num)
                buckets[idx][1] = max(buckets[idx][1], num)

        # Step 5: Calculate the maximum gap
        max_gap = 0
        prev_max = min_num  # Start from the minimum number

        for i in range(bucket_count):
            if buckets[i][0] is None:  # Skip empty buckets
                continue
            # The gap is the difference between the current bucket's min and the previous bucket's max
            max_gap = max(max_gap, buckets[i][0] - prev_max)
            # Update prev_max to the max of the current bucket
            prev_max = buckets[i][1]

        return max_gap
