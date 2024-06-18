from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)

        for s in strs:
            # Sort the string and use tuple as key
            sorted_tuple = tuple(sorted(s))
            anagram_map[sorted_tuple].append(s)

        # Convert values (lists of anagrams) to list and return
        return list(anagram_map.values())


if __name__ == '__main__':
    s = Solution()
    print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
