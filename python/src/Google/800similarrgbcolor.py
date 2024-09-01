class Solution:
    def similarRGB(self, color: str) -> str:
        def closest_component(component: str) -> str:
            # Convert the hex component to an integer
            num = int(component, 16)
            # Find the closest shorthand component
            closest_val = round(num / 17) * 17  # 17 = 0x11
            # Clamp the value to the range of hex values
            closest_val = min(255, max(0, closest_val))
            # Convert back to hex, ensuring two characters with leading zero if needed
            return '{:02x}'.format(closest_val)

        # Extract the color components (RR, GG, BB)
        r, g, b = color[1:3], color[3:5], color[5:7]

        # Find the closest shorthand for each component
        return f'#{closest_component(r)}{closest_component(g)}{closest_component(b)}'
