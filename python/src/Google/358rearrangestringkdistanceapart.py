"""
LeetCode 358 - Rearrange String k Distance Apart

Given a string s and an integer k, rearrange s such that the same characters are at least 
distance k from each other. If it is not possible to rearrange the string, return an empty string "".

Example 1:
Input: s = "aabbcc", k = 3
Output: "abcabc"
Explanation: The same letters are at least distance 3 from each other.

Example 2:
Input: s = "aaabc", k = 3
Output: ""
Explanation: It is not possible to rearrange the string.
"""
import heapq
from collections import Counter, deque


class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        """
        Rearrange string so same characters are k distance apart.
        
        Approach:
        1. Use Counter to get character frequencies
        2. Use max heap to process most frequent characters first
        3. Use queue to enforce k-distance constraint
        
        Time: O(N log M) where N is string length, M is unique characters
        Space: O(M) for heap and queue
        
        Args:
            s: Input string to rearrange
            k: Minimum distance between same characters
        Returns:
            Rearranged string or empty string if not possible
        """
        if k == 0:
            return s

        # Step 1: Count frequency of each character
        char_count = Counter(s)

        # Step 2: Use a max-heap to store characters by frequency
        max_heap = [(-freq, char) for char, freq in char_count.items()]
        heapq.heapify(max_heap)

        queue = deque()  # To store characters that are waiting to be reinserted
        result = []

        while max_heap:
            freq, char = heapq.heappop(max_heap)
            result.append(char)

            # Decrement the frequency and add to queue with current index
            queue.append((freq+1, char))

            # If the queue length has reached k, reinsert the character at the front
            if len(queue) >= k:
                to_reinsert = queue.popleft()
                if to_reinsert[0] < 0:
                    heapq.heappush(max_heap, to_reinsert)

        # If the result length equals the original string length, return result as string
        return ''.join(result) if len(result) == len(s) else ""


def test_rearrange_string():
    """Test function for rearranging string k distance apart"""
    solution = Solution()
    
    # Test case 1: Basic rearrangement
    print("Test case 1: Basic rearrangement")
    s1, k1 = "aabbcc", 3
    result1 = solution.rearrangeString(s1, k1)
    print(f"Input: s = {s1}, k = {k1}")
    print(f"Output: {result1}")
    assert len(result1) == len(s1), "Test case 1 failed"
    
    # Test case 2: Impossible rearrangement
    print("\nTest case 2: Impossible rearrangement")
    s2, k2 = "aaabc", 3
    result2 = solution.rearrangeString(s2, k2)
    print(f"Input: s = {s2}, k = {k2}")
    print(f"Output: {result2}")
    assert result2 == "", "Test case 2 failed"
    
    # Test case 3: k = 0 (no constraint)
    print("\nTest case 3: No distance constraint")
    s3, k3 = "aaadbbcc", 0
    result3 = solution.rearrangeString(s3, k3)
    print(f"Input: s = {s3}, k = {k3}")
    print(f"Output: {result3}")
    assert result3 == s3, "Test case 3 failed"
    
    # Test case 4: Complex rearrangement
    print("\nTest case 4: Complex rearrangement")
    s4, k4 = "aaadbbcc", 3
    result4 = solution.rearrangeString(s4, k4)
    print(f"Input: s = {s4}, k = {k4}")
    print(f"Output: {result4}")
    assert len(result4) == len(s4), "Test case 4 failed"
    
    print("\nAll test cases passed!")


if __name__ == "__main__":
    test_rearrange_string()
