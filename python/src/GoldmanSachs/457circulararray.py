from typing import List


class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)

        def next_index(i):
            return (i + nums[i]) % n

        for i in range(n):
            if nums[i] == 0:
                continue

            slow, fast = i, next_index(i)
            direction = nums[i] > 0

            while nums[fast] != 0 and (nums[fast] > 0) == direction and (nums[next_index(fast)] > 0) == direction:
                if slow == fast:
                    if slow == next_index(slow):
                        break
                    return True

                slow = next_index(slow)
                fast = next_index(next_index(fast))

            # Mark all elements in the current path as visited
            slow = i
            while nums[slow] != 0 and (nums[slow] > 0) == direction:
                next_slow = next_index(slow)
                nums[slow] = 0
                slow = next_slow

        return False
