from typing import List


class MagicDictionary:

    def __init__(self):
        self.words = set()

    def buildDict(self, dictionary: List[str]) -> None:
        self.words = set(dictionary)

    def search(self, searchWord: str) -> bool:
        for word in self.words:
            if len(word) != len(searchWord):
                continue
            # Count the number of differences between the two words
            diff_count = 0
            for i in range(len(word)):
                if word[i] != searchWord[i]:
                    diff_count += 1
                if diff_count > 1:
                    break
            if diff_count == 1:
                return True
        return False
