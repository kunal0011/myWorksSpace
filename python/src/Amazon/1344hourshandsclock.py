class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        # Calculate the positions of the hour and minute hands in degrees
        hour_angle = (hour % 12) * 30 + (minutes * 0.5)
        minute_angle = minutes * 6

        # Calculate the absolute difference between the two angles
        difference = abs(hour_angle - minute_angle)

        # Return the smaller angle (either difference or 360 - difference)
        return min(difference, 360 - difference)
