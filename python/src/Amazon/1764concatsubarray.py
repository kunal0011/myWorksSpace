class Solution:
    def canChoose(self, groups: list[list[int]], nums: list[int]) -> bool:
        idx = 0  # index in nums
        n = len(nums)

        # Iterate over each group in groups
        for group in groups:
            found = False

            # Try to match group in nums starting from index idx
            while idx + len(group) <= n:
                # Check if nums[idx:idx+len(group)] matches group
                if nums[idx:idx+len(group)] == group:
                    found = True
                    idx += len(group)  # Move index forward
                    break

                # Move to the next index in nums
                idx += 1

            # If the group was not found, return False
            if not found:
                return False

        return True
