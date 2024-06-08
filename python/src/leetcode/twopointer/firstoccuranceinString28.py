# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

# Example 1:

# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
# Example 2:

# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

# Constraints:

# 1 <= haystack.length, needle.length <= 104
# haystack and needle consist of only lowercase English characters.


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        left=0
        right =0

        if len(haystack) < len(needle):
            return -1

        while left < len(haystack):

            if haystack[left] != needle[right]:
                left += 1
                right = 0
            else:
                out1 = left
                count = 0
                while right != len(needle) and out1< len(haystack):
                    if haystack[out1] != needle[right]:
                        break
                    else:
                        count+=1  
                    right += 1
                    out1 += 1
                if count == len(needle):
                    return left
                left+=1
                right=0

            
        return -1


class Solution1:
    def strStr(self, haystack: str, needle: str) -> int:

        #return haystack.find(needle)
            h_len = len(haystack)
            n_len = len(needle)
            
            if n_len == 0:
                return 0
            if n_len > h_len:
                return -1
            
            # Slide over the haystack
            for i in range(h_len - n_len + 1):
                # Check the substring from the current index i
                if haystack[i:i + n_len] == needle:
                    return i
            
            return -1
    
if __name__ == '__main__':
    s = Solution1()
    #print(s.strStr("sadbutsad","sad"))
    #print(s.strStr("leetcode","leeto"))
    print(s.strStr("mississippi","issipi"))
    # print(s.strStr("",""))