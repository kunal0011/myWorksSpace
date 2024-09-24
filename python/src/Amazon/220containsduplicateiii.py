from typing import List


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if t < 0 or k < 1:
            return False

        bucket = {}
        bucket_size = t + 1  # Bucket size is t + 1 to handle the range of numbers

        for i, num in enumerate(nums):
            bucket_id = num // bucket_size

            # If a number exists in the current bucket, return True
            if bucket_id in bucket:
                return True

            # Check adjacent buckets
            if bucket_id - 1 in bucket and abs(num - bucket[bucket_id - 1]) <= t:
                return True
            if bucket_id + 1 in bucket and abs(num - bucket[bucket_id + 1]) <= t:
                return True

            # Insert the number into the bucket
            bucket[bucket_id] = num

            # Remove elements outside the sliding window
            if i >= k:
                del bucket[nums[i - k] // bucket_size]

        return False
