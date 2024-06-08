# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

# Example 1:

# Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:

# Input: s = "axc", t = "ahbgdc"
# Output: false
 

# Constraints:

# 0 <= s.length <= 100
# 0 <= t.length <= 104
# s and t consist only of lowercase English letters.

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        if s == "":
            return True

        left = 0
        right = 0
        count=0
        while left < len(t):
            if  t[left] != s[right]:
                left += 1
            else:
                count+=1
                if count==len(s):
                    return True
                left+=1
                right+=1
        return False
    
if __name__ == '__main__':
    s =Solution()
    print(s.isSubsequence("axc","ahbgdc"))
    print(s.isSubsequence("abc","ahbgdc"))
    print(s.isSubsequence("b","abc"))  