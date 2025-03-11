"""
LeetCode 359 - Logger Rate Limiter

Design a logger system that receives a stream of messages along with their timestamps.
Each unique message should only be printed at most every 10 seconds.

Time Complexity: O(1) for each shouldPrintMessage call
Space Complexity: O(M) where M is the number of unique messages stored
"""

class Logger:
    def __init__(self):
        # Dictionary to store the last timestamp when each message was printed
        self.message_dict = {}
        self.WINDOW_SIZE = 10  # Making the window size a class constant for better maintainability
        
    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        
        Args:
            timestamp (int): The current timestamp (in seconds)
            message (str): The message to be printed
            
        Returns:
            bool: True if the message can be printed, False otherwise
        """
        # Check if the message is in the dictionary and not expired
        if message in self.message_dict and timestamp - self.message_dict[message] < self.WINDOW_SIZE:
            return False
            
        # Update the timestamp and return True
        self.message_dict[message] = timestamp
        return True
    
    def cleanup(self, current_timestamp: int) -> None:
        """
        Optional cleanup method to remove expired entries.
        Can be called periodically to prevent memory growth.
        """
        self.message_dict = {
            msg: ts for msg, ts in self.message_dict.items() 
            if current_timestamp - ts < self.WINDOW_SIZE
        }


def run_tests():
    # Test Case 1: Basic functionality
    logger = Logger()
    test_cases = [
        # timestamp, message, expected output
        (1, "foo", True),
        (2, "bar", True),
        (3, "foo", False),  # Should be false because it's within 10 seconds
        (8, "bar", False),
        (10, "foo", False),
        (11, "foo", True),  # Should be true because it's after 10 seconds
    ]
    
    all_passed = True
    for i, (timestamp, message, expected) in enumerate(test_cases, 1):
        result = logger.shouldPrintMessage(timestamp, message)
        if result != expected:
            print(f"❌ Test {i} failed!")
            print(f"Input: timestamp={timestamp}, message='{message}'")
            print(f"Expected: {expected}, Got: {result}")
            all_passed = False
        else:
            print(f"✅ Test {i} passed!")
    
    # Test Case 2: Testing cleanup functionality
    logger = Logger()
    logger.shouldPrintMessage(1, "message1")
    logger.shouldPrintMessage(2, "message2")
    logger.shouldPrintMessage(3, "message3")
    
    # Before cleanup
    initial_size = len(logger.message_dict)
    print(f"\nBefore cleanup: {initial_size} messages in memory")
    
    # Simulate time passing and cleanup
    logger.cleanup(15)  # Cleanup messages older than 5 seconds
    final_size = len(logger.message_dict)
    print(f"After cleanup: {final_size} messages in memory")
    
    if all_passed:
        print("\nAll test cases passed! 🎉")


if __name__ == "__main__":
    run_tests()
