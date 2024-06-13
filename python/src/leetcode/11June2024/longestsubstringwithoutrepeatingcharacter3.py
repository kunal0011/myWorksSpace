
# Given a string s, find the length of the longest 
# substring
#  without repeating characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

# Constraints:

# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.


from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:      
        n = len(s)   
        left, right = 0, 0
        d = defaultdict(list)
        max_len = 0
        while(right < n):
            if s[right] not in d:
                d[s[right]].append(right)
                #max_len = max(max_len,right-left-1)
            else:
                max_len = max(max_len,right-left)
                while left < right:
                    if s[left] != s[right]:
                        del d[s[left]]
                        left += 1
                    else:
                        left = d[s[right]][-1] + 1 
                        d[s[right]].clear()
                        d[s[right]].append(right)
                        break           
            right += 1

        
        return max(max_len,right-left)
    
class Solution1:
  def lengthOfLongestSubstring(self, s): # map for index
    d = {} # value => its index
    i = 0
    ans = 0
    for j, c in enumerate(s):
      if c in d:
        # mast max check i, example "abba"
        i = max(i, d[c] + 1)
      d[c] = j
      ans = max(ans, j - i + 1)
    return ans
    
if __name__ == '__main__':
    s = Solution1()
    print(s.lengthOfLongestSubstring("abcabcbb"))
    print(s.lengthOfLongestSubstring("bbbbb")) 
    print(s.lengthOfLongestSubstring("pwwkew"))
    print(s.lengthOfLongestSubstring("ab"))
    print(s.lengthOfLongestSubstring(" "))
    print(s.lengthOfLongestSubstring("aa"))
    print(s.lengthOfLongestSubstring("tmmzuxt"))  