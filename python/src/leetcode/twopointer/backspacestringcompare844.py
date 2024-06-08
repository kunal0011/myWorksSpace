# Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

# Note that after backspacing an empty text, the text will continue empty.

 

# Example 1:

# Input: s = "ab#c", t = "ad#c"
# Output: true
# Explanation: Both s and t become "ac".
# Example 2:

# Input: s = "ab##", t = "c#d#"
# Output: true
# Explanation: Both s and t become "".
# Example 3:

# Input: s = "a#c", t = "b"
# Output: false
# Explanation: s becomes "c" while t becomes "b".

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build_final_string(s: str) -> str:
            stack = []
            for char in s:
                if char != '#':
                    stack.append(char)
                elif stack:
                    stack.pop()
            return ''.join(stack)
        
        return build_final_string(s) == build_final_string(t)

    

if __name__ == '__main__':
    s =Solution()
    print(s.backspaceCompare("ab#c","ad#c")) 
    print(s.backspaceCompare("ab##","c#d#"))
    print(s.backspaceCompare("a#c","b"))
    