class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        left = 0
        right = 0
        type1 = False
        if(len(typed)<len(name)):
            return type1
        if(name == typed):
            return True
        while left < len(name) or right < len(typed):
            if left < len(name) and  right < len(typed) and name[left] == typed[right]:
                counta=0
                countb=0
                while(left<len(name) and left+1<len(name) and name[left] == name[left+1]):
                    counta+=1
                    left+=1
                while( right < len(typed) and right+1 < len(typed) and typed[right] == typed[right+1]):
                    countb+=1
                    right+=1
                if countb-counta >= 1:
                    type1 = True
                elif countb-counta == 0:
                    pass
                else:
                    type1 = False
                    break  
            else:
                type1 = False
                break 
            if left < len(name):
                    left+=1 
            if right < len(typed):
                    right+=1   
        return type1                                           


class Solution1:
    def isLongPressedName(self, name: str, typed: str) -> bool:
             
             i, j = 0, 0
    
             while j < len(typed):
                if i < len(name) and name[i] == typed[j]:
                    i += 1
                    j += 1
                elif j > 0 and typed[j] == typed[j - 1]:
                    j += 1
                else:
                    return False
    
             return i == len(name)
         



if __name__  == '__main__':
    s = Solution1()
    print(s.isLongPressedName("alex","aaleexa"))   
