class ValidWordAbbr:
    def __init__(self, dictionary):
        self.abbr_map = {}
        for word in set(dictionary):
            abbr = self._get_abbreviation(word)
            if abbr not in self.abbr_map:
                self.abbr_map[abbr] = word
            else:
                self.abbr_map[abbr] = ""  # Ambiguous abbreviation

    def _get_abbreviation(self, word):
        if len(word) <= 2:
            return word
        return word[0] + str(len(word) - 2) + word[-1]

    def isUnique(self, word):
        abbr = self._get_abbreviation(word)
        if abbr not in self.abbr_map:
            return True
        return self.abbr_map[abbr] == word
