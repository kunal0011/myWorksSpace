class Logger:

    def __init__(self):
        # Dictionary to store the last printed time of each message
        self.message_timestamp = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        # Check if the message is in the dictionary
        if message in self.message_timestamp:
            # If the message has been printed in the last 10 seconds, return False
            if timestamp - self.message_timestamp[message] < 10:
                return False
        # Update the timestamp and return True
        self.message_timestamp[message] = timestamp
        return True
