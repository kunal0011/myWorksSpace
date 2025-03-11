import random


class RandomizedSet:
    def __init__(self):
        self.nums = []  # List to store the elements
        self."""
LeetCode 380: Insert Delete GetRandom O(1)

Implement the RandomizedSet class:
- RandomizedSet(): Initializes the RandomizedSet object.
- bool insert(int val): Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
- bool remove(int val): Removes an item val from the set if present. Returns true if the item was present, false otherwise.
- int getRandom(): Returns a random element from the current set of elements (guaranteed to be valid). Each element must have the same probability of being returned.

All functions must work in O(1) time complexity on average.

Example:
Input
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output
[null, true, false, true, 2, true, false, 2]

Time Complexity:
- insert(): O(1)
- remove(): O(1)
- getRandom(): O(1)
Space Complexity: O(n) where n is the number of elements
"""

import random
from typing import List, Optional


class RandomizedSet:
    def __init__(self):
        """
        Initialize your data structure here.
        Using a list for O(1) random access and a dict for O(1) lookup
        """
        self.nums = []  # List to store numbers
        self.val_to_index = {}  # Dictionary to store value -> index mapping

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        
        Args:
            val: Value to insert
            
        Returns:
            bool: True if value was not present, False otherwise
        """
        if val in self.val_to_index:
            return False
            
        # Add new element at the end of the list
        self.nums.append(val)
        # Store its index in the hash map
        self.val_to_index[val] = len(self.nums) - 1
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        
        Args:
            val: Value to remove
            
        Returns:
            bool: True if value was present, False otherwise
        """
        if val not in self.val_to_index:
            return False
            
        # Get index of element to remove
        idx = self.val_to_index[val]
        last_val = self.nums[-1]
        
        # Move last element to the position of element to remove
        self.nums[idx] = last_val
        self.val_to_index[last_val] = idx
        
        # Remove the last element
        self.nums.pop()
        del self.val_to_index[val]
        
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        
        Returns:
            int: Random element from the set
        """
        return random.choice(self.nums)


def run_test_cases() -> None:
    """Function to run comprehensive test cases"""
    
    # Test case 1: Basic operations
    print("\nTest Case 1: Basic operations")
    randomized_set = RandomizedSet()
    operations = []
    
    operations.append(f"insert(1) -> {randomized_set.insert(1)}")  # Returns true
    operations.append(f"remove(2) -> {randomized_set.remove(2)}")  # Returns false
    operations.append(f"insert(2) -> {randomized_set.insert(2)}")  # Returns true
    operations.append(f"getRandom() -> {randomized_set.getRandom()}")  # Returns either 1 or 2
    operations.append(f"remove(1) -> {randomized_set.remove(1)}")  # Returns true
    operations.append(f"insert(2) -> {randomized_set.insert(2)}")  # Returns false
    random_val = randomized_set.getRandom()
    operations.append(f"getRandom() -> {random_val}")  # Returns 2
    
    print("Operations performed:")
    for op in operations:
        print(op)
    print(f"Final state of set: {randomized_set.nums}")
    
    # Test case 2: Multiple insertions
    print("\nTest Case 2: Multiple insertions")
    rs2 = RandomizedSet()
    operations = []
    
    for i in range(5):
        operations.append(f"insert({i}) -> {rs2.insert(i)}")
    
    print("Operations performed:")
    for op in operations:
        print(op)
    print(f"Final state of set: {rs2.nums}")
    
    # Test case 3: Insert duplicates
    print("\nTest Case 3: Insert duplicates")
    rs3 = RandomizedSet()
    operations = []
    
    operations.append(f"insert(1) -> {rs3.insert(1)}")  # Returns true
    operations.append(f"insert(1) -> {rs3.insert(1)}")  # Returns false
    operations.append(f"insert(2) -> {rs3.insert(2)}")  # Returns true
    
    print("Operations performed:")
    for op in operations:
        print(op)
    print(f"Final state of set: {rs3.nums}")
    
    # Test case 4: Remove non-existent
    print("\nTest Case 4: Remove non-existent")
    rs4 = RandomizedSet()
    operations = []
    
    operations.append(f"insert(1) -> {rs4.insert(1)}")
    operations.append(f"remove(2) -> {rs4.remove(2)}")  # Returns false
    operations.append(f"remove(1) -> {rs4.remove(1)}")  # Returns true
    operations.append(f"remove(1) -> {rs4.remove(1)}")  # Returns false
    
    print("Operations performed:")
    for op in operations:
        print(op)
    print(f"Final state of set: {rs4.nums}")
    
    # Test case 5: Random distribution
    print("\nTest Case 5: Random distribution test")
    rs5 = RandomizedSet()
    for i in range(3):
        rs5.insert(i)
    
    # Test random distribution
    count = {0: 0, 1: 0, 2: 0}
    trials = 3000
    
    for _ in range(trials):
        val = rs5.getRandom()
        count[val] += 1
    
    print("Random distribution after 3000 trials:")
    for num, freq in count.items():
        print(f"Number {num}: {freq/trials:.2%}")


if __name__ == "__main__":
    run_test_cases()pos = {}   # Hashmap to store element -> index mapping

    def insert(self, val: int) -> bool:
        if val in self.pos:
            return False
        # Insert the element and add its position in the hashmap
        self.pos[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.pos:
            return False
        # Swap the element with the last one in the list and update the hashmap
        last_element = self.nums[-1]
        idx_to_remove = self.pos[val]
        self.nums[idx_to_remove] = last_element
        self.pos[last_element] = idx_to_remove
        # Remove the last element from the list and delete val from hashmap
        self.nums.pop()
        del self.pos[val]
        return True

    def getRandom(self) -> int:
        # Return a random element from the list
        return random.choice(self.nums)

# Test cases


def test_randomized_set():
    rs = RandomizedSet()

    # Test case 1: Insert elements
    assert rs.insert(1) == True, "Test case 1 failed"
    assert rs.insert(2) == True, "Test case 1 failed"
    assert rs.insert(1) == False, "Test case 1 failed"  # 1 is already present

    # Test case 2: Remove elements
    assert rs.remove(2) == True, "Test case 2 failed"
    assert rs.remove(2) == False, "Test case 2 failed"  # 2 is already removed

    # Test case 3: getRandom
    assert rs.getRandom() in [1], "Test case 3 failed"  # Only 1 is present

    print("All test cases passed!")


# Run the tests
test_randomized_set()
