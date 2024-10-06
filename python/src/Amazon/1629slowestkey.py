class Solution:
    def slowestKey(self, releaseTimes, keysPressed):
        # Initialize with the first key and its duration
        max_duration = releaseTimes[0]
        slowest_key = keysPressed[0]

        # Loop through from the second element to the end
        for i in range(1, len(releaseTimes)):
            # Calculate the current duration
            current_duration = releaseTimes[i] - releaseTimes[i - 1]

            # Check if we need to update the slowest key
            if current_duration > max_duration or (current_duration == max_duration and keysPressed[i] > slowest_key):
                max_duration = current_duration
                slowest_key = keysPressed[i]

        return slowest_key
