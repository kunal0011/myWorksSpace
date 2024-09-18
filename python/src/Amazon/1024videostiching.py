from typing import List


class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        # Sort clips by their start time; if two clips have the same start time, sort by end time in descending order
        clips.sort(key=lambda x: (x[0], x[1]))

        # Initialize variables
        end = 0         # The farthest point we can reach
        count = 0       # The number of clips used
        i = 0           # Pointer to the current clip
        n = len(clips)  # Number of clips

        while end < T:
            # Find the clip that starts before or at 'end' and has the farthest reach
            farthest = end
            while i < n and clips[i][0] <= end:
                farthest = max(farthest, clips[i][1])
                i += 1

            # If no clip can be found that extends the reach, it's impossible to cover the interval
            if farthest == end:
                return -1

            # Move to the farthest point
            end = farthest
            count += 1

        return count


# Testing
solution = Solution()
clips = [[0, 2], [4, 6], [8, 10], [1, 9], [1, 5], [5, 9]]
T = 10
print("Python Test Result:", solution.videoStitching(clips, T))  # Output: 3
