def countSubstringsWithoutRepeatingCharacters(s: str) -> int:
    n = len(s)
    left = 0
    char_set = set()
    count = 0

    for right in range(n):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        count += (right - left + 1)

    return count


# Example usage:
s1 = "abcabc"
print(countSubstringsWithoutRepeatingCharacters(s1))  # Output: 10

s2 = "aaaaa"
print(countSubstringsWithoutRepeatingCharacters(s2))  # Output: 5

s3 = "abac"
print(countSubstringsWithoutRepeatingCharacters(s3))  # Output: 7
