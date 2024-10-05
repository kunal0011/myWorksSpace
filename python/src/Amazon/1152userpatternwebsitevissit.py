from collections import defaultdict, Counter
from itertools import combinations


class Solution:
    def mostVisitedPattern(self, username, timestamp, website):
        # Step 1: Group the websites visited by each user, sorted by timestamp
        user_data = defaultdict(list)
        for u, t, w in sorted(zip(username, timestamp, website), key=lambda x: (x[0], x[1])):
            user_data[u].append(w)

        # Step 2: For each user, generate all 3-sequences and track them
        pattern_count = Counter()
        for user, websites in user_data.items():
            # Generate all possible 3-sequences from the user's website visit history
            if len(websites) >= 3:
                # Use a set to avoid counting the same sequence multiple times per user
                unique_3_seqs = set(combinations(websites, 3))
                for seq in unique_3_seqs:
                    pattern_count[seq] += 1

        # Step 3: Find the most common 3-sequence (with lexicographical tie-break)
        return min(pattern_count, key=lambda x: (-pattern_count[x], x))
