class Solution:
    def outerTrees(self, trees):
        # Helper function to calculate the orientation
        def orientation(p, q, r):
            # Return the cross product of vectors pq and qr
            return (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])

        # Sort the points
        trees = sorted(trees)

        # Build the lower hull
        lower = []
        for p in trees:
            while len(lower) >= 2 and orientation(lower[-2], lower[-1], p) < 0:
                lower.pop()
            lower.append(p)

        # Build the upper hull
        upper = []
        for p in reversed(trees):
            while len(upper) >= 2 and orientation(upper[-2], upper[-1], p) < 0:
                upper.pop()
            upper.append(p)

        # Remove the last point of each half because it's repeated at the beginning of the other half
        return list(set(lower[:-1] + upper[:-1]))
