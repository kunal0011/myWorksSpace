from collections import Counter
from itertools import permutations
from typing import List


class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        # Count the frequency of each character
        freq = Counter(s)

        # Check for more than one odd frequency characters
        odd_char = ''
        half = []

        for char, count in freq.items():
            if count % 2 == 1:
                if odd_char:
                    return []  # More than one odd frequency character, no palindrome possible
                odd_char = char
            half.append(char * (count // 2))

        # Generate permutations of half of the palindrome
        half_str = ''.join(half)
        permutations_set = set(permutations(half_str))

        # Construct the full palindromes
        palindromes = []
        for half_perm in permutations_set:
            half_perm_str = ''.join(half_perm)
            full_palindrome = half_perm_str + odd_char + half_perm_str[::-1]
            palindromes.append(full_palindrome)

        return palindromes
