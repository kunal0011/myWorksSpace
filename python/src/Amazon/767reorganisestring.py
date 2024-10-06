import heapq
from collections import Counter


class Solution:
    def reorganizeString(self, s: str) -> str:
        # Count frequency of each character
        count = Counter(s)

        # Create a max heap based on character frequencies
        max_heap = [(-freq, char) for char, freq in count.items()]
        heapq.heapify(max_heap)

        result = []

        # Previous character and its frequency (for re-insertion)
        prev_char = None
        prev_freq = 0

        # While there are characters left to process
        while max_heap:
            freq, char = heapq.heappop(max_heap)
            result.append(char)  # Append current character to result

            # If we have a previous character that we delayed, re-insert it
            if prev_freq < 0:
                heapq.heappush(max_heap, (prev_freq, prev_char))

            # Update previous character and frequency
            prev_char = char
            prev_freq = freq + 1  # Decrease the frequency (since we used it)

        # Join the result list into a string
        reorganized_str = ''.join(result)

        # Check if the rearranged string is valid
        if len(reorganized_str) != len(s):
            return ""

        return reorganized_str

# Test cases


def test_reorganize_string():
    solution = Solution()

    # Test case 1
    assert solution.reorganizeString("aab") == "aba" or solution.reorganizeString(
        "aab") == "bab", "Test case 1 failed"

    # Test case 2
    assert solution.reorganizeString(
        "aaab") == "", "Test case 2 failed"  # Not possible to rearrange

    # Test case 3
    assert solution.reorganizeString("aabbcc") == "abcabc" or solution.reorganizeString(
        "aabbcc") == "abccab" or solution.reorganizeString("aabbcc") == "bacbac", "Test case 3 failed"

    # Test case 4
    assert solution.reorganizeString(
        "") == "", "Test case 4 failed"  # Empty string

    # Test case 5
    assert solution.reorganizeString("abc") == "abc" or solution.reorganizeString("abc") == "acb" or solution.reorganizeString(
        "abc") == "bac" or solution.reorganizeString("abc") == "bca", "Test case 5 failed"

    print("All test cases passed!")


# Run the tests
test_reorganize_string()
