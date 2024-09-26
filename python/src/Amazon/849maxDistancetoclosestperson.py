from typing import List


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        max_distance = 0

        # Find the first and last occupied seat
        first_person = seats.index(1)
        last_person = n - 1 - seats[::-1].index(1)

        # Max distance to the first person (if someone sits at index 0)
        max_distance = max(max_distance, first_person)

        # Max distance to the last person (if someone sits at index n-1)
        max_distance = max(max_distance, n - 1 - last_person)

        # Iterate through the array and find the max distance between two people
        previous_person = first_person

        for i in range(first_person + 1, n):
            if seats[i] == 1:
                distance_between_people = i - previous_person
                # The best seat is in the middle between two people
                max_distance = max(max_distance, distance_between_people // 2)
                previous_person = i

        return max_distance
