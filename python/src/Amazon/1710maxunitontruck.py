class Solution:
    def maximumUnits(self, boxTypes, truckSize):
        # Sort the boxTypes based on the number of units per box in descending order
        boxTypes.sort(key=lambda x: -x[1])

        max_units = 0
        for boxes, units_per_box in boxTypes:
            # If the truck can carry all boxes of this type
            if truckSize >= boxes:
                max_units += boxes * units_per_box
                truckSize -= boxes
            else:
                # If the truck can only carry a part of these boxes
                max_units += truckSize * units_per_box
                break

        return max_units
