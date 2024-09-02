class Solution:
    def readBinaryWatch(self, turnedOn: int):
        times = []

        # Iterate over all possible hours (0 to 11)
        for h in range(12):
            # Iterate over all possible minutes (0 to 59)
            for m in range(60):
                # Count the number of 1s in the binary representation of hours and minutes
                if bin(h).count('1') + bin(m).count('1') == turnedOn:
                    # Format the time correctly (minute portion should always have two digits)
                    times.append(f"{h}:{m:02d}")

        return times
