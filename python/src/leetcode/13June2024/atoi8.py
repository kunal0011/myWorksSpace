class Solution:
    def myAtoi(self, s: str) -> int:
        if s=="":
            return 0

        count = 0
        while(count < len(s)):
            if(s[count] == ' '):
                count +=1
            else:
                break
            
        s1=''
        if count< len(s)and s[count] == '-':
            s1 = '-'
            count+=1
        elif count< len(s) and s[count] == '+':
            count+=1
        while count < len(s):
            if s[count] == '0':
                count +=1
            else:
                break
        s = list(s[count:])
        result = []
        
        for k,v in enumerate(s):
            if v.isdigit():
                result.append(v)
            else:
                break
        if len(result) == 0:
            return 0 
        if s1=='-':
            result.insert(0,'-')
        s = int(''.join(result))
        if s <= 2**31-1 and s >= -2**31:
            return s
        elif s >2**31-1:
            return 2**31-1
        else:
            return -2**31


if __name__ == '__main__':
    s = Solution()
    print(s.myAtoi("42"))
    print(s.myAtoi(" -042"))
    print(s.myAtoi("1337c0d3"))
    print(s.myAtoi("0-1"))
    print(s.myAtoi("-91283472332"))
    print(s.myAtoi("+1"))