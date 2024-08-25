def validWordAbbreviation(word: str, abbr: str) -> bool:
    i = 0  # Pointer for word
    j = 0  # Pointer for abbr

    while i < len(word) and j < len(abbr):
        if abbr[j].isdigit():
            if abbr[j] == '0':  # Leading zeros are not allowed
                return False
            num = 0
            while j < len(abbr) and abbr[j].isdigit():
                num = num * 10 + int(abbr[j])
                j += 1
            i += num
        else:
            if i >= len(word) or word[i] != abbr[j]:
                return False
            i += 1
            j += 1

    return i == len(word) and j == len(abbr)


# Example usage:
print(validWordAbbreviation("internationalization", "i12iz4n"))  # True
print(validWordAbbreviation("apple", "a2e"))  # False
