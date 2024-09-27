from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        n = len(nums)
        self.nums = nums
        self.tree = [0] * (2 * n)
        # Build the segment tree
        for i in range(n):
            self.tree[n + i] = nums[i]
        for i in range(n - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def update(self, index: int, val: int) -> None:
        # Update the value at index
        n = len(self.nums)
        pos = index + n
        self.tree[pos] = val
        # Update the tree
        while pos > 1:
            pos //= 2
            self.tree[pos] = self.tree[2 * pos] + self.tree[2 * pos + 1]

    def sumRange(self, left: int, right: int) -> int:
        # Compute the sum of the range [left, right]
        n = len(self.nums)
        left += n
        right += n
        sum_ = 0
        while left <= right:
            if left % 2 == 1:
                sum_ += self.tree[left]
                left += 1
            if right % 2 == 0:
                sum_ += self.tree[right]
                right -= 1
            left //= 2
            right //= 2
        return sum_
