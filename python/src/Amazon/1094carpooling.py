class Solution:
    def carPooling(self, trips, capacity):
        # List to track all changes in the number of passengers
        timeline = []

        # For each trip, record two events: pickup and drop-off
        for num_passengers, start, end in trips:
            # Add num_passengers at the pickup location
            timeline.append((start, num_passengers))
            # Subtract num_passengers at the drop-off location
            timeline.append((end, -num_passengers))

        # Sort the timeline by the location (start first)
        # If two events happen at the same time, drop-offs should be processed before pickups
        timeline.sort()

        # Variable to track current number of passengers in the car
        current_passengers = 0

        # Process the events in order
        for location, passenger_change in timeline:
            current_passengers += passenger_change
            # If at any point the number of passengers exceeds capacity, return False
            if current_passengers > capacity:
                return False

        # If we processed all events without exceeding capacity, return True
        return True

# Test cases


def test_car_pooling():
    solution = Solution()

    # Test case 1
    trips = [[2, 1, 5], [3, 3, 7]]
    capacity = 4
    assert solution.carPooling(
        trips, capacity) == False, f"Test case 1 failed: {solution.carPooling(trips, capacity)}"

    # Test case 2
    trips = [[2, 1, 5], [3, 3, 7]]
    capacity = 5
    assert solution.carPooling(
        trips, capacity) == True, f"Test case 2 failed: {solution.carPooling(trips, capacity)}"

    # Test case 3
    trips = [[2, 1, 5], [3, 5, 7]]
    capacity = 3
    assert solution.carPooling(
        trips, capacity) == True, f"Test case 3 failed: {solution.carPooling(trips, capacity)}"

    # Test case 4
    trips = [[3, 2, 7], [3, 7, 9], [8, 3, 9]]
    capacity = 11
    assert solution.carPooling(
        trips, capacity) == True, f"Test case 4 failed: {solution.carPooling(trips, capacity)}"

    print("All test cases passed!")


# Run the tests
test_car_pooling()
