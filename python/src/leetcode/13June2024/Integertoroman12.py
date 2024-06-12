from collections import OrderedDict
class Solution:
    def intToRoman(self, num: int) -> str:
        d = OrderedDict()
        d[1000] = 'M'
        d[900] = 'CM'
        d[500] = 'D'
        d[400] = 'CD'
        d[100] = 'C'
        d[90] = 'XC'
        d[50] = 'L'
        d[40] = 'XL'
        d[10] = 'X'
        d[9] = 'IX'
        d[5] = 'V'
        d[4] = 'IV'
        d[1] = 'I'
        result = []
        for k,v in d.items():
            if num >= k:
                while num >= k:
                    result.append(v)
                    num -= k

        return ''.join(result)

class Solution1:
    def intToRoman(self, num: int) -> str:
        cs = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
        vs = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
        ans = []
        for c, v in zip(cs, vs):
            while num >= v:
                num -= v
                ans.append(c)
        return ''.join(ans)

    
if __name__ == '__main__':
    s = Solution1()
    print(s.intToRoman(123))
    print(s.intToRoman(3749))
    print(s.intToRoman(58))
    print(s.intToRoman(1994))