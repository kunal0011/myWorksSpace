from typing import List


class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)

        # Step 1: Preprocessing - Plates prefix sum array
        plates_prefix = [0] * n
        count = 0
        for i in range(n):
            if s[i] == '*':
                count += 1
            plates_prefix[i] = count

        # Step 2: Preprocessing - Left and right nearest candle arrays
        left_candle = [-1] * n
        right_candle = [-1] * n

        # Left candle positions
        last_candle = -1
        for i in range(n):
            if s[i] == '|':
                last_candle = i
            left_candle[i] = last_candle

        # Right candle positions
        last_candle = -1
        for i in range(n-1, -1, -1):
            if s[i] == '|':
                last_candle = i
            right_candle[i] = last_candle

        # Step 3: Answer queries
        result = []
        for left, right in queries:
            # Find the nearest right candle after left
            left_candle_idx = right_candle[left]
            # Find the nearest left candle before right
            right_candle_idx = left_candle[right]

            # If valid candles exist and they enclose a valid range
            if left_candle_idx != -1 and right_candle_idx != -1 and left_candle_idx < right_candle_idx:
                plates_count = plates_prefix[right_candle_idx] - \
                    plates_prefix[left_candle_idx]
                result.append(plates_count)
            else:
                result.append(0)

        return result
