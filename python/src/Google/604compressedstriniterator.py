class StringIterator:
    def __init__(self, compressedString: str):
        self.compressedString = compressedString
        self.index = 0
        self.current_char = ''
        self.current_count = 0

    def _parseNext(self):
        if self.index >= len(self.compressedString):
            return

        # Read the next character
        self.current_char = self.compressedString[self.index]
        self.index += 1

        # Read the number following the character
        num_start = self.index
        while self.index < len(self.compressedString) and self.compressedString[self.index].isdigit():
            self.index += 1
        self.current_count = int(self.compressedString[num_start:self.index])

    def next(self) -> str:
        if self.current_count == 0:
            self._parseNext()

        if self.current_count > 0:
            self.current_count -= 1
            return self.current_char
        else:
            return ' '  # Return space if there are no more characters

    def hasNext(self) -> bool:
        return self.current_count > 0 or self.index < len(self.compressedString)
