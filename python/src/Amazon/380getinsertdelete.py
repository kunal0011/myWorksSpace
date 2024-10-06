import random


class RandomizedSet:
    def __init__(self):
        self.nums = []  # List to store the elements
        self.pos = {}   # Hashmap to store element -> index mapping

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
