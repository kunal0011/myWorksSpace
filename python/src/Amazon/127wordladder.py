from collections import deque


class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        # Convert the wordList to a set for O(1) lookups
        wordSet = set(wordList)

        # If the endWord is not in the word list, there's no possible transformation
        if endWord not in wordSet:
            return 0

        # BFS queue: each element is a tuple (current_word, transformation_steps)
        queue = deque([(beginWord, 1)])

        # While the queue is not empty
        while queue:
            current_word, steps = queue.popleft()

            # Try changing each character of current_word
            for i in range(len(current_word)):
                # Try all possible letters from 'a' to 'z'
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    new_word = current_word[:i] + c + current_word[i+1:]

                    # If the new word matches endWord, return the number of steps
                    if new_word == endWord:
                        return steps + 1

                    # If the new word is in the word list and not yet visited
                    if new_word in wordSet:
                        wordSet.remove(new_word)  # Mark as visited
                        queue.append((new_word, steps + 1))

        # If no transformation was found
        return 0
