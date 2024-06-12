class Solution:
    def reverse(self, x: int) -> int:
        
        x = list(str(x)[::-1])
        if x[-1] == '-':
            x.remove('-')
            x.insert(0,'-')
        x = ''.join(x)
        max_val = pow(2,31)-1
        min_val = -pow(2,31)
        x = int(x)
        if x <= max_val and x >= min_val:
            return x
        else:
            return 0
        
class Solution1:
    def reverse(self, x: int) -> int:
        ans = 0
        mi, mx = -(2**31), 2**31 - 1
        while x:
            if ans < mi // 10 + 1 or ans > mx // 10:
                return 0
            y = x % 10
            if x < 0 and y > 0:
                y -= 10
            ans = ans * 10 + y
            x = (x - y) // 10
        return ans        
        
        
    
if __name__ == '__main__':
    s = Solution1()
    #print(s.reverse(1563847412))
    print(s.reverse(-123))
    #print(s.reverse(120))