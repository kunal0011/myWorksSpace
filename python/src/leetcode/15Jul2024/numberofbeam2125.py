from typing import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        # Step 1: Extract the rows that contain security devices
        devices_per_row = [row.count('1') for row in bank if '1' in row]

        # Step 2: Calculate the total number of laser beams
        total_beams = 0
        for i in range(len(devices_per_row) - 1):
            total_beams += devices_per_row[i] * devices_per_row[i + 1]

        return total_beams
