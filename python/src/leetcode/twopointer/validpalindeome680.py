# Given a string s, return true if the s can be palindrome after deleting at most one character from it.

 

# Example 1:

# Input: s = "aba"
# Output: true
# Example 2:

# Input: s = "abca"
# Output: true
# Explanation: You could delete the character 'c'.
# Example 3:

# Input: s = "abc"
# Output: false
 

# Constraints:

# 1 <= s.length <= 105
# s consists of lowercase English letters.

class Solution:

    def isPalindrome1(self,s:str) -> bool:
        left = 0
        right = len(s)-1
        isPalindrome = True

        while left<right:
            if(s[left]!=s[right]):
                isPalindrome = False
                return isPalindrome
            left+=1
            right-=1
        return isPalindrome


    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        #isPalindrome = True
        deletionCount = 0

        while left < right:

            if s[left] != s[right]:
                if deletionCount<1 and self.isPalindrome1(s[left:right]):
                    deletionCount += 1
                    return True
                elif deletionCount<1 and self.isPalindrome1(s[left+1:right+1]):
                    deletionCount += 1
                    return True
                else:
                    return False
            elif(s[left]== s[right]):
                left += 1
                right -= 1

        return True
    

class Solution1:

    def validPalindrome(self, s: str) -> bool:          
          def is_palindrome(left, right):

            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

          left, right = 0, len(s) - 1

          while left < right:
            if s[left] != s[right]:
                # Try deleting either left or right character
                return is_palindrome(left + 1, right) or is_palindrome(left, right - 1)
            left += 1
            right -= 1          

 

          return True

    

if __name__ == '__main__':
    s =Solution1()
    print(s.validPalindrome("aba"))
    print(s.validPalindrome("abca"))
    print(s.validPalindrome("abc"))
    print(s.validPalindrome("deeee"))
    print(s.validPalindrome("atbbga"))