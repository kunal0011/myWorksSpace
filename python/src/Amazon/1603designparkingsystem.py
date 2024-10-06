class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        # Initialize the parking system with available slots
        self.slots = {1: big, 2: medium, 3: small}

    def addCar(self, carType: int) -> bool:
        # If there are available slots for this car type, park it and reduce the slot count
        if self.slots[carType] > 0:
            self.slots[carType] -= 1
            return True
        else:
            return False

# Test cases


def test_parking_system():
    # Test case 1
    parkingSystem = ParkingSystem(1, 1, 0)
    assert parkingSystem.addCar(
        1) == True, "Test case 1 failed: big slot should be available"
    assert parkingSystem.addCar(
        2) == True, "Test case 1 failed: medium slot should be available"
    assert parkingSystem.addCar(
        3) == False, "Test case 1 failed: no small slot available"
    assert parkingSystem.addCar(
        1) == False, "Test case 1 failed: big slot should be full"

    # Test case 2
    parkingSystem = ParkingSystem(2, 1, 1)
    assert parkingSystem.addCar(
        3) == True, "Test case 2 failed: small slot should be available"
    assert parkingSystem.addCar(
        2) == True, "Test case 2 failed: medium slot should be available"
    assert parkingSystem.addCar(
        2) == False, "Test case 2 failed: no medium slot left"
    assert parkingSystem.addCar(
        1) == True, "Test case 2 failed: big slot should be available"
    assert parkingSystem.addCar(
        1) == True, "Test case 2 failed: second big slot should be available"
    assert parkingSystem.addCar(
        1) == False, "Test case 2 failed: big slots should be full now"

    print("All test cases passed!")


# Run the tests
test_parking_system()
