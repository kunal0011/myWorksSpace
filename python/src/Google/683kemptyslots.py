class Solution:
    def kEmptySlots(self, bulbs, k):
        n = len(bulbs)
        days = [0] * n

        # Convert bulbs array into the day each position blooms
        for day, position in enumerate(bulbs):
            days[position - 1] = day + 1

        left, right = 0, k + 1
        result = float('inf')

        # Iterate with a sliding window of size k+2 (two bulbs with k empty slots between them)
        while right < n:
            valid = True
            for i in range(left + 1, right):
                if days[i] < days[left] or days[i] < days[right]:
                    valid = False
                    left, right = i, i + k + 1
                    break

            if valid:
                result = min(result, max(days[left], days[right]))
                left, right = right, right + k + 1

        return -1 if result == float('inf') else result
