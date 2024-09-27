class Logger:
    def __init__(self):
        # Dictionary to store the last timestamp when each message was printed
        self.message_dict = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        # Check if the message is in the dictionary
        if message in self.message_dict:
            # If the message was printed less than 10 seconds ago, return False
            if timestamp - self.message_dict[message] < 10:
                return False

        # Otherwise, print the message and update the timestamp
        self.message_dict[message] = timestamp
        return True
