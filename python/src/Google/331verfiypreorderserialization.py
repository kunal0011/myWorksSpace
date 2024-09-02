class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        # Split the string by commas into nodes
        nodes = preorder.split(',')
        # Start with 1 available slot (for the root)
        slots = 1

        for node in nodes:
            # Every node consumes one slot
            slots -= 1

            # If at any point slots are negative, it's invalid
            if slots < 0:
                return False

            # Non-null nodes create two more slots (for their children)
            if node != '#':
                slots += 2

        # At the end, we should have used exactly all slots
        return slots == 0
