from bisect import bisect_right


class Solution:
    def numSmallerByFrequency(self, queries, words):
        def f(s):
            return s.count(min(s))

        # Step 1: Calculate the frequency of the smallest character for each word in words
        word_frequencies = sorted(f(word) for word in words)

        # Step 2: Calculate the result for each query
        result = []
        for query in queries:
            query_freq = f(query)
            # Use bisect_right to find the position where query_freq would fit in word_frequencies
            # Count how many words have a greater frequency
            result.append(len(word_frequencies) -
                          bisect_right(word_frequencies, query_freq))

        return result
