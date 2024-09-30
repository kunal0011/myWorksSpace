import heapq


class KthLargest:

    def __init__(self, k: int, nums):
        self.k = k
        # Use a heap to store the k largest elements
        self.min_heap = []

        # Add all elements from nums to the heap
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        # Add the new value to the heap
        heapq.heappush(self.min_heap, val)

        # If the heap grows larger than k, remove the smallest element
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

        # The kth largest element will be the smallest element in the heap
        return self.min_heap[0]


# Test the solution with some test cases
if __name__ == "__main__":
    # Initialize the object with k=3 and an initial list [4, 5, 8, 2]
    kthLargest = KthLargest(3, [4, 5, 8, 2])

    # Test the add method
    # Expected output: 4 (the 3rd largest element after adding 3)
    print(kthLargest.add(3))
    # Expected output: 5 (the 3rd largest element after adding 5)
    print(kthLargest.add(5))
    # Expected output: 5 (the 3rd largest element after adding 10)
    print(kthLargest.add(10))
    # Expected output: 8 (the 3rd largest element after adding 9)
    print(kthLargest.add(9))
    # Expected output: 8 (the 3rd largest element after adding 4)
    print(kthLargest.add(4))
