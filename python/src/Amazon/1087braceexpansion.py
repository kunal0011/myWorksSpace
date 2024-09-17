from itertools import product
from typing import List

# Problem:
# You are given a string expression that contains groups of letters that are enclosed in curly braces {}. Inside each group, letters are separated by commas. Your task is to generate all possible words formed by choosing one letter from each group and return them sorted lexicographically.

# For example:
# Input: {a,b}c{d,e}f
# Output: ["acdf", "acef", "bcdf", "bcef"]


class Solution:
    def expand(self, s: str) -> List[str]:
        # Parse the string to create a list of options for each position
        groups = []
        i = 0
        while i < len(s):
            if s[i] == '{':
                # Start of a group
                i += 1
                group = []
                while s[i] != '}':
                    if s[i] != ',':
                        group.append(s[i])
                    i += 1
                # sort to ensure lexicographical order
                groups.append(sorted(group))
            else:
                # Just a single character (not in braces)
                groups.append([s[i]])
            i += 1

        # Use itertools.product to get all combinations
        result = [''.join(combo) for combo in product(*groups)]
        return result
