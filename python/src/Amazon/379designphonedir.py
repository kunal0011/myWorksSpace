"""
LeetCode 379: Design Phone Directory

Design a Phone Directory which supports the following operations:

1. get(): Provides a number which is not assigned to anyone. Returns -1 if no number is available.
2. check(number): Check if a number is available or not.
3. release(number): Recycle or release a number.

The system should support efficient allocation and deallocation with the following constraints:
- Numbers are available from 0 to maxNumbers-1
- No two users can acquire the same number
- Released numbers can be re-used
- Each valid number should be released exactly once

Time Complexity: 
- get(): O(1)
- check(number): O(1)
- release(number): O(1)
Space Complexity: O(N) where N is maxNumbers
"""

from collections import deque


class PhoneDirectory:
    def __init__(self, maxNumbers: int):
        """
        Initialize the PhoneDirectory with a queue of available numbers
        and a set to track which numbers are currently in use.
        
        Args:
            maxNumbers (int): The maximum number of available phone numbers (0 to maxNumbers-1)
        """
        # Using deque for O(1) operations on both ends
        self.available_numbers = deque(range(maxNumbers))
        # Using set for O(1) lookup of in-use numbers
        self.in_use = set()

    def get(self) -> int:
        """
        Provides an available number. Returns -1 if no number is available.
        
        Returns:
            int: An available number, or -1 if none are available
        """
        if self.available_numbers:
            number = self.available_numbers.popleft()
            self.in_use.add(number)
            return number
        return -1

    def check(self, number: int) -> bool:
        """
        Check if a number is available.
        
        Args:
            number (int): The number to check
            
        Returns:
            bool: True if the number is available, False otherwise
        """
        return number not in self.in_use

    def release(self, number: int) -> None:
        """
        Release a number back to the available pool.
        
        Args:
            number (int): The number to release
        """
        if number in self.in_use:
            self.in_use.remove(number)
            self.available_numbers.append(number)


def run_test_cases() -> None:
    """Function to run comprehensive test cases"""
    
    # Test case 1: Basic operations
    print("\nTest Case 1: Basic operations")
    pd1 = PhoneDirectory(3)
    results = []
    results.append(f"get() -> {pd1.get()}")         # Should return 0
    results.append(f"get() -> {pd1.get()}")         # Should return 1
    results.append(f"check(2) -> {pd1.check(2)}")   # Should return True
    results.append(f"get() -> {pd1.get()}")         # Should return 2
    results.append(f"check(2) -> {pd1.check(2)}")   # Should return False
    pd1.release(2)
    results.append(f"check(2) -> {pd1.check(2)}")   # Should return True
    
    print("Expected: ['get() -> 0', 'get() -> 1', 'check(2) -> True', 'get() -> 2', 'check(2) -> False', 'check(2) -> True']")
    print(f"Got: {results}")
    print(f"Result: {'PASSED' if results == ['get() -> 0', 'get() -> 1', 'check(2) -> True', 'get() -> 2', 'check(2) -> False', 'check(2) -> True'] else 'FAILED'}")
    
    # Test case 2: Release and reuse
    print("\nTest Case 2: Release and reuse")
    pd2 = PhoneDirectory(2)
    results = []
    results.append(f"get() -> {pd2.get()}")         # Should return 0
    results.append(f"get() -> {pd2.get()}")         # Should return 1
    results.append(f"get() -> {pd2.get()}")         # Should return -1 (no numbers available)
    pd2.release(0)
    results.append(f"get() -> {pd2.get()}")         # Should return 0 (reused)
    
    print("Expected: ['get() -> 0', 'get() -> 1', 'get() -> -1', 'get() -> 0']")
    print(f"Got: {results}")
    print(f"Result: {'PASSED' if results == ['get() -> 0', 'get() -> 1', 'get() -> -1', 'get() -> 0'] else 'FAILED'}")
    
    # Test case 3: Check operation
    print("\nTest Case 3: Check operation")
    pd3 = PhoneDirectory(3)
    results = []
    results.append(f"check(0) -> {pd3.check(0)}")   # Should return True
    results.append(f"check(1) -> {pd3.check(1)}")   # Should return True
    results.append(f"check(2) -> {pd3.check(2)}")   # Should return True
    pd3.get()  # Get 0
    results.append(f"check(0) -> {pd3.check(0)}")   # Should return False
    
    print("Expected: ['check(0) -> True', 'check(1) -> True', 'check(2) -> True', 'check(0) -> False']")
    print(f"Got: {results}")
    print(f"Result: {'PASSED' if results == ['check(0) -> True', 'check(1) -> True', 'check(2) -> True', 'check(0) -> False'] else 'FAILED'}")
    
    # Test case 4: Multiple releases
    print("\nTest Case 4: Multiple releases")
    pd4 = PhoneDirectory(1)
    results = []
    results.append(f"get() -> {pd4.get()}")         # Should return 0
    pd4.release(0)
    results.append(f"get() -> {pd4.get()}")         # Should return 0
    pd4.release(0)
    results.append(f"get() -> {pd4.get()}")         # Should return 0
    
    print("Expected: ['get() -> 0', 'get() -> 0', 'get() -> 0']")
    print(f"Got: {results}")
    print(f"Result: {'PASSED' if results == ['get() -> 0', 'get() -> 0', 'get() -> 0'] else 'FAILED'}")


if __name__ == "__main__":
    run_test_cases()
