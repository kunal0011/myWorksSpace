"""
LeetCode 1108: Defanging an IP Address

Problem Statement:
Given a valid IPv4 address address, return a defanged version of that IP address.
A defanged IP address replaces every period '.' with '[.]'.

Logic:
1. Use string replace method to substitute '.' with '[.]'
2. Can also use string join with split if replace not available
3. Alternative: iterate through string and build new string

Time Complexity: O(n) where n is length of string
Space Complexity: O(n) for creating new string
"""

from typing import List


class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')


def test_defang_ip_addr():
    solution = Solution()

    # Test case 1: Basic IP address
    address1 = "1.1.1.1"
    result1 = solution.defangIPaddr(address1)
    assert result1 == "1[.]1[.]1[.]1", f"Test case 1 failed. Expected '1[.]1[.]1[.]1', got {result1}"
    print(f"Test case 1 passed: {address1} -> {result1}")

    # Test case 2: IP with double digits
    address2 = "255.100.50.0"
    result2 = solution.defangIPaddr(address2)
    assert result2 == "255[.]100[.]50[.]0", f"Test case 2 failed. Expected '255[.]100[.]50[.]0', got {result2}"
    print(f"\nTest case 2 passed: {address2} -> {result2}")

    # Test case 3: Local IP
    address3 = "127.0.0.1"
    result3 = solution.defangIPaddr(address3)
    assert result3 == "127[.]0[.]0[.]1", f"Test case 3 failed. Expected '127[.]0[.]0[.]1', got {result3}"
    print(f"\nTest case 3 passed: {address3} -> {result3}")

    print("\nAll test cases passed!")


if __name__ == "__main__":
    test_defang_ip_addr()
