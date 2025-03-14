class Solution:
    def countSmaller(self, nums):
        def merge_sort(enum):
            half = len(enum) // 2
            if half:
                left, right = merge_sort(enum[:half]), merge_sort(enum[half:])
                for i in range(len(enum))[::-1]:
                    if not right or left and left[-1][1] > right[-1][1]:
                        smaller[left[-1][0]] += len(right)
                        enum[i] = left.pop()
                    else:
                        enum[i] = right.pop()
            return enum

        smaller = [0] * len(nums)
        merge_sort(list(enumerate(nums)))
        return smaller


print(Solution().countSmaller([5, 2, 6, 1]))
