class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        map_s_to_t = {}  # Mapping from characters in s to characters in t
        map_t_to_s = {}  # Mapping from characters in t to characters in s

        for char_s, char_t in zip(s, t):
            # Check if char_s is already in map_s_to_t
            if char_s in map_s_to_t:
                if map_s_to_t[char_s] != char_t:
                    return False  # Inconsistent mapping
            else:
                map_s_to_t[char_s] = char_t

            # Check if char_t is already in map_t_to_s
            if char_t in map_t_to_s:
                if map_t_to_s[char_t] != char_s:
                    return False  # Inconsistent mapping
            else:
                map_t_to_s[char_t] = char_s

        return True  # If we reach here, the strings are isomorphic
