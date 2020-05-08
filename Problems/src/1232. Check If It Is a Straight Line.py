class Solution:
    """my first sol"""
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:

        x1, y1, x2, y2 = *coordinates[0], *coordinates[1]

        if x2 - x1 == 0:
            slope = float("inf")
        else:
            slope = (y2 - y1) / (x2 - x1)

        if slope == float("inf"):
            for x, y in coordinates[2:]:
                if x != x1:
                    return False

        else:
            for x, y in coordinates[2:]:
                if y != y1 + slope * (x - x1):
                    return False

        return True

    """my sol after online hint"""
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:

        x1, y1, x2, y2 = *coordinates[0], *coordinates[1]
        dy, dx = y2 - y1, x2 - x1

        return all(dy * (x - x1) == dx * (y - y1) for x, y in coordinates[2:])