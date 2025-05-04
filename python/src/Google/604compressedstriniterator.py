"""
LeetCode 604 - Design Compressed String Iterator

Problem Statement:
Design and implement a data structure for a compressed string iterator. The given compressed string will be in the form of each character followed by its count (e.g., a2b3c4).

Implement the StringIterator class:
- StringIterator(String compressedString) initializes the object with the compressed string.
- next() returns the next character if the original string still has uncompressed characters, otherwise returns ' '.
- hasNext() returns true if there is still at least one character to decompress, otherwise returns false.

Logic:
- Use two pointers to keep track of current character and its count
- Parse the compressed string to extract character and its count
- Maintain current count and decrement it for each next() call
- When current count becomes 0, move to next character-count pair
- Use string and integer parsing to handle multi-digit counts

Time Complexity:
- Constructor: O(1)
- next(): O(1) amortized
- hasNext(): O(1)

Space Complexity: O(1)
"""


class StringIterator:
    def __init__(self, compressedString: str):
        self.s = compressedString
        self.ptr = 0  # pointer to current character
        self.curr_char = ' '
        self.curr_count = 0
        self.length = len(compressedString)

    def next(self) -> str:
        if not self.hasNext():
            return ' '

        # If we've used up current character's count, move to next char
        if self.curr_count == 0:
            if self.ptr >= self.length:
                return ' '

            self.curr_char = self.s[self.ptr]
            self.ptr += 1

            # Parse the count (handle multi-digit numbers)
            count = 0
            while self.ptr < self.length and self.s[self.ptr].isdigit():
                count = count * 10 + int(self.s[self.ptr])
                self.ptr += 1
            self.curr_count = count

        self.curr_count -= 1
        return self.curr_char

    def hasNext(self) -> bool:
        return self.curr_count > 0 or self.ptr < self.length


# Test driver
def test_string_iterator():
    print("Test Case 1:")
    iterator = StringIterator("L1e2t1C1o1d1e1")
    test_cases = [
        ("next()", iterator.next()),    # returns "L"
        ("next()", iterator.next()),    # returns "e"
        ("next()", iterator.next()),    # returns "e"
        ("next()", iterator.next()),    # returns "t"
        ("next()", iterator.next()),    # returns "C"
        ("next()", iterator.next()),    # returns "o"
        ("next()", iterator.next()),    # returns "d"
        ("next()", iterator.next()),    # returns "e"
        ("hasNext()", iterator.hasNext()),  # returns false
        ("next()", iterator.next()),    # returns " "
    ]

    for operation, result in test_cases:
        print(f"{operation}: {result}")

    print("\nTest Case 2:")
    iterator2 = StringIterator("a10")
    for i in range(15):
        print(f"next(): {iterator2.next()}")
    print(f"hasNext(): {iterator2.hasNext()}")


if __name__ == "__main__":
    test_string_iterator()
