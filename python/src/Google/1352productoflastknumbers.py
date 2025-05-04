"""
LeetCode 1352: Product of the Last K Numbers

Problem Statement:
Design an algorithm that supports two operations:
1. Adding a positive integer to the data structure
2. Returning the product of the last k numbers

Logic:
1. Use prefix products array to store running products
2. For add operation:
   - If number is 0, reset prefix array to [1]
   - Otherwise, multiply last prefix by new number
3. For getProduct operation:
   - If k is too large (means zero was encountered), return 0
   - Otherwise, divide last prefix by prefix at (length-k-1)
   
Time Complexity:
- add: O(1)
- getProduct: O(1)
Space Complexity: O(n) where n is number of elements added
"""


class ProductOfNumbers:

    def __init__(self):
        self.prefix_products = [1]  # Start with a dummy product of 1

    def add(self, num: int) -> None:
        if num == 0:
            # Reset if a zero is added
            self.prefix_products = [1]
        else:
            # Multiply the last prefix product by the new number
            self.prefix_products.append(self.prefix_products[-1] * num)

    def getProduct(self, k: int) -> int:
        if k >= len(self.prefix_products):
            return 0  # If k is larger than or equal to the length of prefix_products, a zero was included
        return self.prefix_products[-1] // self.prefix_products[-k-1]


def test_product_of_numbers():
    # Test case 1: Basic operations
    obj = ProductOfNumbers()
    obj.add(3)
    obj.add(2)
    obj.add(4)
    result1 = obj.getProduct(2)  # Should return 8 (2*4)
    assert result1 == 8, f"Test case 1 failed. Expected 8, got {result1}"
    print(f"Test case 1 passed: {result1}")

    # Test case 2: With zero
    obj2 = ProductOfNumbers()
    obj2.add(0)
    obj2.add(2)
    obj2.add(5)
    result2 = obj2.getProduct(2)  # Should return 10 (2*5)
    assert result2 == 10, f"Test case 2 failed. Expected 10, got {result2}"
    print(f"\nTest case 2 passed: {result2}")

    # Test case 3: Get product beyond zero
    obj3 = ProductOfNumbers()
    obj3.add(0)
    obj3.add(2)
    result3 = obj3.getProduct(3)  # Should return 0
    assert result3 == 0, f"Test case 3 failed. Expected 0, got {result3}"
    print(f"\nTest case 3 passed: {result3}")

    # Test case 4: Single element product
    obj4 = ProductOfNumbers()
    obj4.add(5)
    result4 = obj4.getProduct(1)  # Should return 5
    assert result4 == 5, f"Test case 4 failed. Expected 5, got {result4}"
    print(f"\nTest case 4 passed: {result4}")

    print("\nAll test cases passed!")


if __name__ == "__main__":
    test_product_of_numbers()
