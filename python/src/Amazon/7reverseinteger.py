class Solution:
    def reverse(self, x: int) -> int:

        x = list(str(x)[::-1])
        if x[-1] == '-':
            x.remove('-')
            x.insert(0, '-')
        x = ''.join(x)
        max_val = pow(2, 31)-1
        min_val = -pow(2, 31)
        x = int(x)
        if x <= max_val and x >= min_val:
            return x
        else:
            return 0
