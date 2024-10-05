from collections import defaultdict


class Solution:
    def fourSumCount(self, nums1, nums2, nums3, nums4) -> int:
        count = 0
        # Create a dictionary to store the frequency of sums from nums1 and nums2
        sum_map = defaultdict(int)

        # Compute all pair sums from nums1 and nums2 and store in the hashmap
        for a in nums1:
            for b in nums2:
                sum_map[a + b] += 1

        # Compute all pair sums from nums3 and nums4, and check if their negation exists in sum_map
        for c in nums3:
            for d in nums4:
                target = -(c + d)
                if target in sum_map:
                    count += sum_map[target]

        return count
