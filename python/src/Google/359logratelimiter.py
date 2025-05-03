"""
LeetCode 359 - Logger Rate Limiter

Design a logger system that receives a stream of messages along with their timestamps.
Each unique message should only be printed at most every 10 seconds.
All messages will come in chronological order. Several messages may arrive at the same timestamp.

Implement the Logger class:
- Logger() Initializes the logger object.
- shouldPrintMessage(timestamp: int, message: str) -> bool
  Returns true if the message should be printed in the given timestamp, otherwise returns false.
"""

class Logger:
    def __init__(self):
        self.message_timestamp = {}
    
    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.message_timestamp or timestamp - self.message_timestamp[message] >= 10:
            self.message_timestamp[message] = timestamp
            return True
        return False

def test_logger():
    logger = Logger()
    test_cases = [
        (1, "foo"),      # returns true
        (2, "bar"),      # returns true
        (3, "foo"),      # returns false
        (8, "bar"),      # returns false
        (10, "foo"),     # returns false
        (11, "foo"),     # returns true
        (12, "foo"),     # returns false
    ]
    
    print("Testing Logger Rate Limiter:")
    for timestamp, message in test_cases:
        result = logger.shouldPrintMessage(timestamp, message)
        print(f"timestamp: {timestamp}, message: {message}, should print: {result}")

if __name__ == "__main__":
    test_logger()
