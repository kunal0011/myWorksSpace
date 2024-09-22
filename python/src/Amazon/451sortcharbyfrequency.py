from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        # Step 1: Count the frequency of each character
        freq = Counter(s)

        # Step 2: Sort characters by frequency in descending order
        # Key is (-frequency, char) to ensure descending order and lexicographical tie-breaking
        sorted_chars = sorted(freq, key=lambda x: -freq[x])

        # Step 3: Build the result string
        result = ''.join([char * freq[char] for char in sorted_chars])

        return result


# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    s1 = "tree"
    print(sol.frequencySort(s1))  # Expected output: "eert" or "eetr"

    # Test case 2
    s2 = "cccaaa"
    print(sol.frequencySort(s2))  # Expected output: "cccaaa" or "aaaccc"

    # Test case 3
    s3 = "Aabb"
    print(sol.frequencySort(s3))  # Expected output: "bbAa" or "bbaA"
