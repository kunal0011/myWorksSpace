class Solution:
    def areSentencesSimilar(self, sentence1, sentence2, similarPairs):
        # If the sentences have different lengths, they can't be similar
        if len(sentence1) != len(sentence2):
            return False

        # Create a set for similarity pairs for quick lookup
        similar_set = set()
        for pair in similarPairs:
            similar_set.add((pair[0], pair[1]))
            similar_set.add((pair[1], pair[0]))  # Add both directions

        # Check each word in both sentences
        for word1, word2 in zip(sentence1, sentence2):
            if word1 != word2 and (word1, word2) not in similar_set:
                return False

        return True
