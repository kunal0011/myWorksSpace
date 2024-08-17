import heapq


class StockPrice:

    def __init__(self):
        self.timestamp_price = {}
        self.max_timestamp = float('-inf')
        self.min_heap = []
        self.max_heap = []

    def update(self, timestamp: int, price: int) -> None:
        # Update the timestamp's price
        self.timestamp_price[timestamp] = price

        # Update the max timestamp
        if timestamp > self.max_timestamp:
            self.max_timestamp = timestamp

        # Push to heaps
        heapq.heappush(self.min_heap, (price, timestamp))
        heapq.heappush(self.max_heap, (-price, timestamp))

    def current(self) -> int:
        # Return the price at the latest timestamp
        return self.timestamp_price[self.max_timestamp]

    def maximum(self) -> int:
        # Get the maximum price by checking the max-heap
        while True:
            price, timestamp = heapq.heappop(self.max_heap)
            if self.timestamp_price[timestamp] == -price:
                heapq.heappush(self.max_heap, (price, timestamp))
                return -price

    def minimum(self) -> int:
        # Get the minimum price by checking the min-heap
        while True:
            price, timestamp = heapq.heappop(self.min_heap)
            if self.timestamp_price[timestamp] == price:
                heapq.heappush(self.min_heap, (price, timestamp))
                return price
