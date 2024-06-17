class Solution:
    def countAndSay(self, n: int) -> str:

        def countAndSay1(n) -> str:
            if n == 1:
                return '1'
            out = countAndSay1(n-1)
            if len(out) == 1:
                return ''.join([str(1), out[0]])
            if len(out) == 2:
                if out[0] == out[1]:
                    return ''.join([str(2), out[0]])
                else:
                    return ''.join([str(1), out[0], str(1), out[1]])

            l = []
            count = 1
            left = 0
            while left < len(out)-1:
                if out[left] == out[left+1]:
                    count += 1
                else:
                    l.append(str(count))
                    l.append(out[left])
                    count = 1
                left += 1

            if out[len(out)-1] == out[left]:
                l.append(str(count))
                l.append(out[left])
            else:
                l.append(str(1))
                l.append(out[len(out)-1])
            return ''.join(l)
        return countAndSay1(n)


class Solution1:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        def describe(s):
            result = []
            i = 0
            while i < len(s):
                count = 1
                while i + 1 < len(s) and s[i] == s[i + 1]:
                    count += 1
                    i += 1
                result.append(str(count) + s[i])
                i += 1
            return ''.join(result)
        result = "1"
        for _ in range(2, n + 1):
            result = describe(result)

        return result


if __name__ == '__main__':
    s = Solution()

    print(s.countAndSay(1))
    print(s.countAndSay(2))
    print(s.countAndSay(3))
    print(s.countAndSay(4))
    print(s.countAndSay(5))
    print(s.countAndSay(6))
    print(s.countAndSay(7))
