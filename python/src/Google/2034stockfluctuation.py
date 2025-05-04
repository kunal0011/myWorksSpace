"""
LeetCode 2034. Stock Price Fluctuation

Problem Statement:
You are given a stream of records about a particular stock. Each record contains a timestamp and the 
corresponding price of the stock at that timestamp. Unfortunately due to the volatile nature of the stock 
market, the records do not come in order. Even worse, some records may be incorrect. Another record with 
the same timestamp may appear later in the stream which contains the correct price.

Design an algorithm that:
- Updates the price of the stock at a particular timestamp, correcting the price from any previous records 
  that had the same timestamp.
- Finds the latest price of the stock based on the current records.
- Finds the maximum price the stock has been based on the current records.
- Finds the minimum price the stock has been based on the current records.

Time Complexity: 
- update: O(log n)
- current: O(1)
- maximum/minimum: O(log n) amortized
Space Complexity: O(n) where n is number of timestamps
"""

import heapq
from typing import List


class StockPrice:
    def __init__(self):
        # timestamp_price: Maps timestamp to its correct price
        # max_timestamp: Keeps track of the latest timestamp
        # min_heap: Heap for finding minimum price
        # max_heap: Heap for finding maximum price (uses negative values)
        self.timestamp_price = {}
        self.max_timestamp = float('-inf')
        self.min_heap = []
        self.max_heap = []

    def update(self, timestamp: int, price: int) -> None:
        # Update the timestamp's price in our map
        self.timestamp_price[timestamp] = price

        # Keep track of the most recent timestamp
        if timestamp > self.max_timestamp:
            self.max_timestamp = timestamp

        # Add to both heaps. Note: max heap uses negative price
        heapq.heappush(self.min_heap, (price, timestamp))
        heapq.heappush(self.max_heap, (-price, timestamp))

    def current(self) -> int:
        # Simply return the price at the most recent timestamp
        return self.timestamp_price[self.max_timestamp]

    def maximum(self) -> int:
        # Keep popping from max heap until we find a valid price
        while True:
            price, timestamp = heapq.heappop(self.max_heap)
            # Check if this price is still valid
            if self.timestamp_price[timestamp] == -price:
                heapq.heappush(self.max_heap, (price, timestamp))
                return -price

    def minimum(self) -> int:
        # Keep popping from min heap until we find a valid price
        while True:
            price, timestamp = heapq.heappop(self.min_heap)
            # Check if this price is still valid
            if self.timestamp_price[timestamp] == price:
                heapq.heappush(self.min_heap, (price, timestamp))
                return price


# Test driver
if __name__ == "__main__":
    def test_stock_price():
        print("Test Case 1:")
        stockPrice = StockPrice()

        # Test operations
        operations = [
            ("update", [1, 10]),
            ("update", [2, 5]),
            ("current", []),
            ("maximum", []),
            ("update", [1, 3]),
            ("maximum", []),
            ("minimum", [])
        ]

        for op, params in operations:
            if op == "update":
                print(f"Updating timestamp={params[0]} with price={params[1]}")
                stockPrice.update(params[0], params[1])
                print(f"Current price map: {stockPrice.timestamp_price}")
            elif op == "current":
                result = stockPrice.current()
                print(f"Current price: {result}")
            elif op == "maximum":
                result = stockPrice.maximum()
                print(f"Maximum price: {result}")
            elif op == "minimum":
                result = stockPrice.minimum()
                print(f"Minimum price: {result}")

        print("\nTest Case 2:")
        stockPrice2 = StockPrice()

        # More complex test case
        updates = [
            (1, 100),
            (2, 80),
            (1, 90),    # Correcting timestamp 1
            (3, 110),
            (2, 85),    # Correcting timestamp 2
            (4, 95)
        ]

        for timestamp, price in updates:
            print(f"\nUpdating timestamp={timestamp} with price={price}")
            stockPrice2.update(timestamp, price)
            print(f"Current price: {stockPrice2.current()}")
            print(f"Maximum price: {stockPrice2.maximum()}")
            print(f"Minimum price: {stockPrice2.minimum()}")

    # Run the tests
    test_stock_price()
