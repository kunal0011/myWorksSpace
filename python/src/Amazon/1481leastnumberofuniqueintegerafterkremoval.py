from collections import Counter


class Solution:
    def findLeastNumOfUniqueInts(self, arr, k: int) -> int:
        # Step 1: Count the frequency of each element
        freq = Counter(arr)

        # Step 2: Sort the frequencies by ascending order of frequency
        freq_sorted = sorted(freq.values())

        # Step 3: Remove elements by frequency
        # Start with the total number of unique integers
        unique_count = len(freq_sorted)

        for count in freq_sorted:
            if k >= count:
                # Remove all occurrences of this element
                k -= count
                unique_count -= 1  # Reduce the unique integer count
            else:
                break  # No more complete removal possible, stop the process

        return unique_count

# Test cases


def test_findLeastNumOfUniqueInts():
    sol = Solution()

    # Test Case 1: Removing least frequent elements
    assert sol.findLeastNumOfUniqueInts(
        [5, 5, 4], 1) == 1, "Test Case 1 Failed"

    # Test Case 2: Removing multiple least frequent elements
    assert sol.findLeastNumOfUniqueInts(
        [4, 3, 1, 1, 3, 3, 2], 3) == 2, "Test Case 2 Failed"

    # Test Case 3: All elements are removed
    assert sol.findLeastNumOfUniqueInts(
        [2, 4, 1, 1, 2, 3, 4], 5) == 1, "Test Case 3 Failed"

    # Test Case 4: No elements need to be removed
    assert sol.findLeastNumOfUniqueInts(
        [1, 2, 3], 0) == 3, "Test Case 4 Failed"

    print("All test cases passed!")


# Run the tests
test_findLeastNumOfUniqueInts()
