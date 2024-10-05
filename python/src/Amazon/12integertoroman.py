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
        for k, v in d.items():
            if num >= k:
                while num >= k:
                    result.append(v)
                    num -= k

        return ''.join(result)
