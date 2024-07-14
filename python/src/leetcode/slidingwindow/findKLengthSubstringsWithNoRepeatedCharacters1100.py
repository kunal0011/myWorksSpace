def findKLengthSubstringsWithNoRepeatedCharacters(s: str, k: int) -> list[str]:
    n = len(s)
    if k > n:
        return []

    char_set = set()
    result = []
    left = 0

    for right in range(n):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        char_set.add(s[right])

        if right - left + 1 == k:
            result.append(s[left:right + 1])
            char_set.remove(s[left])
            left += 1

    return result


# Example usage:
s1 = "abcabc"
k1 = 3
print(findKLengthSubstringsWithNoRepeatedCharacters(
    s1, k1))  # Output: ['abc', 'bca', 'cab']

s2 = "abcdefg"
k2 = 2
# Output: ['ab', 'bc', 'cd', 'de', 'ef', 'fg']
print(findKLengthSubstringsWithNoRepeatedCharacters(s2, k2))

s3 = "aaaaa"
k3 = 2
print(findKLengthSubstringsWithNoRepeatedCharacters(s3, k3))  # Output: []
