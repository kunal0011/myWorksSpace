class NumArray:
    def __init__(self, nums):
        n = len(nums)
        self.nums = nums
        self.tree = [0] * (2 * n)
        self.build_tree(nums)

    def build_tree(self, nums):
        n = len(nums)
        for i in range(n):
            self.tree[n + i] = nums[i]
        for i in range(n - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def update(self, index, val):
        n = len(self.nums)
        pos = n + index
        self.tree[pos] = val
        while pos > 1:
            pos //= 2
            self.tree[pos] = self.tree[2 * pos] + self.tree[2 * pos + 1]

    def sumRange(self, left, right):
        n = len(self.nums)
        left += n
        right += n + 1
        sum_ = 0
        while left < right:
            if left % 2 == 1:
                sum_ += self.tree[left]
                left += 1
            if right % 2 == 1:
                right -= 1
                sum_ += self.tree[right]
            left //= 2
            right //= 2
        return sum_
